Use the core review capability defined in `src/skills/pragmatic-review/SKILL.md`.

This file is an adapter-local scope reference.

Set scope to:
- staged changes only

Evidence boundary:
- inspect only `git diff --cached`
- do not silently include unstaged changes

If nothing is staged, say so clearly and stop.

