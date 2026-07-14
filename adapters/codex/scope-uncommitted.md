Use the core review capability defined in `src/skills/pragmatic-review/SKILL.md`.

This file is an adapter-local scope reference.

Set scope to:
- current working-tree uncommitted changes

Evidence boundary:
- inspect staged changes with `git diff --cached`
- inspect unstaged tracked changes with `git diff`
- include relevant untracked files when they can be read directly

If there is nothing relevant in the selected scope, say so clearly and stop.

