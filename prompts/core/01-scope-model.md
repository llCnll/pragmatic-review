# Assessment Scope

Supported scopes:

1. Working-tree changes: staged, unstaged, and relevant untracked code.
2. Staged changes, inspected with git diff --cached.
3. A revision range explicitly named by the user.
4. Explicit files, directories, or another identified code set.

Use the requested scope, with working-tree changes as the default. A quality focus sets priorities within that code set.

For a diff, separate changed behavior and newly introduced issues from relevant existing context. For a whole-file or directory audit, report that coverage and its baseline. If the resolved set is empty, report the observation and finish.
