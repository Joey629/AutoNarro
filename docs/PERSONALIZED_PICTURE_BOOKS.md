# 专属练习绘本

## 能力

- 汇总同一 `child_id` 下 **≥2 次**已完成评估（宏观 SS/SC、TNW、未达标 A2–A16）
- 调用 **DeepSeek**（`DEEPSEEK_API_KEY`）生成原创绘本 JSON（标题、分页旁白、练习重点）
- **插画**：从 `allowed_scene_keys` 映射到 `frontend/static/picturebooks/scenes/*.svg`（程序生成，非文生图）

## DeepSeek 能否生成图像？

**目前不能。** DeepSeek 开放 API 以文本对话为主，不提供 DALL·E 类文生图。本产品：

| 环节 | 技术 |
|------|------|
| 故事与分页文案 | DeepSeek |
| 分镜场景选择 | DeepSeek 输出 `scene_key` |
| 页面配图 | 内置 12 种场景 SVG |

若未来接入图像 API（通义万相、Stable Diffusion 等），可在 `personalized_picture_book_service._attach_images` 扩展。

## API

- `GET /api/personalized-picture-books/status?child_id=`
- `GET /api/personalized-picture-books?child_id=`
- `GET /api/personalized-picture-books/{id}`
- `POST /api/personalized-picture-books/generate` — body: `{ "child_id", "child_name?", "evaluation_ids?": [] }`

## 配置

- `configs/personalized_picture_book.json` — 最少评估次数、SS 中文标签、允许的场景 key
- `configs/llm_config.json` + `.env` 中 `DEEPSEEK_API_KEY`

## 前端

侧栏 **专属绘本** → `panel-learning-courses`，脚本 `personalized-books.js`。

## 维护

```bash
python scripts/generate_personalized_scenes.py
```
