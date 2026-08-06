# OOSIS Programme Charter

## Mission

Develop open, evidence-led standards and implementation resources that make OSINT workflows and products safer, more reviewable, and more interoperable.

## Canonical naming

- **OOSIS** is the umbrella programme, matching the OWASP project name *OWASP Open Source Intelligence Standard*.
- **OOVS** is the normative OWASP OSINT Verification Standard.
- Other acronyms identify separately versioned programme assets.

These are the only abbreviations used in this repository.

## Principles

- **Mission-led:** every artefact supports a stated decision or protective outcome.
- **Testable:** normative language has evidence, procedure, pass criteria, and limitations.
- **Rights-aware:** authority, necessity, proportionality, minimisation, correction, and safeguarding are design controls.
- **Open and interoperable:** mature standards are mapped or profiled rather than needlessly replaced.
- **Globally reviewable:** legal and regional differences are explicit; no jurisdiction is presented as universal.
- **Accurate status:** published assets are backed by real content, and roadmap items are named as such.

## Asset inventory

| Asset | State | Home |
| --- | --- | --- |
| OOVS | v0.1.0 released | [oovs](../oovs/README.md) |
| OIG | 0.1 preview schema and synthetic graph | [oig](../oig/README.md) |
| OTTM | 0.1 preview schema and first record | [ottm](../ottm/README.md) |
| OOTG | Scenario template published | [ootg](../ootg/README.md) |
| Validation tooling | Available | [scripts](../scripts/validate_assets.py) and [tests](../tests/README.md) |
| OOSIS Top 10 | Methodology published; editions on the roadmap | [concept and method](../docs/top-ten-concept.md) |
| Intelligence Packs, benchmarks, solution landscape, translations, reference flow | On the roadmap | [roadmap](../docs/roadmap.md) |

Directories are created when an asset has content to publish, so the repository structure always reflects delivered work.

## Delivery focus

The active release line is OOVS plus the minimum OIG, OTTM, and OOTG content needed for one synthetic cyber-exposure/CTI vertical slice. A new initiative joins the line when it has an approved charter, a named lead, reviewer capacity, a safe fixture and evidence plan, a measurable release outcome, and a public contact route.

Use the [initiative template](INITIATIVE_TEMPLATE.md) for proposals. See the [release scope](RELEASE_SCOPE.md), [roadmap](../docs/roadmap.md), [governance](../GOVERNANCE.md), [release policy](RELEASE_POLICY.md), and [design review](DESIGN_REVIEW.md).
