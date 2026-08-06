# OWASP Open Source Intelligence Standard

> **Current release:** [OOVS v0.1.0](oovs/v0.1/standard.md) — ten testable requirements for assessing an OSINT workflow or intelligence product.

The OWASP Open Source Intelligence Standard (OOSIS) is a community-led programme for safer, more testable, and more interoperable open-source intelligence. Its normative core is the **OWASP OSINT Verification Standard (OOVS)**.

## Start here

- Read the [OOVS v0.1.0 standard](oovs/v0.1/standard.md).
- Use the [machine-readable requirements](oovs/v0.1/requirements.json) and [acceptance tests](oovs/v0.1/tests.json) in your own tooling.
- Record results with the [assessment schema](oovs/v0.1/assessment.schema.json) and [worked example](oovs/v0.1/examples/synthetic-assessment.json).
- Review the [release notes](releases/v0.1.0/README.md), [safety policy](docs/safety-rights-and-misuse-policy.md), [governance](GOVERNANCE.md), and [prior-art positioning](docs/prior-art-and-positioning.md).

## What OOVS v0.1.0 gives you

| Capability | How it is delivered |
| --- | --- |
| A testable assurance baseline | Ten L1 requirements with objectives, evidence, procedures, and pass criteria |
| Two clear assessment targets | A defined workflow or a defined intelligence product |
| Portable results | JSON Schema for assessment output, plus a worked synthetic example |
| Automatable adoption | Requirements, tests, and schemas published as data, not only prose |
| Verification discipline | Source-origin checks so repeated reporting is not mistaken for independent corroboration |
| Rights-aware controls | Purpose, minimisation, provenance, safeguarding, AI accountability, dissemination, and correction |
| Interoperability grounding | Conservative mappings to established public guidance |

## Programme assets

| Asset | Available now | Purpose |
| --- | --- | --- |
| **OOVS** | v0.1.0 released | Normative verification requirements, tests, and assessment format |
| **OIG** | 0.1 preview schema and synthetic graph | Minimal graph model for provenance-preserving exchange |
| **OTTM** | 0.1 preview schema and first technique record | Structured technique and tool-capability vocabulary |
| **OOTG** | Scenario template | Practitioner testing scenarios with safe fixtures |
| Top 10, packs, benchmarks, landscape, translations, reference flow | Published method and design notes | Roadmap items built on OOVS implementation evidence |

The [roadmap](docs/roadmap.md) sequences the next release: a reproducible synthetic cyber-exposure/CTI vertical slice built on OOVS.

## Scope of the standard

OOVS assesses a defined workflow or product against published requirements. Within that scope it is designed to be used immediately by security teams, investigators, journalists, NGOs, researchers, and public-interest organisations.

Like other voluntary standards, OOVS is not a certification or accreditation scheme, does not determine legal compliance or evidentiary admissibility, and does not imply endorsement by any government, agency, court, or vendor. It complements the [Berkeley Protocol](https://www.ohchr.org/sites/default/files/2022-04/OHCHR_BerkeleyProtocol.pdf), [ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)/[206](https://www.dni.gov/files/documents/ICD/ICD-206.pdf), [W3C PROV](https://www.w3.org/TR/prov-overview/), [STIX/TAXII](https://www.oasis-open.org/standard/stix-version-2-1/), and [CASE/UCO](https://caseontology.org/), and it is a standard rather than an intelligence platform such as OpenCTI, MISP, or Aleph.

## Validate the repository

Python 3.10 or newer is recommended.

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-validation.txt
python3 scripts/validate_assets.py
```

Validation covers JSON Schema conformance, cross-file semantics, Markdown/JSON requirement parity, positive and expected-failure fixtures, local documentation links, and release-manifest file hashes. The same command runs in [CI](.github/workflows/validate-structured-assets.yml).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and the [Code of Conduct](CODE_OF_CONDUCT.md). Implementation results, assessor feedback, technique records, mappings, translations, and reviews are all welcome.

Use synthetic, consented, anonymised, or non-sensitive public examples. Do not submit personal data, live-case material, victim information, target lists, credentials, or harmful operational detail.

## License

Copyright © 2026 OWASP Foundation and contributors.

Unless a file states otherwise, documentation and structured standard content in this repository are licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](LICENSE) (CC BY-SA 4.0). You may share and adapt the material, including commercially, provided you give appropriate credit, link to the license, indicate changes, and license your contributions under the same terms.

When citing the standard, reference the asset, version, and requirement identifier, for example `OWASP OOVS v0.1.0, OOVS-v0.1.0-04`.
