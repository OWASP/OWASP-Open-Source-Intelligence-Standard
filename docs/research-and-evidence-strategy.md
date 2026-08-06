# Research and Evidence Strategy

## Purpose

Research is how OOSIS avoids becoming a collection of opinions. The project should turn research, real tools, operational lessons, and community review into structured artefacts: technique records, graph fields, mappings, benchmarks, and Intelligence Packs. A promising paper or impressive tool is not a standard by itself—it becomes a testable hypothesis, implementation input, or benchmark candidate.

## Contributed inputs (non-normative)

The project is mission-led. Research papers, tools, and operational experience contributed by anyone — including project leaders — are sources of questions, datasets, and implementation lessons. They carry no privileged status in the standard, and a contribution with stronger evidence or broader utility takes precedence.

Contributors declare relevant interests when they propose material derived from their own work, as required by the [conflicts-of-interest rule](../GOVERNANCE.md#conflicts-of-interest).

### Categories of useful input

| Input type | Contribution to OOSIS | Concrete output |
| --- | --- | --- |
| Threat and attack-chain research | Explains how fragmented public information, reconnaissance, and manipulation combine | Technique records and defensive exposure guidance, with quantitative claims verified before release |
| Attribution and identity research | Cross-domain analysis, adversarial robustness, and identity obfuscation | Graph relations for personas and campaigns, entity-resolution benchmarks, AI robustness tests |
| Model evaluation research | Generalisation limits and evaluation design | AI evaluation vocabulary and high-risk analysis profiles; a research result is never treated as operational assurance |
| Working tools and pipelines | Workflow design, exports, enrichment, and reporting patterns | Technique records, graph examples, and action-oriented output formats |
| Established knowledge bases such as MITRE ATT&CK, STIX, MISP, and OpenCTI | Mature interchange, sharing, and taxonomies | Mapping layers and reference integrations rather than reinvention |

## Research workstreams

### 1. Technique science

For each OTTM technique, establish: purpose, inputs, expected artefacts, reliability, failure modes, operational cost, validation method, and tool capability classes. Do not write tool-focused pages until the technique record exists.

### 2. Graph and interchange design

Compare source models from STIX, MISP, OpenCTI, academic knowledge graphs, and the founding projects. Publish gaps as issues. Add only the minimum new objects needed to represent cross-domain OSINT.

### 3. AI and fusion evaluation

Build synthetic corpora that measure extraction, translation, entity resolution, claim/media analysis, graph reasoning, and AI research-agent citation integrity. Publish false-positive and calibration results alongside accuracy.

### 4. Mission packs

Use workshops with practitioners to define priority intelligence requirements, output types, decision points, and test fixtures. A pack is accepted only when practitioners can run it on synthetic material and explain the value of its output.

### 5. Information confrontation

Treat the cognitive domain as a first-class mission area: claims, narratives, media, actors/personas, coordination signals, audiences, time, and countermeasures all need graph representation. The project can publish detection, resilience, and analytical-framework material without publishing harmful influence-operation playbooks.

## Evidence hierarchy

1. **Normative authority:** applicable law, binding regulation, official policy, and established standards—always jurisdiction/context bound.
2. **Empirical evidence:** peer-reviewed research, transparent data, reproducible methods, independent replications.
3. **Practice evidence:** documented pilots, redacted audits, exercises, and post-incident lessons with known limitations.
4. **Expert consensus:** diverse, declared expertise reached through a public and challengeable process.
5. **Anecdote or vendor assertion:** useful for hypotheses only; never enough for a normative requirement.

## Artefact evidence packet

Every proposed technique, graph object, mapping, benchmark, or normative requirement should include:

- problem and decision consequence;
- artefact definition and observable test;
- sources, claims supported, populations/contexts, and conflicts of interest;
- likely benefit and potential harm/cost;
- exceptions and residual risks;
- pilot or validation plan;
- dissenting views and an expiry/review date.

## Citation rule

Before a source enters a release bibliography, verify its title, author list, version, persistent identifier, publication status, and licence from the publisher or archival record. Cite the specific edition and clause used, and state the scope and limitations of any result relied upon.

Where publisher metadata cannot be confirmed, the source stays in a verification queue rather than being cited as settled. This is the same provenance discipline OOVS asks implementers to apply.

## Publication guardrail

The project will not make causal or quantitative claims such as a percentage increase in phishing success unless the underlying study, methods, data, scope, and limitations are independently verified. When a study demonstrates a harmful capability, use it to improve detection, resilience, training, and verification—not to turn attack-effectiveness results into a public recipe.
