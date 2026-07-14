# Directory Structure

```text
.
├── README.md
├── package.json
├── docs/
├── examples/
├── src/
│   ├── skills/
│   │   └── pragmatic-review/
│   │       ├── SKILL.md
│   │       ├── agents/
│   │       └── prompts/
│   ├── profiles/
│   └── model/
├── adapters/
├── scripts/
└── publish/
```

Key directories:
- `src/skills/pragmatic-review/`: self-contained source skill
- `src/skills/pragmatic-review/agents/openai.yaml`: UI/product metadata, not review behavior source
- `src/skills/pragmatic-review/prompts/core/`: stable worldview, scope model, prioritization, output contract
- `src/skills/pragmatic-review/prompts/routing/`: context-aware module selection
- `src/skills/pragmatic-review/prompts/modules/`: focused review lenses by problem type
- `src/skills/pragmatic-review/prompts/specializations/`: reusable domain overlays
- `src/profiles/`: canonical profile registry
- `src/model/`: internal scope and lens definitions
- `adapters/`: platform-specific wrappers and reference surfaces
- `scripts/`: validation and publish-build helpers
- `publish/pragmatic-review/`: generated clawhub/skillhub-ready skill package

Important:
- The runtime skill source is `src/skills/pragmatic-review/`, not a loose shared prompt folder.
- The generated installable package is `publish/pragmatic-review/`.
- Installation transport such as `npx clawhub install ...` is documented separately and is not runtime skill logic.

