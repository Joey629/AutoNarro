#!/usr/bin/env bash
# 共享路径与常量（Mac 内测常驻：Web + Cloudflare Tunnel）
set -euo pipefail

MAC_DAEMON_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MAC_DAEMON_LABEL="com.autonarro.web"
MAC_DAEMON_PLIST="${HOME}/Library/LaunchAgents/${MAC_DAEMON_LABEL}.plist"
MAC_DAEMON_LOG_DIR="${MAC_DAEMON_ROOT}/data/logs"
MAC_DAEMON_WEB_LOG="${MAC_DAEMON_LOG_DIR}/launchd_web.log"
MAC_DAEMON_WEB_ERR="${MAC_DAEMON_LOG_DIR}/launchd_web.err.log"
MAC_DAEMON_WEB_PID="${MAC_DAEMON_LOG_DIR}/launchd_web.pid"
MAC_DAEMON_CF_CONFIG="${HOME}/.cloudflared/config.yml"
MAC_DAEMON_CF_LABEL="com.autonarro.cloudflared"
MAC_DAEMON_CF_PLIST="${HOME}/Library/LaunchAgents/${MAC_DAEMON_CF_LABEL}.plist"
MAC_DAEMON_CF_LOG="${MAC_DAEMON_LOG_DIR}/launchd_cloudflared.log"
MAC_DAEMON_CF_ERR="${MAC_DAEMON_LOG_DIR}/launchd_cloudflared.err.log"
MAC_DAEMON_PORT="${PORT:-8000}"

mac_daemon_python() {
  local py="${MAC_DAEMON_ROOT}/.venv/bin/python"
  if [[ -x "$py" ]]; then
    echo "$py"
    return 0
  fi
  command -v python3
}

mac_daemon_cloudflared() {
  if command -v cloudflared >/dev/null 2>&1; then
    command -v cloudflared
    return 0
  fi
  if [[ -x /opt/homebrew/bin/cloudflared ]]; then
    echo /opt/homebrew/bin/cloudflared
    return 0
  fi
  return 1
}

mac_daemon_ensure_logs() {
  mkdir -p "$MAC_DAEMON_LOG_DIR"
}

mac_daemon_wait_health() {
  local i
  for i in $(seq 1 45); do
    if curl -sf "http://127.0.0.1:${MAC_DAEMON_PORT}/api/health" >/dev/null 2>&1; then
      return 0
    fi
    sleep 2
  done
  return 1
}
