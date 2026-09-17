#!/usr/bin/env sh
set -eu

usage() {
  echo "Usage: $0 --target PATH [--template generic|kotlin-android|typescript|python] [--dry-run] [--force]"
}

target=''
template='generic'
dry_run='false'
force='false'

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

[ -n "$target" ] || { echo 'Missing --target.' >&2; usage >&2; exit 2; }
[ -d "$target" ] || { echo "Target directory does not exist: $target" >&2; exit 1; }

case "$template" in
  generic|kotlin-android|typescript|python) ;;
  *) echo "Unknown template: $template" >&2; exit 2 ;;
esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(dirname "$script_dir")
contract_source="$repo_root/templates/$template/AGENTS.md"
contract_target="$target/AGENTS.md"
skills_target="$target/.agents/skills"

if [ -e "$contract_target" ] && [ "$force" != 'true' ]; then
  echo "Refusing to overwrite $contract_target. Re-run with --force after reviewing it." >&2
  exit 1
fi

echo "Template: $template"
echo "Contract: $contract_source -> $contract_target"
echo "Skills: $repo_root/skills -> $skills_target"

[ "$dry_run" = 'true' ] && { echo 'Dry run: no files changed.'; exit 0; }

mkdir -p "$skills_target"
cp "$contract_source" "$contract_target"
for skill_dir in "$repo_root"/skills/*; do
  skill_name=$(basename "$skill_dir")
  mkdir -p "$skills_target/$skill_name"
  cp -R "$skill_dir"/. "$skills_target/$skill_name/"
done

echo 'Installed Agent Practices.'
echo 'Next: fill every <placeholder> in AGENTS.md, delete skills you will not use, then run a real agent task.'
"$script_dir/placeholders.sh" "$target" || true
