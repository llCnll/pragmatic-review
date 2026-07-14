# Extensibility Strategy

## Design rule

Extend by composition, not by prompt accretion.

## Stable extension points

1. Add a module when a new recurring risk pattern appears.
2. Add a specialization when one domain consistently needs extra context.
3. Add a scope label when a new scope shape is needed.
4. Add a lens label when a new review focus is needed.
5. Add a platform adapter only after the core behavior is stable.

## New module contract

A new module should define:
- what it looks for
- what it prioritizes
- what it explicitly avoids
- what evidence threshold is required

If a new concern cannot meet those four points, it should not become a module yet.

## New internal label contract

A new scope label should define:
- the evidence boundary
- the default stop condition
- whether untracked files are in scope

A new lens label should define:
- the added focus areas
- the main bias it introduces
- the main classes of low-value feedback it suppresses

If an internal label cannot explain those items clearly, it is probably mixing concerns.

## New platform adapter contract

A new adapter should define:
- how it invokes `pragmatic-review`
- how it maps scope intent to platform-local wrappers or prompts
- how it maps lens intent to platform-local wrappers or prompts
- how it mirrors the canonical policy in `src/profiles/review-profiles.yaml`
- what commands or files it needs for diff access

Keep adapters thin. If an adapter needs custom review philosophy, the framework is leaking.

When duplicated wrappers exist across adapters, add or update a lightweight validation check so they do not silently drift apart.
Prefer a cross-platform validator such as Python for distributable tooling.

## Support for additional agents

The following tools can usually consume the same core assets with light wrapping:
- Aider
- Continue
- Cline
- Windsurf
- Gemini CLI
- generic MCP-compatible agents

Recommended approach:
- reuse `src/skills/pragmatic-review/` when the tool understands markdown skills
- keep scope and lens as composition concepts from `src/model/`
- otherwise wrap `pragmatic-review` plus the needed scope and lens guidance in the tool's prompt format

