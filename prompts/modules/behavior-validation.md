# Behavior and Validation Evidence

Load for changes governed by confirmed requirements or contracts, or involving permissions, migrations, concurrency, shared state, external effects, and recovery.

## Contract alignment

Trace confirmed acceptance into code, tests, and caller-facing sources. Trace the diff back to its requirements and approved changes. Use code and runtime results as current facts, and record material contractual decisions still awaiting confirmation.

For refactors, assess behavior preservation against observable results and state boundaries.

## Risk and evidence

Read [validation evidence](../../references/validation-evidence.md) for the relevant capability and target-environment checks. Relate each critical behavior to its implementation path, state boundary, verification method, environment, expectation, and actual result.

For outbound HTTP, compare business payload, final method, address, headers, query, body, and remote result. Assess compatibility, successful checkpoints, partial failure, and recovery according to the actual use case.

Report material gaps with their coverage and operational impact, then suggest the smallest verification or correction that can resolve them.
