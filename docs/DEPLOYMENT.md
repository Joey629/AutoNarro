# Narro 对外部署与安全指南

> 目标：让他人使用 SaaS，同时 **narratives.csv 专家语料绝不通过 HTTP 泄露**。

## 核心安全原则

| 资产 | 存储位置 | 是否对外暴露 |
|------|----------|--------------|
| `data/narratives.csv` | 服务器磁盘 | **否** — 仅推理时读入内存算常模均值 |
| `data/evaluations.db` | 服务器磁盘 | **否** — 无下载接口 |
| `models/` | 服务器磁盘 | **否** — 中间件拦截 |
| 用户提交的叙事 | SQLite | 仅授权 API 返回**该用户**自己的记录 |

应用已内置 `backend/security.py`：拦截 `/data/`、`*.csv`、`narratives.csv`、`/models/` 等路径。

---

## 推荐部署方式（按易用程度）

### 方式 A：内网 / 园所 VPN（最安全）

- 服务器只监听内网 IP 或 [Tailscale](https://tailscale.com) 私有地址
- 教师通过 VPN 访问 `http://100.x.x.x:8000/platform`
- **无需公网暴露**，语料风险最低

### 方式 B：Cloudflare Tunnel（免公网 IP）

```bash
# 本机已运行 python run_web.py
cloudflared tunnel --url http://127.0.0.1:8000
```

配合 Cloudflare Access 邮箱白名单 + `NARRO_REQUIRE_API_KEY=1`。

### 方式 C：云服务器 + Nginx + HTTPS（正式试点）

见 `deploy/nginx.conf.example`。

---

## 生产环境变量（必配）

```bash
export NARRO_API_KEY="长随机字符串"          # 分发给试点机构
export NARRO_REQUIRE_API_KEY=1               # 强制所有 /api/* 带 Key
export NARRO_HTTPS=1                         # 启用 HSTS（HTTPS 时）
export DEEPSEEK_API_KEY="..."                    # 可选 AI 辅导
```

前端首次打开 `/platform` 时在浏览器控制台设置（或后续做登录页）：

```javascript
localStorage.setItem("narro_api_key", "与服务器相同的 Key");
```

---

## Docker 部署

```bash
# 确保 narratives.csv 在 data/ 但不会被 HTTP 下载
docker compose -f docker-compose.prod.yml up -d --build
```

使用 `docker-compose.prod.yml`（勿将 `data/narratives.csv` 挂载到公开卷）。

---

## 防爬虫清单

- [x] 路径中间件阻断语料与 CSV
- [x] `robots.txt` Disallow
- [ ] 生产强制 `NARRO_REQUIRE_API_KEY`
- [ ] Nginx `limit_req` 限流
- [ ] 仅 HTTPS + 机构 IP 白名单（可选）
- [ ] 不把 `narratives.csv` 打进 Docker 镜像上传公网仓库（仅私有部署机拷贝）

---

## 域名规划（主域：autonarro.com）

| 路径 | 用途 |
|------|------|
| `https://autonarro.com/` | 品牌官网（营销） |
| `https://autonarro.com/platform` | SaaS 工作台 |
| `https://autonarro.com/api/*` | API（需 Key） |

详见 **`docs/DEPLOYMENT_AUTONARRO.md`**、`deploy/nginx.autonarro.com.conf.example`。  
域名配置见 `configs/brand.json`（`domain` 字段）。

注册域名后，DNS A/CNAME 指向服务器，Nginx 配置 SSL（Let's Encrypt certbot）。

---

## 自检

```bash
# 应返回 403
curl -I http://你的域名/data/narratives.csv
curl -I http://你的域名/narratives.csv

# 应 401（若开启 REQUIRE_API_KEY）
curl http://你的域名/api/history

# 应 200 + Key
curl -H "X-API-Key: $NARRO_API_KEY" http://你的域名/api/health
```
