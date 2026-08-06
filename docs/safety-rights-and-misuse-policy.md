# Safety, Rights, and Misuse Policy

## Purpose

OSINT can help protect people from serious harm. It can also scale harassment, discrimination, false accusation, unlawful surveillance, and exploitation. This policy makes responsible use a design requirement of OOVS rather than a disclaimer.

## Operating principles

1. **Lawful, necessary, proportionate:** establish authority and the least intrusive effective approach before work starts.
2. **Do no additional harm:** do not make a vulnerable person more discoverable or a harmful actor more capable.
3. **Human accountability:** a named human owns high-consequence decisions; automation informs rather than decides.
4. **Verification before consequence:** distinguish reports, leads, and verified findings; carry uncertainty forward.
5. **Data minimisation and expiry:** collect, retain, access, and share only what the approved purpose needs.
6. **Independent challenge:** enable privacy, legal, safeguarding, and domain expertise to question a decision.

## Jurisdiction and professional responsibility

This policy and OOVS provide an assurance framework, not legal advice or authority to investigate. Laws, mandates, platform rules, contracts, professional duties, and safeguarding procedures vary by context and change over time. Implementers must identify the obligations that actually apply and obtain qualified review for high-consequence work.

Before material collection or processing, the responsible team should record:

- the decision or protective objective and accountable owner;
- authority or policy basis and jurisdiction/context;
- necessity, proportionality, and less-intrusive alternatives;
- data categories, incidental-data treatment, access, retention, and deletion;
- foreseeable affected people, disparate impacts, and safe failure mode;
- correction, redress, safeguarding, and escalation routes; and
- review/expiry date and stop conditions.

“Publicly available” describes accessibility; it does not by itself establish legal authority, fairness, necessity, accuracy, or permission for a particular use.

## Content boundary

| Category | Repository treatment |
| --- | --- |
| Defensive, lawful verification and governance | Publishable after normal review |
| High-risk cases: terrorism, child safety, conflict, elections, biometrics, tracking, attribution | Publish policy controls, synthetic scenarios, review criteria, and outcome measures; require enhanced review |
| Personal identifiers, live cases, sensitive victim data, suspected-person lists | Never publish or accept in project spaces |
| Methods for stalking, covert identity linking, account compromise, evasion, coercion, social engineering, or access-control bypass | Do not publish; redirect discussion to legitimate protective controls |
| Suspected illegal child sexual abuse material or imminent threat material | Do not download, reproduce, or investigate through this project; follow the applicable organisational emergency/safeguarding reporting route |

## High-risk use review

Before publishing a profile or requirement about high-risk use, the proposer must document:

- the public-interest outcome and authority model;
- affected people and likely disparate impacts;
- data categories, access, retention, and deletion plan;
- human decision point, appeal/correction options, and escalation route;
- validation measures, false-positive/false-negative harms, and safe failure mode;
- legal, privacy, safeguarding, and domain-expert review; and
- why the content cannot reasonably enable abuse if released.

The project will publish only the portion that is safe and broadly useful. Operational details belong, if anywhere, within authorised organisations and their applicable law—not in an open OWASP standard.

## Governance and review

### Founding roles

- **Project leaders:** OWASP compliance, release approval, continuity, and public accountability.
- **Editors/maintainers:** quality, terminology, issue triage, and evidence traceability.
- **Safety and rights review group:** privacy, human rights, child safeguarding, legal/policy, and abuse-prevention expertise.
- **Technical and method working group:** evidence methods, provenance, AI assurance, interoperability, and test procedures.
- **Use-case working groups:** cyber, fraud, child safety, counter-terrorism support, humanitarian/public-interest, and corporate security.

No single group should control normative requirements, safety review, and release approval. At least two organisations or unaffiliated reviewers should participate in substantive releases once the project has grown beyond its founding team.

### Review classes

| Change | Required review |
| --- | --- |
| Typo or link | One maintainer |
| Non-normative explanatory material | One editor + one subject reviewer |
| Normative requirement or test method | Two reviewers, public review window, recorded resolution |
| High-risk material | Two subject reviewers plus one safety/rights reviewer, public review window, release-leader approval |
| Scope, governance, or release | Leaders, recorded decision, public notice |

### Decision record

Every material decision receives a short decision record: context, options, evidence, conflicts of interest, decision, dissent/uncertainty, owner, and review date. Use a pull request or issue so the record is public and searchable.

## Incident and correction process

1. **Contain:** remove or restrict unsafe sensitive content quickly; preserve only the minimum record needed for review.
2. **Assess:** determine affected people, source, distribution, and needed notifications with OWASP escalation where applicable.
3. **Correct:** fix the document, release a correction note, and notify known downstream users when material.
4. **Learn:** record the cause and changed control without re-publishing sensitive details.

This project will not adjudicate individual accusations or conduct investigations into named people.
