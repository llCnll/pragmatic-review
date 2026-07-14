Support three scope classes only:
1. working-tree uncommitted changes
2. staged changes
3. other explicitly requested ranges

Default to working-tree uncommitted changes unless the user explicitly specifies another scope.

Scope resolution:
1. user-explicit target
2. working-tree uncommitted changes
3. stop if there is nothing relevant to review

Working-tree uncommitted changes include:
- staged changes via `git diff --cached`
- unstaged tracked changes via `git diff`
- untracked files when they are part of the current work and can be read directly

Staged changes mean staged-only:
- use `git diff --cached`
- do not silently add unstaged changes

Do not silently expand from the chosen scope to:
- the current file
- the full branch
- the full repository
