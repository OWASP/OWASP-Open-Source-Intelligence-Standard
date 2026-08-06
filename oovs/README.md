# OOVS — OWASP OSINT Verification Standard

OOVS is the normative assurance core of the OOSIS programme. It defines testable requirements for a bounded OSINT workflow or intelligence product.

## Current release

**OOVS v0.1.0** establishes the L1 Foundational baseline: ten requirements, ten acceptance tests, and a portable assessment format.

- [Standard](v0.1/standard.md)
- [Machine-readable requirements](v0.1/requirements.json)
- [Requirement catalogue schema](v0.1/requirements.schema.json)
- [Acceptance tests](v0.1/tests.json)
- [Assessment-result schema](v0.1/assessment.schema.json)
- [Worked synthetic assessment](v0.1/examples/synthetic-assessment.json)
- [External mappings](v0.1/mappings.md)
- [Release notes](../releases/v0.1.0/README.md)

## Scope

The L1 baseline is consequence-sensitive: verification depth and safeguards scale with the impact of an error, rather than with a job title. It supports two assessment targets — a defined **workflow** or a defined **intelligence product**.

Later versions can add assurance depth and profiles where implementation evidence shows a distinct risk, consequence, or interoperability need.

## How to use it

1. Define the target, intended decision, scope, exclusions, period, sample, and high-consequence factors.
2. Assess every requirement as `Implemented`, `Partially implemented`, `Not implemented`, or `Not applicable`, with controlled evidence references.
3. Validate the result against `assessment.schema.json`.
4. Publish scope, method, aggregate results, and limitations; distinguish self-assessment from independent assessment.
5. Send implementation feedback through the repository issue templates, without personal, case, victim, or operational data.

Run local validation from the repository root:

```sh
python3 -m pip install -r requirements-validation.txt
python3 scripts/validate_assets.py
```

## Versioning

Requirement identifiers use `OOVS-v0.1.0-NN` and acceptance tests use `OOVS-v0.1.0-TNN`. Identifiers are stable within the 0.1 line under the [release policy](../programme/RELEASE_POLICY.md), so reports and tooling should always cite the version.
