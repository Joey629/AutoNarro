#!/usr/bin/env bash
# Mac 内测：注册 Web（LaunchAgent）+ Cloudflare Tunnel（系统服务），开机自启
#
# 用法: bash scripts/mac_daemon_install.sh
# 前提: ~/.cloudflared/config.yml 已配置 autonarro 隧道（见 docs/DEPLOYMENT_POC.md 阶段 1）
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck source=scripts/mac_daemon_common.sh
source "${ROOT}/scripts/mac_daemon_common.sh"

PY="$(mac_daemon_python)"
CF="$(mac_daemon_cloudflared || true)"
mac_daemon_ensure_logs

echo ">>> 金声玉叙 Mac 内测常驻安装"
echo "    仓库: ${MAC_DAEMON_ROOT}"
echo ""

if [[ ! -f "${MAC_DAEMON_ROOT}/.env" ]]; then
  echo "警告: 未找到 .env，请先 cp .env.example .env 并填入 DEEPSEEK_API_KEY"
fi

if [[ ! -f "${MAC_DAEMON_CF_CONFIG}" ]]; then
  echo "错误: 未找到 ${MAC_DAEMON_CF_CONFIG}"
  echo "请先完成 Cloudflare Tunnel 配置（docs/DEPLOYMENT_POC.md 阶段 1）"
  exit 1
fi

if [[ ! -f "${MAC_DAEMON_ROOT}/frontend/static/css/workbench.css" ]]; then
  echo ">>> 构建前端 …"
  (cd "${MAC_DAEMON_ROOT}/frontend" && npm ci && npm run build)
fi

# 停掉手动启动的进程，避免与 LaunchAgent 冲突
if [[ -f "${MAC_DAEMON_ROOT}/data/logs/cloudflared.pid" ]]; then
  kill "$(cat "${MAC_DAEMON_ROOT}/data/logs/cloudflared.pid")" 2>/dev/null || true
fi
if [[ -f "${MAC_DAEMON_ROOT}/data/logs/poc_web.pid" ]]; then
  kill "$(cat "${MAC_DAEMON_ROOT}/data/logs/poc_web.pid")" 2>/dev/null || true
fi
PIDS=$(lsof -ti ":${MAC_DAEMON_PORT}" 2>/dev/null || true)
if [[ -n "$PIDS" ]]; then
  echo ">>> 停止占用 :${MAC_DAEMON_PORT} 的旧进程 …"
  kill $PIDS 2>/dev/null || true
  sleep 1
  lsof -ti ":${MAC_DAEMON_PORT}" 2>/dev/null | xargs kill -9 2>/dev/null || true
fi

mkdir -p "${HOME}/Library/LaunchAgents"
cat > "${MAC_DAEMON_PLIST}" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${MAC_DAEMON_LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${PY}</string>
    <string>run_web.py</string>
  </array>
  <key>WorkingDirectory</key>
  <string>${MAC_DAEMON_ROOT}</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>NARRO_BART_FORCE_CPU</key>
    <string>1</string>
    <key>REGRESSION_FORCE_CPU</key>
    <string>1</string>
    <key>PYTHONPATH</key>
    <string>${MAC_DAEMON_ROOT}/src</string>
    <key>PORT</key>
    <string>${MAC_DAEMON_PORT}</string>
  </dict>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>StandardOutPath</key>
  <string>${MAC_DAEMON_WEB_LOG}</string>
  <key>StandardErrorPath</key>
  <string>${MAC_DAEMON_WEB_ERR}</string>
</dict>
</plist>
EOF

echo ">>> 注册 Web LaunchAgent: ${MAC_DAEMON_PLIST}"
launchctl bootout "gui/$(id -u)" "${MAC_DAEMON_PLIST}" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "${MAC_DAEMON_PLIST}"
launchctl enable "gui/$(id -u)/${MAC_DAEMON_LABEL}"
launchctl kickstart -k "gui/$(id -u)/${MAC_DAEMON_LABEL}"

echo ">>> 等待本机 Web 就绪 …"
if ! mac_daemon_wait_health; then
  echo "Web 启动超时，查看: tail -f ${MAC_DAEMON_WEB_ERR}"
  exit 1
fi
echo "    本机健康检查 OK  http://127.0.0.1:${MAC_DAEMON_PORT}/api/health"

if [[ -z "$CF" ]]; then
  echo "错误: 未找到 cloudflared，请 brew install cloudflared"
  exit 1
fi

# 新版 cloudflared 的 `service install <路径>` 会把路径当 token，命名隧道需自定义 LaunchAgent
echo ">>> 注册 Cloudflare Tunnel LaunchAgent …"
"${CF}" service uninstall 2>/dev/null || true
launchctl bootout "gui/$(id -u)" "${HOME}/Library/LaunchAgents/com.cloudflare.cloudflared.plist" 2>/dev/null || true
rm -f "${HOME}/Library/LaunchAgents/com.cloudflare.cloudflared.plist"

cat > "${MAC_DAEMON_CF_PLIST}" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${MAC_DAEMON_CF_LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${CF}</string>
    <string>--config</string>
    <string>${MAC_DAEMON_CF_CONFIG}</string>
    <string>tunnel</string>
    <string>run</string>
    <string>autonarro</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>StandardOutPath</key>
  <string>${MAC_DAEMON_CF_LOG}</string>
  <key>StandardErrorPath</key>
  <string>${MAC_DAEMON_CF_ERR}</string>
</dict>
</plist>
EOF

launchctl bootout "gui/$(id -u)" "${MAC_DAEMON_CF_PLIST}" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "${MAC_DAEMON_CF_PLIST}"
launchctl enable "gui/$(id -u)/${MAC_DAEMON_CF_LABEL}"
launchctl kickstart -k "gui/$(id -u)/${MAC_DAEMON_CF_LABEL}"

echo ">>> 等待隧道连接 …"
sleep 5
if ! pgrep -f "cloudflared.*tunnel run autonarro" >/dev/null 2>&1; then
  echo "隧道未启动，查看: tail -f ${MAC_DAEMON_CF_ERR}"
  exit 1
fi
echo "    cloudflared 已运行"
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  安装完成。建议 Mac 接电源并关闭自动休眠（见下方命令）        ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "状态检查:  bash scripts/mac_daemon_status.sh"
echo "卸载:      bash scripts/mac_daemon_uninstall.sh"
echo ""
echo "── 防止熄屏后断网（接电源时执行一次，需密码）──"
echo "  sudo pmset -c sleep 0 disksleep 0 displaysleep 10"
echo "  pmset -g   # 确认 sleep 为 0"
echo ""
echo "── 系统设置（推荐）──"
echo "  系统设置 → 电池 → 接通电源时：关闭自动休眠 / 防止 Mac 自动睡眠"
echo ""
