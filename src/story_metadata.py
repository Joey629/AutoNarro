"""从叙事正文推断故事主题，并按语料规则绑定任务类型。"""
from __future__ import annotations

from typing import Literal, Optional

StoryType = Literal["cat", "dog", "bird", "goat"]
TaskType = Literal["Telling", "Retelling"]

STORY_LABELS = {
    "cat": "小猫与蝴蝶",
    "dog": "小狗与香肠",
    "bird": "小鸟一家",
    "goat": "小羊与狐狸",
}

# 常模语料：猫/狗仅复述，鸟/羊仅讲述
TASK_BY_STORY: dict[str, TaskType] = {
    "cat": "Retelling",
    "dog": "Retelling",
    "bird": "Telling",
    "goat": "Telling",
}

# (关键词, 权重) — 针对儿童叙事四则寓言调优
_STORY_KEYWORD_WEIGHTS: dict[str, list[tuple[str, float]]] = {
    "cat": [("蝴蝶", 4), ("黄蝴蝶", 3), ("小猫", 2), ("鱼桶", 2), ("鱼钩", 2)],
    "dog": [("香肠", 4), ("气球", 3), ("老鼠", 2), ("灰老鼠", 3), ("小狗", 2)],
    "bird": [("鸟妈妈", 5), ("小鸟", 4), ("鸟爸", 4), ("虫子", 2), ("鸭妈妈", 4), ("鸭子", 3)],
    "goat": [("狐狸", 4), ("小羊", 3), ("大灰狼", 3), ("吃草", 2), ("乌鸦", 3), ("鹦鹉", 3)],
}


def task_type_for_story(story_type: str) -> TaskType:
    st = str(story_type).strip().lower()
    if st not in TASK_BY_STORY:
        raise ValueError(f"未知 story_type: {story_type}")
    return TASK_BY_STORY[st]


def detect_story_type(text: str) -> tuple[StoryType, float, dict[str, float]]:
    """
    基于关键词加权投票推断故事主题。
    返回 (story_type, confidence, raw_scores)。
    """
    t = (text or "").strip()
    if len(t) < 5:
        raise ValueError("叙事文本过短，无法识别故事主题")

    scores: dict[str, float] = {k: 0.0 for k in _STORY_KEYWORD_WEIGHTS}
    for st, pairs in _STORY_KEYWORD_WEIGHTS.items():
        for kw, w in pairs:
            if kw in t:
                scores[st] += w

    # 鸟/羊故事中常出现「小猫」等干扰词，降权猫分
    if scores["bird"] >= 4 and scores["cat"] <= 6:
        scores["cat"] *= 0.5
    if scores["goat"] >= 6 and scores["bird"] < 4:
        scores["bird"] *= 0.7

    total = sum(scores.values())
    if total <= 0:
        return "cat", 0.0, scores

    best = max(scores, key=scores.get)  # type: ignore[arg-type]
    confidence = scores[best] / total
    return best, round(confidence, 4), scores  # type: ignore[return-value]


def resolve_story_and_task(
    text: str,
    story_type: Optional[str] = None,
    task_type: Optional[str] = None,
) -> tuple[str, str, float, bool, bool]:
    """
    解析最终 story_type / task_type。
    返回 (story_type, task_type, detection_confidence, story_inferred, task_inferred)。
    """
    story_inferred = not story_type
    if story_type:
        st = str(story_type).strip().lower()
        if st not in TASK_BY_STORY:
            raise ValueError(f"未知 story_type: {story_type}")
        conf = 1.0
    else:
        st, conf, _ = detect_story_type(text)

    task_inferred = not task_type
    if task_type:
        tt = str(task_type).strip()
        if tt not in ("Telling", "Retelling"):
            raise ValueError(f"未知 task_type: {task_type}")
        expected = task_type_for_story(st)
        if tt != expected:
            tt = expected
            task_inferred = True
    else:
        tt = task_type_for_story(st)

    return st, tt, conf, story_inferred, task_inferred
