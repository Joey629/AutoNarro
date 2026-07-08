# autonarro.com 部署清单

**POC 最快路径（本机 + 临时 HTTPS）：** 见 [DEPLOYMENT_POC.md](DEPLOYMENT_POC.md) → `bash scripts/poc_tunnel.sh`

## URL 规划

| 地址 | 用途 |
|------|------|
| `https://autonarro.com/` | 品牌官网 |
| `https://autonarro.com/platform` | SaaS 工作台（beta） |
| `https://autonarro.com/app` | 旧路径，301 跳转到 `/platform` |
| `https://autonarro.com/api/health` | 健康检查 |

默认模型版本：`narro_v4`（BART 线索 + QiDeBERTa-base 宏观 SS + XGB 宏观 SC），见 `configs/model_registry.json`。

## 1. DNS

在域名注册商添加：

- `A` 记录：`autonarro.com` → 云服务器公网 IP  
- `A` 或 `CNAME`：`www.autonarro.com` → 同上或 `autonarro.com`

若用 **Cloudflare**：可开代理（橙云），再配合 Tunnel 或源站 443。

## 2. 服务器准备（Ubuntu 示例）

```bash
# 依赖
sudo apt update && sudo apt install -y git nginx certbot python3-venv

# 代码（私有仓库用 deploy key）
git clone <your-repo> /opt/autonarro && cd /opt/autonarro

# 环境（勿提交 .env）
cp .env.example .env
# 编辑: NARRO_API_KEY, DEEPSEEK_API_KEY, NARRO_MODEL_VERSION=narro_v4

# 权重与语料（scp/rsync，勿进公开 git）
# models/micro_narro_v4.pth
# models/pretrained/qideberta-base/
# models/pretrained/bart-chinese-uer/
# models/bart_narro_v4/
# models/macro_xgb_narro_v4/
# data/narratives.csv

cd frontend && npm ci && npm run build && cd ..
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## 3. 生产进程

**Docker（推荐）**

```bash
export NARRO_API_KEY="长随机串"
export NARRO_REQUIRE_API_KEY=1
export NARRO_HTTPS=1
export NARRO_MODEL_VERSION=narro_v4
docker compose -f docker-compose.prod.yml up -d --build
```

**或 systemd + run_web.py**

```bash
export PORT=8000 NARRO_MODEL_VERSION=narro_v4 NARRO_REQUIRE_API_KEY=1 ...
python run_web.py   # 建议用 systemd 守护
```

## 4. Nginx + HTTPS

```bash
sudo cp deploy/nginx.autonarro.com.conf.example /etc/nginx/sites-available/autonarro.com
sudo ln -sf /etc/nginx/sites-available/autonarro.com /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
sudo certbot --nginx -d autonarro.com -d www.autonarro.com
```

## 5. Beta 用户 API Key

浏览器打开 `/platform` 后，控制台执行（与服务器 `NARRO_API_KEY` 一致）：

```javascript
localStorage.setItem("narro_api_key", "你的试点 Key");
```

## 6. 无公网 IP 时（Cloudflare Tunnel）

```bash
# 本机或服务器上已运行 run_web.py / docker
cloudflared tunnel --url http://127.0.0.1:8000
```

在 Cloudflare DNS 将 `autonarro.com` CNAME 到 tunnel 地址；可用 **Cloudflare Access** 做邮箱白名单 closed beta。

## 7. 发布前自检

```bash
PYTHONPATH=src python scripts/check_release.py
curl -I https://autonarro.com/data/narratives.csv   # 应 403
curl -H "X-API-Key: $NARRO_API_KEY" https://autonarro.com/api/health
```

## 8. 训练与线上分离

- **训练**：本地 / GPU 云 / CI → 产出新 `models/`  
- **上线**：仅 rsync 新权重到服务器，改 `model_registry.json` 的 `active_version` 或版本条目，重启服务  

不要在用户请求路径上 `train_*`。
