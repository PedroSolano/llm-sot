#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
BRANCH="${1:-main}"

cd "$ROOT"
python3 ./validate-registry.py

if [[ ! -d .git ]]; then
  echo
  echo "This folder is not a Git checkout."
  echo "Copy/rsync its CONTENTS into the root of your llm-sot checkout, then commit/push there."
  exit 2
fi

git status --short
echo
echo "Validated. Review the diff, then commit/push normally:"
echo "  git add AGENTS.md agents skills factory routing README.md VERSION"
echo "  git commit -m 'Software factory registry v10.5.0'"
echo "  git push origin $BRANCH"
