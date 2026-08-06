# OWASP OSINT Verification Standard (OOVS) v0.1.0

- **Version:** 0.1.0
- **Status:** Released
- **Release date:** 2026-08-05
- **Assurance baseline:** L1 — Foundational
- **Normative source:** this document and `requirements.json`
- **Machine-readable artefacts:** `requirements.json`, `requirements.schema.json`, `tests.json`, `assessment.schema.json`
- **License:** CC BY-SA 4.0

## 1. Purpose

The OWASP OSINT Verification Standard (OOVS) defines a testable assurance baseline for an open-source-intelligence **workflow** or **intelligence product**. It answers a practical question: is a defined target authorised, bounded, traceable, analytically transparent, appropriately verified, safely disseminated, and governed for its intended use?

OOVS is the normative assurance core of the OWASP Open Source Intelligence Standard (OOSIS) programme. It complements, rather than replaces, professional training, applicable law, and organisational policy.

## 2. Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described by [BCP 14](https://www.rfc-editor.org/info/bcp14) when, and only when, they appear in uppercase.

Sections 1–7 and the ten requirement statements are normative. Rationale, examples, mappings, and templates are informative unless explicitly marked otherwise.

## 3. Terms

- **Assessment period:** the explicit time interval and sample to which an OOVS assessment applies.
- **Assessment target:** either a defined workflow or a defined intelligence product.
- **Corroboration:** evidence that supports or challenges a claim and has been evaluated for relevance, quality, and independence.
- **High-consequence use:** use that can materially affect a person's safety, liberty, rights, access, reputation, livelihood, or privacy, or a comparably significant public or organisational interest.
- **Independent origin:** a source of relevant information that does not derive the material assertion from the same underlying origin as another counted source. Separate publications, accounts, or reposts are not necessarily independent.
- **Intelligence product:** an assessment prepared to support a stated decision or protective action, rather than an unassessed collection of links or data.
- **Material claim:** a statement that can affect a judgment, action, risk rating, attribution, referral, or public communication.
- **Provenance record:** structured information identifying what was observed, from where, when, by whom or what, how it was acquired, and how it was transformed or handled.
- **Verification record:** a structured record of a claim, the checks performed, evidence considered, contradictions and alternatives, result, uncertainty, reviewer, and time.
- **Workflow:** a repeatable sequence for framing, collecting, preserving, processing, analysing, reviewing, disseminating, and correcting OSINT-derived material.

## 4. Assessment and result model

### 4.1 Assessment targets

This version supports two targets:

1. **Workflow assessment:** a named, bounded workflow used for stated use cases; or
2. **Product assessment:** a named product or product type created during a defined period.

A tool, model, team, supplier, or organisation can supply evidence within an assessment. OOVS scopes results to the assessed workflow or product rather than declaring an entire organisation or product line conformant.

### 4.2 Required scope

Every assessment **MUST** record:

- OOVS version;
- target type, name, owner, and intended decision or use;
- included and excluded processes, systems, locations, and use cases;
- assessment period and sample-selection method;
- whether high-consequence use is in scope;
- assessor role and any material conflict of interest;
- result and evidence reference for every requirement; and
- limitations, open findings, and next review date.

Evidence references **SHOULD** point to controlled records rather than copying personal, operational, or restricted data into an assessment report.

### 4.3 Requirement result states

| State | Meaning |
| --- | --- |
| `Implemented` | All pass criteria were met for the assessed scope and sample. |
| `Partially implemented` | Some controls or evidence exist, but at least one pass criterion was not met. |
| `Not implemented` | The requirement is absent, ineffective, or unsupported by evidence. |
| `Not applicable` | An objective precondition is absent and the written rationale was accepted by the assessor. Cost, inconvenience, or lack of evidence is not a valid rationale. |

An assessment outcome is `meets_all_applicable` only when every applicable requirement is `Implemented`. Any other combination is `does_not_meet`. A result applies to the stated scope and period.

### 4.4 Public claim format

Use this wording when publishing a result:

> **[Target] was assessed against OOVS v0.1.0 for [scope] during [period]. The recorded outcome was [meets_all_applicable / does_not_meet]. An OOVS assessment records a defined scope and result; it is not certification or a determination of legal compliance.**

Self-assessment and independent assessment **MUST** be distinguished. The OWASP project publishes the standard; it does not approve individual assessment results.

## 5. Foundational requirements

### OOVS-v0.1.0-01 — Authorised purpose and proportionality

**Objective:** Prevent collection or analysis without a defined, accountable, and appropriately bounded purpose.

**Requirement:** Before material collection or processing begins, the assessment target MUST record the intended decision or protective outcome, accountable owner, applicable authority or policy basis, scope, necessity, expected benefit, foreseeable harm, less-intrusive alternatives, retention intent, review point, and stop or escalation conditions. Work MUST stop or be escalated when authority or purpose is materially unclear.

**Minimum evidence:** approved mission or product plan; authority/policy reference; pre-work necessity, proportionality, and risk record; retention/review date.

**Assessment procedure:** select representative work initiated during the assessment period and confirm the required record existed before material collection, matched the actual activity, and was re-approved after material scope changes.

**Pass criteria:** all sampled work has a timely, accountable record; activity remains within its approved purpose and scope; material deviations are stopped or approved and recorded.

### OOVS-v0.1.0-02 — Collection boundary and data minimisation

**Objective:** Limit collection to relevant information obtained through authorised, permitted means.

**Requirement:** The assessment target MUST define and enforce source, technique, field, access, and time boundaries. It MUST minimise incidental and sensitive data and document approved exceptions. It MUST NOT bypass access controls, obtain or use credentials without authority, induce disclosure through deception, or treat public availability alone as sufficient authority to process data.

**Minimum evidence:** collection plan; source/technique allow and deny rules; tool configuration; minimisation and incidental-data handling rules; exception approvals.

**Assessment procedure:** compare sampled acquisitions and tool settings with approved boundaries, including rejected or escalated collections and the disposition of incidental data.

**Pass criteria:** sampled collection is relevant and within boundary; prohibited methods are blocked; sensitive exceptions have prior approval and safeguards; unnecessary data is not retained.

### OOVS-v0.1.0-03 — Source provenance and integrity

**Objective:** Let an authorised reviewer determine what was observed, its origin, and its transformation history.

**Requirement:** Every material item MUST have a provenance record containing a source reference, observation time and time zone, collector or system, acquisition method, original-versus-derived status, material transformations, handling context, and an integrity mechanism appropriate to the source and consequence. Original and derived artefacts MUST remain distinguishable. A hash or provenance credential MUST NOT be represented as proof that content is truthful or authentic.

**Minimum evidence:** provenance records; source snapshots or controlled references where permitted; transformation logs; integrity values where appropriate; chain-of-handling record for consequential material.

**Assessment procedure:** trace sampled product claims backward through transformations to the observed source and forward to derived artefacts; verify timestamps, identifiers, and integrity controls are internally consistent.

**Pass criteria:** sampled material is traceable without silent gaps; originals and derivatives are distinguishable; changes are recorded; integrity signals are described within their actual limits.

### OOVS-v0.1.0-04 — Source and claim assessment

**Objective:** Prevent source reputation, repetition, metadata, or automation from being mistaken for proof.

**Requirement:** The assessment target MUST evaluate source reliability separately from claim credibility and MUST link each material claim to supporting and contradicting evidence. When apparent corroboration affects a decision, the analyst MUST investigate shared origins far enough to avoid counting reposts, quotations, syndicated reports, or model restatements as independent support. Earliest-discoverable-instance, metadata, detector, and content-provenance results MUST be treated as signals with documented limitations, not standalone proof.

**Minimum evidence:** source assessments; claim-evidence links; origin or citation-chain notes; contradiction and gap log; verification record.

**Assessment procedure:** sample material claims, reconstruct their evidence chains, cluster evidence that shares an origin, and confirm source reliability did not substitute for assessment of the specific claim.

**Pass criteria:** every sampled material claim is traceable; common origins are not overcounted; contradictions and unknowns are visible; technical signals are not overstated.

### OOVS-v0.1.0-05 — Corroboration and confidence

**Objective:** Align verification depth and expressed confidence with the consequence of error.

**Requirement:** Every material analytic judgment MUST state confidence and its basis, including provenance quality, independence, contradictions, assumptions, and significant gaps. High-consequence claims MUST receive corroboration appropriate to the decision and threat model, including independent-origin evidence where reasonably available. When sufficient corroboration is unavailable, the claim MUST be labelled unverified or insufficiently corroborated and MUST NOT be the sole basis for consequential action unless a documented, authorised emergency process applies.

**Minimum evidence:** confidence statement; corroboration rationale; source-independence assessment where relevant; alternatives/contradictions; emergency approval when used.

**Assessment procedure:** compare the language and proposed action for sampled claims with the strength, independence, and recency of evidence; test whether multiple mentions were incorrectly treated as multiple origins.

**Pass criteria:** confidence is supported rather than asserted; verification depth is consequence-sensitive; unsupported claims are appropriately constrained; exceptions are authorised, time-limited, and reviewed.

> OOVS sets no universal fixed source count. Two weak reports can be less probative than one strong primary record, and many reports can share one origin.

### OOVS-v0.1.0-06 — Analytic transparency and reproducibility

**Objective:** Make reasoning reviewable without requiring unsafe disclosure.

**Requirement:** Intelligence products MUST distinguish observed information, analytic inference, assumptions, alternatives, and unknowns. Material methods, selection criteria, queries, transformations, exclusions, and limitations MUST be recorded at a level that enables an authorised, competent reviewer to reconstruct the reasoning while protecting sensitive data and methods.

**Minimum evidence:** analytic record; method/query log; fact-inference labels; alternatives; peer or independent review notes; reproducibility result.

**Assessment procedure:** have an authorised reviewer reconstruct a representative product's reasoning from controlled records and document whether the reviewer reaches a materially compatible conclusion and why any difference arose.

**Pass criteria:** reasoning can be followed end to end; material assumptions and exclusions are explicit; reproduction differences are captured and resolved or carried as uncertainty.

### OOVS-v0.1.0-07 — Rights, privacy, and safeguarding

**Objective:** Prevent avoidable harm and preserve applicable rights throughout the information lifecycle.

**Requirement:** The assessment target MUST identify applicable legal, policy, contractual, human-rights, privacy, records, and safeguarding obligations for its context and MUST implement risk-proportionate minimisation, access control, security, retention/deletion, accuracy review, and correction or redress routes. High-consequence use MUST receive documented specialist review. Material concerning minors or vulnerable people MUST follow applicable safeguarding and reporting procedures and MUST NOT be placed in public project channels.

**Minimum evidence:** contextual obligations register; risk or impact assessment; access review; retention/deletion records; safeguarding route; correction/redress procedure and sampled outcomes.

**Assessment procedure:** inspect safeguards across sampled records and products, test access and expiry, and verify that a material error can be corrected through all known downstream recipients.

**Pass criteria:** obligations are context-specific rather than assumed universal; controls match the risk; access and retention are enforced; correction and safeguarding routes are usable.

### OOVS-v0.1.0-08 — AI and automation assurance

**Objective:** Keep humans accountable and prevent automated output from laundering uncertainty.

**Requirement:** AI-generated or AI-transformed output MUST be treated as an unverified analytical aid until validated against traceable evidence. The assessment target MUST record the system and version, relevant configuration, input provenance, material transformations, evaluation method, known limitations, material output changes, and accountable human reviewer. AI output MUST NOT be counted as independent corroboration of its inputs or make an unreviewed high-consequence determination.

**Minimum evidence:** system inventory/version record; input/output and transformation trace; task-relevant evaluation; error monitoring; human review and override record; prohibited-use controls.

**Assessment procedure:** trace sampled AI-assisted statements to inputs and reviewer decisions; test known failure cases and verify the workflow prevents unreviewed high-consequence release or action.

**Pass criteria:** AI involvement is visible; material outputs are evidence-traceable and validated; limitations are communicated; accountable human review occurs before consequence.

**Applicability:** may be `Not applicable` only when no AI system materially collects, transforms, ranks, links, summarises, analyses, or drafts content in the assessed target.

### OOVS-v0.1.0-09 — Dissemination and action controls

**Objective:** Preserve uncertainty, handling intent, and need-to-know boundaries through action and sharing.

**Requirement:** Intelligence products MUST identify their intended decision, audience, confidence, caveats, handling restrictions, validity or review time, and accountable release authority. Dissemination MUST use the minimum necessary detail and preserve material caveats downstream. The workflow MUST distinguish an allegation or report, a lead, an analytic assessment, and a verified finding, and MUST provide a route to withdraw or correct distributed material.

**Minimum evidence:** approved product; recipient/authority record; handling decision; action log; downstream correction or withdrawal mechanism.

**Assessment procedure:** inspect sampled releases and recipient lists, follow one claim into a downstream product or action, and test correction propagation.

**Pass criteria:** recipients and detail are justified; caveats persist; status is not inflated; corrective messages can reach known recipients. A handling scheme such as TLP is used where appropriate and is not represented as a substitute for law or policy.

### OOVS-v0.1.0-10 — Governance, audit, and improvement

**Objective:** Ensure accountable ownership, competent challenge, correction, and measurable learning.

**Requirement:** The assessment target MUST assign accountable roles; define competence and training expectations; maintain an independent challenge route proportionate to risk; review controls periodically; and record incidents, material errors, corrections, assessment findings, and resulting improvements. High-consequence release approval MUST NOT rely solely on the person or automated system that produced the judgment.

**Minimum evidence:** role and separation-of-duty record; competence/training evidence; review schedule; audit sample; challenge decisions; incident/correction log; improvement actions.

**Assessment procedure:** inspect governance records, trace a challenge or correction to its disposition, and verify overdue actions and repeat failures are escalated.

**Pass criteria:** ownership and review are operating in practice; challenge can change an outcome; corrections reach affected products; improvement actions have owners and due dates.

## 6. Lifecycle gates

| Gate | Required question | Primary requirements |
| --- | --- | --- |
| G0 — Initiate | Is the purpose authorised, necessary, proportionate, and safely bounded? | 01, 02, 07 |
| G1 — Acquire | Is collection permitted, minimised, and traceable? | 02, 03 |
| G2 — Assess | Are claims, origins, contradictions, and uncertainty evaluated? | 04, 05, 06 |
| G3 — Automate | Is automation traceable, evaluated, and human-accountable? | 03, 06, 08 |
| G4 — Release | Is sharing necessary, controlled, caveated, and actionable? | 07, 09, 10 |
| G5 — Learn | Were errors, outcomes, and improvements captured? | 07, 10 |

## 7. Assessment evidence rules

1. Evidence **MUST** be sufficient to support the recorded result but **SHOULD** be referenced rather than duplicated.
2. Sampling **MUST** be described and **MUST** include exceptions, failed cases, and high-consequence items where they exist.
3. An assessor **MUST** record limitations and conflicts of interest.
4. Absence of evidence cannot be scored `Implemented`.
5. Sensitive evidence **MUST** remain under the assessed organisation's authorised controls.
6. A public assessment **SHOULD** publish scope, method, aggregate results, limitations, and safe evidence references.

## 8. Informative confidence statement

> **Assessment:** [material judgment].  
> **Confidence:** [low / moderate / high], based on [provenance, independent origins, methods, and recency].  
> **Observed information:** [brief list].  
> **Inference and assumptions:** [brief list].  
> **Contradictions, alternatives, and gaps:** [brief list].  
> **Appropriate use:** [supported decision].  
> **Not sufficient for:** [unsupported decision].  
> **Review or expiry:** [time/event].

This template does not impose a universal probability lexicon or source-grading system. An implementation may use a controlled lexicon when it defines the terms, trains users, and keeps source reliability, information credibility, likelihood, and confidence distinct.

## 9. External mappings

The informative [mappings](mappings.md) identify related public guidance. A mapping means "relevant to" rather than equivalent to or compliant with. Applicable law and organisational policy always require contextual analysis by qualified people.

## 10. Versioning and feedback

Requirement identifiers use the `OOVS-v0.1.0-NN` pattern and are stable within the 0.1 line, as described in the [release policy](../../programme/RELEASE_POLICY.md). Later versions may add requirements, add assurance depth for higher-consequence use, and publish clause-level mappings.

Implementation feedback shapes the next version. Useful contributions include assessment results from synthetic or non-sensitive material, wording that produced inconsistent assessments, requirements that were difficult to implement in small teams, and jurisdictional considerations that need an explicit profile. Use the repository issue templates, and do not include personal, live-case, victim, credential, or operationally sensitive information.
