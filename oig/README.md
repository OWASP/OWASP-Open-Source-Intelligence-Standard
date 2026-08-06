# OIG — OSINT Intelligence Graph

## Purpose

OIG is the cross-domain, machine-readable model for sources, evidence, entities, infrastructure, claims, media, events, relationships, uncertainty, and actions. It enables information to move between tools and teams without losing meaning.

## Available now

- [OIG 0.1 JSON Schema](schema/oig-bundle-0.1.schema.json)
- [Synthetic mission graph](examples/synthetic-mission-graph-0.1.json)
- [Interoperability and handling baseline](../programme/INTEROPERABILITY_AND_HANDLING.md)
- [Validator](../scripts/validate_assets.py)

The 0.1 preview schema is deliberately small: it represents ambiguity explicitly, distinguishes observations, claims, events, and actions, and preserves source, time, method, confidence, and handling context for material relationships.

## On the roadmap

A gap analysis against [W3C PROV](https://www.w3.org/TR/prov-overview/) and [CASE/UCO](https://caseontology.org/), followed by STIX, MISP, ATT&CK, and OpenCTI mappings with round-trip reporting. New primitives are added only where that analysis shows existing models do not cover a need. See the [roadmap](../docs/roadmap.md).
