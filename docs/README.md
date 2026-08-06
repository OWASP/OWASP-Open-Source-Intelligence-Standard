# Working Papers and Design Notes

The `docs/` directory contains strategy papers, architecture notes, pointers, and other informative guidance. Normative content lives in the asset directories and is named by a release manifest.

## Source-of-truth hierarchy

| Asset type | Canonical location |
| --- | --- |
| Governance | [`GOVERNANCE.md`](../GOVERNANCE.md) |
| Programme charter, release scope, release policy | [`programme/`](../programme/) |
| OOVS standard, requirements, tests, schemas | [`oovs/`](../oovs/) |
| OOTG scenarios | [`ootg/`](../ootg/) |
| OIG schemas and examples | [`oig/`](../oig/) |
| OTTM schema and records | [`ottm/`](../ottm/) |
| Validation and fixtures | [`scripts/`](../scripts/) and [`tests/`](../tests/) |
| Release definition | [`releases/<version>/`](../releases/) notes, manifest, and Git tag |

A document is normative only when its text says so and the applicable release manifest names it. Strategy notes cannot override released requirements.

## Recommended reading

1. [Project charter](project-charter.md)
2. [OOVS v0.1.0 standard](../oovs/v0.1/standard.md)
3. [Safety, Rights, and Misuse Policy](safety-rights-and-misuse-policy.md)
4. [Roadmap](roadmap.md)
5. [Public-sector adoption path](public-sector-adoption.md)
6. [Research and evidence strategy](research-and-evidence-strategy.md)
7. [Prior art and positioning](prior-art-and-positioning.md)

The numbered design notes in this directory describe the programme's longer-term technical and organisational model. For what a given version delivers, read its release notes and manifest.
