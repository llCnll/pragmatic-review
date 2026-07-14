# Scope Model

This repository treats scope as a first-class routing concept, not as a public skill name.

## Supported scope classes

1. `scope-uncommitted`
- meaning: current working-tree uncommitted changes
- inspect with:
  - `git status --short`
  - `git diff --cached`
  - `git diff`
- include relevant untracked files when they are part of the current work and can be read directly
- default when the user does not specify another range

2. `scope-staged`
- meaning: staged changes only
- inspect with:
  - `git diff --cached`
- do not widen to unstaged files unless the user explicitly changes scope

3. explicit other range
- examples:
  - current file
  - selected files
  - branch diff
  - PR diff
  - repo-wide review
- must be user-explicit

## Scope rules

- Never widen scope silently beyond the user-selected or default scope.
- If the selected scope has no relevant changes, say so clearly and stop.
- Scope decides what evidence is allowed.
