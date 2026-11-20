#!/usr/bin/env python3
"""Generate README.md from registry/focus-ecosystem.yaml.

Usage:
  python3 scripts/build_readme.py           # rewrite README.md
  python3 scripts/build_readme.py --check   # exit 1 if README.md is out of date
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry" / "focus-ecosystem.yaml"
README = ROOT / "README.md"
TEMPLATE = ROOT / "scripts" / "README.template.md"


def esc(text: str) -> str:
    return str(text).replace("|", "\\|")


def render(data: dict) -> str:
    entries = data["entries"]
    out = []
    for cat in data["categories"]:
        rows = [e for e in entries if e["category"] == cat["id"]]
        if not rows:
            continue
        out.append(f"### {cat['title']}\n")
        out.append(f"{cat['blurb']}\n")
        out.append("| Name | Type | Description |")
        out.append("|---|---|---|")
        for e in rows:
            flag = " (unverified)" if e.get("status") == "unverified" else ""
            out.append(
                f"| [{esc(e['name'])}]({e['url']}){flag} | {e['kind']} | {esc(e['description'])} |"
            )
        out.append("")
    out.append("### Data generators publishing FOCUS\n")
    out.append("Providers listed in the FOCUS provider directory.\n")
    out.append("| Provider | Getting started |")
    out.append("|---|---|")
    for p in data["providers"]:
        out.append(f"| {esc(p['name'])} | [Link]({p['url']}) |")
    out.append("")
    return "\n".join(out)


def main() -> int:
    data = yaml.safe_load(REGISTRY.read_text())
    ids = [e["id"] for e in data["entries"]]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        print(f"Duplicate ids: {sorted(dupes)}", file=sys.stderr)
        return 2
    cats = {c["id"] for c in data["categories"]}
    bad = [e["id"] for e in data["entries"] if e["category"] not in cats]
    if bad:
        print(f"Unknown category on: {bad}", file=sys.stderr)
        return 2

    newest = max(str(e["verified"]) for e in data["entries"])
    body = TEMPLATE.read_text()
    text = body.replace("{{INDEX}}", render(data)).replace("{{VERIFIED}}", newest)
    if "--check" in sys.argv:
        if not README.exists() or README.read_text() != text:
            print("README.md is out of date. Run: python3 scripts/build_readme.py", file=sys.stderr)
            return 1
        print("README.md is up to date.")
        return 0
    README.write_text(text)
    print(f"Wrote {README} ({len(data['entries'])} entries, {len(data['providers'])} providers).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
