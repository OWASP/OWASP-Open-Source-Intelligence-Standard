# Release and Compatibility Policy

## Content states

- **Development:** active content on the default branch; it may change before the next release.
- **Released:** versioned content with release notes, a manifest, hashes, and a validation record. OOVS v0.1.0 is released.
- **Superseded:** a previous release kept available for reference, with a migration note.

A release is defined by its version, release notes, and manifest. Reports, tools, training, and mappings **MUST** cite a released version and its identifiers.

## Versioning

Specifications, schemas, vocabularies, and guides use `MAJOR.MINOR.PATCH`.

- **MAJOR:** breaking change to requirement meaning, identifier contract, or schema semantics.
- **MINOR:** backward-compatible additions such as new requirements, profiles, fields, or scenarios.
- **PATCH:** corrections and non-breaking clarifications.

## Identifier conventions

| Asset | Pattern | Example |
| --- | --- | --- |
| OOVS requirement | `OOVS-v<version>-<number>` | `OOVS-v0.1.0-03` |
| OOVS test | `OOVS-v<version>-T<number>` | `OOVS-v0.1.0-T03` |
| OOTG scenario | `OOTG-v<version>-<domain>-<number>` | `OOTG-v0.1.0-MEDIA-003` |
| OTTM technique | `OTTM-<domain>-<number>` | `OTTM-WEB-001` |
| OIG object | `oig:<type>:<local-id>` | `oig:claim:synthetic-001` |
| Intelligence Pack | `OIP-<domain>-v<version>` | `OIP-CYBER-v0.1.0` |

Identifiers are stable within a minor line. A later version may add identifiers; it does not silently renumber or reuse published ones.

## Release checks

Every release requires:

- complete release notes and a manifest with canonical files and SHA-256 hashes;
- passing validation for schemas, cross-file semantics, Markdown/JSON parity, positive and expected-failure fixtures, and local links;
- explicit normative and informative boundaries;
- documented scope, compatibility, and migration notes;
- project-leader approval of the exact content; and
- no open critical safety or rights finding.

## Criteria for the 1.0 line

Promoting the standard to a long-term 1.0 line adds evidence requirements on top of the release checks:

1. every requirement demonstrably assessable with consistent results between independent assessors;
2. implementations reported by multiple independent organisations, with meaningful regional and sector diversity;
3. a public comment period of at least 45 days with a published disposition for every material comment;
4. an implementation report covering measured outcomes, interoperability loss, and open questions;
5. accessibility, security, and rights review records;
6. clause-level external mappings reviewed against primary sources; and
7. named, non-conflicted reviewers and release approvers.

## Deprecation and correction

Published identifiers are never silently removed or reused. Deprecation names the replacement, preserves historic content, and includes migration guidance. Material factual or safety corrections receive a patch release or correction notice, with downstream notification where feasible.

## Release manifest

Every manifest records:

- release ID, asset, version, status, and date;
- scope;
- required runtime and validation command;
- canonical files with SHA-256 hashes;
- validation result;
- quality checks;
- compatibility and identifier-stability statement; and
- scope notes for content planned in later versions.

Commit and tag fields are populated when the release is tagged.

## Source formats

Specifications publish in Markdown plus accessible rendered formats where maintained. Structured content publishes as JSON, JSON-LD, or CSV as appropriate. Human-readable and machine-readable forms are both first-class release outputs.

## Certification boundary

OOVS releases are standards content. Assessment results record a scope and outcome; they are not certificates. Any future certification scheme would require separate governance for assessor competence, impartiality, evidence sampling, report validity, surveillance, appeals, conflicts, scheme ownership, marks, and accreditation.
