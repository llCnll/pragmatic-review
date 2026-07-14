from __future__ import annotations

import json
from pathlib import Path
import re


CHECKS = [
    {
        "name": "lens-frontend",
        "files": [
            "adapters/codex/lens-frontend.md",
        ],
        "required": ["frontend"],
    },
    {
        "name": "lens-backend",
        "files": [
            "adapters/codex/lens-backend.md",
        ],
        "required": ["backend"],
    },
    {
        "name": "lens-reliability",
        "files": [
            "adapters/codex/lens-reliability.md",
        ],
        "required": ["reliability"],
    },
    {
        "name": "lens-architecture",
        "files": [
            "adapters/codex/lens-architecture.md",
        ],
        "required": ["architecture"],
    },
    {
        "name": "scope-uncommitted",
        "files": [
            "adapters/codex/scope-uncommitted.md",
        ],
        "required": ["current working-tree uncommitted changes"],
    },
    {
        "name": "scope-staged",
        "files": [
            "adapters/codex/scope-staged.md",
        ],
        "required": ["git diff --cached"],
    },
]

EXPECTED_SCOPES = ["scope-uncommitted", "scope-staged"]
EXPECTED_LENSES = ["lens-frontend", "lens-backend", "lens-reliability", "lens-architecture"]
EXPECTED_WRAPPERS = EXPECTED_SCOPES + EXPECTED_LENSES

EXPECTED_FILE_SETS = {
    "Claude command": ["adapters/claude/.claude/commands/pragmatic-review.md"],
    "Claude skill": ["adapters/claude/.claude/skills/pragmatic-review/SKILL.md"],
    "OpenCode skill": ["adapters/opencode/.opencode/skills/pragmatic-review/SKILL.md"],
    "Roo mode": ["adapters/roo/.roomodes"],
    "Codex reference": [f"adapters/codex/{name}.md" for name in EXPECTED_WRAPPERS],
    "Cursor lens rule": [
        "adapters/cursor/.cursor/rules/10-lens-frontend.mdc",
        "adapters/cursor/.cursor/rules/11-lens-backend.mdc",
        "adapters/cursor/.cursor/rules/12-lens-architecture.mdc",
        "adapters/cursor/.cursor/rules/13-lens-reliability.mdc",
    ],
    "Example workflow": [f"examples/workflows/{name}.md" for name in EXPECTED_WRAPPERS],
}

ADAPTER_SINGLE_ENTRY_GLOBS = [
    "adapters/claude/.claude/commands/*.md",
    "adapters/claude/.claude/skills/*/SKILL.md",
    "adapters/opencode/.opencode/skills/*/SKILL.md",
]

BASE_MODULES = [
    "src/skills/pragmatic-review/prompts/modules/maintainability.md",
    "src/skills/pragmatic-review/prompts/modules/duplication-abstraction.md",
    "src/skills/pragmatic-review/prompts/modules/cognitive-complexity.md",
]

CONDITIONAL_MODULES = [
    "src/skills/pragmatic-review/prompts/modules/coupling-side-effects.md",
    "src/skills/pragmatic-review/prompts/modules/errors-observability.md",
    "src/skills/pragmatic-review/prompts/modules/obvious-performance.md",
    "src/skills/pragmatic-review/prompts/modules/architecture-drift.md",
]

SOURCE_SKILL = Path("src/skills/pragmatic-review/SKILL.md")
SOURCE_AGENT_METADATA = Path("src/skills/pragmatic-review/agents/openai.yaml")
PUBLISH_SKILL = Path("publish/pragmatic-review/SKILL.md")
PUBLISH_AGENT_METADATA = Path("publish/pragmatic-review/agents/openai.yaml")
ROOT_PACKAGE = Path("package.json")
PUBLISH_PACKAGE = Path("publish/pragmatic-review/package.json")
PATH_TOKEN_RE = re.compile(r"`([^`]+)`|@([^\s]+)")


def looks_like_path(token: str) -> bool:
    if token.startswith(("http:", "https:", "C:", "~", "$", "#")):
        return False
    if token.startswith("git "):
        return False
    if token.endswith("/") or "*" in token or " " in token:
        return False
    return "/" in token or token.startswith(".")


def iter_reference_files(root: Path) -> list[Path]:
    search_roots = ["src", "adapters", "publish", "docs", "examples"]
    files: list[Path] = []
    for rel_root in search_roots:
        base = root / rel_root
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and (path.suffix.lower() in {".md", ".mdc", ".json"} or path.name == ".roomodes"):
                files.append(path)
    root_readme = root / "README.md"
    if root_readme.exists():
        files.append(root_readme)
    return files


def validate_path_references(root: Path, errors: list[str]) -> None:
    for path in iter_reference_files(root):
        content = path.read_text(encoding="utf-8", errors="ignore")
        rel_path = path.relative_to(root).as_posix()
        if re.search(r"\b[A-Za-z]:\\Users\\", content):
            errors.append(f"Local absolute user path leaked into {rel_path}")
        for line_number, line in enumerate(content.splitlines(), 1):
            for match in PATH_TOKEN_RE.finditer(line):
                token = match.group(1) or match.group(2)
                if not token or not looks_like_path(token):
                    continue

                local_candidate = (path.parent / token).resolve()
                root_candidate = (root / token).resolve()
                if local_candidate.exists() or root_candidate.exists():
                    continue

                errors.append(f"Missing referenced path in {rel_path}:{line_number}: {token}")


def validate_core_modules(root: Path, errors: list[str]) -> None:
    source_content = (root / SOURCE_SKILL).read_text(encoding="utf-8")
    cursor_core = root / "adapters/cursor/.cursor/rules/01-pragmatic-review-core.mdc"
    cursor_content = cursor_core.read_text(encoding="utf-8")

    for module in BASE_MODULES + CONDITIONAL_MODULES:
        source_ref = module.replace("src/skills/pragmatic-review/", "")
        if source_ref not in source_content:
            errors.append(f"Source skill does not load core module: {module}")

    for module in BASE_MODULES:
        cursor_ref = "@../../../../" + module
        if cursor_ref not in cursor_content:
            errors.append(f"Cursor core rule does not load base module: {module}")

    for module in CONDITIONAL_MODULES:
        cursor_ref = "@../../../../" + module
        if cursor_ref in cursor_content:
            errors.append(f"Cursor core rule should not eagerly load conditional module: {module}")


def validate_publish_output(root: Path, errors: list[str]) -> None:
    source = (root / SOURCE_SKILL).read_text(encoding="utf-8")
    publish_path = root / PUBLISH_SKILL
    if not publish_path.exists():
        errors.append(f"Missing publish skill: {PUBLISH_SKILL.as_posix()}")
        return

    actual_publish = publish_path.read_text(encoding="utf-8")
    if source != actual_publish:
        errors.append("publish/pragmatic-review/SKILL.md is stale relative to src/skills/pragmatic-review/SKILL.md")

    root_package = json.loads((root / ROOT_PACKAGE).read_text(encoding="utf-8"))
    publish_package = json.loads((root / PUBLISH_PACKAGE).read_text(encoding="utf-8"))
    skill_package = root_package["skillPackage"]
    expected_package = {
        "name": skill_package["name"],
        "version": root_package["version"],
        "description": skill_package["description"],
        "license": skill_package["license"],
    }
    if publish_package != expected_package:
        errors.append("publish/pragmatic-review/package.json is stale relative to root package.json")

    publish_readme = root / "publish/pragmatic-review/README.md"
    if publish_readme.exists():
        errors.append("publish/pragmatic-review/README.md should not be included in the runtime skill package")

    source_metadata = root / SOURCE_AGENT_METADATA
    publish_metadata = root / PUBLISH_AGENT_METADATA
    if not source_metadata.exists():
        errors.append(f"Missing source agent metadata: {SOURCE_AGENT_METADATA.as_posix()}")
    elif not publish_metadata.exists():
        errors.append(f"Missing publish agent metadata: {PUBLISH_AGENT_METADATA.as_posix()}")
    else:
        source_agent = source_metadata.read_text(encoding="utf-8")
        publish_agent = publish_metadata.read_text(encoding="utf-8")
        if source_agent != publish_agent:
            errors.append("publish/pragmatic-review/agents/openai.yaml is stale relative to source metadata")
        if "$pragmatic-review" not in source_agent:
            errors.append("agents/openai.yaml default_prompt should explicitly mention $pragmatic-review")


def validate_expected_file_sets(root: Path, errors: list[str]) -> None:
    for label, rel_paths in EXPECTED_FILE_SETS.items():
        for rel_path in rel_paths:
            if not (root / rel_path).exists():
                errors.append(f"Missing {label}: {rel_path}")


def validate_opencode_agents(root: Path, errors: list[str]) -> None:
    opencode_path = root / "adapters/opencode/opencode.json"
    if not opencode_path.exists():
        errors.append("Missing OpenCode config: adapters/opencode/opencode.json")
        return

    content = json.loads(opencode_path.read_text(encoding="utf-8"))
    agents = content.get("agent", {})
    if set(agents) != {"pragmatic-review"}:
        errors.append(f"OpenCode should expose only pragmatic-review agent, found: {sorted(agents)}")


def validate_public_skill_semantics(root: Path, errors: list[str]) -> None:
    public_files = [
        root / "README.md",
        root / "docs/framework-overview.md",
        root / "docs/platform-matrix.md",
        root / SOURCE_SKILL,
        root / PUBLISH_SKILL,
    ]
    banned_patterns = [
        "scope-* entrypoint",
        "lens-* entrypoint",
        "scope-* and lens-* entrypoints",
        "public entrypoint",
        "public entry point",
        "公开入口",
        "全局入口",
    ]
    banned_install_patterns = [
        "npm install -g",
        "postinstall",
        "$codex_home/skills",
        "~/.codex/skills",
        "install-codex-skill",
    ]
    for path in public_files:
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8").lower()
        rel_path = path.relative_to(root).as_posix()
        for pattern in banned_patterns:
            if pattern in content:
                errors.append(f"Misleading public skill semantics in {rel_path}: {pattern}")
        for pattern in banned_install_patterns:
            if pattern in content:
                errors.append(f"Outdated install semantics in {rel_path}: {pattern}")


def validate_publish_install_semantics(root: Path, errors: list[str]) -> None:
    publish_package = json.loads((root / PUBLISH_PACKAGE).read_text(encoding="utf-8"))
    if "scripts" in publish_package:
        errors.append("publish/pragmatic-review/package.json should not define npm lifecycle scripts for clawhub install")

    publish_root = root / "publish/pragmatic-review"
    forbidden_paths = [
        publish_root / "scripts/install-codex-skill.mjs",
    ]
    for path in forbidden_paths:
        if path.exists():
            errors.append(f"Outdated npm install helper should not be published: {path.relative_to(root).as_posix()}")

    reference_files = [
        root / "README.md",
        root / "adapters/codex/USAGE.md",
    ]
    required = "npx clawhub install pragmatic-review"
    for path in reference_files:
        if path.exists() and required not in path.read_text(encoding="utf-8"):
            errors.append(f"Missing clawhub install command in {path.relative_to(root).as_posix()}")


def validate_natural_language_cheatsheet(root: Path, errors: list[str]) -> None:
    path = root / "examples/workflows/natural-language-cheatsheet.md"
    if not path.exists():
        errors.append("Missing natural language cheatsheet")
        return

    content = path.read_text(encoding="utf-8")
    stale_phrases = [
        "只有 core",
        "范围和方向都不明确",
        "几乎没有路由信息",
    ]
    for phrase in stale_phrases:
        if phrase in content:
            errors.append(f"Natural language cheatsheet contains stale scope wording: {phrase}")

    weak_examples = [
        "`review 一下代码`",
        "`帮我看看有没有问题`",
    ]
    for example in weak_examples:
        example_index = content.find(example)
        if example_index == -1:
            errors.append(f"Missing weak natural language example: {example}")
            continue
        next_example_index = content.find("- `", example_index + len(example))
        section = content[example_index: next_example_index if next_example_index != -1 else len(content)]
        if "默认 `scope-uncommitted`" not in section:
            errors.append(f"Weak natural language example should still default to scope-uncommitted: {example}")


def validate_single_entry_adapters(root: Path, errors: list[str]) -> None:
    for pattern in ADAPTER_SINGLE_ENTRY_GLOBS:
        files = sorted(path.relative_to(root).as_posix() for path in root.glob(pattern))
        expected_suffix = "pragmatic-review.md" if "commands" in pattern else "pragmatic-review/SKILL.md"
        if not files:
            errors.append(f"No files found for adapter surface: {pattern}")
            continue
        unexpected = [path for path in files if not path.endswith(expected_suffix)]
        if unexpected:
            errors.append(f"Adapter exposes non-public scope/lens entries: {unexpected}")

    roo_path = root / "adapters/roo/.roomodes"
    if roo_path.exists():
        content = roo_path.read_text(encoding="utf-8")
        slugs = re.findall(r"^\s*-\s+slug:\s+([^\s]+)", content, flags=re.MULTILINE)
        if slugs != ["pragmatic-review"]:
            errors.append(f"Roo should expose only pragmatic-review mode, found: {slugs}")

    adapter_files = [
        *[path for pattern in ADAPTER_SINGLE_ENTRY_GLOBS for path in root.glob(pattern)],
        root / "adapters/opencode/opencode.json",
        root / "adapters/roo/.roomodes",
    ]
    misleading_terms = ["范围入口", "方向入口", "全局入口", "公开入口", "entrypoint", "entry point"]
    for path in adapter_files:
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8", errors="ignore").lower()
        rel_path = path.relative_to(root).as_posix()
        for term in misleading_terms:
            if term.lower() in content:
                errors.append(f"Misleading adapter entry wording in {rel_path}: {term}")


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors: list[str] = []

    for check in CHECKS:
        for rel_path in check["files"]:
            path = root / rel_path
            if not path.exists():
                errors.append(f"Missing file for {check['name']}: {rel_path}")
                continue

            content = path.read_text(encoding="utf-8")
            for token in check["required"]:
                if token not in content:
                    errors.append(f"Missing token '{token}' in {rel_path}")

    validate_path_references(root, errors)
    validate_core_modules(root, errors)
    validate_publish_output(root, errors)
    validate_expected_file_sets(root, errors)
    validate_opencode_agents(root, errors)
    validate_public_skill_semantics(root, errors)
    validate_single_entry_adapters(root, errors)
    validate_publish_install_semantics(root, errors)
    validate_natural_language_cheatsheet(root, errors)

    if errors:
        for error in errors:
            print(error)
        return 1

    print("Preset parity validation: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
