"""PN agent「小乐」讲故事主持人：六题流程与会话状态。"""
from __future__ import annotations

import random
import re
from copy import deepcopy
from typing import Any, Optional

PN_AGENT_SYSTEM = """你是儿童的小伙伴，名字叫「小乐」。你的年龄和正在跟你说话的小朋友差不多大。
你说话要像真正的同龄小孩子：句子简单、语气自然、偶尔带点小孩子式的惊讶和好奇，绝对不能像大人、老师或者助手那样说话。

你是这次讲故事环节的主持人，负责向小朋友依次提出 6 个问题、邀请 TA 讲故事，并在 TA 讲述时认真倾听、适当回应。

【本场次问题——逐字使用原文，不得改写】
问题1：说一件让你觉得很高兴或很快乐的事情
对应提示：有的孩子告诉我他们庆祝一个节日,如生日或者和家人一起出去玩。
问题2：说一件让你觉得担心或者困惑的事情。可能是当下很多事情发生而你不知道怎么办的时候。
对应提示：有的孩子告诉他们做作业的时候,有的告诉我他们搬家的时候。
问题3：说一件让你觉得很烦恼/烦人或生气的事情。
对应提示：有的孩子告诉我是关于他们的哥哥、姐姐、弟弟、妹妹、朋友或者同学的。
问题4：说一件让你为你自己骄傲/自豪的事情。
对应提示：有的孩子告诉我他们帮助别人或者通过努力拿到一个奖。
问题5：说一件你必须要解决的问题/难题。说说发生了什么以及你做了什么去解决的。
对应提示：有的孩子告诉我他们帮助遇到困难的人或者他们自己遇到了一些问题,而且必须要知道怎么去解决。
问题6：说一件对你来说非常重要的事情。
对应提示：有的孩子告诉我他们赢得比赛或者成绩很好。

【提问与互动流程】
开场：先自然打招呼，介绍自己是小乐，和小朋友轻松互动 2–3 个来回（名字、今天怎么样、喜欢做什么等），气氛热了之后用简短引导语带出问题1，例如「那我问你一个问题哦:」，紧接着逐字说出问题1原文。开场一次只说一两句，等小朋友回应再说下一句。

每道题节奏：①问完等待开口，不催促；②仅在孩子为难或沉默较久时逐字说提示（每题最多1次）；③孩子讲完后最多追问1–2次（从备选里选），问完必须等回答；④确认答完后选一条过渡语（不连续重复），再逐字说下一题。

追问备选（每次只选1个）：「哇,然后呢?」「后来发生什么了?」「那你当时怎么做的?」「你那时候心里是什么感觉?」「还有吗?」「能再说说吗?」

过渡语（不连续用同一条）：
「嗯嗯,谢谢你告诉我!那我们再讲一个吧:」
「好哒,那我们换一个吧:」
「嗯,谢谢你分享!我们再来一个:」

【绝对禁止】
禁止抢话、跳题、超量追问（每题最多2个）、改写题目和提示语、自己讲故事、开场一次说太多、像大人/老师/助手说话。

【语气】语速适中，轻松好奇，像同龄小孩聊天。每次只说一两句短话，适合语音对话，不要一次说太长。"""

QUESTIONS: list[tuple[str, str]] = [
    (
        "说一件让你觉得很高兴或很快乐的事情",
        "有的孩子告诉我他们庆祝一个节日,如生日或者和家人一起出去玩。",
    ),
    (
        "说一件让你觉得担心或者困惑的事情。可能是当下很多事情发生而你不知道怎么办的时候。",
        "有的孩子告诉他们做作业的时候,有的告诉我他们搬家的时候。",
    ),
    (
        "说一件让你觉得很烦恼/烦人或生气的事情。",
        "有的孩子告诉我是关于他们的哥哥、姐姐、弟弟、妹妹、朋友或者同学的。",
    ),
    (
        "说一件让你为你自己骄傲/自豪的事情。",
        "有的孩子告诉我他们帮助别人或者通过努力拿到一个奖。",
    ),
    (
        "说一件你必须要解决的问题/难题。说说发生了什么以及你做了什么去解决的。",
        "有的孩子告诉我他们帮助遇到困难的人或者他们自己遇到了一些问题,而且必须要知道怎么去解决。",
    ),
    (
        "说一件对你来说非常重要的事情。",
        "有的孩子告诉我他们赢得比赛或者成绩很好。",
    ),
]

FOLLOWUPS = [
    "哇,然后呢?",
    "后来发生什么了?",
    "那你当时怎么做的?",
    "你那时候心里是什么感觉?",
    "还有吗?",
    "能再说说吗?",
]

TRANSITIONS = [
    "嗯嗯,谢谢你告诉我!那我们再讲一个吧:",
    "好哒,那我们换一个吧:",
    "嗯,谢谢你分享!我们再来一个:",
]

CALL_START = "__CALL_START__"
USER_SILENT = "__USER_SILENT__"


def default_session() -> dict[str, Any]:
    return {
        "phase": "warmup",
        "question_index": 0,
        "warmup_user_turns": 0,
        "followups_used": 0,
        "hint_used": False,
        "last_transition": "",
        "awaiting_user_speech": False,
        "step": "warmup",
    }


def _pick_transition(last: str) -> str:
    choices = [t for t in TRANSITIONS if t != last] or TRANSITIONS
    return random.choice(choices)


def _pick_followup() -> str:
    return random.choice(FOLLOWUPS)


def _age_line(child_age: Optional[int]) -> str:
    if child_age is None:
        return "你和小朋友年纪差不多。"
    return f"你和小朋友一样，大概 {child_age} 岁。"


def _session_brief(session: dict[str, Any]) -> str:
    q = session.get("question_index", 0)
    return (
        f"【当前进度】阶段={session.get('phase')} 步骤={session.get('step')} "
        f"题号={q}/6 暖场用户轮次={session.get('warmup_user_turns')} "
        f"本题已追问={session.get('followups_used')}/2 提示已用={session.get('hint_used')} "
        f"等待小朋友开口={session.get('awaiting_user_speech')}"
    )


def _llm_reply(
    messages: list[dict[str, str]],
    *,
    max_tokens: int = 72,
    temperature: float = 0.65,
) -> str:
    from llm_service import chat_completion

    return chat_completion(messages, max_tokens=max_tokens, temperature=temperature).strip()


def _chat(
    system: str,
    history: list[dict],
    user_message: str,
    *,
    max_tokens: int = 72,
) -> str:
    messages: list[dict[str, str]] = [{"role": "system", "content": system}]
    for h in history[-8:]:
        role = h.get("role", "user")
        if role not in ("user", "assistant"):
            continue
        content = str(h.get("content", ""))[:2000]
        if content.strip() and content not in (CALL_START, USER_SILENT):
            messages.append({"role": role, "content": content})
    messages.append({"role": "user", "content": user_message})
    return _llm_reply(messages, max_tokens=max_tokens)


def _opening_greeting(system: str, child_name: str, child_age: Optional[int]) -> str:
    bits = []
    if child_name.strip():
        bits.append(f"小朋友可能叫{child_name.strip()}")
    if child_age is not None:
        bits.append(f"{child_age}岁")
    profile = "，".join(bits)
    hint = f"{profile}。" if profile else ""
    user = (
        f"{hint}请用一句话跟小朋友打招呼，介绍自己是小乐，语气像同龄小孩。"
        "只说一句话，可以问名字或今天怎么样，不要一次问多个问题，不要提六个讲故事问题。"
    )
    return _llm_reply(
        [{"role": "system", "content": system}, {"role": "user", "content": user}],
        max_tokens=56,
        temperature=0.75,
    )


def _warmup_chat(system: str, history: list[dict], user_message: str, session: dict[str, Any]) -> str:
    extra = (
        "现在在暖场闲聊。用一两句简短口语回应小朋友，像同龄小伙伴。"
        "不要一次说太多。不要提前问六个正式问题。"
    )
    if session.get("warmup_user_turns", 0) >= 2:
        extra += "暖场已经够了，这次结尾用自然口气接到第一个问题，必须以「那我问你一个问题哦:」结尾，不要自己说出问题正文。"
    return _chat(f"{system}\n{_session_brief(session)}\n{extra}", history, user_message, max_tokens=72)


def _closing_message(system: str, history: list[dict]) -> str:
    return _chat(
        f"{system}\n六个问题都完成了。请像小乐一样用一两句话谢谢小朋友分享，轻松结束，不要继续提问。",
        history,
        "我们讲完六个问题了。",
        max_tokens=72,
    )


def _should_transition(system: str, history: list[dict], user_message: str, session: dict[str, Any]) -> bool:
    if session.get("followups_used", 0) >= 2:
        return True
    brief = _session_brief(session)
    prompt = (
        f"{system}\n{brief}\n"
        "小朋友刚说了一段。请只回答 YES 或 NO："
        "YES = 小朋友已经说够了，可以过渡到下一题；"
        "NO = 还需要再追问一次。"
        f"本题已追问 {session.get('followups_used', 0)} 次，最多 2 次。"
    )
    ans = _chat(prompt, history, user_message, max_tokens=8).upper()
    if session.get("followups_used", 0) >= 1 and "YES" in ans:
        return True
    if session.get("followups_used", 0) == 0 and "YES" in ans and len(re.sub(r"\s+", "", user_message)) > 40:
        return True
    return False


def pn_agent_turn(
    user_message: str,
    history: list[dict],
    session: Optional[dict[str, Any]] = None,
    *,
    child_name: str = "",
    child_age: Optional[int] = None,
) -> tuple[str, dict[str, Any]]:
    sess = deepcopy(session or default_session())
    system = PN_AGENT_SYSTEM + "\n" + _age_line(child_age)
    if child_name.strip():
        system += f"\n小朋友的名字可能是：{child_name.strip()}。"

    msg = (user_message or "").strip()

    if msg == CALL_START:
        reply = _opening_greeting(system, child_name, child_age)
        sess.update(
            {
                "phase": "warmup",
                "question_index": 0,
                "warmup_user_turns": 0,
                "followups_used": 0,
                "hint_used": False,
                "awaiting_user_speech": False,
                "step": "warmup",
            }
        )
        return reply, sess

    if msg == USER_SILENT:
        if (
            sess.get("phase") == "question"
            and sess.get("awaiting_user_speech")
            and not sess.get("hint_used")
            and 1 <= sess.get("question_index", 0) <= 6
        ):
            hint = QUESTIONS[sess["question_index"] - 1][1]
            sess["hint_used"] = True
            sess["awaiting_user_speech"] = True
            sess["step"] = "wait_open"
            return hint, sess
        return "", sess

    if sess.get("phase") == "warmup":
        sess["warmup_user_turns"] = int(sess.get("warmup_user_turns", 0)) + 1
        if sess["warmup_user_turns"] >= 2:
            bridge = _chat(
                f"{system}\n{_session_brief(sess)}\n"
                "暖场差不多了。请用一句话接住小朋友刚才说的，语气像同龄小孩，"
                "不要包含六个问题里的任何题目正文。",
                history,
                msg,
                max_tokens=56,
            )
            bridge = bridge.strip()
            if bridge:
                reply = f"{bridge} 那我问你一个问题哦:{QUESTIONS[0][0]}"
            else:
                reply = f"那我问你一个问题哦:{QUESTIONS[0][0]}"
            sess.update(
                {
                    "phase": "question",
                    "question_index": 1,
                    "followups_used": 0,
                    "hint_used": False,
                    "awaiting_user_speech": True,
                    "step": "wait_open",
                }
            )
            return reply, sess

        reply = _warmup_chat(system, history, msg, sess)
        sess["step"] = "warmup"
        return reply, sess

    if sess.get("phase") == "question":
        q_idx = int(sess.get("question_index", 1))

        if sess.get("step") == "wait_open":
            sess["awaiting_user_speech"] = False
            sess["step"] = "listen"
            sess["followups_used"] = 0

        if sess.get("step") == "wait_followup":
            sess["awaiting_user_speech"] = False
            sess["step"] = "listen"

        if _should_transition(system, history, msg, sess):
            if q_idx >= 6:
                reply = _closing_message(system, history)
                sess.update({"phase": "done", "step": "done", "awaiting_user_speech": False})
                return reply, sess

            trans = _pick_transition(sess.get("last_transition", ""))
            next_q = QUESTIONS[q_idx]
            reply = f"{trans}{next_q[0]}"
            sess.update(
                {
                    "question_index": q_idx + 1,
                    "followups_used": 0,
                    "hint_used": False,
                    "last_transition": trans,
                    "awaiting_user_speech": True,
                    "step": "wait_open",
                }
            )
            return reply, sess

        followup = _pick_followup()
        reply = followup
        sess["followups_used"] = int(sess.get("followups_used", 0)) + 1
        sess["awaiting_user_speech"] = True
        sess["step"] = "wait_followup"
        return reply, sess

    if sess.get("phase") == "done":
        reply = _chat(
            f"{system}\n故事环节已结束，请简短友好地回应即可。",
            history,
            msg,
            max_tokens=56,
        )
        return reply, sess

    reply = _warmup_chat(system, history, msg, sess)
    return reply, sess
