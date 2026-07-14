---
name: pragmatic-review
description: Core maintainability-first code review skill for Claude Code. Use when review scope and focus should be inferred from user intent or natural language, with one public skill product.
---

Use this source skill as the main navigation path:
- `../../../../../src/skills/pragmatic-review/SKILL.md`

Load source-of-truth core files:
- `../../../../../src/skills/pragmatic-review/prompts/core/00-identity.md`
- `../../../../../src/skills/pragmatic-review/prompts/core/01-scope-model.md`
- `../../../../../src/skills/pragmatic-review/prompts/core/02-prioritization.md`
- `../../../../../src/skills/pragmatic-review/prompts/core/03-output-contract.md`
- `../../../../../src/skills/pragmatic-review/prompts/routing/review-router.md`
- `../../../../../src/skills/pragmatic-review/prompts/anti-patterns/catalog.md`

Default base modules:
- `../../../../../src/skills/pragmatic-review/prompts/modules/maintainability.md`
- `../../../../../src/skills/pragmatic-review/prompts/modules/duplication-abstraction.md`
- `../../../../../src/skills/pragmatic-review/prompts/modules/cognitive-complexity.md`

Conditionally load additional modules when the router finds matching evidence:
- `../../../../../src/skills/pragmatic-review/prompts/modules/coupling-side-effects.md`
- `../../../../../src/skills/pragmatic-review/prompts/modules/errors-observability.md`
- `../../../../../src/skills/pragmatic-review/prompts/modules/obvious-performance.md`
- `../../../../../src/skills/pragmatic-review/prompts/modules/architecture-drift.md`

Load specializations only when the selected lenses warrant them:
- `../../../../../src/skills/pragmatic-review/prompts/specializations/frontend.md`
- `../../../../../src/skills/pragmatic-review/prompts/specializations/backend.md`
- `../../../../../src/skills/pragmatic-review/prompts/specializations/reliability.md`
- `../../../../../src/skills/pragmatic-review/prompts/specializations/architecture.md`
- `../../../../../src/skills/pragmatic-review/prompts/specializations/performance.md`

Resolve scope and lens from natural language:
- default scope is current working-tree uncommitted changes
- staged-only scope requires explicit user intent
- frontend, backend, reliability, and architecture are optional review focus directions

Output in Chinese by default.

