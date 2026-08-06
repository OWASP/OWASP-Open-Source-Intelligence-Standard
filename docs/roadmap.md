# Roadmap

## Strategic focus

The programme advances one release line at a time: **OOVS**, plus the minimum graph, technique, and scenario content needed to demonstrate it end to end. This keeps every published asset backed by real content.

## Delivered — OOVS v0.1.0

- L1 Foundational baseline with ten testable requirements.
- Machine-readable requirement catalogue, acceptance tests, and assessment schema.
- Worked synthetic assessment and expected-failure fixtures.
- Conservative external mappings and prior-art positioning.
- Governance, safety, contribution, correction, and release policies.
- Automated validation for schemas, semantics, parity, fixtures, links, and manifest hashes.

## Next — implementation evidence (0 to 3 months)

### OOVS

- Publish assessor guidance, sampling guidance, and an assessment report template.
- Gather implementation results from synthetic and non-sensitive material.
- Measure consistency between independent assessors and investigate disagreement.
- Refine any wording that produced inconsistent assessments.

### Supporting assets

- 12 reviewed OTTM records across six technique families.
- Six OOTG scenarios with expected outputs and safe fixtures.
- A minimal OIG profile with published gap analysis and mappings to W3C PROV, CASE/UCO, STIX, MISP, and OpenCTI.
- One synthetic cyber mission card, collection boundary, graph profile, action product, and ground-truth fixture.

## Then — reproducible vertical slice (3 to 6 months)

- A small CLI and static reference flow.
- One end-to-end synthetic cyber mission: plan, collect fixture, preserve provenance, assess claims, export, produce an action output, and assess against OOVS.
- Design partners across research, CSIRT or nonprofit, and public-interest or public-sector contexts.
- Participation from at least three regions or materially different legal and operational contexts.
- A public comment period with published disposition for every material comment.
- An implementation report covering measured outcomes, mapping loss, assessor agreement, false-link rates, and open questions.

## Then — the 1.0 line (6 to 12 months)

Promotion to 1.0 follows the criteria in the [release policy](../programme/RELEASE_POLICY.md), including independent implementations, published comment disposition, accessibility and rights review, clause-level mappings, and an implementation report. Self-assessment and independent-assessment templates ship with it.

## Then — adoption profiles (12 to 24 months)

- Narrowly scoped profiles based on demonstrated demand and consequence.
- A public-sector adoption kit: procurement language, jurisdictional crosswalk method, impact-assessment templates, records and retention controls, security and accessibility requirements, and information-sharing profiles.
- Expanded CTI interoperability, and one additional domain with qualified external co-leads.
- A Top 10 evidence call using a published methodology and safe aggregate submissions.
- Assessor competence and scheme governance work, which any future certification would depend on.

## Metrics

| Area | Target or measure |
| --- | --- |
| Testability | 100% of normative requirements have procedure, evidence, pass, and fail criteria |
| Provenance | At least 95% required-field completion in implementations; gaps reported by field |
| Reproducibility | At least 80% of expected synthetic outcomes reproduced independently |
| Assessor consistency | Agreement tracked per requirement; candidate target 0.8 or above |
| Analytic quality | False-link, false-positive, contradiction-detection, and correction rates |
| Interoperability | Field-level mapping coverage and round-trip loss |
| Utility | Review time, time-to-insight, decision clarity, and implementation effort |
| Community | External implementers, multi-region review, maintainer depth, reviewer independence |
| Safety | Zero open critical findings; all fixtures synthetic or non-sensitive |

## Sequencing rules

- Requirements and profiles follow implementation evidence.
- OIG stays a profile of existing models unless gap analysis justifies new primitives.
- Domain packs ship with qualified external co-leads and safe fixtures.
- New programme branches wait until the current slice is reproducible.
- Every deliverable has a named owner, evidence plan, and safety review.
