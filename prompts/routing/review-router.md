# Review Router

1. Determine the requested mode: code review by default, [standards audit](../../references/standards-audit.md) for rule conformance, categories, inventories, or measured counts. Follow the requested depth.
2. Resolve scope using the [scope model](../core/01-scope-model.md). Report an empty code set when that is the resolved result.
3. Read applicable repository instructions, development rules, check configuration, and confirmed contracts. Apply the [engineering-quality baseline](../../references/engineering-guidelines.md) within the project rules; read applicable rules together with their prerequisites and exceptions.
4. Classify the change shape and domain. Start with [maintainability](../modules/maintainability.md), [duplication and abstraction](../modules/duplication-abstraction.md), and [cognitive complexity](../modules/cognitive-complexity.md).
5. Add modules by evidence:
   - coordination or shared state: [coupling and side effects](../modules/coupling-side-effects.md);
   - failure paths: [errors and observability](../modules/errors-observability.md);
   - visible performance waste: [performance](../modules/obvious-performance.md);
   - dependency or ownership movement: [architecture drift](../modules/architecture-drift.md);
   - confirmed behavior contracts or high-risk validation: [behavior and validation](../modules/behavior-validation.md) and the matching [evidence requirements](../../references/validation-evidence.md).
6. Select a matching [domain specialization](../specializations/) or [engineering pattern](../../references/patterns/index.md) when it improves the assessment.
7. Apply the [evidence filter](../anti-patterns/catalog.md) and [mode-specific output](../core/03-output-contract.md). For an audit, preserve requested coverage and separate rule provenance, examples, and measured counts.
