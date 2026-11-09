---
name: pragmatic-review
description: Review code diffs or audit development-standard compliance using repository rules, evidence, and maintainability criteria.
---

# Pragmatic Review

Assess selected changes against repository rules and confirmed contracts. Provide general engineering-quality criteria, review methods, and reusable improvement patterns.

## Authority and mode

User instructions and repository-specific rules take precedence over general defaults. Treat confirmed contracts as acceptance, code and runtime results as current facts, and patterns as options whose applicability is supported by evidence.

Choose the requested output purpose:

- **Code review** is the default: report actionable findings ranked by operational and maintenance cost.
- **Standards audit** applies to development-rule conformance checks, problem categories, compliance inventories, or measured counts. Follow [standards audit](references/standards-audit.md) at the requested granularity.
- **Implementation, diagnosis, or validation guidance:** Read the [engineering-quality baseline](references/engineering-guidelines.md), [validation evidence](references/validation-evidence.md), or [pattern index](references/patterns/index.md) for the requested decision, and act within the user's authorized task.

## Read model

For review and audit, read:

- `prompts/core/`: authority, scope, prioritization, and mode-specific output.
- [engineering-quality baseline](references/engineering-guidelines.md): shared implementation, diagnosis, and assessment criteria.
- [review router](prompts/routing/review-router.md).
- [evidence filter](prompts/anti-patterns/catalog.md).

Start with maintainability, duplication-abstraction, and cognitive-complexity in `prompts/modules/`. Load coupling-side-effects, errors-observability, obvious-performance, architecture-drift, or behavior-validation when the diff supplies matching evidence.

Apply the shared baseline within repository rules and confirmed acceptance. Read [validation evidence](references/validation-evidence.md) for relevant risk boundaries, and select patterns or domain specializations that help assess an observed issue or proposed improvement.

Scope selects the code under assessment; focus sets priorities inside that scope. Each finding meets the evidence threshold. Investigate an `if`, constant, mapping, Mixin, or DTO conversion through its ownership, behavior, and concrete cost.
