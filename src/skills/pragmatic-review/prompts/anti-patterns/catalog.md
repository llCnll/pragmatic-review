# Anti-pattern Suppression

Suppress feedback when it falls into these buckets:

## Low-signal feedback

Do not comment on:
- formatting
- naming preferences with no maintenance payoff
- tiny cleanup ideas with no future-cost reduction

## Fake abstraction

Do not recommend abstraction when:
- there are only a few simple call sites
- the abstraction hides business intent
- the abstraction increases navigation cost
- the abstraction creates a generic helper with weak ownership

## Architecture as religion

Do not recommend:
- new layers just because layering sounds cleaner
- interface extraction without a concrete need
- "clean architecture" moves that make debugging harder

## Speculative refactor

Do not recommend a refactor unless you can name:
- the current cost
- the likely future pain
- why the suggested change reduces it

## Premature generalization

Do not generalize for hypothetical future use when the current change does not justify it.

## Micro-optimization

Do not report:
- trivial allocations
- tiny loops
- style-level performance folklore

Only report performance when the waste is obvious and practical.

