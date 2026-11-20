# Contributing

Add or fix an entry by editing [`registry/focus-ecosystem.yaml`](registry/focus-ecosystem.yaml). Do not edit `README.md` directly.

1. Add an entry under `entries` with a unique `id`, a `category` from the list at the top of the file, a `kind`, the canonical `url`, a one-sentence `description`, the `owner`, a `status`, and today's date in `verified`.
2. Run `pip install pyyaml` then `python3 scripts/build_readme.py`.
3. Commit both the YAML and the regenerated `README.md`.
4. Open a pull request. CI checks that the README matches the registry and that links resolve.

## Rules

- Link to the canonical source, not a mirror or a blog post about it, unless the post is the only documentation.
- Describe what the thing does. Leave out marketing language and opinions.
- Set `status: unverified` if you could not open the link or confirm the claim. Unverified entries are shown as such and listed in the backlog.
- Mark retired projects `status: archived` rather than deleting them, so people can find out why a link went stale.
- Keep descriptions to one sentence, and use plain text without em dashes.

## When the spec ships a release

Update the version line in `scripts/README.template.md`, add the new `spec-site-vX-Y` entry and its PDF if published, and refresh counts in the descriptions.
