# OOVS v0.1 Informative Mappings

## Mapping rule

These mappings help reviewers compare OOVS with established public guidance. They are **informative** and deliberately conservative: "related" means relevant to, not equivalent to, endorsed by, or compliant with. Clause-level crosswalks are published after primary-source and specialist review.

| OOVS requirement | Related public sources | Relationship and limit |
| --- | --- | --- |
| 01 — Purpose and proportionality | [Berkeley Protocol](https://www.ohchr.org/sites/default/files/2022-04/OHCHR_BerkeleyProtocol.pdf); [EU Law Enforcement Directive](https://eur-lex.europa.eu/eli/dir/2016/680/oj) | Related to professional planning, legal basis, necessity, proportionality, and accountability. Applicability varies by mandate and jurisdiction. |
| 02 — Collection boundary and minimisation | [Berkeley Protocol](https://www.ohchr.org/sites/default/files/2022-04/OHCHR_BerkeleyProtocol.pdf); [EU Law Enforcement Directive](https://eur-lex.europa.eu/eli/dir/2016/680/oj) | Related to lawful collection, minimisation, and protections for personal data. OOVS does not determine legal authority. |
| 03 — Provenance and integrity | [Berkeley Protocol](https://www.ohchr.org/sites/default/files/2022-04/OHCHR_BerkeleyProtocol.pdf); [W3C PROV Overview](https://www.w3.org/TR/prov-overview/) | Related to identification, collection, preservation, provenance, entities, activities, and agents. OOVS is not a digital-forensics admissibility rule. |
| 04 — Source and claim assessment | [ICD 203 Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf); [Berkeley Protocol](https://www.ohchr.org/sites/default/files/2022-04/OHCHR_BerkeleyProtocol.pdf) | Related to source quality, alternatives, uncertainty, and verification. OOVS adds an explicit common-origin check but does not prescribe a universal grading scale. |
| 05 — Corroboration and confidence | [ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf); [ICD 206 Sourcing Requirements](https://www.dni.gov/files/documents/ICD/ICD-206.pdf) | Related to confidence, sourcing, uncertainty, and distinctions between underlying information and analysis. OOVS does not claim Intelligence Community compliance. |
| 06 — Transparency and reproducibility | [ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf); [ICD 206](https://www.dni.gov/files/documents/ICD/ICD-206.pdf) | Related to explaining judgments, sourcing, assumptions, alternatives, and uncertainty. Sensitive-source rules remain organisation-specific. |
| 07 — Rights, privacy, and safeguarding | [Berkeley Protocol](https://www.ohchr.org/sites/default/files/2022-04/OHCHR_BerkeleyProtocol.pdf); [EU Law Enforcement Directive](https://eur-lex.europa.eu/eli/dir/2016/680/oj) | Related to dignity, safety, accuracy, security, retention, rights, oversight, and correction. The EU source is a jurisdictional example, not a global default. |
| 08 — AI and automation | [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework); [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | Related to governing, mapping, measuring, managing, human oversight, transparency, and risk controls. The AI RMF is voluntary; the EU Act has defined legal scope and phased obligations. |
| 09 — Dissemination and action | [ICD 206](https://www.dni.gov/files/documents/ICD/ICD-206.pdf); [FIRST TLP 2.0](https://www.first.org/tlp/) | Related to sourcing transparency and sharing boundaries. TLP is optional and does not replace classification, law, contract, privacy, or safeguarding rules. |
| 10 — Governance, audit, and improvement | [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework); [ISO/IEC Directives, Part 2](https://www.iso.org/sites/directives/current/part2/index.xhtml) | Related to governance, accountable review, measurable requirements, and improvement. OOVS has no accredited conformity-assessment scheme. |

## Interoperability context

OOVS should coexist with, profile, or map to mature models rather than recreate them:

- [STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) and [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html) for cyber-threat information and transport;
- [MISP](https://www.misp-project.org/) and [OpenCTI](https://docs.opencti.io/latest/) for operational CTI sharing and knowledge-graph workflows;
- [CASE](https://caseontology.org/) and [UCO](https://unifiedcyberontology.org/) for cyber-investigation and provenance concepts; and
- [W3C PROV](https://www.w3.org/TR/prov-overview/) for general provenance representation.

Mappings state field loss, extension use, handling effects, and round-trip limitations, and they are published separately from any converter implementation.

## Clause-level crosswalk process

To extend a mapping beyond this high-level index, contributors:

1. cite the exact edition and stable primary-source location;
2. quote or paraphrase only what licensing permits;
3. identify scope, jurisdiction, exceptions, and normative strength;
4. obtain review from a subject specialist independent of the mapping author;
5. test the mapping against at least one synthetic implementation; and
6. publish gaps and non-equivalences, not only apparent matches.
