"""SC 双轨：一致性与回退逻辑单元测试。"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sc_dual_track import (  # noqa: E402
    clip_episode_score,
    compute_agreement,
    episode_dict_to_sum,
    load_sc_dual_models,
    predict_sc_dual,
    regression_ling_dim_for_bundle,
    ScDualModels,
)


def test_clip_episode_score():
    assert clip_episode_score(2.4) == 2
    assert clip_episode_score(-1) == 0
    assert clip_episode_score(3.9) == 3


def test_compute_agreement_flag_review():
    main = {"SC_E1": 2, "SC_E2": 2, "SC_E3": 2}
    direct = {"SC_E1": 0, "SC_E2": 0, "SC_E3": 0}
    agr = compute_agreement(main, direct)
    assert agr["delta_sum"] == 6
    assert agr["flag_review"] is True


def test_compute_agreement_ok():
    ep = {"SC_E1": 1, "SC_E2": 2, "SC_E3": 1}
    agr = compute_agreement(ep, dict(ep))
    assert agr["delta_sum"] == 0
    assert agr["flag_review"] is False


def test_episode_dict_to_sum():
    assert episode_dict_to_sum({"SC_E1": 1, "SC_E2": 2, "SC_E3": 0}) == 3


class _FakeReg:
    n_features_in_ = 768 + 11

    def predict(self, X):
        return np.array([2.3])


def test_regression_ling_dim_legacy():
    bundle = ScDualModels(
        legacy={
            "SC_E1": _FakeReg(),
            "SC_E2": type("_H", (), {"n_features_in_": 3072 + 11})(),
            "SC_E3": _FakeReg(),
        }
    )
    bundle.legacy_kind = "regression"
    assert regression_ling_dim_for_bundle(bundle) == 11


def test_predict_sc_dual_legacy_only(tmp_path):
    leg = tmp_path / "legacy"
    leg.mkdir()
    import joblib

    for ep in ("SC_E1", "SC_E2", "SC_E3"):
        joblib.dump(_FakeReg(), leg / f"auto_xgb_model_{ep}.joblib")

    bundle = load_sc_dual_models(None, None, str(leg))
    assert bundle.has_legacy

    g = np.zeros((1, 768), dtype=np.float32)
    h = np.zeros((1, 3072), dtype=np.float32)
    ling = np.zeros((1, 11), dtype=np.float32)
    out = predict_sc_dual(bundle, g, h, ling, None)
    assert out["pred_SC_Sum"] == 6.0  # 2+2+2 rounded
    assert out["sc_main"] is not None
    assert out["sc_direct"] is not None
