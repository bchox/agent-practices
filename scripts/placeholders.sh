#!/usr/bin/env sh
set -eu

usage() {
  echo "Usage: $0 [--strict] [PATH]"
}

strict='false'
path='.'

while [ "$#" -gt 0 ]; do
  case "$1" in
    --strict)
      strict='true'
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      path=$1
      shift
      ;;
  esac
done

[ -d "$path" ] || { echo "Not a directory: $path" >&2; exit 1; }

tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT HUP INT TERM

# Angle-bracket tokens that still look like template slots.
# Ignore HTML-ish tags and already-filled examples.
find "$path" \( -path "$path/.git" -o -path "$path/.agents" \) -prune -o \
  -type f \( -name '*.md' -o -name '*.yml' -o -name '*.yaml' \) -print |
while IFS= read -r file; do
  grep -nE '<[a-z][a-z0-9-]*>' "$file" 2>/dev/null | grep -vE '<https?://' || true
done > "$tmp"

if [ ! -s "$tmp" ]; then
  echo "No template placeholders remain under $path."
  exit 0
fi

echo "Unfilled placeholders:"
cat "$tmp"

if [ "$strict" = 'true' ]; then
  echo "Replace every <placeholder> before committing this contract." >&2
  exit 1
fi
exit 0
