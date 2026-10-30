# Review Router

1. Resolve scope using prompts/core/01-scope-model.md. Stop when the selected scope contains no relevant changes.
2. Classify the change shape: hotfix, refactor, feature, cleanup, or boundary movement. Infer frontend, backend, or mixed domain from the diff.
3. Load the base modules: maintainability, duplication-abstraction, and cognitive-complexity.
4. Add modules by evidence:
   - coordination or shared state: coupling-side-effects
   - failure paths: errors-observability
   - visible performance waste: obvious-performance
   - dependency or ownership movement: architecture-drift
   - confirmed behavior contracts or high-risk verification: behavior-validation
5. Apply a specialization when the requested review lens or changed code warrants it.
6. Apply prompts/anti-patterns/catalog.md and the output threshold to filter and rank findings.
