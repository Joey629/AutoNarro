#!/usr/bin/env bash
# Narro POC：本机 run_web + Cloudflare 快速隧道（无需先配 DNS）
#
# 用法:
#   bash scripts/poc_tunnel.sh
#
# 首次会尝试: brew install cloudflared
# 保持本终端不要关；关掉后公网链接立即失效
#
# 绑定 autonarro.com 见 docs/DEPLOYMENT_AUTONARRO.md §6

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PORT="${PORT:-8000}"

if ! command -v cloudflared >/dev/null 2>&1; then
  echo ">>> 安装 cloudflared …"
  if command -v brew >/dev/null 2>&1; then
    brew install cloudflared
  else
    echo "请先安装: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/"
    exit 1
  fi
fi

if [[ ! -f frontend/static/css/workbench.css ]]; then
  echo ">>> 构建前端 …"
  (cd frontend && npm ci && npm run build)
fi

if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi

# POC 默认：不强制 API Key（试点跑通后再在 .env 开 NARRO_REQUIRE_API_KEY=1）
export NARRO_MODEL_VERSION="${NARRO_MODEL_VERSION:-narro_v4}"
export NARRO_BART_FORCE_CPU="${NARRO_BART_FORCE_CPU:-1}"
export PYTHONPATH="${ROOT}/src"

if curl -sf "http://127.0.0.1:${PORT}/api/health" >/dev/null 2>&1; then
  echo ">>> 检测到已有服务 :${PORT}"
else
  echo ">>> 启动 Narro Web（后台）… 日志: data/logs/poc_web.log"
  mkdir -p data/logs
  PY="${ROOT}/.venv/bin/python"
  [[ -x "$PY" ]] || PY="$(command -v python3)"
  nohup "$PY" run_web.py > data/logs/poc_web.log 2>&1 &
  echo $! > data/logs/poc_web.pid
  echo "    PID=$(cat data/logs/poc_web.pid)"
  for i in $(seq 1 60); do
    if curl -sf "http://127.0.0.1:${PORT}/api/health" >/dev/null 2>&1; then
      echo ">>> Web 就绪 http://127.0.0.1:${PORT}"
      break
    fi
    if [[ "$i" -eq 60 ]]; then
      echo "启动超时，查看: tail -f data/logs/poc_web.log"
      exit 1
    fi
    sleep 2
  done
fi

mkdir -p data/logs
CF_LOG="${ROOT}/data/logs/poc_tunnel.log"
: > "$CF_LOG"

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  隧道运行期间请保持本终端窗口打开（合盖/休眠/Ctrl+C 都会断）  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo "    本地: http://127.0.0.1:${PORT}/app"
echo "    公网 URL 约 10 秒后出现；也可: cat data/logs/poc_tunnel_url.txt"
echo ""

# 后台等待日志里出现 URL 后写入文件并醒目打印
(
  for _ in $(seq 1 90); do
    u="$(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$CF_LOG" 2>/dev/null | head -1)"
    if [[ -n "$u" ]]; then
      echo "$u" > "${ROOT}/data/logs/poc_tunnel_url.txt"
      echo ""
      echo "=============================================="
      echo "  POC 公网地址（复制到浏览器，勿改 xxxx）:"
      echo "  $u"
      echo "  工作台: ${u}/app"
      echo "=============================================="
      echo ""
      break
    fi
    sleep 1
  done
) &

cloudflared tunnel --url "http://127.0.0.1:${PORT}" 2>&1 | tee -a "$CF_LOG"
