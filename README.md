<!-- GENERATED FILE. Edit scripts/README.template.md or registry/focus-ecosystem.yaml, then run scripts/build_readme.py. -->
# FOCUS Ecosystem

One index of everything around the FinOps Open Cost and Usage Specification (FOCUS): the spec, column and use case libraries, sandbox, validator, converters, tools, conformance program, and the data generators that publish FOCUS.

FOCUS is an open specification that defines how technology billing data generators produce consistent cost and usage datasets. This repo only links to the work. It does not host or modify it.

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

### Specification

The normative FOCUS specification, its releases, and its source.

| Name | Type | Description |
|---|---|---|
| [FOCUS Specification v1.4 (latest)](https://focus.finops.org/docs/specification/v1-4/) | doc | Latest published release. 123 columns, 5 datasets. |
| [FOCUS Specification v1.3](https://focus.finops.org/docs/specification/v1-3/) | doc | 78 columns, 3 datasets. |
| [FOCUS Specification v1.2](https://focus.finops.org/docs/specification/v1-2/) | doc | 57 columns. Introduced SaaS and PaaS mappings. |
| [FOCUS Specification v1.1](https://focus.finops.org/docs/specification/v1-1/) | doc | 50 columns. |
| [FOCUS Specification v1.0](https://focus.finops.org/docs/specification/v1-0/) | doc | First general availability release. 43 columns. |
| [FOCUS Specification v0.5](https://focus.finops.org/docs/specification/v0-5/) | doc | Pre-GA release. 21 columns. |
| [FOCUS 1.5 Release Overview](https://focus.finops.org/focus-1-5-release-scope/) | doc | Scope of the in-progress 1.5 release, including AI token billing labels and a SKU Price dataset. |
| [FOCUS_Spec](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec) | repo | Source of the specification. Active development happens on the working_draft branch. |
| [FOCUS v1.3 PDF](https://focus.finops.org/wp-content/uploads/2025/12/FOCUS_spec-v1_3.pdf) | doc | Published PDF of v1.3. |
| [FOCUS v1.2 PDF](https://focus.finops.org/wp-content/uploads/2025/05/FOCUS-spec-v1_2.pdf) | doc | Published PDF of v1.2. |
| [FOCUS v1.1 PDF](https://focus.finops.org/wp-content/uploads/2024/11/FOCUS-spec-v1_1.pdf) | doc | Published PDF of v1.1. |

### Column Library and Data Model

Column definitions, schema reference, and machine-readable access.

| Name | Type | Description |
|---|---|---|
| [Column Library](https://focus.finops.org/docs/column-library/) | site | Definitions for every FOCUS column with category, dataset, and version history. |
| [FOCUS Data Model (spreadsheet)](https://focus.finops.org/docs/tools-assets/assets/data-model/) | doc | Flat, filterable reference of every dataset, column, feature level, and allowed value. |

### Use Case Library

FinOps scenarios with SQL queries written against FOCUS columns.

| Name | Type | Description |
|---|---|---|
| [Use Case Library (spec section)](https://focus.finops.org/docs/specification/v1-2/sections/use-case-library/) | doc | Use cases organized by persona and capability. Individual use cases live under /docs/use-cases/<version>/<slug>/ and number 100+. |
| [Example use case page (v1.4)](https://focus.finops.org/docs/use-cases/v1-4/allocate-multi-currency-charges-per-application-2/) | doc | Shows the per-use-case page format with linked columns, personas, and SQL. |

### Sandbox and Sample Data

Anonymized real FOCUS billing data you can query or download.

| Name | Type | Description |
|---|---|---|
| [FOCUS Sandbox](https://focus.finops.org/sandbox/) | site | Run Use Case Library SQL against anonymized multi-cloud FOCUS data (September 2024 billing month). |
| [Query Sandbox docs](https://focus.finops.org/docs/tools-assets/tools/query-sandbox/) | doc | Documentation page for the sandbox. |
| [FOCUS Sandbox and sample data available now](https://www.finops.org/insights/focus-sandbox/) | doc | How the sandbox was built and how to use it (December 2024). |
| [FOCUS-Sample-Data](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS-Sample-Data) | repo | Repository to store and share samples of FOCUS datasets. |

### Validator

Check a dataset against a specific FOCUS version.

| Name | Type | Description |
|---|---|---|
| [focus_validator](https://github.com/finopsfoundation/focus_validator) | repo | Python application that validates datasets against a FOCUS version. Used by the Conformance Program. |
| [focus-validator on PyPI](https://pypi.org/project/focus-validator/) | package | Package listing. PyPI text still references the older focus-spec-validator repo name, so prefer the GitHub repo above for current docs. |
| [FOCUS Validator docs](https://focus.finops.org/docs/tools-assets/tools/focus-validator/) (unverified) | doc | Documentation page on focus.finops.org (content was empty when checked). |

### Converters and Mapping

Turn native billing data into FOCUS.

| Name | Type | Description |
|---|---|---|
| [focus_converters](https://github.com/finopsfoundation/focus_converters) | repo | CLI that converts AWS, Google Cloud, Azure, and Oracle Cloud billing data to FOCUS using YAML rules. MIT licensed. |
| [focus-converter on PyPI](https://pypi.org/project/focus-converter/) | package | Install with pip install focus_converter. |
| [focus_converter_oraclecloud](https://github.com/finopsfoundation/focus_converter_oraclecloud) | repo | Oracle Cloud converter repository. No description on GitHub. |
| [focus_converter_googlecloud](https://github.com/finopsfoundation/focus_converter_googlecloud) | repo | Google Cloud converter repository. No description on GitHub. |
| [FOCUS_Mapping_Templates](https://github.com/finopsfoundation/FOCUS_Mapping_Templates) | repo | Open repository of FOCUS mapping templates. |

### Other Tools

Supporting utilities, requirements tooling, and AI access.

| Name | Type | Description |
|---|---|---|
| [FOCUS MCP Server](https://focus.finops.org/docs/tools-assets/tools/focus-mcp-server/) | tool | Read-only MCP access to the spec, columns, use cases, queries, and providers. Connection URL: https://focus.finops.org/wp-json/focus/v1/mcp |
| [focus_scrub](https://github.com/finopsfoundation/focus_scrub) | repo | Tool for scrubbing PII from FOCUS datasets. |
| [focus_requirements_model_analyzer](https://github.com/FinOps-Open-Cost-and-Usage-Spec/focus_requirements_model_analyzer) | repo | Model and view FOCUS normative requirements. |
| [FOCUS_RM_Extraction](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_RM_Extraction) | repo | Extract and compare the Requirements Model for FOCUS development. |
| [focus-otel-semconv](https://github.com/FinOps-Open-Cost-and-Usage-Spec/focus-otel-semconv) | repo | Community specification repository for a focus.* identifier registry (OpenTelemetry semantic conventions). Fork. |

### Conformance and Governance

Certification, project charter, and contribution mechanics.

| Name | Type | Description |
|---|---|---|
| [Certified FOCUS Conformance Program](https://focus.finops.org/certified-focus-program/) | program | Certification guide, branding rules, and requirements for data providers. |
| [FinOps Certified FOCUS Conformant (requirements)](https://www.finops.org/certification-for-organizations/finops-certified-focus-conformant/) | program | Steps to certify, including sample data and the validator run. |
| [foundation (FOCUS)](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation) | repo | FOCUS project charter and legal documentation, including the membership agreement package. |
| [EasyCLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA) | repo | Setup for EasyCLA, which manages specification membership signatures. |
| [Become a Contributor](https://focus.finops.org/contribute/) | doc | How to join FOCUS working groups and contribute. |

### Adoption and Guides

Who produces and consumes FOCUS, and how to start.

| Name | Type | Description |
|---|---|---|
| [focus.finops.org](https://focus.finops.org/) | site | Home of the FOCUS project. |
| [What is FOCUS?](https://focus.finops.org/what-is-focus/) | doc | Overview for newcomers. |
| [FOCUS FAQs](https://focus.finops.org/faqs/) | doc | Frequently asked questions. |
| [Get Started with FOCUS Datasets](https://focus.finops.org/docs/implementation/get-started/get-started-with-focus-datasets/) | doc | How to get FOCUS data from each provider. |
| [Papers and guides](https://focus.finops.org/docs/tools-assets/assets/supporting-assets/) | doc | Papers on FinOps data workflows, data center cost modeling, and provider pipelines. |
| [FOCUS for Technology Categories](https://focus.finops.org/technology-categories/) | doc | How FOCUS applies from public cloud to AI, with mapping guidance. |
| [FOCUS Adoption](https://focus.finops.org/adoption/) | doc | Generators and consumers of FOCUS data. |
| [FinOps Vendors Adopting FOCUS](https://focus.finops.org/adoption/finops-vendors/) | doc | FinOps tools and their level of FOCUS adoption. |
| [FinOps Practitioners Adopting FOCUS](https://focus.finops.org/adoption/finops-practitioners/) | doc | Practitioner success stories. |
| [SaaS Vendors Adopting FOCUS](https://focus.finops.org/adoption/saas-vendors/) | doc | SaaS vendor adoption. |
| [FinOps Foundation FOCUS topic page](https://www.finops.org/topic/focus/) | site | FOCUS content on finops.org. |

### Community

Where to ask questions and give feedback.

| Name | Type | Description |
|---|---|---|
| [Give Feedback](https://focus.finops.org/feedback/) | community | GitHub issues, the |

### Data generators publishing FOCUS

Providers listed in the FOCUS provider directory.

| Provider | Getting started |
|---|---|
| Alibaba Cloud | [Link](https://www.alibabacloud.com/help/en/user-center/user-guide/export-alibaba-cloud-standard-billing-focus) |
| AWS | [Link](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-standard.html) |
| Cloudflare | [Link](https://developers.cloudflare.com/api/resources/billing/) |
| CoreWeave | [Link](https://docs.coreweave.com/billing/focus-export-api) |
| Databricks | [Link](https://github.com/databricks-solutions/cloud-infra-costs/tree/main/focus) |
| Google Cloud | [Link](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup) |
| Grafana Cloud | [Link](https://grafana.com/docs/grafana-cloud/cost-management-and-billing/focus/) |
| Huawei Cloud | [Link](https://support.huaweicloud.com/intl/en-us/usermanual-cost/costcenter_000002_03_07.html) |
| Microsoft Azure | [Link](https://learn.microsoft.com/azure/cost-management-billing/costs/tutorial-export-acm-data) |
| MongoDB | [Link](https://www.mongodb.com/products/updates/now-ga-mongodb-atlas-support-for-focus-v1-3-cost-and-usage-reports/) |
| Nebius | [Link](https://docs.nebius.com/signup-billing/usage/export) |
| Oracle Cloud | [Link](https://docs.oracle.com/iaas/Content/Billing/Tasks/accessingusagereports.htm) |
| OVHcloud | [Link](https://docs.ovhcloud.com/en/guides/manage-and-operate/cost-center/export-billing-data-to-bucket) |
| Redis | [Link](https://redis.io/docs/latest/operate/rc/api/examples/generate-cost-report/) |
| Snowflake | [Link](https://docs.snowflake.com/en/sql-reference/billing/focus_cost_usage_v1_3) |
| STACKIT | [Link](https://docs.stackit.cloud/platform/cost-and-billing/focus/) |
| Tencent Cloud | [Link](https://intl.cloud.tencent.com/document/product/555/67495) |
| Vercel | [Link](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges) |

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
