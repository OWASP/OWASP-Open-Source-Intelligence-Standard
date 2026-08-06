# Project Charter

## 1. Mission

Build an open, vendor-neutral assurance and interoperability programme that helps people turn publicly available information into reviewable intelligence without losing provenance, uncertainty, rights, or accountability.

The programme aims to become a practical reference of the kind established OWASP projects provide, built through published evidence, independent implementations, open review, and durable community governance.

## 2. Naming and architecture

- **OWASP Open Source Intelligence Standard (OOSIS):** the umbrella programme and repository.
- **OWASP OSINT Verification Standard (OOVS):** the normative assurance standard.
- **OIG, OTTM, OOTG, packs, benchmarks, landscape, translations, and reference implementations:** separately versioned programme assets.

OOVS is the normative core rather than a synonym for the whole programme, so each asset can be released and cited on its own schedule.

## 3. Assurance proposition

OOVS makes five questions assessable for a defined workflow or intelligence product:

1. **Purpose:** Is the work authorised, necessary, proportionate, and bounded?
2. **Evidence:** Can material claims be traced to observations, transformations, and independent origins?
3. **Analysis:** Are facts, inference, assumptions, alternatives, and uncertainty distinguishable?
4. **Action:** Is dissemination controlled, caveated, correctable, and tied to an intended decision?
5. **Governance:** Are accountable people, challenge, audit, safety, and improvement operating in practice?

## 4. Scope

### In scope

- Testable assurance requirements and portable assessment results for OSINT workflows and products.
- Safe, synthetic examples and acceptance tests.
- Provenance, source and claim assessment, confidence, reproducibility, AI, dissemination, privacy, safeguarding, correction, and governance controls.
- Mappings and profiles that connect mature standards and open formats.
- Technique, graph, scenario, pack, benchmark, and reference artefacts as they are delivered.

### Out of scope

- Live investigations, victim data, personal dossiers, suspected-person lists, target packages, or operational intelligence.
- Instructions enabling unauthorised access, account compromise, stalking, coercion, social engineering, or evasion.
- Legal advice, authority determinations, evidence-admissibility opinions, or replacement of due process and professional standards.
- Certification or accreditation of organisations, people, tools, models, or products.
- A hosted intelligence service or production platform.

## 5. OOVS v0.1.0 contents

- Ten L1 requirements in human- and machine-readable form.
- A JSON Schema for the requirement catalogue.
- One acceptance test per requirement.
- An assessment-result schema with a worked synthetic example.
- Conservative prior-art and external mapping notes.
- Safety, governance, contribution, release, and correction processes.
- Positive and expected-failure validation fixtures.
- Automated schema, semantic, parity, and link checks.
- Release notes and a manifest with canonical files and hashes.

## 6. Criteria for the 1.0 line

The [release policy](../programme/RELEASE_POLICY.md) defines promotion criteria, including consistent independent assessment results, implementations from multiple organisations with regional diversity, a published public-comment disposition, an implementation report, accessibility and rights review records, clause-level mappings, and named non-conflicted approvers.

## 7. Measures of progress

| Measure | Current signal | 1.0 signal |
| --- | --- | --- |
| Requirement quality | Every requirement has evidence, procedure, and pass criteria | Consistent independent assessor results |
| Reproducibility | Synthetic example validates in CI | Independent reproductions by multiple organisations |
| Provenance | Required fields validate | 95% or better completeness in implementations |
| Analytic quality | Origin and contradiction checks are testable | Measured false-link and correction outcomes |
| Interoperability | Mapping relationships are explicit and scoped | Published round-trip loss and compatibility results |
| Community | Public contribution and role-nomination path | Multiple organisations, regions, and maintainers |
| Safety | Synthetic fixtures only | No open critical safety findings |

## 8. Expansion rule

A new programme deliverable needs a named maintainer, evidence plan, safe fixture, measurable release test, and a dependency on the current release line. Otherwise it stays on the roadmap. This keeps the published portfolio aligned with delivered content.
