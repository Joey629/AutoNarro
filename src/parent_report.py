"""面向教师/家长的简短可解释摘要（非诊断）。"""
from __future__ import annotations

from typing import Any, Optional


def generate_parent_summary(
    *,
    age: int,
    regression: dict[str, Any],
    microstructure: dict[str, Any],
    linguistics: Optional[dict[str, Any]] = None,
    peer_macro: Optional[float] = None,
    peer_micro: Optional[float] = None,
    n_peer: int = 0,
    narrative_quality: Optional[dict[str, Any]] = None,
) -> str:
    """根据模型分与专家常模生成 3–5 句通俗说明。"""
    nq = narrative_quality or (linguistics or {}).get("narrative_quality") or {}
    sc = regression.get("pred_SC_Sum")
    micro_sum = microstructure.get("sum")
    lines = [
        "【可读摘要 · 仅供参考，不替代专业评估】",
        f"本次为 {age} 岁儿童叙事自动分析结果。",
    ]

    if nq.get("status") == "insufficient":
        # 质量提示由前端横幅展示，摘要中不再重复同一句
        core = (linguistics or {}).get("core") or {}
        if core.get("TNW") is not None:
            lines.append(
                f"当前仅检测到约 {core.get('TNW')} 个词、{core.get('TNU')} 个句子，"
                "请引导孩子按图卡完整讲述后再评估。"
            )
        lines.append("本次未生成宏观 SC 与宏观 SS（故事结构）分数。")
        return "\n".join(lines)

    # low_quality / sc_capped：提示语仅出现在前端质量横幅，摘要不再重复

    if sc is not None and peer_macro is not None and n_peer > 0:
        if sc > peer_macro:
            lines.append(
                f"宏观 SC（情节完整性，pred_SC_Sum）约为 {sc:.1f} 分，高于同龄同组专家常模均值（{peer_macro:.1f}，n={n_peer}），"
                "说明情节组织相对更完整。"
            )
        else:
            lines.append(
                f"宏观 SC（情节完整性）约为 {sc:.1f} 分，低于或接近同龄常模（{peer_macro:.1f}，n={n_peer}），"
                "可在讲述顺序、因果衔接上继续练习。"
            )
    elif sc is not None:
        beta = "（beta，模型校准中）" if regression.get("pred_SC_Sum_beta") else ""
        lines.append(f"宏观 SC（情节完整性）约为 {sc:.1f} 分{beta}。")

    if micro_sum is not None:
        if peer_micro is not None and n_peer > 0:
            cmp = "高于" if micro_sum > peer_micro else "低于或接近"
            lines.append(
                f"宏观 SS（故事结构 A2–A16）达标 {micro_sum}/15 项，{cmp}同龄专家常模（{peer_micro:.1f}/15）。"
            )
        else:
            lines.append(f"宏观 SS（故事结构）达标 {micro_sum}/15 项（如角色、因果、结局等）。")

    core = (linguistics or {}).get("core") or {}
    if core.get("TNW"):
        lines.append(
            f"语言产出：约 {core.get('TNW')} 个词、{core.get('TNU')} 个句子，"
            f"平均句长约 {core.get('MLU', '—')} 词/句（Jieba 自动统计）。"
        )

    failed = [
        t["id"]
        for t in (microstructure.get("tasks") or [])
        if not t.get("value")
    ]
    if failed and len(failed) <= 6:
        lines.append(f"可重点关注尚未达标的要素：{', '.join(failed)}。")
    elif failed:
        lines.append(f"尚有 {len(failed)} 项故事结构（SS）要素未达标，详见下方列表。")

    lines.append("建议结合录音与课堂观察综合判断；必要时由专业人员复核。")
    return "\n".join(lines)
