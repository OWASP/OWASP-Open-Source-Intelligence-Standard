# Founding Design Review

- **Review date:** 2026-08-05
- **Scope:** OOVS v0.1.0 and the wider repository structure
- **Type:** internal design review by the founding team

This record documents the design decisions behind the first release and the controls that keep the programme honest as it grows. Publishing it is deliberate: a standard should show its reasoning.

## Decisions and outcomes

| Question | Decision | Outcome in v0.1.0 |
| --- | --- | --- |
| How should the standard be executable rather than narrative? | Pair every requirement with machine-readable fields and an acceptance test | Requirement catalogue, test catalogue, assessment schema, and automated validation |
| How should readers tell normative content from design notes? | Publish a source-of-truth hierarchy and manifest-defined releases | `docs/README.md` hierarchy plus release manifest naming canonical files |
| How should assurance levels be structured? | Use one consequence-sensitive baseline instead of audience or job-title tiers | L1 Foundational baseline with high-consequence conditions inside each requirement |
| How much corroboration should be required? | Scale verification depth to consequence and test source independence | `OOVS-v0.1.0-04` and `OOVS-v0.1.0-05`, with no universal fixed source count |
| How should external standards be treated? | Map conservatively and state non-equivalence | `oovs/v0.1/mappings.md` and `docs/prior-art-and-positioning.md` |
| How wide should the first release be? | Release the assurance core, then build one reproducible vertical slice | OOVS v0.1.0 released; cyber slice sequenced next |
| How should safety be enforced in an open repository? | Make synthetic examples and content boundaries a design rule | Safety policy, synthetic fixtures, and review classes |

## Ongoing controls

1. **Evidence before expansion:** new requirements and profiles follow implementation feedback rather than intuition.
2. **Distributed ownership:** maintainer, safety, and release roles are published and openly recruited to reduce founder dependence.
3. **Neutral positioning:** OWASP hosting is not presented as legal authority, endorsement, or operational validation.
4. **Mapping discipline:** clause-level crosswalks require primary-source and specialist review before publication.
5. **Domain expertise:** packs covering sensitive domains are published with qualified co-leads.
6. **Safe collaboration:** public channels use synthetic, consented, anonymised, or non-sensitive material only.

## Review cadence

This review is revisited at each minor release, and its controls are reassessed whenever scope, governance, or safety policy changes.
