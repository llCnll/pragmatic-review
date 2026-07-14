# Review Framework Spec

## Goals

Build a cross-platform review system that behaves like a pragmatic senior engineer:
- maintainability-first
- anti-overengineering
- high signal-to-noise
- low verbosity
- stable under repeated use
- extensible without growing into a giant prompt

## Non-goals

Do not optimize for:
- exhaustive checklists
- subjective style opinions
- abstraction for its own sake
- theoretical purity
- micro-optimization
- one universal prompt that tries to review everything at once

## Core design

Use a layered runtime instead of a monolith.

1. Core worldview
2. Scope resolution
3. Context-aware routing
4. Small review modules
5. Domain specializations
6. Output contract

This keeps the stable parts stable and the fast-changing parts isolated.

## Model

Use one public skill plus two orthogonal internal composition axes.

Core:
- `pragmatic-review`

Internal scope labels:
- `scope-uncommitted`
- `scope-staged`
- future examples: `scope-pr`, `scope-branch`, `scope-file`

Internal lens labels:
- `lens-frontend`
- `lens-backend`
- `lens-reliability`
- `lens-architecture`

Execution model:
- core + one scope + zero or more lenses

Public product model:
- `pragmatic-review` is the only public skill users need to name
- scope and lens should normally be selected through natural language
- platform adapters may mirror internal labels only as implementation details, not as separate public products

Examples:
- `pragmatic-review + scope-uncommitted`
- `pragmatic-review + scope-staged + lens-reliability`
- `pragmatic-review + scope-uncommitted + lens-frontend`

## Scope model

Support three scope classes:

1. Working-tree uncommitted changes
2. Staged changes
3. Other explicitly requested ranges

Default scope:
- working-tree uncommitted changes

### Scope definitions

Working-tree uncommitted changes:
- the default pre-commit review scope
- includes staged changes via `git diff --cached`
- includes unstaged tracked changes via `git diff`
- may include relevant untracked files when they are part of the current work and can be read directly

Staged changes:
- only the index
- use when the user explicitly asks for staged-only review
- inspect with `git diff --cached`

Other explicitly requested ranges:
- current file
- specific files
- branch diff
- PR diff
- repo-wide review

Scope precedence:
1. user-explicit scope
2. working-tree uncommitted default
3. never silently widen beyond that default

## Review worldview

The reviewer should optimize for:
- lower cognitive complexity
- lower future bug risk
- lower future diff complexity
- easier debugging
- easier future extension

The reviewer should avoid:
- low-value cleanup comments
- style-only comments
- speculative refactors
- fake abstractions
- generic helper explosion

## Module taxonomy

Split modules by problem type, not by technology.

Primary modules:
- maintainability
- duplication and abstraction
- cognitive complexity
- coupling and side effects
- errors and observability
- obvious performance only
- architecture drift

Why this split:
- problem-type modules age better than stack-specific checklists
- the same lens works across frontend, backend, CLI, services, and scripts
- lenses can be composed on top instead of forked

## Routing model

Routing selects which modules to activate.

Inputs:
- review scope
- changed files
- change shape
- risk signals
- explicit user intent
- active lenses

Routing dimensions:
- domain: frontend, backend, mixed
- change shape: hotfix, refactor, feature, new layer, cleanup
- risk: state sync, transaction ordering, retries, side effects, architecture movement

Output:
- active modules
- active specializations
- output depth

## Output contract

Only emit findings that are both actionable and worth fixing.

Each finding should include:
1. severity
2. category
3. location
4. problem
5. why it matters
6. suggested improvement
7. tradeoff
8. estimated value: high / medium / low
9. estimated impact

Allowed empty result:
- "No high-signal findings in the selected scope."

## Profile registry

`src/profiles/review-profiles.yaml` is the canonical profile registry and policy spec for this repository.

Important:
- it is not automatically parsed by every platform adapter at runtime
- adapters may inline or mirror the same policy in their native prompt format
- if the registry changes, corresponding adapters or skills should be updated to preserve consistency

The registry should express:
- scope labels
- lens labels
- recommended compositions
- output caps

## Extensibility contract

Add new behavior by extending one layer only.

Examples:
- new risk lens: add one module
- new platform: add one adapter
- new scope label: add one scope model entry and adapter support if needed
- new lens label: add one lens model entry and adapter support if needed

Do not:
- duplicate core philosophy into every adapter
- mix scope semantics with lens semantics in one preset name
- let platform files become the source of truth

The source of truth stays in:
- `src/skills/pragmatic-review/prompts/` for shared runtime behavior
- `src/profiles/review-profiles.yaml` for canonical profile policy
- `src/model/` for internal scope and lens semantics

