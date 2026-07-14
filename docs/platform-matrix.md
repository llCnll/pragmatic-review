# Platform Matrix

## Current adapter targets

- Cursor: `.cursor/rules/*.mdc`
- Claude Code: `.claude/commands/*.md` and `.claude/skills/*/SKILL.md`
- RooCode: `adapters/roo/.roomodes`
- OpenCode: `opencode.json` and `.opencode/skills/*/SKILL.md`
- Codex CLI / Codex app: clawhub/skillhub package plus adapter-local reference prompt files
- ChatGPT / GPT: reusable system prompt files

## Notes

- Cursor rules support metadata such as `description`, `globs`, and `alwaysApply`.
- Claude Code supports project slash commands under `.claude/commands/`; keep command files as thin orchestration wrappers over the same framework.
- Keep the RooCode adapter thin and treat it as compatibility output rather than the long-term source of truth.
- OpenCode supports both agents in `opencode.json` and tool-compatible skills in `.opencode/skills/`.

## Strategy

Treat platform files as adapters over the same core framework:
- `src/skills/pragmatic-review/prompts/core/`
- `src/skills/pragmatic-review/prompts/routing/`
- `src/skills/pragmatic-review/prompts/modules/`
- `src/skills/pragmatic-review/prompts/specializations/`
- `src/profiles/review-profiles.yaml`

Important:
- `pragmatic-review` is the only public clawhub/skillhub skill product
- `scope-*` files or adapter-local skills represent scope wrappers or reference files, not public skill products
- `lens-*` files or adapter-local skills represent review-bias wrappers or reference files, not public skill products
- `src/profiles/review-profiles.yaml` is the canonical registry for scope, lens, and composition policy
- adapters are not required to parse the registry directly at runtime

