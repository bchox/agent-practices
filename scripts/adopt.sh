#!/usr/bin/env sh
set -eu

usage() {
  echo "Usage: $0 --target PATH [--template NAME] [--skills all|NAME,NAME] [--dry-run] [--force]"
  echo "       $0 --list"
}

target=''
template='generic'
dry_run='false'
force='false'
selected_skills='all'
list_only='false'

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      [ "$#" -ge 2 ] || { usage >&2; exit 2; }
      target=$2
      shift 2
      ;;
    --template)
      [ "$#" -ge 2 ] || { usage >&2; exit 2; }
      template=$2
      shift 2
      ;;
    --dry-run)
      dry_run='true'
      shift
      ;;
    --skills)
      [ "$#" -ge 2 ] || { usage >&2; exit 2; }
      selected_skills=$2
      shift 2
      ;;
    --list)
      list_only='true'
      shift
      ;;
    --force)
      force='true'
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(dirname "$script_dir")

if [ "$list_only" = 'true' ]; then
  echo 'Templates:'
  for template_dir in "$repo_root"/templates/*; do
    [ -f "$template_dir/AGENTS.md" ] && echo "  $(basename "$template_dir")"
  done
  echo 'Skills:'
  for skill_dir in "$repo_root"/skills/*; do
    [ -f "$skill_dir/SKILL.md" ] && echo "  $(basename "$skill_dir")"
  done
  exit 0
fi

[ -n "$target" ] || { echo 'Missing --target.' >&2; usage >&2; exit 2; }
[ -d "$target" ] || { echo "Target directory does not exist: $target" >&2; exit 1; }

contract_source="$repo_root/templates/$template/AGENTS.md"
contract_target="$target/AGENTS.md"
skills_target="$target/.agents/skills"

[ -f "$contract_source" ] || { echo "Unknown template: $template" >&2; exit 2; }

if [ "$selected_skills" = 'all' ]; then
  skill_names=''
  for skill_dir in "$repo_root"/skills/*; do
    skill_names="$skill_names $(basename "$skill_dir")"
  done
else
  skill_names=$(printf '%s' "$selected_skills" | tr ',' ' ')
fi

for skill_name in $skill_names; do
  [ -f "$repo_root/skills/$skill_name/SKILL.md" ] || { echo "Unknown skill: $skill_name" >&2; exit 2; }
done

if [ -e "$contract_target" ] && [ "$force" != 'true' ]; then
  echo "Refusing to overwrite $contract_target. Re-run with --force after reviewing it." >&2
  exit 1
fi

echo "Template: $template"
echo "Contract: $contract_source -> $contract_target"
echo "Skills:$skill_names -> $skills_target"

[ "$dry_run" = 'true' ] && { echo 'Dry run: no files changed.'; exit 0; }

mkdir -p "$skills_target"
cp "$contract_source" "$contract_target"
for skill_name in $skill_names; do
  skill_dir="$repo_root/skills/$skill_name"
  mkdir -p "$skills_target/$skill_name"
  cp -R "$skill_dir"/. "$skills_target/$skill_name/"
done

echo 'Installed Agent Practices.'
echo 'Next: fill every <placeholder> in AGENTS.md, delete skills you will not use, then run a real agent task.'
"$script_dir/placeholders.sh" "$target" || true
