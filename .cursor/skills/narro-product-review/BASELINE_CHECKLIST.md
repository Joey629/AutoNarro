# Narro Top-10 行动项 — 评审基线清单

> 来源：2026-05 三域深度评审汇总。修复后请将 `baseline-status.json` 中对应项标为 `done` 并注明 PR/日期。

## 如何使用

1. 跑评审前：复制本表到报告中的「Status vs baseline」列  
2. 修复后：更新 `baseline-status.json`  
3. 回归：pytest + golden + 手动 UX 走查（见 SKILL.md）

---

## Top 10

| # | 行动项 | 验收标准 | 关键路径 |
|---|--------|----------|----------|
| 1 | 身份 + 租户 + 角色分离 | `tenant_id` 落库且查询过滤；`/api/admin/*` 使用 `NARRO_ADMIN_API_KEY` | `backend/tenant.py`, `evaluation_store.py`, `auth.py`, `api/routers/admin.py` |
| 2 | 推理串行化 + 去掉双 BART | `_infer_lock`；`predict(..., predicted_ist_words=)` | `evaluation_service.py`, `pipeline_predict_report.py` |
| 3 | 鉴权 fail-closed + Docker 秘密隔离 | `NARRO_REQUIRE_API_KEY=1` 无 key 时 503；`.dockerignore` 含 `.env`、语料 CSV | `auth.py`, `.dockerignore` |
| 4 | 修复 XSS + 统一 escape | 用户文本不进未转义 `innerHTML`；单一 `NarroUI.escapeHtml` | `narro-ui.js`, `app.js` |
| 5 | 可见讲述指引 + caption | `#storyInstruction` 可见；`#storyPanelCaption` 展示 | `index.html`, `app.js`, `narro.css` |
| 6 | 移动端 responsive | ≤767px 侧栏抽屉；Narro 对话全屏 | `narro.css`, `index.html`, `app.js` |
| 7 | Profile gate + 家长向结果分层 | 评估前 dialog；专业详情 `<details>` 折叠 | `app.js`, `index.html` |
| 8 | pytest + CI golden | `tests/`；`.github/workflows/ci.yml` | `tests/test_*.py` |
| 9 | 拆分 main / app / predictor | FastAPI routers；`src/inference/`；`narro-ui.js` | `backend/api/routers/`, `src/inference/` |
| 10 | 替换 alert、dialog a11y、加载分阶段 | `openNarroAlert`；focus trap；评估 loading 文案阶段 | `app.js` |

---

## 合并 P0（跨域）

| ID | 描述 | 基线状态字段 |
|----|------|----------------|
| P0-TENANT | 评估数据按 `NARRO_TENANT_ID` 隔离 | `top10.1` |
| P0-AUTH | API 默认 fail-closed（可配置） | `top10.3` |
| P0-INFER | 推理线程安全 | `top10.2` |
| P0-DOCKER | 镜像不含 secrets/语料 | `top10.3` |
| P0-XSS | 教练/管理表格无存储型 XSS | `top10.4` |
| P0-UX-GUIDE | 讲述指引可见 | `top10.5` |
| P0-UX-MOBILE | 手机可完成主流程 | `top10.6` |
| P0-PROFILE | 评估前 profile 提示 | `top10.7` |

---

## 合并 P1（节选）

- 批量 CSV 大小/行数上限 → `job_worker.py` `MAX_BATCH_*`
- LLM history 仅允许 user/assistant → `llm_service.py`
- CORS 可配置 `NARRO_CORS_ORIGINS` → `api/main.py`
- Expert override 字段白名单 → `api/routers/history.py`
- 导出带 API Key → `narro-ui.js` `downloadWithAuth`
- `backfill_record_labels` 不在每次 list 调用 → `maybe_backfill_record_labels`

---

## 手动回归清单（UX）

- [ ] 叙事评估：选故事 → 看图 → 讲述 → 评估 → 自动进「我的记录」  
- [ ] 个人信息保存后评估使用档案年龄/姓名  
- [ ] 侧栏展开/收起：三项图标间距一致  
- [ ] 手机宽度：汉堡菜单打开侧栏、关闭遮罩  
- [ ] 历史详情：专业详情默认折叠，可展开  
- [ ] 配置 `NARRO_API_KEY` 后导出 TXT/CSV 成功  
