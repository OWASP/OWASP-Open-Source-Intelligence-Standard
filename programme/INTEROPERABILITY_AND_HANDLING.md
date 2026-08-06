# Interoperability and Information-Handling Baseline

## Purpose

OOSIS must add value by connecting existing standards, not by inventing unnecessary replacement formats. The baseline below applies to public examples and future implementation profiles.

## Interoperability approach

| Need | OOSIS approach |
| --- | --- |
| Cross-domain graph exchange | OIG JSON and JSON-LD profile; JSON-LD is a W3C Recommendation for serialising linked data and directed graphs |
| Cyber threat-intelligence representation | Map applicable OIG content to STIX 2.1 |
| Cyber threat-intelligence transport | Support TAXII 2.1 profiles where an implementation needs RESTful exchange |
| Cyber sharing/taxonomies | Map appropriate content to MISP objects, taxonomies, galaxies, and sharing distribution fields |
| Handling boundaries | Preserve existing labels; use FIRST TLP 2.0 labels when TLP is selected by a source or sharing community |
| Local/regional requirements | Implement as explicit profiles/extensions; do not present one jurisdiction’s rule as global default |

## Handling model

OOSIS does not create a competing sensitivity label. A record may carry:

- `handling_label`: a source-provided or community-selected label, such as `TLP:CLEAR`, `TLP:GREEN`, `TLP:AMBER`, or `TLP:RED`;
- `handling_basis`: source policy, contract, consent, law, or programme rule;
- `distribution_note`: a short human-readable caveat; and
- `retention_note`: a contextual retention constraint, where applicable.

FIRST TLP 2.0 defines four sharing-boundary labels used by the worldwide CSIRT community. OOSIS references the label unchanged when it applies; it does not reinterpret TLP or claim that TLP alone resolves legal, privacy, contractual, or safeguarding obligations.

## Minimum OIG metadata

Every material object or relationship should preserve: creator/collector, source reference, observed time, method/technique, transformation history, confidence, and handling context. This is the minimum needed for an external team to interpret and reuse information without silently stripping operational meaning.

## Security considerations

JSON-LD and graph data should be treated as data, not executable content. Implementers must validate input, avoid automatic dereferencing of untrusted identifiers/URLs, apply resource limits, and preserve source handling constraints through conversions.

## References

- [W3C JSON-LD 1.1](https://www.w3.org/TR/json-ld/)
- [OASIS STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/)
- [OASIS TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html)
- [FIRST Traffic Light Protocol 2.0](https://www.first.org/tlp/)
