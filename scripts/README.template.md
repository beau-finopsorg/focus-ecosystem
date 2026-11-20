<!-- GENERATED FILE. Edit scripts/README.template.md or registry/focus-ecosystem.yaml, then run scripts/build_readme.py. -->
# FOCUS Ecosystem

One index of everything around the FinOps Open Cost and Usage Specification (FOCUS): the spec, column and use case libraries, sandbox, validator, converters, tools, conformance program, and the data generators that publish FOCUS.

FOCUS is an open specification that defines how technology billing data generators produce consistent cost and usage datasets. This repo only links to the work. It does not host or modify it.

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

{{INDEX}}
## GitHub organizations

FOCUS work is split across two GitHub organizations.

- [FinOps-Open-Cost-and-Usage-Spec](https://github.com/FinOps-Open-Cost-and-Usage-Spec): the specification, sample data, and governance.
- [finopsfoundation](https://github.com/finopsfoundation): validator, converters, mapping templates, and other tooling.

## Machine-readable registry

[`registry/focus-ecosystem.yaml`](registry/focus-ecosystem.yaml) is the source of truth. This README is generated from it, so edit the YAML and run `python3 scripts/build_readme.py`. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Keeping this current

- A weekly workflow checks every link and opens an issue when one breaks.
- Every pull request checks that this README matches the registry.
- Open questions about coverage are tracked in [docs/backlog.md](docs/backlog.md).

## Trademarks

The authoritative sources are the linked projects. FOCUS and related marks belong to their owners. See the [project policies](https://lfprojects.org).

## License

[MIT](LICENSE) for the contents of this repo. Linked projects carry their own licenses. The FOCUS specification is published under CC BY 4.0.
