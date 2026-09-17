#!/usr/bin/env sh
set -eu

test_root=$(mktemp -d "${TMPDIR:-/tmp}/agent-practices.XXXXXX")
trap 'rm -rf "$test_root"' EXIT HUP INT TERM
target="$test_root/project"
mkdir "$target"

./scripts/adopt.sh --list > "$test_root/catalog.txt"
grep -q '^  monorepo$' "$test_root/catalog.txt"
grep -q '^  database-changes$' "$test_root/catalog.txt"

./scripts/adopt.sh --target "$target" --template typescript --dry-run
test ! -e "$target/AGENTS.md"

./scripts/adopt.sh --target "$target" --template typescript
test -f "$target/AGENTS.md"
test -f "$target/.agents/skills/debugging/SKILL.md"
test -f "$target/.agents/skills/dependency-management/SKILL.md"

if ./scripts/adopt.sh --target "$target" --template generic >/dev/null 2>&1; then
  echo 'Overwrite protection did not stop a second install.' >&2
  exit 1
fi

./scripts/adopt.sh --target "$target" --template python --force
grep -q 'Python guide' "$target/AGENTS.md"

selective="$test_root/selective"
mkdir "$selective"
./scripts/adopt.sh --target "$selective" --template infrastructure --skills security,code-review
test -f "$selective/.agents/skills/security/SKILL.md"
test -f "$selective/.agents/skills/code-review/SKILL.md"
test ! -e "$selective/.agents/skills/testing/SKILL.md"

if ./scripts/adopt.sh --target "$selective" --template unknown --force >/dev/null 2>&1; then
  echo 'Unknown templates must fail.' >&2
  exit 1
fi

if ./scripts/adopt.sh --target "$selective" --skills unknown --force >/dev/null 2>&1; then
  echo 'Unknown skills must fail.' >&2
  exit 1
fi

./scripts/placeholders.sh "$target" | grep -q '<project-name>'
if ./scripts/placeholders.sh --strict "$target" >/dev/null 2>&1; then
  echo 'placeholders --strict should fail on an unfilled template.' >&2
  exit 1
fi

filled="$test_root/filled"
mkdir "$filled"
cp examples/minimal-repository/AGENTS.md "$filled/AGENTS.md"
./scripts/placeholders.sh --strict "$filled"

./scripts/catalog.py --check

# Test init.sh / init.py CLI and auto-detection
./scripts/init.sh --list > "$test_root/init-catalog.txt"
grep -q '^  typescript$' "$test_root/init-catalog.txt"
grep -q '^  testing$' "$test_root/init-catalog.txt"

# 1. TypeScript auto-detection and script scraper
ts_target="$test_root/ts_app"
mkdir "$ts_target"
cat << 'EOF' > "$ts_target/package.json"
{
  "name": "sample-ts-app",
  "scripts": {
    "test": "vitest run",
    "lint": "eslint .",
    "typecheck": "tsc --noEmit"
  }
}
EOF
touch "$ts_target/tsconfig.json"
touch "$ts_target/pnpm-lock.yaml"

./scripts/init.sh --target "$ts_target" --yes --dry-run
test ! -e "$ts_target/AGENTS.md"

./scripts/init.sh --target "$ts_target" --yes
test -f "$ts_target/AGENTS.md"
grep -q '# sample-ts-app TypeScript guide' "$ts_target/AGENTS.md"
grep -q '`pnpm run typecheck`, `pnpm run lint`, and `pnpm test`' "$ts_target/AGENTS.md"
./scripts/placeholders.sh --strict "$ts_target"

# Overwrite protection without --force
if ./scripts/init.sh --target "$ts_target" --yes >/dev/null 2>&1; then
  echo 'init.sh overwrite protection did not stop overwrite without --force.' >&2
  exit 1
fi

./scripts/init.sh --target "$ts_target" --force --yes
grep -q '# sample-ts-app TypeScript guide' "$ts_target/AGENTS.md"

# 2. Python auto-detection and script scraper
py_target="$test_root/py_pkg"
mkdir "$py_target"
cat << 'EOF' > "$py_target/pyproject.toml"
[project]
name = "sample-python-pkg"

[tool.ruff]
line-length = 88

[tool.mypy]
strict = true

[tool.pytest.ini_options]
testpaths = ["tests"]
EOF
touch "$py_target/uv.lock"

./scripts/init.sh --target "$py_target" --yes --skills security,code-review
test -f "$py_target/AGENTS.md"
grep -q '# sample-python-pkg Python guide' "$py_target/AGENTS.md"
grep -q '`uv run ruff check . && uv run ruff format --check .`, `uv run mypy .`, and `uv run pytest`' "$py_target/AGENTS.md"
test -f "$py_target/.agents/skills/security/SKILL.md"
test -f "$py_target/.agents/skills/code-review/SKILL.md"
test ! -e "$py_target/.agents/skills/testing/SKILL.md"
./scripts/placeholders.sh --strict "$py_target"

echo 'Adoption tests passed.'
