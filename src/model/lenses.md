# Lens Model

Lenses bias the review without changing the underlying review philosophy.

## `lens-frontend`

Focus on:
- duplicated state
- effect complexity
- lifecycle coupling
- rerender cascades
- source-of-truth clarity

Suppress:
- CSS nitpicks
- speculative component extraction

## `lens-backend`

Focus on:
- side-effect ordering
- partial failure paths
- transaction boundary clarity
- workflow ownership
- hidden write ordering assumptions

## `lens-reliability`

Focus on:
- retry safety
- idempotency
- rollback safety
- timeout handling
- observability

Require:
- a concrete failure mode

## `lens-architecture`

Focus on:
- boundary drift
- ownership confusion
- helper explosion
- fake abstraction
- dependency direction

## Lens rules

- Lenses add focus. They do not replace the core maintainability-first worldview.
- Use zero or more lenses on top of the core capability.
- Prefer no lens over activating an irrelevant one.
