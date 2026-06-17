#!/usr/bin/env bash
# 停止占用 8000 的旧进程并启动最新 Narro Web（含认证 API）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PORT="${PORT:-8000}"
echo "Stopping anything on port ${PORT}..."
PIDS=$(lsof -ti ":${PORT}" 2>/dev/null || true)
if [ -n "$PIDS" ]; then
  kill $PIDS 2>/dev/null || true
  sleep 1
  lsof -ti ":${PORT}" 2>/dev/null | xargs kill -9 2>/dev/null || true
fi
echo "Starting python run_web.py ..."
exec python run_web.py
