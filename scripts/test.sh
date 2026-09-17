#!/usr/bin/env sh
set -eu

test_root=$(mktemp -d "${TMPDIR:-/tmp}/agent-practices.XXXXXX")
trap 'rm -rf "$test_root"' EXIT HUP INT TERM
target="$test_root/project"
mkdir "$target"

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

./scripts/placeholders.sh "$target" | grep -q '<project-name>'
if ./scripts/placeholders.sh --strict "$target" >/dev/null 2>&1; then
  echo 'placeholders --strict should fail on an unfilled template.' >&2
  exit 1
fi

filled="$test_root/filled"
mkdir "$filled"
cp examples/minimal-repository/AGENTS.md "$filled/AGENTS.md"
./scripts/placeholders.sh --strict "$filled"

echo 'Adoption tests passed.'
