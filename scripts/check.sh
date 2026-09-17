#!/usr/bin/env sh
set -eu

required_files='README.md LICENSE CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md AGENTS.md docs/architecture.md docs/conventions.md'
for file in $required_files; do
  test -f "$file" || { echo "Missing required file: $file" >&2; exit 1; }
done

for skill in coding-best-practices documentation git-workflow testing code-review security; do
  test -f "skills/$skill/SKILL.md" || { echo "Missing skill: $skill" >&2; exit 1; }
done

if grep -RIn '[[:blank:]]$' --include='*.md' --include='*.yml' --include='*.yaml' .; then
  echo 'Trailing whitespace found.' >&2
  exit 1
fi

echo 'Repository checks passed.'
