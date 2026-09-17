#!/usr/bin/env sh
set -eu

required_files='README.md LICENSE CONTRIBUTING.md CODE_OF_CONDUCT.md GOVERNANCE.md SECURITY.md SUPPORT.md AGENTS.md CHANGELOG.md ROADMAP.md VERSION catalog.json catalog.schema.json docs/adoption-reports.md docs/architecture.md docs/conventions.md docs/getting-started.md docs/compatibility.md docs/skill-authoring.md'
for file in $required_files; do
  test -f "$file" || { echo "Missing required file: $file" >&2; exit 1; }
done

for skill_dir in skills/*; do
  skill=$(basename "$skill_dir")
  skill_file="$skill_dir/SKILL.md"
  test -f "$skill_file" || { echo "Missing SKILL.md: $skill" >&2; exit 1; }
  first_line=$(sed -n '1p' "$skill_file")
  test "$first_line" = '---' || { echo "Missing YAML frontmatter: $skill_file" >&2; exit 1; }
  grep -q "^name: $skill$" "$skill_file" || { echo "Skill name does not match directory: $skill_file" >&2; exit 1; }
  grep -q '^description: Use when ' "$skill_file" || { echo "Skill description must start with 'Use when ': $skill_file" >&2; exit 1; }
  grep -q '^Done when ' "$skill_file" || { echo "Missing Done when line: $skill_file" >&2; exit 1; }
done

for template_dir in templates/*; do
  template=$(basename "$template_dir")
  test -f "$template_dir/AGENTS.md" || { echo "Missing AGENTS.md: $template" >&2; exit 1; }
done

find . -path './.git' -prune -o \( -name '*.md' -o -name '*.yml' -o -name '*.yaml' \) -type f -print |
while IFS= read -r file; do
  if grep -n '[[:blank:]]$' "$file"; then
    echo "Trailing whitespace found in $file." >&2
    exit 1
  fi
done

test -x scripts/adopt.sh || { echo 'scripts/adopt.sh must be executable.' >&2; exit 1; }
test -x scripts/init.sh || { echo 'scripts/init.sh must be executable.' >&2; exit 1; }
test -x scripts/init.py || { echo 'scripts/init.py must be executable.' >&2; exit 1; }
test -x scripts/check.sh || { echo 'scripts/check.sh must be executable.' >&2; exit 1; }
test -x scripts/test.sh || { echo 'scripts/test.sh must be executable.' >&2; exit 1; }
test -x scripts/placeholders.sh || { echo 'scripts/placeholders.sh must be executable.' >&2; exit 1; }
test -x scripts/catalog.py || { echo 'scripts/catalog.py must be executable.' >&2; exit 1; }

./scripts/catalog.py --check

echo 'Repository checks passed.'
