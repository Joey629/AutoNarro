#!/usr/bin/env bash
# 检查 Mac 内测常驻服务状态
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck source=scripts/mac_daemon_common.sh
source "${ROOT}/scripts/mac_daemon_common.sh"

echo "=== 金声玉叙 Mac 内测常驻 ==="
echo ""

echo "[Web LaunchAgent] ${MAC_DAEMON_LABEL}"
if launchctl print "gui/$(id -u)/${MAC_DAEMON_LABEL}" >/dev/null 2>&1; then
  launchctl print "gui/$(id -u)/${MAC_DAEMON_LABEL}" 2>/dev/null | grep -E "state =|pid =|last exit" || true
else
  echo "  未安装（运行 bash scripts/mac_daemon_install.sh）"
fi
echo ""

echo "[本机 :${MAC_DAEMON_PORT}]"
if curl -sf "http://127.0.0.1:${MAC_DAEMON_PORT}/api/health" >/dev/null 2>&1; then
  echo "  OK  http://127.0.0.1:${MAC_DAEMON_PORT}/api/health"
else
  echo "  不可达"
fi
echo ""

echo "[Cloudflare Tunnel] ${MAC_DAEMON_CF_LABEL}"
if launchctl print "gui/$(id -u)/${MAC_DAEMON_CF_LABEL}" >/dev/null 2>&1; then
  launchctl print "gui/$(id -u)/${MAC_DAEMON_CF_LABEL}" 2>/dev/null | grep -E "state =|pid =|last exit" || true
elif launchctl print "gui/$(id -u)/com.cloudflare.cloudflared" >/dev/null 2>&1; then
  echo "  检测到旧版 com.cloudflare.cloudflared（需重装: bash scripts/mac_daemon_install.sh）"
else
  echo "  未安装（运行 bash scripts/mac_daemon_install.sh）"
fi
if launchctl print "gui/$(id -u)/${MAC_DAEMON_CF_LABEL}" 2>/dev/null | grep -q "state = running"; then
  pgrep -fl cloudflared 2>/dev/null | head -2 || echo "  (LaunchAgent running)"
else
  echo "  cloudflared 未运行 → 外网 autonarro.com 会报 Error 1033"
fi
echo ""

echo "[公网 autonarro.com]"
CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 https://autonarro.com/api/health 2>/dev/null || echo "000")
if [[ "$CODE" == "200" ]]; then
  echo "  OK  https://autonarro.com/api/health"
else
  echo "  HTTP ${CODE}（若 1033/5xx，检查 cloudflared 与 Mac 是否休眠）"
fi
echo ""

echo "[电源/休眠]"
pmset -g custom 2>/dev/null | head -20 || pmset -g 2>/dev/null | head -10
echo ""
echo "日志: tail -f ${MAC_DAEMON_WEB_LOG}"
echo "      tail -f ${MAC_DAEMON_CF_ERR}"
