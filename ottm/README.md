# OTTM — OSINT Technique & Tool Matrix

## Purpose

OTTM is a versioned, machine-readable technique vocabulary and capability matrix. It describes what a technique accomplishes, where it fits in a mission workflow, inputs/outputs, limitations, validation needs, and tool capability classes.

## Available now

- [Technique Record 0.1 JSON Schema](schema/technique-record-0.1.schema.json)
- [OTTM-WEB-001 — Public Web Change Detection](examples/OTTM-WEB-001.json)
- [Validator](../scripts/validate_assets.py)

## Record design

Each `OTTM-*` record carries a stable ID, technique objective, domains, mission uses, lifecycle stages, inputs, outputs, OIG mappings, reliability and failure modes, tool capability classes, limitations, and source references.

## Coverage

Coverage grows across web and archive, infrastructure, cyber, media, geospatial and time, documents and language, social and persona, financial and commercial, information integrity, and fusion and graph analysis. The next 12 reviewed records support the synthetic cyber-exposure slice on the [roadmap](../docs/roadmap.md).

OTTM records describe a capability rather than endorsing a particular vendor or tool.
