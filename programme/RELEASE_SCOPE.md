# Release Scope and Sequencing

This document defines what each release line contains and how new work joins it.

## Two distinct milestones

The programme separates:

1. **OOVS releases:** versioned verification-standard content. OOVS v0.1.0 is released.
2. **OOSIS vertical slices:** end-to-end demonstrations that combine OOVS with graph, technique, and scenario assets.

Keeping them separate lets the standard be adopted and cited now, while the wider programme grows against implementation evidence.

## OOVS v0.1.0 scope

| Included | Delivered as |
| --- | --- |
| Standard | Ten L1 requirements in canonical Markdown |
| Machine-readable catalogue | Full requirement fields validated by JSON Schema |
| Acceptance tests | One structured test per requirement |
| Assessment format | JSON Schema plus a worked synthetic result |
| Mappings | Informative prior-art relationships with non-equivalence statements |
| Safety and governance | Safety, correction, contribution, governance, and release rules |
| Validation | Schema, semantic, parity, fixture, link, and manifest checks |
| Release package | Notes, manifest, hashes, compatibility, and scope notes |

## Next slice: synthetic Cyber Exposure and CTI

The following release line targets one reproducible vertical slice:

- a minimal OIG profile justified against W3C PROV, CASE/UCO, and STIX rather than assumed novel;
- 12 reviewed OTTM records across six technique families;
- six OOTG scenarios with safe fixtures;
- one synthetic Cyber Exposure/CTI Intelligence Pack;
- a small reference flow that validates, traces, exports, and assesses a synthetic product; and
- an implementation report including interoperability loss and open questions.

Broader technique catalogues, additional packs, and benchmark rounds follow this slice.

## Planned for later versions

- OOSIS Top 10 editions, produced through a published methodology and safe data call.
- Additional assurance depth and profiles for higher-consequence use.
- Clause-level external crosswalks reviewed against primary sources.
- Public-sector adoption resources such as procurement language and impact-assessment templates.
- Translations, benchmark rounds, and a solution landscape with neutral inclusion criteria.

Any future certification scheme would require its own governance, as stated in the [release policy](RELEASE_POLICY.md).

## Scope discipline

A new deliverable enters a release line when it has:

1. a named maintainer;
2. an evidence plan;
3. a safe fixture or example;
4. a measurable release test; and
5. a demonstrated dependency on the current slice.

Proposals that do not yet meet these criteria stay on the roadmap, which keeps every published asset backed by real content. Deliverables without an active maintainer are paused and reported rather than silently carried, and domain packs are published with qualified co-leads from that domain.
