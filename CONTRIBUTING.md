# Contributing to OOSIS and OOVS

Thank you for helping make OSINT practice more reliable, reviewable, and safe.

## Before contributing

1. Read the [Code of Conduct](CODE_OF_CONDUCT.md), [governance](GOVERNANCE.md), and [Safety, Rights, and Misuse Policy](docs/safety-rights-and-misuse-policy.md).
2. Check the [source-of-truth hierarchy](docs/README.md) and current [release scope](programme/RELEASE_SCOPE.md).
3. Do not submit personal data, live-case material, victim information, suspected-person lists, credentials, exploit instructions, target packages, or operationally sensitive details.
4. Use synthetic, consented, anonymised, or non-sensitive public examples.

## Local validation

Python 3.10 or newer is recommended.

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-validation.txt
python3 scripts/validate_assets.py
```

The dependency is pinned. Do not update it without reviewing its release and rerunning all positive and negative fixtures.

## Contribution routes

### Editorial correction

Open a focused pull request. Explain whether a requirement's meaning changes. A meaning change is normative, even if it looks like wording.

### OOVS requirement or test

Use the [requirement proposal template](docs/templates/requirement-template.md). Include:

- the decision failure, harm, or assurance gap;
- one testable normative statement;
- applicability and objective `Not applicable` conditions;
- required evidence, procedure, pass criteria, and failure conditions;
- small-team implementation considerations;
- primary sources with exact version/scope and limitations;
- safety, rights, misuse, accessibility, and interoperability effects;
- alternatives, conflicts of interest, and dissent; and
- a safe fixture or implementation-validation plan.

Normative changes follow the public review and approval process in [GOVERNANCE.md](GOVERNANCE.md#change-classes).

### Structured asset

Validate against the declared JSON Schema and add or update both a valid and an invalid fixture when schema semantics change. Stable identifiers must not be silently renumbered.

### Mapping

A mapping must state direction, version, field semantics, loss, extension use, handling effects, and non-equivalence. Never use “compliant with” when only a conceptual relationship was reviewed.

### High-risk material

Material involving biometrics, minors, vulnerable people, political activity, conflict, attribution, large-scale personal-data collection, or high-consequence automation needs enhanced safety/rights and domain review. Open-source publication may be limited to controls, synthetic scenarios, and outcome measures.

## Normative writing

Use uppercase **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** only for testable provisions. Keep one main obligation per requirement where possible. Avoid universal source counts, legal conclusions, unspecified “best practice,” and claims that hashes, metadata, detectors, AI, or repeated reports prove authenticity.

## Review expectations

Reviewers assess correctness, testability, implementability, evidence, compatibility, safety, rights, and status claims. Proposal authors must not be the sole approving reviewers. Material disagreements and unresolved limitations are recorded, not erased for consensus optics.

## Developer Certificate of Origin

The project intends to use the [Developer Certificate of Origin](https://developercertificate.org/) subject to current OWASP policy. Sign commits with `git commit -s` only after confirming you have the right to contribute the material under the repository license.

## License

Unless stated otherwise, contributed documentation and structured standard content are accepted under the repository's [CC BY-SA 4.0](LICENSE) license, and you confirm you hold the rights to contribute the material on those terms. Do not submit third-party text, images, datasets, or schemas without compatible rights and attribution.
