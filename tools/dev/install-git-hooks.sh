#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HOOK_SRC="$ROOT_DIR/tools/dev/hooks/pre-push"
HOOK_DST="$ROOT_DIR/.git/hooks/pre-push"

if [[ ! -d "$ROOT_DIR/.git" ]]; then
  echo "[error] .git directory not found. Run this script from a git clone."
  exit 1
fi

if [[ ! -f "$HOOK_SRC" ]]; then
  echo "[error] Hook source not found: $HOOK_SRC"
  exit 1
fi

cp "$HOOK_SRC" "$HOOK_DST"
chmod +x "$HOOK_DST"

echo "[ok] pre-push hook installed at .git/hooks/pre-push"
