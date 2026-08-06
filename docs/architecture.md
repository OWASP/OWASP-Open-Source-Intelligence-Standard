# OOSIS Product Architecture

> **Document type:** Architecture design note describing the long-term technical model. Release contents and sequencing are defined by the [release scope](../programme/RELEASE_SCOPE.md) and [roadmap](roadmap.md), which supersede the coverage targets below.

## Executive thesis

OOSIS should not compete with a single OSINT tool, intelligence platform, or commercial data provider. It should define the **open grammar of actionable intelligence** so that a tool, an analyst, an AI agent, and an intelligence platform can work together without losing context, provenance, or analytical meaning.

The project has a meaningful opening because the present ecosystem is fragmented:

| Existing asset | What it solves well | What remains missing |
| --- | --- | --- |
| [Bellingcat Online Investigations Toolkit](https://www.bellingcat.com/resources/2024/09/24/bellingcat-online-investigations-toolkit/) | Discovery and explanation of investigation tools | A common operational model, machine-readable technique schema, fusion model, and cross-domain intelligence packs |
| [MITRE ATT&CK](https://attack.mitre.org/resources/attack-data-and-tools/) | Cyber-adversary knowledge and structured ATT&CK data | Physical, social, financial, media, and cognitive OSINT domains; end-to-end OSINT workflow |
| [STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) | Machine-readable cyber-threat information exchange | A general OSINT graph with source/claim/media/location/persona constructs and multi-domain profiles |
| [MISP](https://misp-project.org/) | Sharing, correlation, taxonomies, and cyber/fraud/counter-terrorism collaboration | A universal methodology and a standard technique/tool matrix |
| [OpenCTI](https://docs.opencti.io/latest/usage/getting-started/) | A cyber-threat intelligence knowledge graph and connectors | Open standard definitions for multi-domain OSINT collection, fusion, and analytic products |
| [ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) | Analytic tradecraft principles | An openly implementable OSINT technical and data architecture |

These projects and public standards demonstrate substantial prior art. OOSIS should not claim an empty field or recreate mature provenance, CTI, investigation, or platform capabilities. Its defensible role is a cross-domain, rights-aware assurance and interoperability layer: portable acceptance tests, scoped assessment results, and mappings that preserve provenance and uncertainty. See [Prior Art and Defensible Positioning](prior-art-and-positioning.md).

## Product model

```text
Mission Question
      │
      ▼
OOSIS Operational Model ──► Technique & Tool Matrix ──► Collection / Enrichment
      │                                                             │
      │                                                             ▼
      │                                                   OSINT Intelligence Graph
      │                                                             │
      ▼                                                             ▼
Intelligence Pack ◄──── AI / Fusion / Analytic patterns ───► Actionable Product
      │                                                             │
      └────────────── OOVS assurance + benchmark + maturity ───────┘
```

The standard supplies the language and test criteria. A future reference implementation can supply schemas, converters, parsers, dashboards, graph queries, and benchmark runners. Third parties can build compliant tools without being locked into one vendor.

## 1. OSINT Operational Model (OOM)

The lifecycle is not a generic “collect-analyse-report” diagram. Each stage has concrete inputs, outputs, decisions, data structures, and automation opportunities.

| Stage | Core question | Required output | Automation and technical opportunity |
| --- | --- | --- | --- |
| 1. Mission framing | What decision must change? | Intelligence requirement, target environment, priority indicators, time horizon | Requirement templates, risk/asset context, task queue |
| 2. Collection design | Which sources and techniques can answer it? | Source/technique plan, collection hypotheses, expected artefacts | Tool selection, source health monitoring, query orchestration |
| 3. Acquisition | What raw material was obtained? | Immutable source record, snapshot/reference, acquisition metadata | APIs, crawlers, archives, feeds, parsers, scheduled jobs |
| 4. Processing | How is raw material made analysable? | Normalised entities, extracted observables, translated/transcribed media, hashes | OCR, ASR, translation, metadata extraction, file/media analysis |
| 5. Fusion | What connects to what? | Entity-resolution decisions, relationships, temporal/geospatial graph | Graph construction, similarity scoring, resolution queues, link analysis |
| 6. Analysis | What does the fused picture mean? | Hypotheses, confidence, scenarios, indicators, recommended action | Pattern detection, timeline analysis, network analysis, AI-assisted synthesis |
| 7. Action and learning | What must happen now, and what did we learn? | Actionable product, hand-off, feedback, outcome labels | STIX/MISP/OpenCTI export, alerting, case hand-off, benchmark feedback |

### Design rules

- **Mission first:** start with a decision and priority intelligence requirements, not a favourite tool.
- **Evidence is data:** source, extraction, transformation, and uncertainty are first-class graph objects.
- **Fusion is explicit:** never silently collapse two identities, accounts, documents, or events into one entity.
- **Action is typed:** distinguish a lead, an alert, an indicator, a hypothesis, an assessment, and a verified finding.
- **Feedback trains the system:** outcome labels are how people, rules, and AI improve over time.

## 2. OSINT Technique & Tool Matrix (OTTM)

The matrix is the practitioner heartbeat of the project. It must be more useful than a list of links and more stable than a tool review.

### Matrix entry design

Each technique record contains:

- **Identifier:** stable, versioned ID such as `OTTM-WEB-001`.
- **Technique:** what analytical outcome the method enables.
- **Domain and modality:** web, social, infrastructure, media, geospatial, document, identity, network, financial, cognitive, or cross-domain.
- **Inputs and outputs:** expected source types and graph objects created.
- **Workflow position:** one or more OOM stages.
- **Tool capability classes:** open source, commercial, manual, API, or AI-assisted—not an endorsement list.
- **Reliability signals:** reproducibility, source volatility, false-link risk, known blind spots, and validation steps.
- **Operational conditions:** skill level, time, cost, scale, language/region coverage, rate limits, and data-residency considerations.
- **Mappings:** OOSIS graph objects, STIX/MISP where applicable, ATT&CK/counter-fraud/other relevant taxonomies.
- **Use cases and test fixtures:** synthetic examples and measurable success criteria.

### Initial taxonomy

| Family | Examples of capability areas | Typical intelligence output |
| --- | --- | --- |
| WEB | search, archives, change detection, document discovery, code/repository intelligence | source corpus, historical state, exposed artefact |
| INFRA | domains, certificates, DNS, cloud/service exposure, code/asset correlation | infrastructure graph, exposure hypothesis, defensive priority |
| SOCIAL & PERSONA | public persona, community, behavioural, relationship, and narrative analysis | persona graph, coordinated-behaviour hypothesis, influence map |
| MEDIA | image/video/audio metadata, provenance, manipulation analysis, visual matching, transcription | verified media record, extracted entities, claim evidence |
| GEO & TIME | geolocation, chronolocation, route/event reconstruction, satellite/map analysis | location/time confidence, event timeline |
| DOCUMENT & LANGUAGE | OCR, document metadata, translation, authorship/stylometry research, semantic clustering | searchable corpus, language-normalised claim set |
| FINANCIAL & COMMERCIAL | company/public-record, trade, blockchain/public-ledger, fraud-pattern analysis | ownership/transaction relationship graph, risk lead |
| CYBER | exposure discovery, malware/report analysis, indicators, ATT&CK mapping, threat-actor research | CTI bundle, detection/hardening recommendation |
| COGNITIVE | narrative tracking, coordinated inauthentic behaviour analysis, synthetic-content assessment, information confrontation mapping | narrative timeline, campaign hypothesis, resilience action |
| FUSION | entity resolution, graph analysis, link/timeline analysis, confidence aggregation | multi-source intelligence graph and analytic assessment |

Records are selected for coverage rather than tool popularity, with each one usable as a complete example of the record format. Breadth is added later without degrading the model. The [roadmap](roadmap.md) sets the record count for each release.

## 3. OSINT Intelligence Graph (OIG)

The OIG is the technical centrepiece. It enables a common representation of intelligence beyond a report or spreadsheet. It is deliberately compatible with existing cyber standards rather than trying to replace them.

### Core node types

| Group | Initial node types |
| --- | --- |
| Actors and identity | `Person`, `Organisation`, `Persona`, `Account`, `Group`, `Device` |
| Digital/physical infrastructure | `Domain`, `IP`, `Certificate`, `Service`, `Asset`, `Location`, `Route` |
| Evidence and information | `Source`, `Document`, `Media`, `ArchiveSnapshot`, `Observable`, `Claim`, `Translation`, `Extraction` |
| Intelligence | `Event`, `Incident`, `Campaign`, `ThreatActor`, `Technique`, `Indicator`, `Assessment`, `Hypothesis`, `Action` |
| Context | `TimeInterval`, `Language`, `Jurisdiction`, `Tag`, `CollectionTask`, `ToolRun`, `Confidence` |

### Core relationship types

`observed_in`, `published_by`, `controls`, `uses`, `hosts`, `resolves_to`, `registered_to`, `linked_to`, `same_as`, `likely_same_as`, `supports`, `contradicts`, `mentions`, `depicts`, `located_at`, `occurred_at`, `occurred_during`, `precedes`, `part_of`, `targets`, `attributed_to`, `associated_with`, `derived_from`, `collected_by`, `analysed_by`, `actioned_by`, and `supersedes`.

Every relationship carries at least: assertion source, time, method, analyst/system, confidence, and status. The graph must represent uncertainty: `likely_same_as` is not `same_as`; `supports` is not proof.

### Interoperability profile

- **STIX 2.1:** export cyber observables, indicators, reports, threat actors, campaigns, relationships, and markings where the source material is CTI.
- **MISP:** map events, attributes, objects, galaxies, taxonomies, and sharing markings for operational threat sharing.
- **OpenCTI:** provide import/export mappings for cyber and strategic graph workflows.
- **JSON-LD:** publish an OIG JSON-LD context for general cross-domain graph interchange.
- **CSV/Parquet:** support plain tabular exchange for small teams and research datasets.

### Minimum viable schema deliverable

`schemas/oig/0.1/` should contain JSON Schema, JSON-LD context, relationship vocabulary, example graph, validation tests, and STIX/MISP mapping tables. A reference bundle might look like:

```json
{
  "id": "oig:claim:example-001",
  "type": "Claim",
  "statement": "[Synthetic claim text]",
  "asserted_by": "oig:source:example-001",
  "observed_at": "2026-07-27T12:00:00Z",
  "confidence": {"level": "moderate", "basis": ["independent-corroboration"]},
  "relationships": [
    {"type": "supports", "target_ref": "oig:event:example-001", "method": "document-analysis"}
  ]
}
```

The example must remain synthetic. Its purpose is to enable developers to build parsers, graph stores, and analytic applications immediately.

## 4. Intelligence Packs

An Intelligence Pack is where OOSIS becomes operational. It is a versioned package that combines mission questions, technique references, graph objects, analytic patterns, tool capability classes, validation rules, output templates, and benchmark fixtures for one domain.

| Pack | Mission focus | First outputs |
| --- | --- | --- |
| **Cyber Exposure & Threat Intelligence** | External attack surface, threat actor reporting, vulnerability/exposure prioritisation, defensive detection context | STIX/MISP profile, asset-to-threat graph, ATT&CK mapping, action templates |
| **Fraud & Financial Crime** | Scam infrastructure, mule/network patterns, impersonation, financial/commerce intelligence | entity/organisation graph, risk-signal schema, timeline and link-analysis patterns |
| **Information Confrontation & Cognitive Security** | Coordinated narratives, synthetic/deceptive media, persona ecosystems, hostile influence operations | claim-media-persona graph, narrative timeline, coordination hypotheses, resilience/detection outputs |
| **Child Safety & Safeguarding** | Early-risk intelligence, authorised referral support, victim-centred harm prevention | restricted public profile: requirements, escalation/record model, synthetic test cases; no case or victim material |
| **Counter-Terrorism Support** | Threat indicators, event/campaign context, network and propaganda analysis for authorised prevention work | high-level intelligence requirement and graph profile, source/claim timeline, referral and information-sharing model |
| **Maritime & Supply-Chain Intelligence** | Vessel, port, company, route, sanctions/compliance, incident context | entity-route-event graph and anomaly/verification patterns |

Packs are released one at a time, each with a public charter and contributors who have genuine domain expertise, so no pack depends on a small team standardising every mission at once. The [roadmap](roadmap.md) sequences them.

## 5. AI, data fusion, and analyst augmentation

AI is central to the project, but it needs a disciplined role. OOSIS should standardise patterns rather than bless one model or vendor.

| Pattern | Value | Required benchmark |
| --- | --- | --- |
| Multilingual extraction and translation | Makes global sources searchable and comparable | entity/claim preservation across languages |
| Media/document extraction | Converts unstructured evidence into graph objects | extraction accuracy and provenance retention |
| Entity resolution | Connects accounts, infrastructure, organisations, and events | precision/recall with false-link cost weighting |
| Graph-assisted hypothesis generation | Surfaces non-obvious relationships and gaps | human analyst agreement and contradiction sensitivity |
| Narrative/campaign clustering | Identifies coordinated information activity | temporal/network validation and false-positive analysis |
| AI research agent | Speeds source discovery and structured research | citation integrity, source quality, tool-action logs, human acceptance rate |
| Decision-product drafting | Produces repeatable briefings | factuality, caveat preservation, and reviewer score |

The key innovation is not “add a chatbot.” It is the ability to trace an AI-generated analytic sentence back through graph objects to sources, transformations, tools, and human approval.

## 6. OOVS: assurance as a force multiplier

OOVS is the acceptance-test layer for the ecosystem. It answers questions such as:

- Is an OIG export complete and provenance-preserving?
- Does a technique entry state its false-link and source-volatility limits?
- Does an AI workflow retain inputs, transformations, outputs, and reviewer decisions?
- Does an Intelligence Pack produce products that another team can consume, challenge, and action?
- Does a tool integration generate the mandatory graph fields and test fixtures?

This makes OOVS practical. Teams can use it to evaluate a tool, pipeline, analyst workflow, or finished intelligence product—not just read a governance checklist.

## 7. Benchmark programme

Benchmarks give the project credibility and create a contribution flywheel.

### Benchmark tracks

1. **Provenance:** does a workflow preserve source and transformation history?
2. **Entity resolution:** can it link synthetic multi-platform entities without over-linking?
3. **Claim/media verification:** can it distinguish corroboration, contradiction, and insufficient evidence?
4. **Timeline/geospatial reasoning:** can it build a correct event sequence from controlled public artefacts?
5. **Cyber exposure fusion:** can it connect a synthetic organisation, infrastructure, exposure signals, and defensive actions?
6. **Information confrontation:** can it identify structured narrative coordination without confusing ordinary organic activity for a campaign?

### Benchmark rules

- Use synthetic, consented, or properly licensed public material.
- Publish ground truth, task definitions, metric definitions, baseline systems, and known limitations.
- Measure precision, recall, calibration, reproducibility, analyst time, and false-positive harm—not just raw accuracy.
- Separate research leaderboards from operational claims. A benchmark score is not an authorisation to make a high-consequence decision.

## 8. What is genuinely new

OOSIS becomes consequential if it delivers all of the following together:

1. **A technique language** that users and tool builders can share.
2. **A cross-domain intelligence graph** that retains claims, provenance, uncertainty, and relationships.
3. **Interchange mappings** that let cyber teams interoperate with STIX, MISP, and OpenCTI instead of starting from zero.
4. **Intelligence Packs** that turn an abstract framework into missions practitioners recognise.
5. **Benchmark fixtures** that let the community test tools, AI, and analyst workflows openly.
6. **OOVS acceptance tests** that make the ecosystem defensible and procurement-ready.

No one of these is unique. The combination, maintained openly under OWASP, can be.

## 9. Reference implementation path

The standard is documentation-first and executable: structured data and validators come before any application.

| Repository area | Purpose | State |
| --- | --- | --- |
| `oovs/` | Requirements, acceptance tests, assessment schema | Released |
| `oig/` | Graph schema and synthetic examples | Preview |
| `ottm/` | Technique record schema and records | Preview |
| `ootg/` | Testing scenarios and fixtures | Template published |
| `scripts/`, `tests/` | Validation and fixtures | Available |
| `releases/` | Version notes, manifests, and hashes | Available |

Directories for mappings, Intelligence Packs, benchmarks, and reference converters are added when their first reviewed content is ready, so the layout always reflects delivered work. The near-term milestone is a contributor being able to validate a technique record, load an OIG example, convert a cyber bundle, and reproduce a synthetic benchmark.

## 10. Long-term trajectory

1. **Establish the language:** released assurance requirements, a core graph profile, technique records, and safe fixtures.
2. **Prove implementation:** reference integrations, cross-sector pilots, and published benchmark results.
3. **Become connective tissue:** a common interchange and assurance layer for OSINT tools, fusion teams, AI-assisted workflows, and intelligence education.

Dates and per-release contents are set by the [roadmap](roadmap.md) rather than by this note.

This is sufficiently ambitious to matter—and concrete enough to start this month.
