# Validation Fixtures

`tests/fixtures/manifest.json` declares the positive and expected-failure fixtures executed by `scripts/validate_assets.py`.

Positive fixtures prove that the canonical OOVS catalogue, acceptance tests, synthetic assessment, OIG graph, and OTTM record satisfy their declared schemas and semantic checks. Negative fixtures prove that validation rejects:

- unknown OIG node references;
- missing mandatory OTTM fields;
- invalid OOVS assessment states;
- acceptance tests mapped to unknown requirements; and
- requirements without evidence definitions.

A negative fixture passes the test suite only when it fails validation for the expected reason. All fixture content is synthetic and must remain free of personal, live-case, victim, credential, or operational data.
