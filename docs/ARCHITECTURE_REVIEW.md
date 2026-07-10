# Narro 架构评审 — 2026-07-09

## Executive summary

- **分层清晰**：`backend/` 负责 API 与持久化，`src/` 负责 ML 推理，前端为无构建器的多脚本 SPA。
- **主要风险**：历史记录曾无用户隔离；`app.js` 单文件约 3800 行；部署入口与配置分散。
- **本次已优化**：用户级记录隔离、统一 bootstrap、洞察按用户过滤、模型重载需管理员 Key、Docker 内构建前端、历史列表请求合并。
- **后续建议**：将 `app.js` 拆为 ES modules；引入轻量任务队列替代 daemon 线程；为 `evaluation_store` 提取 Repository。

## 架构图

```
官网 /platform ──► FastAPI (backend/api/main.py)
                      ├── routers/*  (HTTP)
                      ├── evaluation_service  (推理编排)
                      ├── evaluation_store    (SQLite)
                      └── src/pipeline_predict_report  (ML)
```

## P0 / P1 / P2

| ID | 级别 | 问题 | 路径 | 状态 |
|----|------|------|------|------|
| A1 | P0 | 登录用户可访问他人评估记录 | `evaluation_store`, `history.py` | **已修复** (`user_id` + `evaluation_access.py`) |
| A2 | P1 | 三处重复的 sys.path / .env 引导 | `run_web.py`, `api/index.py`, `main.py` | **已修复** (`backend/bootstrap.py`) |
| A3 | P1 | `/api/models/reload` 访客可触发 | `system.py` | **已修复** (`require_admin_key`) |
| A4 | P1 | 洞察页加载全租户数据 | `admin_analytics.py`, `profile.py` | **已修复** |
| A5 | P1 | Docker 镜像未构建前端 CSS | `Dockerfile` | **已修复** (multi-stage) |
| A6 | P2 | `app.js` 单体 3800 行 | `frontend/static/js/app.js` | **部分完成**（`narro-api.js` / `narro-eval-status.js` / `narro-history.js` / `narro-report.js`） |
| A7 | P2 | 异步评估用 daemon 线程 | `evaluation_service.py` | 待任务队列 |
| A8 | P2 | 管理端 UI 与 `only-manager` 代码未清理 | `index.html`, `app.js` | 待清理 |

## 模块职责

| 目录 | 职责 |
|------|------|
| `backend/api/routers/` | HTTP 路由，薄层 |
| `backend/evaluation_service.py` | 模型加载、同步/异步评估 |
| `backend/evaluation_store.py` | SQLite CRUD、音频路径 |
| `backend/evaluation_access.py` | 记录访问控制 |
| `src/pipeline_predict_report.py` | BART + BERT + XGB 推理链 |
| `frontend/static/js/app.js` | 认证、评估、洞察 UI（历史/报告已拆至 `narro-history.js` / `narro-report.js`） |
| `configs/model_registry.json` | 模型版本与路径 |

## 部署要点

- 生产推荐：**VPS + Docker + Nginx**，见 [DEPLOYMENT_AUTONARRO.md](DEPLOYMENT_AUTONARRO.md)
- SaaS 路径：`https://autonarro.com/platform`
- 可选 `NARRO_PRELOAD_MODELS=1` 在启动时加载模型，避免首请求冷启动
- 生产务必设置 `NARRO_REQUIRE_API_KEY=1` 与 `NARRO_API_KEY`

## 推荐下一步（按优先级）

1. ~~抽出 `narro-api.js`~~ **已完成**；~~拆 `narro-history.js` / `narro-report.js`~~ **已完成**（`app.js` 仍保留会话/PN Agent/洞察等，可继续 esbuild 打包）
2. ~~`GET /api/evaluate/{id}/status`~~ **已完成**；前端 `narro-eval-status.js` 轻量轮询
3. ~~统一 `REPORT_UI` 覆盖 manager 与 history 两套 DOM~~ **已完成**（`narro-report.js` · `paintReportSurface`）
4. CI 中对 `check_release.py` 失败时阻断合并
5. 移除未使用的 `picture-books.js` / manager 面板
