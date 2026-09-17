#!/usr/bin/env python3
"""agent-practices init: Intelligent adoption CLI with stack auto-detection and script scraping."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates"
SKILLS_DIR = REPO_ROOT / "skills"
CATALOG_FILE = REPO_ROOT / "catalog.json"


def load_catalog() -> dict[str, object]:
    if CATALOG_FILE.exists():
        try:
            return json.loads(CATALOG_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    templates = [{"name": p.parent.name, "path": p.relative_to(REPO_ROOT).as_posix()}
                 for p in sorted(TEMPLATES_DIR.glob("*/AGENTS.md"))]
    skills = []
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skill_name = skill_file.parent.name
        skills.append({"name": skill_name, "path": skill_file.relative_to(REPO_ROOT).as_posix()})
    return {"templates": templates, "skills": skills}


def get_available_templates() -> list[str]:
    return sorted([p.parent.name for p in TEMPLATES_DIR.glob("*/AGENTS.md") if p.is_file()])


def get_available_skills() -> list[dict[str, str]]:
    catalog = load_catalog()
    raw_skills = catalog.get("skills", [])
    skills_list = []
    for s in raw_skills:
        name = s.get("name", "")
        desc = s.get("description", "")
        if not desc:
            skill_path = SKILLS_DIR / name / "SKILL.md"
            if skill_path.exists():
                for line in skill_path.read_text(encoding="utf-8").splitlines():
                    if line.startswith("description:"):
                        desc = line.partition(":")[2].strip()
                        break
        skills_list.append({"name": name, "description": desc})
    return sorted(skills_list, key=lambda x: x["name"])


def detect_package_manager(target: Path) -> str:
    if (target / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (target / "yarn.lock").exists():
        return "yarn"
    if (target / "bun.lockb").exists() or (target / "bun.lock").exists():
        return "bun"
    return "npm"


def detect_stack(target: Path) -> tuple[str, dict[str, str], list[str]]:
    """Inspects target directory and returns (template_name, replacements, detection_notes)."""
    notes: list[str] = []
    replacements: dict[str, str] = {}
    default_name = target.resolve().name or "my-project"

    # 1. Monorepo detection
    is_monorepo = (
        (target / "pnpm-workspace.yaml").exists()
        or (target / "turbo.json").exists()
        or (target / "lerna.json").exists()
        or (target / "nx.json").exists()
    )
    if not is_monorepo and (target / "package.json").exists():
        try:
            pkg_data = json.loads((target / "package.json").read_text(encoding="utf-8"))
            if "workspaces" in pkg_data:
                is_monorepo = True
        except Exception:
            pass

    if is_monorepo:
        notes.append("Detected workspace/monorepo markers")
        pm = detect_package_manager(target)
        pkg_name = default_name
        pkg_json = target / "package.json"
        if pkg_json.exists():
            try:
                pkg_data = json.loads(pkg_json.read_text(encoding="utf-8"))
                pkg_name = pkg_data.get("name") or default_name
            except Exception:
                pass
        replacements["<project-name>"] = pkg_name
        replacements["<install-command>"] = f"{pm} install"
        if (target / "turbo.json").exists():
            replacements["<affected-check-command>"] = f"{pm} turbo run check"
        elif (target / "nx.json").exists():
            replacements["<affected-check-command>"] = f"{pm} nx affected"
        else:
            replacements["<affected-check-command>"] = f"{pm} test"
        replacements["<full-test-command>"] = f"{pm} test"
        return "monorepo", replacements, notes

    # 2. Android / Kotlin detection
    is_android_kotlin = (
        (target / "build.gradle.kts").exists()
        or (target / "build.gradle").exists()
        or (target / "settings.gradle.kts").exists()
        or (target / "settings.gradle").exists()
        or (target / "app" / "build.gradle").exists()
    )
    if is_android_kotlin:
        notes.append("Detected Gradle/Kotlin project markers")
        app_name = default_name
        for settings_file in [target / "settings.gradle.kts", target / "settings.gradle"]:
            if settings_file.exists():
                try:
                    content = settings_file.read_text(encoding="utf-8")
                    match = re.search(r'rootProject\.name\s*=\s*["\']([^"\']+)["\']', content)
                    if match:
                        app_name = match.group(1)
                        break
                except Exception:
                    pass
        replacements["<app-name>"] = app_name
        return "kotlin-android", replacements, notes

    # 3. Infrastructure detection
    has_tf = list(target.glob("*.tf"))
    is_infra = (
        bool(has_tf)
        or (target / "terragrunt.hcl").exists()
        or (target / "Pulumi.yaml").exists()
        or (target / "cdktf.json").exists()
    )
    if is_infra:
        notes.append("Detected Infrastructure-as-Code markers")
        replacements["<project-name>"] = default_name
        replacements["<format-command>"] = "terraform fmt -check"
        replacements["<validate-command>"] = "terraform validate"
        replacements["<plan-command>"] = "terraform plan"
        replacements["<test-command>"] = "terraform test"
        return "infrastructure", replacements, notes

    # 4. Documentation detection
    is_docs = (
        (target / "mkdocs.yml").exists()
        or (target / "docs" / "conf.py").exists()
        or (target / "docusaurus.config.js").exists()
        or (target / "book.toml").exists()
    )
    if is_docs:
        notes.append("Detected documentation project markers")
        replacements["<project-name>"] = default_name
        if (target / "mkdocs.yml").exists():
            replacements["<preview-command>"] = "mkdocs serve"
            replacements["<link-check-command>"] = "mkdocs build --strict"
        elif (target / "docusaurus.config.js").exists():
            replacements["<preview-command>"] = "npm start"
            replacements["<link-check-command>"] = "npm run build"
        else:
            replacements["<preview-command>"] = "mdbook serve"
            replacements["<link-check-command>"] = "mdbook test"
        replacements["<style-check-command>"] = 'markdownlint "**/*.md"'
        return "documentation", replacements, notes

    # 5. TypeScript / JavaScript detection
    has_tsconfig = (target / "tsconfig.json").exists()
    pkg_json = target / "package.json"
    if has_tsconfig or pkg_json.exists():
        notes.append("Detected Node/JavaScript/TypeScript configuration")
        pm = detect_package_manager(target)
        project_name = default_name
        scripts: dict[str, str] = {}

        if pkg_json.exists():
            try:
                pkg_data = json.loads(pkg_json.read_text(encoding="utf-8"))
                project_name = pkg_data.get("name") or default_name
                scripts = pkg_data.get("scripts", {})
            except Exception:
                pass

        replacements["<project-name>"] = project_name
        replacements["<install-command>"] = f"{pm} install"

        # Typecheck command
        if "typecheck" in scripts:
            replacements["<typecheck-command>"] = f"{pm} run typecheck"
        elif "tsc" in scripts:
            replacements["<typecheck-command>"] = f"{pm} run tsc"
        elif has_tsconfig:
            replacements["<typecheck-command>"] = "npx tsc --noEmit"

        # Lint command
        if "lint" in scripts:
            replacements["<lint-command>"] = f"{pm} run lint"
        elif "check" in scripts:
            replacements["<lint-command>"] = f"{pm} run check"

        # Test command
        if "test" in scripts:
            replacements["<test-command>"] = f"{pm} test"

        # Build command
        if "build" in scripts:
            replacements["<build-command>"] = f"{pm} run build"

        return "typescript", replacements, notes

    # 6. Python detection
    pyproject = target / "pyproject.toml"
    is_python = (
        pyproject.exists()
        or (target / "setup.py").exists()
        or (target / "setup.cfg").exists()
        or (target / "requirements.txt").exists()
        or (target / "Pipfile").exists()
    )
    if is_python:
        notes.append("Detected Python project configuration")
        runner = ""
        if (target / "uv.lock").exists():
            runner = "uv run "
        elif (target / "poetry.lock").exists():
            runner = "poetry run "

        project_name = default_name
        pyproject_content = ""
        if pyproject.exists():
            try:
                pyproject_content = pyproject.read_text(encoding="utf-8")
                match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', pyproject_content)
                if match:
                    project_name = match.group(1)
            except Exception:
                pass

        replacements["<project-name>"] = project_name

        # Formatter / Linter
        if "ruff" in pyproject_content or (target / "ruff.toml").exists() or (target / ".ruff.toml").exists():
            replacements["<format-check-command>"] = f"{runner}ruff check . && {runner}ruff format --check ."
        elif "black" in pyproject_content:
            replacements["<format-check-command>"] = f"{runner}black --check ."
        elif "flake8" in pyproject_content:
            replacements["<format-check-command>"] = f"{runner}flake8 ."

        # Typechecker
        if "mypy" in pyproject_content or (target / "mypy.ini").exists():
            replacements["<typecheck-command>"] = f"{runner}mypy ."
        elif "pyright" in pyproject_content:
            replacements["<typecheck-command>"] = f"{runner}pyright"

        # Test
        if "pytest" in pyproject_content or (target / "pytest.ini").exists() or (target / "tests").is_dir():
            replacements["<test-command>"] = f"{runner}pytest"
        else:
            replacements["<test-command>"] = "python3 -m unittest discover"

        # Generic commands fallback if python template is swapped with generic
        replacements["<install-command>"] = f"{runner.strip()} install" if runner else "pip install -e ."
        replacements["<lint-command>"] = replacements.get("<format-check-command>", "ruff check .")

        return "python", replacements, notes

    # 7. Generic fallback / Makefile detection
    makefile = target / "Makefile"
    if makefile.exists():
        notes.append("Detected Makefile targets")
        try:
            content = makefile.read_text(encoding="utf-8")
            targets = set(re.findall(r"^([a-zA-Z0-9_-]+):", content, flags=re.MULTILINE))
            if "test" in targets:
                replacements["<test-command>"] = "make test"
            if "lint" in targets:
                replacements["<lint-command>"] = "make lint"
            if "build" in targets:
                replacements["<build-command>"] = "make build"
            if "install" in targets:
                replacements["<install-command>"] = "make install"
        except Exception:
            pass

    replacements["<project-name>"] = default_name
    return "generic", replacements, notes


def substitute_content(content: str, replacements: dict[str, str]) -> str:
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    return content


def find_remaining_placeholders(text: str) -> list[str]:
    matches = re.findall(r"<[a-z][a-z0-9-]*>", text)
    return [m for m in matches if not m.startswith("<http")]


def run_wizard(
    detected_template: str,
    available_templates: list[str],
    replacements: dict[str, str],
    all_skills: list[dict[str, str]],
) -> tuple[str, dict[str, str], list[str]]:
    print("Welcome to Agent Practices Setup Wizard")
    print("========================================")
    print(f"Auto-detected template: {detected_template}")

    template_choice = input(f"Use template [{detected_template}] (or enter name / ? to list): ").strip()
    template = detected_template
    if template_choice == "?":
        print("Available templates:", ", ".join(available_templates))
        template_choice = input(f"Choose template [{detected_template}]: ").strip()

    if template_choice and template_choice in available_templates:
        template = template_choice
    elif template_choice and template_choice not in available_templates:
        print(f"Unknown template '{template_choice}', using detected default: {detected_template}")

    print("\nScraped Commands & Metadata:")
    for key, val in list(replacements.items()):
        new_val = input(f"  {key} [{val}]: ").strip()
        if new_val:
            replacements[key] = new_val

    print("\nSelect Skills:")
    print("  [1] All skills (standard complete toolkit)")
    print("  [2] Core essentials (coding-best-practices, testing, code-review, git-workflow, security)")
    print("  [3] Custom selection")
    skill_opt = input("Choose skills option [1]: ").strip()

    selected_skills = [s["name"] for s in all_skills]
    if skill_opt == "2":
        core = {"coding-best-practices", "testing", "code-review", "git-workflow", "security"}
        selected_skills = [s["name"] for s in all_skills if s["name"] in core]
    elif skill_opt == "3":
        print("\nAvailable skills:")
        for idx, s in enumerate(all_skills, 1):
            print(f"  {idx}. {s['name']} - {s['description']}")
        custom_input = input("Enter skill names or numbers (comma-separated): ").strip()
        chosen = set()
        for item in custom_input.split(","):
            item = item.strip()
            if not item:
                continue
            if item.isdigit():
                num = int(item)
                if 1 <= num <= len(all_skills):
                    chosen.add(all_skills[num - 1]["name"])
            elif any(s["name"] == item for s in all_skills):
                chosen.add(item)
        if chosen:
            selected_skills = sorted(list(chosen))

    return template, replacements, selected_skills


def adopt(
    target: Path,
    template: str,
    skills_to_install: list[str],
    replacements: dict[str, str],
    force: bool,
    dry_run: bool,
) -> int:
    template_source = TEMPLATES_DIR / template / "AGENTS.md"
    if not template_source.exists():
        print(f"Error: Unknown template '{template}'", file=sys.stderr)
        return 2

    agents_file = target / "AGENTS.md"
    skills_dir = target / ".agents" / "skills"

    if agents_file.exists() and not force:
        print(
            f"Error: Refusing to overwrite {agents_file}. Re-run with --force after reviewing it.",
            file=sys.stderr,
        )
        return 1

    template_content = template_source.read_text(encoding="utf-8")
    customized_content = substitute_content(template_content, replacements)
    remaining_placeholders = find_remaining_placeholders(customized_content)

    print(f"Template: {template}")
    print(f"Contract: {template_source.relative_to(REPO_ROOT)} -> {agents_file}")
    print(f"Skills: {' '.join(skills_to_install)} -> {skills_dir}")

    if replacements:
        print("Applied substitutions:")
        for k, v in replacements.items():
            if k in template_content:
                print(f"  {k} -> {v}")

    if dry_run:
        print("\nDry run: no files changed.")
        if remaining_placeholders:
            print(f"Placeholders that would remain: {', '.join(remaining_placeholders)}")
        return 0

    target.mkdir(parents=True, exist_ok=True)
    agents_file.write_text(customized_content, encoding="utf-8")

    skills_dir.mkdir(parents=True, exist_ok=True)
    for skill_name in skills_to_install:
        src_skill = SKILLS_DIR / skill_name / "SKILL.md"
        if not src_skill.exists():
            print(f"Error: Unknown skill '{skill_name}'", file=sys.stderr)
            return 2
        dest_skill_dir = skills_dir / skill_name
        dest_skill_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src_skill, dest_skill_dir / "SKILL.md")

    print("Installed Agent Practices.")
    if remaining_placeholders:
        print(f"Note: Unfilled placeholders in AGENTS.md: {', '.join(remaining_placeholders)}")
        print("Fill those before committing your contract.")
    else:
        print("All placeholders successfully configured.")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Single-command adoption CLI with stack auto-detection and script scraping."
    )
    parser.add_argument("--target", default=".", help="Target repository directory (default: current directory)")
    parser.add_argument("--template", help="Template name (overrides auto-detection)")
    parser.add_argument("--skills", default="all", help="Skills to install ('all' or comma-separated list)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    parser.add_argument("--force", action="store_true", help="Overwrite existing AGENTS.md")
    parser.add_argument("-y", "--yes", action="store_true", help="Non-interactive mode: accept all detected defaults")
    parser.add_argument("--list", action="store_true", help="List available templates and skills")

    args = parser.parse_args()

    available_templates = get_available_templates()
    available_skills = get_available_skills()

    if args.list:
        print("Templates:")
        for t in available_templates:
            print(f"  {t}")
        print("Skills:")
        for s in available_skills:
            print(f"  {s['name']}")
        return 0

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target directory does not exist: {target_path}", file=sys.stderr)
        return 1

    detected_template, replacements, notes = detect_stack(target_path)
    template = args.template or detected_template

    if args.skills == "all":
        selected_skills = [s["name"] for s in available_skills]
    else:
        selected_skills = [s.strip() for s in args.skills.split(",") if s.strip()]

    if template not in available_templates:
        print(f"Error: Unknown template '{template}'", file=sys.stderr)
        return 2

    valid_skill_names = {s["name"] for s in available_skills}
    for sk in selected_skills:
        if sk not in valid_skill_names:
            print(f"Error: Unknown skill '{sk}'", file=sys.stderr)
            return 2

    is_interactive = sys.stdin.isatty() and not args.yes and not args.dry_run
    if is_interactive:
        template, replacements, selected_skills = run_wizard(
            template,
            available_templates,
            replacements,
            available_skills,
        )

    return adopt(
        target=target_path,
        template=template,
        skills_to_install=selected_skills,
        replacements=replacements,
        force=args.force,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    raise SystemExit(main())
