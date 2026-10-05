#!/usr/bin/env bash
# Build one upload-ready zip per skill (for Agensi and similar skill marketplaces):
# dist/<skill>.zip containing <skill>/SKILL.md (plus any other files in the folder).
set -euo pipefail

cd "$(dirname "$0")/.."
rm -rf dist
mkdir -p dist

for dir in skills/*/; do
  name=$(basename "$dir")
  if [ ! -f "$dir/SKILL.md" ]; then
    echo "skip $name: no SKILL.md" >&2
    continue
  fi
  (cd skills && zip -qr -X "../dist/$name.zip" "$name" -x '*.DS_Store')
  echo "built dist/$name.zip"
done
