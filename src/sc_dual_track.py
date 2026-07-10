"""
宏观 SC 双轨预测：A 轨 MAIN（含 SS 概率）与 B 轨直接 SC（不含 SS）。
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Optional

import joblib
import numpy as np

import micro_encoder as rfe

SC_EPISODES = ("SC_E1", "SC_E2", "SC_E3")
REVIEW_DELTA_SUM = 2
REVIEW_DELTA_EPISODE = 2


def clip_episode_score(v: float) -> int:
    return int(np.clip(int(np.round(v)), 0, 3))


def _predict_one(model, X: np.ndarray) -> float:
    """回归或四分类 XGB，输出 0–3 情节分。"""
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)
        return float(np.argmax(proba, axis=1)[0])
    raw = float(model.predict(X)[0])
    return float(clip_episode_score(raw))


@dataclass
class ScDualModels:
    """已加载的 SC 模型包。"""

    main: dict[str, Any] = field(default_factory=dict)
    direct: dict[str, Any] = field(default_factory=dict)
    legacy: dict[str, Any] = field(default_factory=dict)
    main_kind: str = "none"  # classifier | regression
    direct_kind: str = "none"
    legacy_kind: str = "none"

    @property
    def has_main(self) -> bool:
        return all(k in self.main for k in SC_EPISODES)

    @property
    def has_direct(self) -> bool:
        return all(k in self.direct for k in SC_EPISODES)

    @property
    def has_legacy(self) -> bool:
        return all(k in self.legacy for k in SC_EPISODES)


def _load_episode_models(model_dir: str, prefix: str) -> tuple[dict[str, Any], str]:
    """尝试 classifier → regression 命名。"""
    out: dict[str, Any] = {}
    for ep in SC_EPISODES:
        for name in (
            f"{prefix}_{ep}.joblib",
            f"auto_xgb_model_{ep}.joblib",
            f"sc_main_{ep}.joblib",
            f"sc_direct_{ep}.joblib",
        ):
            path = os.path.join(model_dir, name)
            if os.path.isfile(path):
                out[ep] = joblib.load(path)
                break
    if len(out) != 3:
        return {}, "none"
    sample = next(iter(out.values()))
    kind = "classifier" if hasattr(sample, "predict_proba") else "regression"
    return out, kind


def load_sc_dual_models(
    main_dir: str | None,
    direct_dir: str | None,
    legacy_dir: str | None = None,
) -> ScDualModels:
    bundle = ScDualModels()
    if main_dir and os.path.isdir(main_dir):
        bundle.main, bundle.main_kind = _load_episode_models(main_dir, "sc_main")
    if direct_dir and os.path.isdir(direct_dir):
        bundle.direct, bundle.direct_kind = _load_episode_models(direct_dir, "sc_direct")
    if legacy_dir and os.path.isdir(legacy_dir):
        bundle.legacy, bundle.legacy_kind = _load_episode_models(legacy_dir, "auto_xgb_model")
    return bundle


def _ling_dim_for_model(model, episode: str, use_micro: bool) -> int:
    n_in = int(getattr(model, "n_features_in_", 778))
    bert_part = 3072 if episode == "SC_E2" else 768
    micro_part = 15 if use_micro else 0
    return max(n_in - bert_part - micro_part, 1)


def regression_ling_dim_for_bundle(bundle: ScDualModels) -> int:
    """推理前语言特征列数上限（跨 MAIN / 直接 / legacy 轨取 max）。"""
    dims: list[int] = []

    def _add(models: dict[str, Any], use_micro: bool) -> None:
        for ep, model in models.items():
            dims.append(_ling_dim_for_model(model, ep, use_micro))

    if bundle.has_main:
        _add(bundle.main, True)
    if bundle.has_direct:
        _add(bundle.direct, False)
    elif bundle.has_legacy:
        _add(bundle.legacy, False)
    if not bundle.has_main and bundle.has_legacy:
        _add(bundle.legacy, False)
    return max(dims) if dims else 10


def _pad_ling(ling: np.ndarray, ling_dim: int) -> np.ndarray:
    n = ling.shape[1]
    if n >= ling_dim:
        return ling[:, :ling_dim]
    pad = np.zeros((ling.shape[0], ling_dim - n), dtype=ling.dtype)
    return np.concatenate([ling, pad], axis=1)


def _build_X(
    model,
    bert_global: np.ndarray,
    bert_hier: np.ndarray,
    ling: np.ndarray,
    micro_prob: Optional[np.ndarray],
    episode: str,
    use_micro: bool,
) -> np.ndarray:
    ling_dim = _ling_dim_for_model(model, episode, use_micro)
    ling_p = _pad_ling(ling, ling_dim)
    mode = "hierarchical" if episode == "SC_E2" else "global"
    feats = {
        "global": bert_global.astype(np.float32),
        "hierarchical": bert_hier.astype(np.float32),
    }
    if use_micro and micro_prob is not None:
        feats["micro_prob"] = micro_prob.reshape(1, -1).astype(np.float32)
    return rfe.build_regression_X(feats, ling_p, mode, use_micro)


def predict_episode_scores(
    bundle: ScDualModels,
    bert_global: np.ndarray,
    bert_hier: np.ndarray,
    ling: np.ndarray,
    micro_prob: Optional[np.ndarray],
    track: str,
) -> Optional[dict[str, int]]:
    models = {"main": bundle.main, "direct": bundle.direct, "legacy": bundle.legacy}.get(track, {})
    if not models or len(models) != 3:
        return None
    use_micro = track == "main" and bundle.has_main
    out: dict[str, int] = {}
    for ep in SC_EPISODES:
        X = _build_X(
            models[ep],
            bert_global,
            bert_hier,
            ling,
            micro_prob,
            ep,
            use_micro=use_micro,
        )
        out[ep] = clip_episode_score(_predict_one(models[ep], X))
    return out


def episode_dict_to_sum(ep: dict[str, int]) -> int:
    return int(ep["SC_E1"] + ep["SC_E2"] + ep["SC_E3"])


def compute_agreement(
    main_ep: Optional[dict[str, int]],
    direct_ep: Optional[dict[str, int]],
) -> dict[str, Any]:
    if not main_ep or not direct_ep:
        return {
            "delta_sum": None,
            "delta_episodes": {},
            "flag_review": False,
            "message": "双轨之一不可用",
        }
    sm = episode_dict_to_sum(main_ep)
    sd = episode_dict_to_sum(direct_ep)
    delta = abs(sm - sd)
    deltas = {ep: abs(main_ep[ep] - direct_ep[ep]) for ep in SC_EPISODES}
    flag = delta >= REVIEW_DELTA_SUM or any(
        deltas[ep] >= REVIEW_DELTA_EPISODE for ep in SC_EPISODES
    )
    msg = "两轨一致" if not flag else f"MAIN 与直接 SC 分歧较大（Δ总和={delta}）"
    return {
        "delta_sum": delta,
        "delta_episodes": deltas,
        "flag_review": flag,
        "message": msg,
    }


def predict_sc_dual(
    bundle: ScDualModels,
    bert_global: np.ndarray,
    bert_hier: np.ndarray,
    ling: np.ndarray,
    micro_prob: Optional[np.ndarray],
) -> dict[str, Any]:
    """
    返回 sc_main, sc_direct, sc_agreement，以及兼容旧 API 的 pred_SC_*（取自 MAIN 轨）。
    """
    main_ep = None
    if bundle.has_main:
        main_ep = predict_episode_scores(
            bundle, bert_global, bert_hier, ling, micro_prob, "main"
        )
    elif bundle.has_legacy:
        main_ep = predict_episode_scores(
            bundle, bert_global, bert_hier, ling, None, "legacy"
        )

    direct_ep = None
    if bundle.has_direct:
        direct_ep = predict_episode_scores(
            bundle, bert_global, bert_hier, ling, None, "direct"
        )
    elif bundle.has_legacy and not bundle.has_main:
        direct_ep = predict_episode_scores(
            bundle, bert_global, bert_hier, ling, None, "legacy"
        )

    agreement = compute_agreement(main_ep, direct_ep)

    def pack(ep: Optional[dict[str, int]], kind: str) -> Optional[dict[str, Any]]:
        if not ep:
            return None
        return {
            "SC_E1": ep["SC_E1"],
            "SC_E2": ep["SC_E2"],
            "SC_E3": ep["SC_E3"],
            "sum": episode_dict_to_sum(ep),
            "track": kind,
        }

    main_kind = bundle.main_kind if bundle.has_main else (
        bundle.legacy_kind if bundle.has_legacy else "none"
    )
    if bundle.has_direct:
        direct_kind = bundle.direct_kind
    elif bundle.has_legacy and not bundle.has_main:
        direct_kind = "legacy_fallback"
    else:
        direct_kind = "none"

    sc_main = pack(main_ep, f"main_{main_kind}")
    sc_direct = pack(direct_ep, f"direct_{direct_kind}")

    regression: dict[str, Any] = {
        "pred_SC_E1": None,
        "pred_SC_E2": None,
        "pred_SC_E3": None,
        "pred_SC_Sum": None,
        "sc_main": sc_main,
        "sc_direct": sc_direct,
        "sc_agreement": agreement,
    }
    if main_ep:
        regression["pred_SC_E1"] = float(main_ep["SC_E1"])
        regression["pred_SC_E2"] = float(main_ep["SC_E2"])
        regression["pred_SC_E3"] = float(main_ep["SC_E3"])
        regression["pred_SC_Sum"] = float(episode_dict_to_sum(main_ep))
    return regression
