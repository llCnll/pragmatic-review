---
name: pragmatic-review
description: Pragmatic, maintainability-first code review for selected changes. Use when reviewing code diffs; scope and review focus follow the user's request.
---

# pragmatic-review

Review selected code changes with high signal and a pragmatic senior-engineer perspective.

## Read model

For each review, load:
- prompts/core/ for identity, scope, prioritization, and output
- prompts/routing/review-router.md
- prompts/anti-patterns/catalog.md

Start with:
- prompts/modules/maintainability.md
- prompts/modules/duplication-abstraction.md
- prompts/modules/cognitive-complexity.md

Load other modules when the router finds matching evidence:
- prompts/modules/coupling-side-effects.md
- prompts/modules/errors-observability.md
- prompts/modules/obvious-performance.md
- prompts/modules/architecture-drift.md
- prompts/modules/behavior-validation.md

Apply a domain specialization only when the requested lens or changed code makes it useful. Scope and review focus are chosen from the user's request; they are not separate public skills.

Scope selects the changes under review; a focus changes what to prioritize. A focus never widens scope or lowers the evidence threshold.

Modules cover recurring problem types; specializations add domain context. Select each independently from the diff and the requested focus.
