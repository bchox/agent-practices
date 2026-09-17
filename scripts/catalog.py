#!/usr/bin/env python3
"""Build or verify the machine-readable Agent Practices catalog."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"missing frontmatter: {path.relative_to(ROOT)}")

    values: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return values
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"invalid frontmatter line in {path.relative_to(ROOT)}: {line}")
        values[key.strip()] = value.strip()
    raise ValueError(f"unclosed frontmatter: {path.relative_to(ROOT)}")


def build() -> dict[str, object]:
    skills = []
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        metadata = frontmatter(path)
        skills.append(
            {
                "name": metadata["name"],
                "description": metadata["description"],
                "path": path.relative_to(ROOT).as_posix(),
            }
        )

    templates = []
    for path in sorted((ROOT / "templates").glob("*/AGENTS.md")):
        templates.append(
            {
                "name": path.parent.name,
                "path": path.relative_to(ROOT).as_posix(),
            }
        )

    return {
        "$schema": "./catalog.schema.json",
        "schemaVersion": 1,
        "projectVersion": (ROOT / "VERSION").read_text(encoding="utf-8").strip(),
        "skills": skills,
        "templates": templates,
    }


def render(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="regenerate catalog.json")
    mode.add_argument("--check", action="store_true", help="fail when catalog.json is stale")
    args = parser.parse_args()

    expected = render(build())
    if args.write:
        CATALOG.write_text(expected, encoding="utf-8")
        print(f"Wrote {CATALOG.relative_to(ROOT)}")
        return 0

    actual = CATALOG.read_text(encoding="utf-8") if CATALOG.exists() else ""
    if actual != expected:
        print("catalog.json is stale; run ./scripts/catalog.py --write")
        return 1
    print("Catalog is current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
