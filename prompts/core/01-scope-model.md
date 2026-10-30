Supported scopes:
1. Working-tree changes
2. Staged changes only
3. Another range explicitly named by the user

Resolve scope in this order: explicit request, then working-tree changes. The working tree includes staged and unstaged tracked changes plus relevant untracked files. Staged-only review uses git diff --cached.

If the selected scope has nothing relevant, report that and stop. Keep review within the selected scope; do not widen it to the current file, branch, or repository.
