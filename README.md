# Narro — 儿童叙事自动评估（v4）

## 项目结构

```
Narro/
├── frontend/          # 前端（静态页面）
│   ├── index.html
│   └── static/
├── backend/           # 后端 API
│   └── api/main.py
├── src/               # 机器学习与批处理脚本
├── models/            # 训练权重（不提交 git）
├── data/              # 数据与划分缓存（narratives.csv 等）
├── configs/
├── docs/
└── run_web.py         # 启动 Web：http://127.0.0.1:8000
```

详见 [FILES.md](FILES.md)。

## 启动 Web

```bash
# 构建 UI（官网 website/css/site.css；工作台 Tailwind workbench.css + narro.css，共用 narro-tokens.css）
cd frontend && npm install && npm run build && cd ..

source .venv/bin/activate
pip install -r requirements.txt
python run_web.py
```

开发时可在 `frontend/` 下运行 `npm run watch` 自动重编译样式。

- **品牌官网**：http://127.0.0.1:8000/
- **SaaS 工作台**：http://127.0.0.1:8000/app

- **官网 / SaaS**：http://127.0.0.1:8000/ 与 `/app`（生产域名见 [docs/DEPLOYMENT_AUTONARRO.md](docs/DEPLOYMENT_AUTONARRO.md)）
- **默认模型**：`narro_v4`（`configs/model_registry.json`）
- **离线训练**：[docs/TRAINING.md](docs/TRAINING.md)
- **部署**：[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)

### POC 功能（Web）

- **单条评估** + 结果导出（TXT / CSV）
- **批量 CSV**（异步任务 + 前端轮询进度）
- **历史记录**（SQLite，`data/evaluations.db`，含模型版本）
- **关于**页：模型版本、常模规模、免责声明
- **Docker**：`docker compose up --build`
- **黄金样本回归**：`PYTHONPATH=src python scripts/run_golden_regression.py`
- **发布前检查**：`PYTHONPATH=src python scripts/check_release.py`
- **可选鉴权**：`NARRO_API_KEY` + 请求头 `X-API-Key`
- **AI 辅导（DeepSeek）**：见下方配置

### AI 辅导（DeepSeek）

1. 复制 LLM 配置：`cp configs/llm_config.example.json configs/llm_config.json`（若尚未存在）
2. 在 [DeepSeek 开放平台](https://platform.deepseek.com/) 创建 API Key
3. 设置环境变量（二选一）：
   - **推荐**：`cp .env.example .env`，编辑 `.env` 填入 `DEEPSEEK_API_KEY=sk-...`，然后 `python run_web.py`（会自动读取 `.env`）
   - 或当前终端：`export DEEPSEEK_API_KEY="sk-..."` 后再启动
4. 重启 Web 后，访问 http://127.0.0.1:8000/api/llm/status 应显示 `"available": true`
- **训练划分**：默认按 `participant_id` 分组（`NARRO_SPLIT_BY_PARTICIPANT=0` 可恢复按 `story_type` 行级划分）

## 批量 CLI

```bash
cd /path/to/Narro
PYTHONPATH=src python src/pipeline_predict_report.py
```

（需准备根目录或 `data/new_data.csv`）

## 数据

- 训练：`data/narratives.csv`（本地，git 忽略）
- 推理输入模板：`data/sample_new_data_template.csv`
