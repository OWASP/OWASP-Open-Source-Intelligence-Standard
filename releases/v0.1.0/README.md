# OOVS v0.1.0 Release Notes

- **Asset:** OWASP OSINT Verification Standard (OOVS)
- **Version:** 0.1.0
- **Status:** Released
- **Date:** 2026-08-05
- **License:** CC BY-SA 4.0

## What this release contains

- The **L1 Foundational baseline**: ten testable requirements covering authorised purpose, collection boundaries, provenance, source and claim assessment, corroboration and confidence, analytic transparency, rights and safeguarding, AI assurance, dissemination, and governance.
- A **machine-readable requirement catalogue** with objectives, normative statements, applicability, evidence, procedures, pass criteria, failure conditions, exceptions, and references.
- **Ten acceptance tests**, one per requirement, with preconditions, sampling guidance, steps, expected evidence, and safety notes.
- An **assessment-result schema** and a worked synthetic example so results are portable between tools and reviewers.
- **External mappings** to established public guidance, with explicit non-equivalence statements.
- **Governance, safety, contribution, and release policies**, including correction and challenge routes.
- **Automated validation**: JSON Schema conformance, cross-file semantics, Markdown/JSON parity, positive and expected-failure fixtures, local links, and manifest hashes.

Canonical files and SHA-256 hashes are recorded in [`manifest.json`](manifest.json).

## Using this version

Cite `OOVS v0.1.0` with any published result, and keep the assessment scope attached to it. Requirement identifiers are stable within the 0.1 line.

An OOVS assessment records a defined scope and result. It is not certification, accreditation, legal advice, or a determination of admissibility, and it does not imply endorsement by any government, agency, court, or vendor.

## Validate the release

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-validation.txt
python3 scripts/validate_assets.py
```

Expected output reports validated schemas, positive fixtures, expected-failure fixtures, Markdown/JSON requirement pairs, local links, and manifest hashes.

## What comes next

The 0.2 line focuses on implementation evidence:

- assessor and sampling guidance plus an assessment report template;
- measured consistency between independent assessors on synthetic cases;
- a reproducible synthetic cyber-exposure/CTI vertical slice using OIG, OTTM, and OOTG;
- clause-level mappings reviewed against primary sources; and
- interoperability round-trip results with existing open formats.

See the [roadmap](../../docs/roadmap.md).

## Feedback

Use the public feedback and implementation-feedback issue templates. Share scope, method, aggregate measures, and wording that produced inconsistent results. Do not include personal, live-case, victim, credential, or operationally sensitive information.
