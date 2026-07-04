"""讲故事页 AI 引导：脚本 + 可选 LLM 润色。"""
from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any, Optional

PROMPTS_PATH = Path(__file__).resolve().parents[1] / "configs" / "story_coach_prompts.json"


def _load_prompts() -> dict[str, Any]:
    if not PROMPTS_PATH.is_file():
        return {}
    return json.loads(PROMPTS_PATH.read_text(encoding="utf-8"))


def _template(key: str, **kwargs: str) -> str:
    p = _load_prompts()
    tpl = p.get(key, "")
    try:
        return tpl.format(**kwargs)
    except KeyError:
        return tpl


def coach_message_script(
    *,
    phase: str,
    panel_index: int = 0,
    panel_total: int = 6,
    caption: str = "",
    child_utterance: str = "",
) -> str:
    """无 LLM 时的固定话术。"""
    p = _load_prompts()
    if phase == "warmup_greet":
        return p.get("warmup_greet", "嗨！我是小乐！准备好一起讲故事了吗？")
    if phase == "warmup_reply":
        return p.get("warmup_reply", "太好了！那我们开始看图片吧。")
    if phase == "warmup_to_story":
        return p.get("warmup_to_story", "好，来看第一张图！")
    if phase == "panel_greet":
        if panel_index == 0:
            return p.get(
                "panel_greet_first",
                p.get("intro", "嗨！我是小乐！看这张图，你看到什么就讲给我听吧。"),
            )
        if panel_total > 0 and panel_index >= panel_total - 1:
            return p.get(
                "panel_greet_last",
                p.get("finish", "最后一张啦，讲完请家长点「开始评估」。"),
            )
        return p.get(
            "panel_greet_next",
            p.get("panel_transition", "好，看下一张。你看到什么？"),
        )
    if phase == "intro":
        return p.get("intro", "你好，我们一起讲故事吧。")
    if phase == "panel_open":
        return _template(
            "panel_open",
            panel=str(panel_index + 1),
            total=str(panel_total),
        )
    if phase == "panel_ask":
        return p.get("panel_ask", "你能说说这张图吗？")
    if phase in ("listen_nudge", "warmup_nudge"):
        key = "warmup_nudge" if phase == "warmup_nudge" else "listen_nudge"
        return p.get(key, "我没听到声音，你可以再说一次吗？")
    if phase == "followup":
        if child_utterance and len(child_utterance.strip()) < 12:
            enc = p.get("encourage") or []
            return random.choice(enc) if enc else p.get("panel_followup", "还有呢？")
        return p.get("panel_followup", "还有呢？")
    if phase == "transition":
        return p.get("panel_transition", "我们看下一张。")
    if phase == "finish":
        return p.get("finish", "讲完了可以点完成评估。")
    if phase == "panel_tap":
        return p.get("panel_tap", p.get("panel_ask", "看看这张图～"))
    if phase == "peek_wake":
        return p.get("peek_wake", "我来啦！")
    return p.get("panel_ask", "请讲讲这张图。")


def coach_message_llm(
    *,
    phase: str,
    story_label: str,
    panel_index: int,
    panel_total: int,
    caption: str,
    child_utterance: str,
    history: list[dict],
) -> Optional[str]:
    from llm_service import chat_completion, is_llm_available

    if not is_llm_available():
        return None
    script = coach_message_script(
        phase=phase,
        panel_index=panel_index,
        panel_total=panel_total,
        caption=caption,
        child_utterance=child_utterance,
    )
    phase_hint = {
        "warmup_greet": "开场：像邻居小朋友一样打招呼，问名字或是否准备好（勿提图片）。",
        "warmup_reply": "孩子刚回应了，热情接一句，邀请一起看图讲（勿描述图片）。",
        "warmup_nudge": "好久没听到孩子说话，温柔提醒对着麦克风说句话（勿批评）。",
        "warmup_to_story": "一句过渡到看图，语气兴奋简短。",
        "panel_greet": "本页只说一句：邀请看当前图自己讲（勿描述画面；末图可提醒家长点评估）。",
        "followup": "孩子刚说了话：先简短附和其内容关键词（不复述画面），再开放式追问一句。",
        "listen_nudge": "几秒没听到孩子说话：温柔提醒再讲一次或大声一点，不要批评。",
    }.get(phase, f"阶段：{phase}。")
    system = (
        "你是小乐，和 4–8 岁孩子差不多大的语音小伙伴。语气像同龄小孩："
        "短句、口语、自然、好奇，每次 1–2 句，不超过 32 字。\n"
        "硬规则：绝不描述、暗示或提问图片里的具体情节/人物/动物/动作/物体"
        "（禁止：小猫、蝴蝶、跳、树、男孩等画面词）。\n"
        "硬规则：不要诊断、不要分数、不要批评孩子。\n"
        "避免连续两次用完全相同的话；少用「还有呢」；可以换用「然后呢」「接着说」「你看到了什么呀」。\n"
        "示例（风格参考，勿照抄）：\n"
        "孩子：我看见了。你：嗯嗯，看见什么啦？\n"
        "孩子：（沉默）你：我在这儿呢，你对着麦克风讲给我听吧。"
    )
    user = (
        f"故事任务：{story_label}。当前第 {panel_index + 1}/{panel_total} 张图（勿描述画面）。\n"
        f"{phase_hint}\n"
        f"孩子刚才说：{child_utterance or '（还没说）'}\n"
        f"参考语气（勿照搬字面，尤其勿含画面词）：{script}\n"
        "请生成你对孩子说的话（仅输出要说的话，无引号）。"
    )
    messages: list[dict[str, str]] = [{"role": "system", "content": system}]
    for h in (history or [])[-8:]:
        role = h.get("role", "assistant")
        if role not in ("user", "assistant"):
            continue
        c = str(h.get("content", ""))[:500]
        if c.strip():
            messages.append({"role": role, "content": c})
    messages.append({"role": "user", "content": user})
    try:
        temp = 0.88 if phase in ("followup", "listen_nudge", "warmup_nudge", "warmup_reply") else 0.82
        out = chat_completion(messages, max_tokens=100, temperature=temp)
        return (out or script).strip()[:200]
    except Exception:
        return None


def guide_child(
    *,
    phase: str,
    story_type: str,
    story_label: str,
    panel_index: int,
    panel_total: int,
    caption: str = "",
    child_utterance: str = "",
    history: list[dict] | None = None,
    use_llm: bool = True,
) -> dict[str, Any]:
    msg = None
    llm_used = False
    if use_llm:
        msg = coach_message_llm(
            phase=phase,
            story_label=story_label,
            panel_index=panel_index,
            panel_total=panel_total,
            caption=caption,
            child_utterance=child_utterance,
            history=history or [],
        )
        llm_used = msg is not None
    if not msg:
        msg = coach_message_script(
            phase=phase,
            panel_index=panel_index,
            panel_total=panel_total,
            caption=caption,
            child_utterance=child_utterance,
        )
    return {
        "message": msg,
        "pet_name": _load_prompts().get("pet_name", "小乐"),
        "phase": phase,
        "story_type": story_type,
        "llm_used": llm_used,
    }
