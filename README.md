<!-- GENERATED FILE. Edit scripts/README.template.md or registry/focus-ecosystem.yaml, then run scripts/build_readme.py. -->
# FOCUS Ecosystem

[![Link check](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/link-check.yml/badge.svg)](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/link-check.yml)
[![Link freshness](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/freshness.yml/badge.svg)](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/freshness.yml)
[![Spec freshness](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/spec-version-watch.yml/badge.svg)](https://github.com/beau-finopsorg/focus-ecosystem/actions/workflows/spec-version-watch.yml)

One index of everything around the FinOps Open Cost and Usage Specification (FOCUS): the spec, column and use case libraries, sandbox, validator, converters, tools, conformance program, and the data generators that publish FOCUS.

FOCUS is an open specification that defines how technology billing data generators produce consistent cost and usage datasets. This repo links to that work. It does not host or modify the specification. It also hosts two unofficial community landscape pages on GitHub Pages at https://beau-finopsorg.github.io/focus-ecosystem/.

Latest spec release: **v1.4**. In progress: **v1.5**. Registry last verified: **2026-11-20**.

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

**Updated** shows when the linked resource itself last changed, checked weekly (last check: **2026-11-21**).

🟢 within 90 days · 🟡 within a year · 🔴 over a year · ⚪ the source publishes no date and has not changed since tracking began

Dates come from commit history, package releases, page metadata, or sitemaps. A date marked \* is when the weekly check first saw the page text change, so it is accurate to within a week.

### Specification

The normative FOCUS specification, its releases, and its source.

| Name | Type | Description | Updated |
|---|---|---|---|
| [FOCUS Specification v1.4 (latest)](https://focus.finops.org/docs/specification/v1-4/) | doc | Latest published release. 123 columns, 5 datasets. | ⚪ Not dated |
| [FOCUS Specification v1.3](https://focus.finops.org/docs/specification/v1-3/) | doc | 78 columns, 3 datasets. | ⚪ Not dated |
| [FOCUS Specification v1.2](https://focus.finops.org/docs/specification/v1-2/) | doc | 57 columns. Introduced SaaS and PaaS mappings. | ⚪ Not dated |
| [FOCUS Specification v1.1](https://focus.finops.org/docs/specification/v1-1/) | doc | 50 columns. | ⚪ Not dated |
| [FOCUS Specification v1.0](https://focus.finops.org/docs/specification/v1-0/) | doc | First general availability release. 43 columns. | ⚪ Not dated |
| [FOCUS Specification v0.5](https://focus.finops.org/docs/specification/v0-5/) | doc | Pre-GA release. 21 columns. | ⚪ Not dated |
| [FOCUS 1.5 Release Overview](https://focus.finops.org/focus-1-5-release-scope/) | doc | Scope of the in-progress 1.5 release, including AI token billing labels and a SKU Price dataset. | 🟢 2026-11-13 |
| [FOCUS_Spec](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec) | repo | Source of the specification. Active development happens on the working_draft branch. | 🟢 2026-11-19 |
| [FOCUS v1.3 PDF](https://focus.finops.org/wp-content/uploads/2025/12/FOCUS_spec-v1_3.pdf) | doc | Published PDF of v1.3. | 🟡 2025-12-09 |
| [FOCUS v1.2 PDF](https://focus.finops.org/wp-content/uploads/2025/05/FOCUS-spec-v1_2.pdf) | doc | Published PDF of v1.2. | 🔴 2025-05-30 |
| [FOCUS v1.1 PDF](https://focus.finops.org/wp-content/uploads/2024/11/FOCUS-spec-v1_1.pdf) | doc | Published PDF of v1.1. | 🔴 2024-11-08 |

### Column Library and Data Model

Column definitions, schema reference, and machine-readable access.

| Name | Type | Description | Updated |
|---|---|---|---|
| [Column Library](https://focus.finops.org/docs/column-library/) | site | Definitions for every FOCUS column with category, dataset, and version history. | 🟡 2026-07-31 |
| [FOCUS Data Model (spreadsheet)](https://focus.finops.org/docs/tools-assets/assets/data-model/) | doc | Flat, filterable reference of every dataset, column, feature level, and allowed value. | 🟡 2026-08-19 |

### Use Case Library

FinOps scenarios with SQL queries written against FOCUS columns.

| Name | Type | Description | Updated |
|---|---|---|---|
| [Use Case Library (spec section)](https://focus.finops.org/docs/specification/v1-2/sections/use-case-library/) | doc | Use cases organized by persona and capability. Individual use cases live under /docs/use-cases/<version>/<slug>/ and number 100+. | ⚪ Not dated |
| [Example use case page (v1.4)](https://focus.finops.org/docs/use-cases/v1-4/allocate-multi-currency-charges-per-application-2/) | doc | Shows the per-use-case page format with linked columns, personas, and SQL. | 🟡 2026-06-03 |

### Sandbox and Sample Data

Anonymized real FOCUS billing data you can query or download.

| Name | Type | Description | Updated |
|---|---|---|---|
| [FOCUS Sandbox](https://focus.finops.org/sandbox/) | site | Run Use Case Library SQL against anonymized multi-cloud FOCUS data (September 2024 billing month). | 🟡 2026-07-31 |
| [Query Sandbox docs](https://focus.finops.org/docs/tools-assets/tools/query-sandbox/) | doc | Documentation page for the sandbox. | 🟡 2026-07-31 |
| [FOCUS Sandbox and sample data available now](https://www.finops.org/insights/focus-sandbox/) | doc | How the sandbox was built and how to use it (December 2024). | 🔴 2025-04-08 |
| [FOCUS-Sample-Data](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS-Sample-Data) | repo | Repository to store and share samples of FOCUS datasets. | 🔴 2024-12-10 |

### Validator

Check a dataset against a specific FOCUS version.

| Name | Type | Description | Updated |
|---|---|---|---|
| [focus_validator](https://github.com/finopsfoundation/focus_validator) | repo | Python application that validates datasets against a FOCUS version. Used by the Conformance Program. | 🟡 2026-08-05 |
| [focus-validator on PyPI](https://pypi.org/project/focus-validator/) | package | Package listing. PyPI text still references the older focus-spec-validator repo name, so prefer the GitHub repo above for current docs. | 🟡 2026-08-05 |
| [FOCUS Validator docs](https://focus.finops.org/docs/tools-assets/tools/focus-validator/) (unverified) | doc | Documentation page on focus.finops.org (content was empty when checked). | 🟡 2026-07-31 |

### Converters and Mapping

Turn native billing data into FOCUS.

| Name | Type | Description | Updated |
|---|---|---|---|
| [focus_converters](https://github.com/finopsfoundation/focus_converters) | repo | CLI that converts AWS, Google Cloud, Azure, and Oracle Cloud billing data to FOCUS using YAML rules. MIT licensed. | 🟢 2026-11-04 |
| [focus-converter on PyPI](https://pypi.org/project/focus-converter/) | package | Install with pip install focus_converter. | 🔴 2024-06-06 |
| [focus_converter_oraclecloud](https://github.com/finopsfoundation/focus_converter_oraclecloud) | repo | Oracle Cloud converter repository. No description on GitHub. | 🔴 2023-07-12 |
| [focus_converter_googlecloud](https://github.com/finopsfoundation/focus_converter_googlecloud) | repo | Google Cloud converter repository. No description on GitHub. | 🔴 2023-06-18 |
| [FOCUS_Mapping_Templates](https://github.com/finopsfoundation/FOCUS_Mapping_Templates) | repo | Open repository of FOCUS mapping templates. | 🟢 2026-11-17 |

### Other Tools

Supporting utilities, requirements tooling, and AI access.

| Name | Type | Description | Updated |
|---|---|---|---|
| [FOCUS MCP Server](https://focus.finops.org/docs/tools-assets/tools/focus-mcp-server/) | tool | Read-only MCP access to the spec, columns, use cases, queries, and providers. Connection URL: https://focus.finops.org/wp-json/focus/v1/mcp | 🟡 2026-07-31 |
| [focus_scrub](https://github.com/finopsfoundation/focus_scrub) | repo | Tool for scrubbing PII from FOCUS datasets. | 🟡 2026-03-19 |
| [focus_requirements_model_analyzer](https://github.com/FinOps-Open-Cost-and-Usage-Spec/focus_requirements_model_analyzer) | repo | Model and view FOCUS normative requirements. | 🟡 2026-06-06 |
| [FOCUS_RM_Extraction](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_RM_Extraction) | repo | Extract and compare the Requirements Model for FOCUS development. | 🟢 2026-11-02 |
| [focus-otel-semconv](https://github.com/FinOps-Open-Cost-and-Usage-Spec/focus-otel-semconv) | repo | Community specification repository for a focus.* identifier registry (OpenTelemetry semantic conventions). Fork. | 🟡 2026-07-25 |
| [focus-tools](https://github.com/beau-finopsorg/focus-tools) | repo | Unofficial community schema maps (FOCUS 1.0 through 1.5) and reference architectures. Version 1.5 is a candidate / pre-release. | ⚪ Not dated |
| [focus-tools (pages)](https://beau-finopsorg.github.io/focus-tools/) | site | Published site for the unofficial community schema maps and reference architectures. | ⚪ Not dated |

### Conformance and Governance

Certification, project charter, and contribution mechanics.

| Name | Type | Description | Updated |
|---|---|---|---|
| [Certified FOCUS Conformance Program](https://focus.finops.org/certified-focus-program/) | program | Certification guide, branding rules, and requirements for data providers. | 🟡 2026-02-19 |
| [FinOps Certified FOCUS Conformant (requirements)](https://www.finops.org/certification-for-organizations/finops-certified-focus-conformant/) | program | Steps to certify, including sample data and the validator run. | 🟢 2026-09-01 |
| [foundation (FOCUS)](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation) | repo | FOCUS project charter and legal documentation, including the membership agreement package. | 🟢 2026-10-22 |
| [EasyCLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA) | repo | Setup for EasyCLA, which manages specification membership signatures. | 🔴 2025-06-24 |
| [Become a Contributor](https://focus.finops.org/contribute/) | doc | How to join FOCUS working groups and contribute. | 🟡 2026-04-10 |

### Adoption and Guides

Who produces and consumes FOCUS, and how to start.

| Name | Type | Description | Updated |
|---|---|---|---|
| [focus.finops.org](https://focus.finops.org/) | site | Home of the FOCUS project. | 🟢 2026-11-18 |
| [What is FOCUS?](https://focus.finops.org/what-is-focus/) | doc | Overview for newcomers. | 🟡 2026-06-10 |
| [FOCUS FAQs](https://focus.finops.org/faqs/) | doc | Frequently asked questions. | 🟡 2026-06-07 |
| [Get Started with FOCUS Datasets](https://focus.finops.org/docs/implementation/get-started/get-started-with-focus-datasets/) | doc | How to get FOCUS data from each provider. | 🟢 2026-11-18 |
| [Papers and guides](https://focus.finops.org/docs/tools-assets/assets/supporting-assets/) | doc | Papers on FinOps data workflows, data center cost modeling, and provider pipelines. | 🟡 2026-07-31 |
| [FOCUS for Technology Categories](https://focus.finops.org/technology-categories/) | doc | How FOCUS applies from public cloud to AI, with mapping guidance. | 🟡 2026-06-08 |
| [FOCUS Adoption](https://focus.finops.org/adoption/) | doc | Generators and consumers of FOCUS data. | 🟡 2026-08-17 |
| [FinOps Vendors Adopting FOCUS](https://focus.finops.org/adoption/finops-vendors/) | doc | FinOps tools and their level of FOCUS adoption. | 🟡 2025-12-05 |
| [FinOps Practitioners Adopting FOCUS](https://focus.finops.org/adoption/finops-practitioners/) | doc | Practitioner success stories. | 🟡 2025-12-05 |
| [SaaS Vendors Adopting FOCUS](https://focus.finops.org/adoption/saas-vendors/) | doc | SaaS vendor adoption. | 🟡 2025-12-05 |
| [FinOps Foundation FOCUS topic page](https://www.finops.org/topic/focus/) | site | FOCUS content on finops.org. | 🟢 2026-11-19 |
| [focus-gap-analyses](https://github.com/beau-finopsorg/focus-gap-analyses) | repo | Unofficial community gap analyses of 98 data generators, based on public documentation only. Ratings are not certification results. | ⚪ Not dated |
| [focus-gap-analyses (pages)](https://beau-finopsorg.github.io/focus-gap-analyses/) | site | Readiness scorecard, by-company index, and HTML copies of the 98 unofficial community gap analyses. | ⚪ Not dated |
| [focus-ecosystem (pages)](https://beau-finopsorg.github.io/focus-ecosystem/) | site | Unofficial community landscape pages: the FOCUS ecosystem landscape (adoption data retrieved 2026-09-08) and the data generator readiness landscape. Ratings are not certification results. | ⚪ Not dated |

### Community

Where to ask questions and give feedback.

| Name | Type | Description | Updated |
|---|---|---|---|
| [Give Feedback](https://focus.finops.org/feedback/) | community | GitHub issues, the \#chat-focus Slack channel in the FinOps Foundation community, and FOCUS community calls. | 🟡 2025-12-05 |

### Data generators publishing FOCUS

Providers listed in the FOCUS provider directory.

| Provider | Getting started | Updated |
|---|---|---|
| Alibaba Cloud | [Link](https://www.alibabacloud.com/help/en/user-center/user-guide/export-alibaba-cloud-standard-billing-focus) | ⚪ Not dated |
| AWS | [Link](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-standard.html) | ⚪ Not dated |
| Cloudflare | [Link](https://developers.cloudflare.com/api/resources/billing/) | ⚪ Not dated |
| CoreWeave | [Link](https://docs.coreweave.com/billing/focus-export-api) | 🟢 2026-11-09 |
| Databricks | [Link](https://github.com/databricks-solutions/cloud-infra-costs/tree/main/focus) | 🟢 2026-10-30 |
| Google Cloud | [Link](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup) | ⚪ Not dated |
| Grafana Cloud | [Link](https://grafana.com/docs/grafana-cloud/cost-management-and-billing/focus/) | ⚪ Not dated |
| Huawei Cloud | [Link](https://support.huaweicloud.com/intl/en-us/usermanual-cost/costcenter_000002_03_07.html) | ⚪ Not dated |
| Microsoft Azure | [Link](https://learn.microsoft.com/azure/cost-management-billing/costs/tutorial-export-acm-data) | 🔴 2025-06-26 |
| MongoDB | [Link](https://www.mongodb.com/products/updates/now-ga-mongodb-atlas-support-for-focus-v1-3-cost-and-usage-reports/) | ⚪ Not dated |
| Nebius | [Link](https://docs.nebius.com/signup-billing/usage/export) | 🟢 2026-11-20 |
| Oracle Cloud | [Link](https://docs.oracle.com/iaas/Content/Billing/Tasks/accessingusagereports.htm) | ⚪ Not dated |
| OVHcloud | [Link](https://docs.ovhcloud.com/en/guides/manage-and-operate/cost-center/export-billing-data-to-bucket) | ⚪ Not dated |
| Redis | [Link](https://redis.io/docs/latest/operate/rc/api/examples/generate-cost-report/) | 🟢 2026-09-25 |
| Snowflake | [Link](https://docs.snowflake.com/en/sql-reference/billing/focus_cost_usage_v1_3) | ⚪ Not dated |
| STACKIT | [Link](https://docs.stackit.cloud/platform/cost-and-billing/focus/) | ⚪ Not dated |
| Tencent Cloud | [Link](https://intl.cloud.tencent.com/document/product/555/67495) | ⚪ Not dated |
| Vercel | [Link](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges) | 🟢 2026-11-05 |

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
