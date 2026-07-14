# Review Router

## Step 1: Resolve scope

Supported scope classes:
- working-tree uncommitted changes
- staged changes
- other explicitly requested ranges

Default to working-tree uncommitted changes.

If using the default scope, inspect:
- staged changes with `git diff --cached`
- unstaged tracked changes with `git diff`
- untracked files when they are relevant to the current work

If there is nothing relevant in the selected scope:
- report that clearly
- do not silently widen scope

## Step 2: Detect change shape

Use the selected scope to classify the change:
- hotfix
- refactor
- feature extension
- new layer or architecture movement
- cleanup

## Step 3: Detect domain

Infer domain from changed files and code shape:
- frontend
- backend
- mixed

## Step 4: Activate base modules

Always start from:
- maintainability
- cognitive-complexity
- duplication-abstraction

Then add:
- coupling-side-effects for coordination logic
- errors-observability for failure paths
- obvious-performance only for visible waste
- architecture-drift for boundary movement

## Step 5: Activate specializations

Use:
- frontend overlay for component, state, and effect changes
- backend overlay for service, API, persistence, and workflow changes
- reliability overlay for retries, ordering, async work, or hotfixes
- architecture overlay for new layers, cross-module movement, or foundational helpers

## Step 6: Apply anti-noise filter

Suppress:
- style comments
- speculative cleanup
- abstract "consider refactoring" advice
- findings below the configured signal threshold
