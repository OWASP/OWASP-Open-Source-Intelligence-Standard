# Prior Art and Defensible Positioning

## Purpose

OOVS must earn trust by showing how it relates to existing standards, doctrine, protocols, and software. It must not claim to be the first OSINT methodology, a universal legal standard, or an open replacement for an intelligence platform.

## Relevant public guidance

| Existing work | Established contribution | OOVS relationship |
| --- | --- | --- |
| [OHCHR/Berkeley Protocol on Digital Open Source Investigations](https://www.ohchr.org/sites/default/files/2022-04/OHCHR_BerkeleyProtocol.pdf) | International professional guidance for identifying, collecting, preserving, verifying, and analysing digital open-source information | Foundational prior art. OOVS can provide compact, machine-readable acceptance criteria while preserving the Protocol's context and safeguards. |
| [ICD 203 Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) | U.S. Intelligence Community analytic tradecraft standards | Useful analytic-quality reference, not a global legal baseline and not an OOVS compliance claim. |
| [ICD 206 Sourcing Requirements](https://www.dni.gov/files/documents/ICD/ICD-206.pdf) | Sourcing and source-description requirements for disseminated analysis | Useful for source/analysis transparency; implementation details remain mandate-specific. |
| [IC OSINT Strategy 2024–2026](https://www.dni.gov/files/ODNI/documents/IC_OSINT_Strategy.pdf) | Public strategy for acquisition/sharing, collection management, innovation, workforce, and tradecraft | Evidence of public-sector priorities, not endorsement of OOVS. |
| [W3C PROV](https://www.w3.org/TR/prov-overview/) | General provenance model and representations | OIG/OOVS should profile or map to it rather than invent an incompatible provenance foundation. |
| [STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) / [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html) | Cyber-threat-information representation and exchange | Use for CTI interoperability; OOSIS should only add cross-domain profiles where a demonstrated gap exists. |
| [CASE](https://caseontology.org/) / [UCO](https://unifiedcyberontology.org/) | Cyber-investigation and unified cyber ontology concepts | Important overlap for evidence, provenance, and investigations; conduct gap analysis before adding OIG primitives. |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | Voluntary framework for governing and managing AI risk | Useful for OOVS AI assurance, evaluation, accountability, and monitoring. |
| [FIRST TLP 2.0](https://www.first.org/tlp/) | Sharing-boundary markings for security communities | Preserve when selected; never impose on every product or treat as a legal/classification scheme. |
| [EU Law Enforcement Directive](https://eur-lex.europa.eu/eli/dir/2016/680/oj) and [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | Binding EU requirements within their respective scopes | Jurisdictional profile inputs, not universal OOVS rules. |

## Software ecosystem

OOVS is a standard, not an operational data platform. Mature systems already cover important capabilities:

- [OpenCTI](https://docs.opencti.io/latest/) provides a STIX-oriented CTI knowledge graph, connectors, cases, enrichment, and reporting.
- [MISP](https://www.misp-project.org/) provides sharing, correlation, taxonomies, galaxies, and synchronisation.
- [Aleph](https://docs.aleph.occrp.org/) provides investigative-data ingestion, search, extraction, entities, networks, and timelines.
- [IntelOwl](https://intelowlproject.github.io/) and [SpiderFoot](https://www.spiderfoot.net/) automate enrichment and collection across many sources.

A commercial platform such as Palantir Foundry combines ingestion, ontology, granular access controls, lineage, applications, actions, audit, retention, and deployment operations. A documentation and conformance project does not become an equivalent platform by defining a graph schema.

## OOVS's defensible niche

OOVS can add distinct value as an open, vendor-neutral **assurance and conformance layer** that:

1. applies a compact set of rights-aware acceptance tests across tools and sectors;
2. preserves the distinction between sources, claims, origins, inference, and action;
3. makes assessment results portable and machine-readable;
4. connects existing provenance, CTI, investigation, privacy, and AI-risk guidance; and
5. supports procurement and pilots without endorsing a vendor.

This position is narrower than “the global OSINT standard” and more credible. Adoption comparable to mature OWASP projects can only follow evidence: independent implementations, transparent methodology, public review, repeatable pilots, stable identifiers, translations, and sustained multi-organisation maintenance.

## Claim policy

Project communications must not use claims such as “first,” “only,” “fully compliant,” “court-ready,” “government-approved,” “agency-grade,” or “industry standard” without independently verifiable evidence and approval to cite the relevant organisation. Aspirational use cases must be labelled as such.
