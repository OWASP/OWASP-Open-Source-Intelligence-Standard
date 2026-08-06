# OOSIS Top Ten — Concept and Methodology

> **Document type:** Concept and methodology note for a future OOSIS Top Ten edition. The candidate themes below become an edition through the published method in this document: an evidence corpus, a safe data call, regional and domain review, and public comment. No edition or ranking is released, and the numbering below is not an identifier scheme.

The OOSIS Top Ten is intended as the programme's most accessible entry point, in the way the OWASP Top 10 creates a shared language for application-security risk. It is derived from evidence, benchmark failures, and field feedback rather than published as a general tool list.

## Candidate title

**OOSIS Top Ten Intelligence Failure Modes**

This framing is strong because it speaks to every user of OSINT: an analyst, a tool builder, a SOC leader, an investigator, a procurement team, an AI developer, and a public-sector unit. It is about why intelligence fails to become action—not about how to target people.

## Candidate failure modes

These candidates come from documented failure patterns and current OOVS requirements. Scoring and review decide the final list and its order.

| # | Failure mode | What breaks | OOSIS response |
| --- | --- | --- | --- |
| 1 | Untrusted provenance | Nobody can establish what was observed, changed, or derived | OIG source and evidence model; OOVS provenance requirements |
| 2 | Identity collapse | Different people, personas, assets, or organisations are wrongly merged | Explicit entity-resolution states, confidence, and benchmark penalties |
| 3 | Context stripping | A true item is used to support a false conclusion | Time, location, source, claim, and contradiction relationships |
| 4 | Synthetic or manipulated media | Generated or edited content is mistaken for evidence | Media-analysis techniques and provenance-signal limits |
| 5 | Tool-chain opacity | Analysts cannot explain what an automated tool did | Tool-run objects, technique records, reproducibility requirements |
| 6 | AI-generated false intelligence | Model output becomes a claim without source support | AI provenance, citation integrity, and human-acceptance measures |
| 7 | Collection blind spots | One platform, language, region, or community is mistaken for reality | Collection hypotheses, source-coverage model, multilingual techniques |
| 8 | Relationship overclaiming | Weak correlations become asserted networks or attribution | Relationship semantics, hypothesis states, false-link cost metrics |
| 9 | Analysis without action | Reports fail to produce a detection, decision, referral, or mitigation | Typed actions, product contracts, and feedback loop |
| 10 | Information-integrity failure | Coordinated narratives and deceptive activity are recognised too late or misread | Claim, media, persona, and timeline analysis with resilience outputs |

## Method to make it credible

1. Collect candidate failure modes from benchmark errors, after-action reviews, research, and public community input.
2. Score each by prevalence, impact, exploitability, detectability, and feasibility of mitigation.
3. Publish the scoring method, source base, disagreements, and limitations.
4. Release the Top Ten with a technique/mapping/benchmark route for every item.
5. Refresh on a predictable cycle; never retroactively rewrite a released edition.

The Top Ten attracts attention. The OIG, Technique Matrix, Intelligence Packs, and benchmarks turn that attention into a durable technical project.
