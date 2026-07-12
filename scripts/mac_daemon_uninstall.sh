#!/usr/bin/env bash
# 卸载 Mac 内测常驻服务
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck source=scripts/mac_daemon_common.sh
source "${ROOT}/scripts/mac_daemon_common.sh"

CF="$(mac_daemon_cloudflared || true)"

echo ">>> 卸载金声玉叙 Mac 常驻服务"

if [[ -f "${MAC_DAEMON_PLIST}" ]]; then
  launchctl bootout "gui/$(id -u)" "${MAC_DAEMON_PLIST}" 2>/dev/null || true
  rm -f "${MAC_DAEMON_PLIST}"
  echo "    已移除 Web LaunchAgent"
fi

if [[ -n "$CF" ]]; then
  "${CF}" service uninstall 2>/dev/null || true
  rm -f "${HOME}/Library/LaunchAgents/com.cloudflare.cloudflared.plist"
fi

if [[ -f "${MAC_DAEMON_CF_PLIST}" ]]; then
  launchctl bootout "gui/$(id -u)" "${MAC_DAEMON_CF_PLIST}" 2>/dev/null || true
  rm -f "${MAC_DAEMON_CF_PLIST}"
  echo "    已移除 Tunnel LaunchAgent"
fi

pgrep -f "cloudflared.*tunnel run" 2>/dev/null | xargs kill 2>/dev/null || true

PIDS=$(lsof -ti ":${MAC_DAEMON_PORT}" 2>/dev/null || true)
if [[ -n "$PIDS" ]]; then
  kill $PIDS 2>/dev/null || true
fi

echo "完成。"
