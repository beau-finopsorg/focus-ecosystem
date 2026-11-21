#!/usr/bin/env python3
"""Record when each linked resource was last updated upstream.

Writes registry/freshness.json, which build_readme.py reads. Each URL is
resolved with the most precise source available, in this order:

  github         last commit on the default branch (or the linked path)
  pypi           upload time of the latest release
  page-metadata  dateModified, article:modified_time, ms.date, and similar
  sitemap        <lastmod> for the URL in the host's sitemap
  http-header    Last-Modified, trusted for non-HTML files only
  content-change the page text changed since the previous run

Usage:
  python3 scripts/check_freshness.py
"""
from __future__ import annotations

import gzip
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from threading import Lock
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry" / "focus-ecosystem.yaml"
FRESHNESS = ROOT / "registry" / "freshness.json"
UA = "Mozilla/5.0 (compatible; focus-ecosystem-freshness/1.0; +https://github.com/beau-finopsorg/focus-ecosystem)"
TIMEOUT = 30
MAX_SITEMAPS = 40
SITEMAP_BUDGET_SECONDS = 60


def fetch(url: str, accept: str = "*/*", headers: dict | None = None):
    req = Request(url, headers={"User-Agent": UA, "Accept": accept, **(headers or {})})
    with urlopen(req, timeout=TIMEOUT) as resp:
        body = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip" or url.endswith(".gz"):
            body = gzip.decompress(body)
        return body, resp.headers


def to_date(value: str) -> str | None:
    value = value.strip()
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        pass
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", value)
    if m:
        return "-".join(m.groups())
    try:
        return parsedate_to_datetime(value).date().isoformat()
    except (TypeError, ValueError):
        return None


def norm(url: str) -> str:
    p = urlparse(url)
    return f"{p.netloc.lower()}{p.path.rstrip('/')}"


# ---- GitHub and PyPI ----

def from_github(url: str) -> str | None:
    p = urlparse(url)
    if p.netloc != "github.com":
        return None
    parts = p.path.strip("/").split("/")
    if len(parts) < 2:
        return None
    owner, repo = parts[:2]
    api = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=1"
    if len(parts) > 4 and parts[2] == "tree":
        api += f"&sha={parts[3]}&path={'/'.join(parts[4:])}"
    headers = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    body, _ = fetch(api, headers=headers)
    commits = json.loads(body)
    return to_date(commits[0]["commit"]["committer"]["date"]) if commits else None


def from_pypi(url: str) -> str | None:
    m = re.match(r"https://pypi\.org/project/([^/]+)", url)
    if not m:
        return None
    body, _ = fetch(f"https://pypi.org/pypi/{m.group(1)}/json")
    times = [f["upload_time_iso_8601"] for f in json.loads(body)["urls"]]
    return to_date(max(times)) if times else None


# ---- Pages ----

META_PATTERNS = [
    r'"dateModified"\s*:\s*"([^"]+)"',
    r'<meta[^>]+(?:property|name|itemprop)="(?:article:modified_time|og:updated_time|dateModified|last-modified|ms\.date)"[^>]+content="([^"]+)"',
    r'<meta[^>]+content="([^"]+)"[^>]+(?:property|name|itemprop)="(?:article:modified_time|og:updated_time|dateModified|last-modified|ms\.date)"',
    r'<time[^>]+itemprop="dateModified"[^>]+datetime="([^"]+)"',
    r'<time[^>]+datetime="([^"]+)"[^>]+itemprop="dateModified"',
]


def from_metadata(html: str) -> str | None:
    found = []
    for pat in META_PATTERNS:
        found += [d for d in map(to_date, re.findall(pat, html, re.I)) if d]
    return max(found) if found else None


class TextExtractor(HTMLParser):
    """Collect visible text, preferring <main> or <article> when present."""

    SKIP = {"script", "style", "noscript", "svg", "nav", "header", "footer", "form", "template"}

    def __init__(self):
        super().__init__()
        self.skip = 0
        self.main = 0
        self.all, self.primary = [], []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag in ("main", "article"):
            self.main += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        elif tag in ("main", "article") and self.main:
            self.main -= 1

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.all.append(data.strip())
            if self.main:
                self.primary.append(data.strip())


def content_hash(body: bytes, content_type: str) -> str:
    if "html" not in content_type:
        return hashlib.sha256(body).hexdigest()
    parser = TextExtractor()
    parser.feed(body.decode("utf-8", "replace"))
    text = " ".join(parser.primary or parser.all)
    return hashlib.sha256(" ".join(text.split()).encode()).hexdigest()


# ---- Sitemaps ----

_sitemaps: dict[str, dict[str, str]] = {}
_host_locks: dict[str, Lock] = {}
_locks_lock = Lock()


def sitemap_for(host: str) -> dict[str, str]:
    """Map normalized URL to lastmod for a host, within a time budget so huge sites give up."""
    with _locks_lock:
        lock = _host_locks.setdefault(host, Lock())
    with lock:
        if host in _sitemaps:
            return _sitemaps[host]
        lastmods: dict[str, str] = {}
        queue = []
        try:
            robots, _ = fetch(f"https://{host}/robots.txt")
            queue = re.findall(r"(?im)^sitemap:\s*(\S+)", robots.decode("utf-8", "replace"))
        except Exception:
            pass
        queue = queue or [f"https://{host}/sitemap.xml"]
        seen, deadline = 0, time.monotonic() + SITEMAP_BUDGET_SECONDS
        while queue and seen < MAX_SITEMAPS and time.monotonic() < deadline:
            url = queue.pop(0)
            seen += 1
            try:
                body, _ = fetch(url, accept="application/xml")
            except Exception:
                continue
            xml = body.decode("utf-8", "replace")
            if "<sitemapindex" in xml:
                queue += re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
                continue
            for block in re.findall(r"<url>(.*?)</url>", xml, re.S):
                loc = re.search(r"<loc>\s*([^<\s]+)\s*</loc>", block)
                mod = re.search(r"<lastmod>\s*([^<\s]+)\s*</lastmod>", block)
                if loc and mod and to_date(mod.group(1)):
                    lastmods[norm(loc.group(1))] = to_date(mod.group(1))
        _sitemaps[host] = lastmods
        return lastmods


# ---- Resolution ----

def resolve(url: str, prev: dict, today: str) -> dict:
    host = urlparse(url).netloc.lower()
    api = {"github.com": ("github", from_github), "pypi.org": ("pypi", from_pypi)}.get(host)
    if api:
        updated = api[1](url)
        if updated:
            return {"updated": updated, "source": api[0]}

    body, headers = fetch(url, accept="text/html,application/xhtml+xml,*/*")
    ctype = headers.get("Content-Type", "")
    digest = content_hash(body, ctype)
    record = {"hash": digest}
    # Some sites stamp build time into their dates. A newer date on unchanged text is noise.
    if prev.get("hash") == digest and prev.get("updated") and prev.get("source") != "content-change":
        return {**record, "updated": prev["updated"], "source": prev["source"]}

    if "html" in ctype:
        updated = from_metadata(body.decode("utf-8", "replace"))
        if updated:
            return {**record, "updated": updated, "source": "page-metadata"}

    updated = sitemap_for(host).get(norm(url))
    if updated:
        return {**record, "updated": updated, "source": "sitemap"}

    if "html" not in ctype and headers.get("Last-Modified"):
        updated = to_date(headers["Last-Modified"])
        if updated:
            return {**record, "updated": updated, "source": "http-header"}

    if prev.get("hash") and prev["hash"] != digest:
        return {**record, "updated": today, "source": "content-change"}
    since = prev.get("tracking_since", today) if prev.get("hash") else today
    return {**record, "updated": prev.get("updated") if prev.get("hash") else None,
            "source": "content-change", "tracking_since": since}


def main() -> int:
    data = yaml.safe_load(REGISTRY.read_text())
    urls = sorted({e["url"] for e in data["entries"]} | {p["url"] for p in data["providers"]})
    old = json.loads(FRESHNESS.read_text()) if FRESHNESS.exists() else {"links": {}}
    today = datetime.now(timezone.utc).date().isoformat()

    def work(url):
        prev = old["links"].get(url, {})
        try:
            return url, resolve(url, prev, today), None
        except Exception as exc:
            return url, prev or {"updated": None, "source": "unreachable"}, exc

    links, failures = {}, []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, record, exc in pool.map(work, urls):
            links[url] = {k: v for k, v in record.items() if v is not None}
            if exc:
                failures.append(f"{url}: {exc}")

    FRESHNESS.write_text(json.dumps({"checked": today, "links": links}, indent=2, sort_keys=True) + "\n")
    counts: dict[str, int] = {}
    for r in links.values():
        key = r["source"] if r.get("updated") else "unknown"
        counts[key] = counts.get(key, 0) + 1
    print(f"Wrote {FRESHNESS} ({len(links)} links): {dict(sorted(counts.items()))}")
    for f in failures:
        print(f"  kept previous record, fetch failed: {f}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
