#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}/src"
export NARRO_BART_FORCE_CPU="${NARRO_BART_FORCE_CPU:-1}"
exec python scripts/train_macro.py
