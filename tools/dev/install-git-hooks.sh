#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HOOKS_SRC_DIR="$ROOT_DIR/tools/dev/hooks"

# Handle git worktree
if [[ -f "$ROOT_DIR/.git" ]]; then
  GIT_DIR=$(cat "$ROOT_DIR/.git" | sed 's/gitdir: //')
  HOOKS_DST_DIR="$GIT_DIR/hooks"
elif [[ -d "$ROOT_DIR/.git" ]]; then
  HOOKS_DST_DIR="$ROOT_DIR/.git/hooks"
else
  echo "[error] Not a git repository"
  exit 1
fi

echo "📦 Installing git hooks..."

# Install pre-push hook
if [[ -f "$HOOKS_SRC_DIR/pre-push" ]]; then
  cp "$HOOKS_SRC_DIR/pre-push" "$HOOKS_DST_DIR/pre-push"
  chmod +x "$HOOKS_DST_DIR/pre-push"
  echo "[ok] pre-push hook installed"
fi

# Install commit-msg hook
if [[ -f "$HOOKS_SRC_DIR/commit-msg" ]]; then
  cp "$HOOKS_SRC_DIR/commit-msg" "$HOOKS_DST_DIR/commit-msg"
  chmod +x "$HOOKS_DST_DIR/commit-msg"
  echo "[ok] commit-msg hook installed"
fi

echo "🎉 Git hooks installed successfully!"
