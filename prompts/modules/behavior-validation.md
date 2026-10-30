# Behavior and Validation Evidence

Load when the diff changes behavior covered by a confirmed requirement, design, or API contract, or touches high-risk boundaries such as permissions, migrations, concurrency, external effects, or irreversible operations.

## Contract alignment

- Treat the confirmed requirement or contract as expected behavior; trace it forward into code, tests, and caller-facing docs.
- Trace changed behavior back to the contract to find material undocumented or unapproved behavior.
- Use code, tests, and runtime results as evidence of observed behavior. Surface unclear contract meaning as an unresolved decision.
- For refactors, assess behavior preservation against relevant observable results and verification evidence.

## Risk evidence

- Relate each critical behavior to its implementation path, state boundary, verification, runtime environment, and observable assertion.
- Use mocks to check application decisions; use integration evidence for semantics owned by databases, caches, and external services.
- For outbound HTTP changes, compare the business payload with the final method, URL, headers, query, body, and field mapping conditions.

Report material gaps with evidence from the contract and changed code, then state caller or operational impact and a practical correction.
