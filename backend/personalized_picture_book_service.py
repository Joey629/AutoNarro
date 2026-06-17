"""基于多次评估结果 + DeepSeek 生成专属练习绘本（文本）；插画用场景 SVG。"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Optional

from evaluation_store import get_evaluation, list_evaluations
from logging_config import setup_logging
from personalized_picture_book_store import get_book, insert_book, list_books

logger = setup_logging()
CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "personalized_picture_book.json"


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.is_file():
        return {}
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def _ss_labels() -> dict[str, str]:
    return load_config().get("ss_labels") or {f"A{i}": f"A{i}" for i in range(2, 17)}


def _allowed_scenes() -> list[str]:
    cfg = load_config()
    return list(cfg.get("allowed_scene_keys") or [])


def _scene_image_url(scene_key: str) -> str:
    key = (scene_key or "sunny_park").strip()
    allowed = _allowed_scenes()
    if allowed and key not in allowed:
        key = allowed[0]
    return f"/static/picturebooks/scenes/{key}.svg"


def load_completed_evaluations(
    child_id: str,
    *,
    evaluation_ids: Optional[list[int]] = None,
    limit: int = 20,
) -> list[dict[str, Any]]:
    cid = (child_id or "").strip()
    if not cid:
        return []

    if evaluation_ids:
        out = []
        for eid in evaluation_ids:
            row = get_evaluation(int(eid))
            if row and (row.get("status") or "completed") == "completed":
                if (row.get("child_id") or "").strip() == cid:
                    out.append(row)
        return sorted(out, key=lambda r: r.get("id") or 0, reverse=True)

    items = list_evaluations(limit=limit, child_id=cid)
    out = []
    for it in items:
        if (it.get("status") or "completed") != "completed":
            continue
        full = get_evaluation(int(it["id"]))
        if full:
            out.append(full)
    return out


def build_aggregate_profile(evaluations: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总多次评估 → 练习画像。"""
    cfg = load_config()
    labels = _ss_labels()
    failed_counts: Counter[str] = Counter()
    sc_vals: list[float] = []
    micro_vals: list[int] = []
    tnw_vals: list[float] = []
    eval_summaries: list[dict[str, Any]] = []

    n = len(evaluations)
    for rank, ev in enumerate(evaluations):
        weight = 1.0 + (n - 1 - rank) * 0.15
        micro = ev.get("microstructure") or {}
        reg = ev.get("regression") or {}
        ling = ev.get("linguistics") or {}
        core = ling.get("core") or {}

        if reg.get("pred_SC_Sum") is not None:
            try:
                sc_vals.append(float(reg["pred_SC_Sum"]))
            except (TypeError, ValueError):
                pass
        if micro.get("sum") is not None:
            try:
                micro_vals.append(int(micro["sum"]))
            except (TypeError, ValueError):
                pass
        if core.get("TNW") is not None:
            try:
                tnw_vals.append(float(core["TNW"]))
            except (TypeError, ValueError):
                pass

        failed = []
        for t in micro.get("tasks") or []:
            tid = t.get("id")
            if tid and not t.get("value"):
                failed_counts[str(tid)] += weight
                failed.append(str(tid))

        eval_summaries.append(
            {
                "evaluation_id": ev.get("id"),
                "created_at": ev.get("created_at"),
                "story_type": ev.get("story_type"),
                "pred_SC_Sum": reg.get("pred_SC_Sum"),
                "micro_sum": micro.get("sum"),
                "TNW": core.get("TNW"),
                "MLU": core.get("MLU"),
                "failed_ss": failed,
            }
        )

    focus_ids = [t for t, _ in failed_counts.most_common(3)]
    focus_labeled = [
        {"id": fid, "label": labels.get(fid, fid), "miss_count_weighted": round(failed_counts[fid], 2)}
        for fid in focus_ids
    ]

    age = evaluations[0].get("age") if evaluations else 5
    try:
        age = int(age)
    except (TypeError, ValueError):
        age = 5

    return {
        "evaluation_count": n,
        "child_name": (evaluations[0].get("child_name") or "").strip() if evaluations else "",
        "age": age,
        "focus_skills": focus_labeled,
        "focus_skill_ids": focus_ids,
        "avg_pred_SC_Sum": round(sum(sc_vals) / len(sc_vals), 2) if sc_vals else None,
        "avg_micro_sum": round(sum(micro_vals) / len(micro_vals), 1) if micro_vals else None,
        "avg_TNW": round(sum(tnw_vals) / len(tnw_vals), 1) if tnw_vals else None,
        "evaluations": eval_summaries,
    }


def _profile_for_llm(profile: dict[str, Any]) -> str:
    lines = [
        f"评估次数：{profile.get('evaluation_count')}",
        f"儿童年龄：{profile.get('age')} 岁",
        f"宏观 SC 均值：{profile.get('avg_pred_SC_Sum')}",
        f"宏观 SS 均值：{profile.get('avg_micro_sum')}/15",
        f"TNW 均值：{profile.get('avg_TNW')}",
        "建议重点练习的故事结构要素：",
    ]
    for f in profile.get("focus_skills") or []:
        lines.append(f"  - {f.get('id')} {f.get('label')}（多次未达标权重 {f.get('miss_count_weighted')}）")
    lines.append("\n各次评估摘要：")
    for e in profile.get("evaluations") or []:
        lines.append(
            f"  #{e.get('evaluation_id')} SC={e.get('pred_SC_Sum')} SS={e.get('micro_sum')}/15 "
            f"TNW={e.get('TNW')} 未达标={','.join(e.get('failed_ss') or []) or '无'}"
        )
    return "\n".join(lines)


def parse_llm_json(text: str) -> dict[str, Any]:
    raw = (text or "").strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", raw)
    if fence:
        raw = fence.group(1).strip()
    return json.loads(raw)


def _attach_images(book: dict[str, Any]) -> dict[str, Any]:
    pages = book.get("pages") or []
    for p in pages:
        sk = (p.get("scene_key") or "sunny_park").strip()
        p["image"] = _scene_image_url(sk)
    book["pages"] = pages
    return book


def generate_book_with_llm(profile: dict[str, Any]) -> dict[str, Any]:
    from llm_service import chat_completion, is_llm_available

    if not is_llm_available():
        raise RuntimeError("未配置 DeepSeek：请设置 DEEPSEEK_API_KEY 并配置 configs/llm_config.json")

    cfg = load_config()
    llm_cfg = cfg.get("llm") or {}
    labels = _ss_labels()
    scenes = _allowed_scenes()
    page_min = (cfg.get("page_count") or {}).get("min", 4)
    page_max = (cfg.get("page_count") or {}).get("max", 6)
    focus = profile.get("focus_skill_ids") or ["A13"]
    focus_desc = "、".join(f"{fid}({labels.get(fid, fid)})" for fid in focus[:3])

    system = (
        "你是儿童绘本编剧，为 4–7 岁孩子写「语言练习绘本」。\n"
        "硬规则：\n"
        "1) 只输出一个 JSON 对象，不要 markdown 说明；\n"
        "2) 故事必须全新原创，禁止小猫追蝴蝶、小狗香肠、小鸟小猫、小羊狐狸等 MAIN 测评故事情节；\n"
        "3) 非诊断、不说教；句子短、适合亲子朗读；\n"
        f"4) 全书 {page_min}–{page_max} 页，每页 caption 一句或两句（≤40 字）；\n"
        f"5) 每页 scene_key 只能从列表中选：{json.dumps(scenes, ensure_ascii=False)}；\n"
        f"6) 重点在故事中自然体现：{focus_desc}。\n"
        "JSON 格式：\n"
        '{"title":"","subtitle":"","target_skills":[],"parent_tip":"","pages":[{"caption":"","scene_key":"","skill_hint":""}]}'
    )
    user = (
        "根据以下多次自动评估汇总的练习画像，生成一本专属练习绘本。\n\n"
        f"{_profile_for_llm(profile)}\n\n"
        "请生成 JSON。"
    )
    out = chat_completion(
        [{"role": "system", "content": system}, {"role": "user", "content": user}],
        max_tokens=int(llm_cfg.get("max_tokens", 2048)),
        temperature=float(llm_cfg.get("temperature", 0.55)),
    )
    book = parse_llm_json(out)
    if not book.get("pages"):
        raise RuntimeError("LLM 未返回有效 pages")
    book.setdefault("target_skills", profile.get("focus_skill_ids") or [])
    book.setdefault("title", "专属练习绘本")
    return _attach_images(book)


def generate_for_child(
    *,
    child_id: str,
    child_name: str = "",
    evaluation_ids: Optional[list[int]] = None,
) -> dict[str, Any]:
    cfg = load_config()
    min_evals = int(cfg.get("min_evaluations", 2))
    max_ctx = int(cfg.get("max_evaluations_in_context", 8))

    cid = (child_id or "").strip()
    if not cid:
        raise ValueError("请先在「个人信息」填写儿童 ID，并在评估时使用同一 ID")

    evals = load_completed_evaluations(cid, evaluation_ids=evaluation_ids, limit=max_ctx)
    if len(evals) < min_evals:
        raise ValueError(
            f"需要至少 {min_evals} 次已完成的评估（当前 {len(evals)} 次）。"
            "请先在「讲故事」完成多次讲述并确保儿童 ID 一致。"
        )

    profile = build_aggregate_profile(evals)
    if child_name:
        profile["child_name"] = child_name.strip()

    book = generate_book_with_llm(profile)
    eids = [int(e["id"]) for e in evals if e.get("id") is not None]

    book_id = insert_book(
        child_id=cid,
        child_name=profile.get("child_name") or child_name,
        age=int(profile.get("age") or 5),
        evaluation_ids=eids,
        title=str(book.get("title") or "专属练习绘本"),
        target_skills=list(book.get("target_skills") or profile.get("focus_skill_ids") or []),
        book=book,
        profile=profile,
    )
    saved = get_book(book_id)
    if not saved:
        raise RuntimeError("绘本保存失败")
    return saved


def get_child_generation_status(child_id: str) -> dict[str, Any]:
    cfg = load_config()
    min_evals = int(cfg.get("min_evaluations", 2))
    evals = load_completed_evaluations((child_id or "").strip(), limit=20)
    books = list_books(child_id=child_id, limit=10)
    return {
        "child_id": (child_id or "").strip(),
        "completed_evaluations": len(evals),
        "min_evaluations_required": min_evals,
        "can_generate": len(evals) >= min_evals,
        "llm_available": _llm_available(),
        "image_mode": "scene_svg",
        "image_note": cfg.get("image_note", ""),
        "books": books,
    }


def _llm_available() -> bool:
    try:
        from llm_service import is_llm_available

        return is_llm_available()
    except Exception:
        return False
