"""DeepSeek / OpenAI 兼容 API：评估后辅导与自由对话。"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Optional

from logging_config import setup_logging

logger = setup_logging()
CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "llm_config.json"
EXAMPLE_PATH = Path(__file__).resolve().parents[1] / "configs" / "llm_config.example.json"


def load_llm_config() -> dict:
    path = CONFIG_PATH if CONFIG_PATH.is_file() else EXAMPLE_PATH
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def is_llm_available() -> bool:
    cfg = load_llm_config()
    key_env = cfg.get("api_key_env", "DEEPSEEK_API_KEY")
    return bool(os.environ.get(key_env) or os.environ.get("DEEPSEEK_API_KEY"))


def _build_evaluation_context(row: dict) -> str:
    reg = row.get("regression") or {}
    micro = row.get("microstructure") or {}
    ling = row.get("linguistics") or {}
    core = ling.get("core") or {}
    failed = [t["id"] for t in micro.get("tasks", []) if not t.get("value")]
    return (
        f"儿童：{row.get('child_name') or row.get('child_id') or '未填'}，年龄 {row.get('age')} 岁\n"
        f"故事类型：{row.get('story_type')}，任务：{row.get('task_type')}\n"
        f"模型宏观 SC（pred_SC_Sum）：{reg.get('pred_SC_Sum')}；宏观 SS 达标 {micro.get('sum')}/15\n"
        f"语言产出 TNW={core.get('TNW')} TNU={core.get('TNU')} MLU={core.get('MLU')}\n"
        f"未达标 SS 项（A2–A16）：{', '.join(failed) if failed else '无'}\n"
        f"可读摘要：\n{row.get('parent_summary') or ''}\n"
    )


def chat_completion(
    messages: list[dict[str, str]],
    *,
    max_tokens: Optional[int] = None,
    temperature: Optional[float] = None,
) -> str:
    cfg = load_llm_config()
    key_env = cfg.get("api_key_env", "DEEPSEEK_API_KEY")
    api_key = os.environ.get(key_env) or os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError(
            "未配置 LLM：请设置环境变量 DEEPSEEK_API_KEY，并复制 configs/llm_config.example.json → llm_config.json"
        )

    base = os.environ.get("DEEPSEEK_BASE_URL") or cfg.get("base_url", "https://api.deepseek.com")
    model = cfg.get("model", "deepseek-chat")
    url = f"{base.rstrip('/')}/v1/chat/completions"

    body = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens or cfg.get("max_tokens", 1024),
        "temperature": temperature if temperature is not None else cfg.get("temperature", 0.4),
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        logger.error("LLM HTTP %s: %s", e.code, err[:500])
        raise RuntimeError(_friendly_llm_error(e.code, err)) from e


def _friendly_llm_error(status: int, raw: str) -> str:
    """将 DeepSeek/OpenAI 兼容 API 的 HTTP 错误转为可读中文。"""
    msg = ""
    try:
        payload = json.loads(raw)
        err = payload.get("error") or {}
        if isinstance(err, dict):
            msg = (err.get("message") or "").strip()
        elif isinstance(err, str):
            msg = err.strip()
    except json.JSONDecodeError:
        msg = raw.strip()[:200]

    if status == 402 or "insufficient balance" in msg.lower():
        return (
            "DeepSeek 账户余额不足（402）。API Key 已生效，但账户没有可用额度。"
            "请登录 https://platform.deepseek.com 充值或检查账单后重试。"
        )
    if status == 401:
        return "DeepSeek API Key 无效或已过期（401）。请检查 .env 中的 DEEPSEEK_API_KEY 是否正确。"
    if status == 429:
        return "DeepSeek 请求过于频繁（429），请稍后再试。"
    if msg:
        return f"LLM 请求失败 ({status})：{msg}"
    return f"LLM 请求失败 ({status})"


def coach_after_evaluation(row: dict, user_question: str = "") -> str:
    cfg = load_llm_config()
    system = cfg.get("system_prompt", "你是儿童叙事辅导助手，非诊断。")
    ctx = _build_evaluation_context(row)
    user_msg = user_question.strip() or (
        "请根据以上自动评估结果，用教师和家长能听懂的语言，给出3-5条具体的改善建议与家庭练习方法。"
    )
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": f"【评估结果】\n{ctx}\n\n【问题】\n{user_msg}"},
    ]
    return chat_completion(messages)


def free_chat(evaluation_row: Optional[dict], user_message: str, history: list[dict]) -> str:
    cfg = load_llm_config()
    system = cfg.get("system_prompt", "你是儿童叙事辅导助手。")
    messages: list[dict[str, str]] = [{"role": "system", "content": system}]
    if evaluation_row:
        messages.append(
            {
                "role": "user",
                "content": f"【当前评估上下文】\n{_build_evaluation_context(evaluation_row)}",
            }
        )
        messages.append({"role": "assistant", "content": "已了解该儿童的评估结果，请提问。"})
    for h in history[-10:]:
        role = h.get("role", "user")
        if role not in ("user", "assistant"):
            continue
        content = str(h.get("content", ""))[:4000]
        if content.strip():
            messages.append({"role": role, "content": content})
    messages.append({"role": "user", "content": user_message})
    return chat_completion(messages)
