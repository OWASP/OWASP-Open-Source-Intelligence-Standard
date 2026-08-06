# Public-Sector and Critical-Infrastructure Adoption Path

## Positioning

OOVS is a vendor-neutral assurance layer that can be used alongside in-house, open-source, or commercial systems. It gives an organisation a published, testable way to show how an OSINT workflow or product was authorised, traced, verified, reviewed, and disseminated.

OOVS is a standard rather than a runtime platform: it does not provide production ingestion, ontology operations, applications, granular authorisation, audit infrastructure, or deployment tooling. Those remain the responsibility of the adopting organisation's systems.

## Adoption ladder

| Stage | Evidence involved | Supportable claim |
| --- | --- | --- |
| Evaluation | Read the standard; run the synthetic example | "Evaluating OOVS" |
| Assessment | Assess one workflow or product with recorded scope and evidence | "Assessed against OOVS v0.1.0 for [scope] during [period]" |
| Design partnership | Approved synthetic or de-identified pilot with published method | "Participating in an OOVS pilot" |
| Independent implementation | Reproduction without founder assistance, with published results | "Implemented the cited OOVS version for the stated scope" |
| Procurement profile | Jurisdiction and sector controls, security and accessibility requirements, contract language, assessor method | Scope-specific procurement reference |

No stage implies endorsement by OWASP, a government, an agency, a court, or a participating reviewer.

## What adopters typically require

### Mission and legal authority

- a defined mission, decision, accountable owner, and authority;
- jurisdiction and mandate-specific legal analysis;
- necessity, proportionality, minimisation, and impact assessment;
- safeguards for minors, vulnerable people, biometrics, political activity, and other sensitive contexts; and
- due process, correction, redress, oversight, and records-management routes.

### Security and operations

- identity, role, purpose, and attribute-based access appropriate to the environment;
- encryption, key management, audit, monitoring, incident response, retention, deletion, backup, and continuity;
- supply-chain, dependency, vulnerability, and secure-development evidence;
- deployment patterns for required sovereignty, data residency, availability, and disconnected operation; and
- controls validated by the adopting organisation.

### Analytic assurance

- measurable provenance completeness and source-origin independence;
- calibrated uncertainty with false-link and false-positive measures;
- independent challenge, reproducibility, and correction propagation;
- AI task evaluation, input and output traceability, human accountability, and prohibited-use enforcement; and
- competence, training, sampling, assessor consistency, and audit evidence.

### Interoperability and procurement

- field-level mappings and round-trip tests for relevant STIX/TAXII, MISP, OpenCTI, W3C PROV, CASE/UCO, and local formats;
- accessibility and low-bandwidth documentation formats;
- open licensing, version support, migration, and exit terms; and
- vendor-neutral acceptance criteria, with no proprietary platform required to use the standard.

## Pilot pattern

A strong first pilot uses one recurring, low-risk product and synthetic or approved de-identified material.

1. **Baseline:** measure review time, provenance completeness, claim traceability, contradiction detection, corrections, and decision clarity.
2. **Intervention:** apply the OOVS plan, provenance and verification records, confidence statement, review gate, and assessment schema for 6 to 12 weeks.
3. **Independent check:** have a reviewer who did not build the workflow assess the same sample.
4. **Measures:** publish agreement, exceptions, implementation effort, false links, missed contradictions, and correction time.
5. **Safety:** stop if the pilot creates unapproved collection, sensitive-data exposure, or rights impact.
6. **Publication:** release aggregate methods, synthetic fixtures, limitations, and standard changes — never case or operational data.

## Adoption resources on the roadmap

The programme plans to publish model procurement requirements and acceptance tests, a jurisdictional-profile template, impact-assessment templates, records and retention controls, security and accessibility profiles, information-sharing profiles, and assessor guidance. See the [roadmap](roadmap.md).

## Legitimacy rule

Government, law-enforcement, and intelligence organisations are welcome adopters and reviewers, but they are not the sole design centre. Civil society, journalism, academia, affected communities, privacy and human-rights experts, small teams, and international users must be able to challenge the standard. Broad legitimacy is a control, not a marketing objective.
