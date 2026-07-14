# Minimal Verification Matrix

High-risk review capabilities need explicit minimum verification rules. The reviewer should not speculate past the evidence in the selected scope.

## Default uncommitted review

Minimum verification:
- confirm scope with `git status --short`
- inspect staged changes with `git diff --cached`
- inspect unstaged tracked changes with `git diff`
- if relevant untracked files are part of the current work, read them directly
- if there are no relevant uncommitted changes, do not infer findings from repo history

## Architecture review

Minimum verification:
- identify the changed boundary directly in the current changes
- compare dependency direction against existing module ownership or documented boundaries
- only call "architecture drift" when the change introduces or reinforces cross-boundary coupling

## Reliability review

Minimum verification:
- point to a concrete failure path in the changed code
- name the missing guardrail: idempotency, retry safety, rollback safety, timeout handling, or ordering
- do not claim reliability risk without a specific failure mode

## Performance review

Minimum verification:
- only report obvious hotspots visible in code shape
- point to repeated work, repeated rendering, repeated transformation, or poor algorithmic structure
- do not report micro-optimization opportunities

## Frontend state/effects review

Minimum verification:
- identify the duplicated source of truth, effect dependency risk, or render cascade directly in the changed component flow
- do not report "rerender risk" without naming the state or prop path that causes it

## Backend side-effect review

Minimum verification:
- identify the ordering of writes, publishes, cache updates, or external calls
- only flag hidden coupling when behavior depends on that ordering or on implicit shared state

