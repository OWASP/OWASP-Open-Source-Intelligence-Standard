# Governance

## Status and purpose

This governance model applies to the OWASP Open Source Intelligence Standard (OOSIS) programme and its OOVS asset. It is designed for transparent, vendor-neutral, safety-aware maintenance. It does not assert an OWASP maturity tier or create an accredited certification body.

## Principles

- **Open decisions:** material decisions are traceable to public issues or pull requests unless sensitive-content handling requires a private OWASP route.
- **Evidence before authority:** requirements and public claims are supported by reviewable evidence and explicit limitations.
- **Separation of interests:** no person or organisation controls proposal, safety review, technical approval, and release approval for a material change.
- **Vendor and government neutrality:** participation does not grant endorsement; conflicts are declared and managed.
- **Safety and rights:** public collaboration uses synthetic, consented, anonymised, or non-sensitive material and follows the repository safety policy.
- **Global applicability through profiles:** jurisdiction-specific rules are labelled and reviewed rather than presented as universal.

## Roles

| Role | Responsibilities | Appointment and limits |
| --- | --- | --- |
| Project leaders | OWASP relationship, continuity, access, release approval, escalation | Recognised through OWASP project records; must follow current OWASP policy |
| Maintainers/editors | Issue triage, editorial quality, schemas, validation, release preparation | Appointed through a public decision based on sustained contribution |
| Requirement reviewers | Testability, evidence, interoperability, implementation impact | Must be independent of the proposal author for normative approval |
| Safety and rights reviewers | Privacy, human rights, safeguarding, misuse, disparate impact | Required for high-risk or rights-affecting material |
| Release manager | Manifest, version, change log, checks, and publication evidence | Cannot be the sole approver of the release |
| Contributors | Issues, reviews, requirements, tests, mappings, code, and translations | Open to all under the Code of Conduct and contribution terms |

Named role holders and their terms should be recorded in a version-controlled `MAINTAINERS.md` after confirmation. Absence of a named owner pauses, rather than silently delegates, that responsibility.

## Change classes

| Change class | Minimum process |
| --- | --- |
| Typo, link, formatting | One maintainer; validation where applicable |
| Informative explanation or example | One maintainer and one relevant subject reviewer |
| Normative requirement, acceptance test, or schema semantics | Public proposal; at least 14 days comment for a minor release; proposal author plus two approving reviewers, including relevant safety review |
| High-risk profile or material | At least two subject reviewers, one safety/rights reviewer, documented misuse review, and public comment |
| Scope, governance, identifier, or compatibility change | Public RFC; at least 30 days comment; leader consensus or documented vote |
| Release | Release checklist plus two approvals, with any open issue disclosed in the release notes |

The public-comment clock starts only when the proposal is complete enough to review. Maintainers may extend it for accessibility, holidays, translation, or material changes.

## Decision record

A material decision records:

- context and requested outcome;
- options and evidence;
- affected assets and compatibility;
- safety, rights, and misuse implications;
- declared conflicts of interest and recusals;
- decision, rationale, dissent, and unresolved uncertainty;
- accountable owner and review date; and
- links to implementation and validation evidence.

Routine changes use lazy consensus. When consensus fails, eligible non-recused maintainers vote; the decision needs a simple majority and at least two affirmative votes. A tie or unresolved safety objection escalates to project leaders and, where appropriate, OWASP governance.

## Conflicts of interest

Contributors and reviewers must declare material employment, funding, vendor, agency, research, or personal interests relevant to a decision. A person with a direct material interest may provide evidence but must not be the deciding reviewer. Sponsorship never buys requirement wording, ranking, endorsement, or release approval.

## Appeals and corrections

Anyone may request reconsideration with new evidence, a process concern, or a documented safety impact. A non-recused maintainer who did not make the original decision coordinates review. Material released errors follow the correction process in the [Safety, Rights, and Misuse Policy](docs/safety-rights-and-misuse-policy.md#incident-and-correction-process).

## Release integrity

- Development content on the default branch is distinguished from released versions.
- Every release has a version, tag, notes, manifest, compatibility statement, scope notes, and validation record.
- Assessment results are scoped statements; they are never presented as certification, accreditation, or legal compliance.
- Promotion to the 1.0 line follows the evidence criteria in the release policy.
- Published requirement identifiers are not silently reused or renumbered.

## Meetings and records

Public meetings, if held, should publish agenda, attendance, decisions, and action items without sensitive or personal case data. Significant decisions must still be represented in an issue or pull request; a meeting alone is not the decision record.

## Amendments

Changes to this document use the structural-change process above. Emergency safety corrections may be applied immediately and must receive retrospective review and a public, non-sensitive explanation.
