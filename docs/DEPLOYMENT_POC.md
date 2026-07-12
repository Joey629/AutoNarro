# POC 部署（方案 A · 最简）

目标：**本机跑通 → 公网 HTTPS 链接 → 他人打开 `/platform` 试用**。不必先买云服务器。

## 阶段 0：5 分钟试通（随机域名）

适合：还没把 `autonarro.com` 迁到 Cloudflare。

```bash
cd /path/to/AutoNarro
source .venv/bin/activate   # 若无: python3 -m venv .venv && pip install -r requirements.txt
cp .env.example .env        # 填 DEEPSEEK_API_KEY=sk-...

bash scripts/poc_tunnel.sh
```

终端会出现**随机**地址（每次启动都不同），例如：

```text
https://requirements-mechanical-last-whereas.trycloudflare.com
```

**不要用** `https://xxxx.trycloudflare.com`（那是文档占位符，浏览器会显示「无法访问」）。

也可查看：`cat data/logs/poc_tunnel_url.txt`

- 官网：上述 URL `/`
- 工作台：上述 URL `/platform`
- 本机自测：`http://127.0.0.1:8000/api/health`

**注意：** Mac 需保持唤醒；关掉终端里 `cloudflared` 或合盖后外网链接会断。

停止：

```bash
kill $(cat data/logs/poc_web.pid)   # 停 Web
# cloudflared 用 Ctrl+C
```

### POC 环境变量建议（`.env`）

```env
DEEPSEEK_API_KEY=sk-...
NARRO_MODEL_VERSION=narro_v4
NARRO_BART_FORCE_CPU=1
# 试点阶段可不设 NARRO_REQUIRE_API_KEY，方便直接打开 /platform
```

上线前再加：

```env
NARRO_API_KEY=用 openssl rand -hex 32 生成
NARRO_REQUIRE_API_KEY=1
```

浏览器 `/platform` 控制台：

```javascript
localStorage.setItem("narro_api_key", "与 NARRO_API_KEY 相同");
location.reload();
```

---

## 阶段 1：绑定 autonarro.com（仍用 Tunnel）

1. [Cloudflare](https://dash.cloudflare.com) → **Add site** → `autonarro.com`
2. 在域名注册商把 **Nameserver** 改成 Cloudflare 提供的两条
3. 本机：

```bash
brew install cloudflared    # 若未装
cloudflared tunnel login
cloudflared tunnel create autonarro
cloudflared tunnel route dns autonarro autonarro.com
```

4. `~/.cloudflared/config.yml`：

```yaml
tunnel: autonarro
credentials-file: /Users/你的用户名/.cloudflared/<隧道ID>.json

ingress:
  - hostname: autonarro.com
    service: http://127.0.0.1:8000
  - hostname: www.autonarro.com
    service: http://127.0.0.1:8000
  - service: http_status:404
```

5. 先 `bash scripts/poc_tunnel.sh` 或手动 `python run_web.py`，再：

```bash
sudo cloudflared service install
sudo cloudflared service start
```

详细清单见 [DEPLOYMENT_AUTONARRO.md](DEPLOYMENT_AUTONARRO.md)。

---

## 阶段 1.5：Mac 内测常驻（推荐 · 小范围试用）

适合：**本机 + autonarro.com 隧道**，给少量内测用户用。Mac 需**接电源**并**防止休眠**。

### 一键安装（Web 开机自启 + Tunnel 系统服务）

```bash
cd /path/to/AutoNarro
bash scripts/mac_daemon_install.sh
```

会完成：

- `run_web.py` → 用户级 LaunchAgent（`com.autonarro.web`，崩溃自动拉起）
- `cloudflared tunnel run autonarro` → 用户级 LaunchAgent（`com.autonarro.cloudflared`，无需 sudo）
- 提示接电源防休眠命令

> **注意：** 不要用 `sudo cloudflared service install <config.yml>`，新版会把路径误当成 token 报错。本脚本使用自定义 LaunchAgent 运行命名隧道。

### 防止熄屏/合盖后断网

**系统设置（推荐）：** 电池 → 接通电源时 → 关闭「自动休眠」/ 防止 Mac 自动进入睡眠。

**终端（接电源 profile，执行一次）：**

```bash
sudo pmset -c sleep 0 disksleep 0 displaysleep 10
pmset -g    # 确认 AC 下 sleep 为 0
```

### 日常命令

```bash
bash scripts/mac_daemon_status.sh    # 本机 + 公网健康检查
bash scripts/mac_daemon_uninstall.sh # 卸载常驻
```

| 现象 | 处理 |
|------|------|
| Error 1033 | `bash scripts/mac_daemon_status.sh`；若 tunnel 未运行 → `launchctl kickstart -k gui/$(id -u)/com.autonarro.cloudflared` 或重装 `mac_daemon_install.sh` |
| 本机 200、公网 1033 | Mac 可能已休眠；唤醒后等 10 秒再试 |
| 改代码后 | Web 会自动由 LaunchAgent 拉起；若需立刻生效：`launchctl kickstart -k gui/$(id -u)/com.autonarro.web` |

---

## 无法访问？

| 现象 | 处理 |
|------|------|
| 打开 `xxxx.trycloudflare.com` | 必须从终端复制**完整** `https://….trycloudflare.com` |
| 换过终端 / 重启过脚本 | URL 已变，重新 `cat data/logs/poc_tunnel_url.txt` |
| 本机 `127.0.0.1:8000` 正常，外网不行 | 手机/公司网可能拦 `trycloudflare.com`；Mac 浏览器先试公网 URL，或改阶段 1 绑 `autonarro.com` |
| 启动超时 | `tail -f data/logs/poc_web.log` |

---

## 自检

```bash
export NARRO_BART_FORCE_CPU=1
PYTHONPATH=src python scripts/check_release.py
curl -s http://127.0.0.1:8000/api/health | head
```
