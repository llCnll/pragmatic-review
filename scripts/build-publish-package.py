from __future__ import annotations

from pathlib import Path
import json
import shutil


ROOT = Path(__file__).resolve().parent.parent
SOURCE_SKILL_ROOT = ROOT / "src" / "skills" / "pragmatic-review"
SOURCE_SKILL = SOURCE_SKILL_ROOT / "SKILL.md"
SOURCE_AGENTS = SOURCE_SKILL_ROOT / "agents"
SOURCE_PROMPTS = SOURCE_SKILL_ROOT / "prompts"
ROOT_PACKAGE = ROOT / "package.json"
PUBLISH_ROOT = ROOT / "publish" / "pragmatic-review"
STAGING_ROOT = ROOT / "publish" / ".pragmatic-review.tmp"
BACKUP_ROOT = ROOT / "publish" / ".pragmatic-review.previous"


def reset_staging_root() -> None:
    if STAGING_ROOT.exists():
        shutil.rmtree(STAGING_ROOT)
    STAGING_ROOT.mkdir(parents=True, exist_ok=True)


def write_publish_skill(target: Path) -> None:
    shutil.copy2(SOURCE_SKILL, target / "SKILL.md")


def write_publish_package_json(target: Path) -> None:
    root_package = json.loads(ROOT_PACKAGE.read_text(encoding="utf-8"))
    skill_package = root_package["skillPackage"]
    content = {
        "name": skill_package["name"],
        "version": root_package["version"],
        "description": skill_package["description"],
        "license": skill_package["license"],
    }
    (target / "package.json").write_text(
        json.dumps(content, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )


def copy_prompts(target: Path) -> None:
    shutil.copytree(SOURCE_PROMPTS, target / "prompts")


def copy_agents(target: Path) -> None:
    if SOURCE_AGENTS.exists():
        shutil.copytree(SOURCE_AGENTS, target / "agents")


def build_into(target: Path) -> None:
    write_publish_skill(target)
    write_publish_package_json(target)
    copy_agents(target)
    copy_prompts(target)


def replace_publish_root() -> None:
    if BACKUP_ROOT.exists():
        shutil.rmtree(BACKUP_ROOT)

    if PUBLISH_ROOT.exists():
        PUBLISH_ROOT.rename(BACKUP_ROOT)

    try:
        STAGING_ROOT.rename(PUBLISH_ROOT)
    except Exception:
        if PUBLISH_ROOT.exists():
            shutil.rmtree(PUBLISH_ROOT)
        if BACKUP_ROOT.exists():
            BACKUP_ROOT.rename(PUBLISH_ROOT)
        raise

    if BACKUP_ROOT.exists():
        shutil.rmtree(BACKUP_ROOT)


def main() -> int:
    reset_staging_root()
    try:
        build_into(STAGING_ROOT)
        replace_publish_root()
    finally:
        if STAGING_ROOT.exists():
            shutil.rmtree(STAGING_ROOT)
    print(f"Publish package prepared at: {PUBLISH_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
