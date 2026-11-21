<!-- GENERATED FILE. Edit scripts/README.template.md or registry/focus-ecosystem.yaml, then run scripts/build_readme.py. -->
# FOCUS Ecosystem

[![Link check](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/link-check.yml/badge.svg)](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/link-check.yml)
[![Link freshness](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/freshness.yml/badge.svg)](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/freshness.yml)
[![Spec freshness](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/spec-version-watch.yml/badge.svg)](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/spec-version-watch.yml)

One index of everything around the FinOps Open Cost and Usage Specification (FOCUS): the spec, column and use case libraries, sandbox, validator, converters, tools, conformance program, and the data generators that publish FOCUS.

FOCUS is an open specification that defines how technology billing data generators produce consistent cost and usage datasets. This repo links to that work. It does not host or modify the specification. It also hosts two unofficial community landscape pages on GitHub Pages at https://beau-finopsorg.github.io/focus-ecosystem/.

Latest spec release: **v1.4**. In progress: **v1.5**. Registry last verified: **{{VERIFIED}}**.

## Start here

| If you want to | Go to |
|---|---|
| Understand FOCUS | [What is FOCUS?](https://focus.finops.org/what-is-focus/) |
| Look up a column | [Column Library](https://focus.finops.org/docs/column-library/) |
| Try queries on real data | [FOCUS Sandbox](https://focus.finops.org/sandbox/) |
| Check a dataset | [focus_validator](https://github.com/finopsfoundation/focus_validator) |
| Convert billing data | [focus_converters](https://github.com/finopsfoundation/focus_converters) |
| Ask an AI assistant about the spec | [FOCUS MCP Server](https://focus.finops.org/docs/tools-assets/tools/focus-mcp-server/) |
| Contribute | [Become a Contributor](https://focus.finops.org/contribute/) |

## Index

**Updated** shows when the linked resource itself last changed, checked weekly (last check: **{{CHECKED}}**).

🟢 within 90 days · 🟡 within a year · 🔴 over a year · ⚪ the source publishes no date and has not changed since tracking began

Dates come from commit history, package releases, page metadata, or sitemaps. A date marked \* is when the weekly check first saw the page text change, so it is accurate to within a week.

{{INDEX}}
## GitHub organizations

FOCUS work is split across two GitHub organizations.

- [FinOps-Open-Cost-and-Usage-Spec](https://github.com/FinOps-Open-Cost-and-Usage-Spec): the specification, sample data, and governance.
- [finopsfoundation](https://github.com/finopsfoundation): validator, converters, mapping templates, and other tooling.

## Related repos

Unofficial community projects by Beau Nelford. They are not official FOCUS, FinOps Foundation, or Linux Foundation publications.

| Repo | Site | What it is |
|---|---|---|
| [focus-ecosystem](https://github.com/beau-finopsorg/focus-ecosystem) (this repo) | [Pages](https://beau-finopsorg.github.io/focus-ecosystem/) | This index, plus the ecosystem landscape and data generator readiness landscape pages. |
| [focus-gap-analyses](https://github.com/beau-finopsorg/focus-gap-analyses) | [Pages](https://beau-finopsorg.github.io/focus-gap-analyses/) | Readiness scorecard and gap analyses of 98 data generators, based on public documentation only. Ratings are not certification results. |
| [focus-tools](https://github.com/beau-finopsorg/focus-tools) | [Pages](https://beau-finopsorg.github.io/focus-tools/) | Schema maps (FOCUS 1.0 through 1.5) and reference architectures. Version 1.5 is a candidate / pre-release. |

## Machine-readable registry

[`registry/focus-ecosystem.yaml`](registry/focus-ecosystem.yaml) is the source of truth. This README is generated from it, so edit the YAML and run `python3 scripts/build_readme.py`. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Keeping this current

- A weekly workflow checks every link and opens an issue when one breaks.
- A weekly workflow records when each linked resource last changed and opens a pull request with the dates.
- Every pull request checks that this README matches the registry.
- Open questions about coverage are tracked in [docs/backlog.md](docs/backlog.md).

## License and disclaimer

The contents of this repo are under the MIT License. Linked projects keep their own licenses. The FOCUS specification is published under CC BY 4.0.

Names and marks belong to their owners. This repo is not an official publication. See the [project policies](https://lfprojects.org) for marks that belong to their owners.

This is a personal and community project by Beau Nelford, FOCUS Technical Community Architect, acting in a personal and community capacity. It is not an official FOCUS, FinOps Foundation, or Linux Foundation publication. It links to other work and hosts unofficial community landscape pages. It does not host or change the specification, and it does not certify or endorse anything it links to. For feedback on the specification itself, use https://focus.finops.org/feedback/.

See [DISCLAIMER.md](DISCLAIMER.md).
