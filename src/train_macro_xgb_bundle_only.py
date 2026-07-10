"""从 macro_sc_dual_bundle.npz 仅训练 XGB 双轨（不加载 PyTorch/BART）。"""

from __future__ import annotations

import os
import sys

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score

TASK_NAMES = [f"A{i}" for i in range(2, 17)]
TARGETS = ["SC_E1", "SC_E2", "SC_E3", "SC_Sum"]
HIER_TARGETS = {"SC_E2"}


def _xgb_n_jobs() -> int:
    v = os.environ.get("NARRO_XGB_N_JOBS", "").strip()
    if v:
        return int(v)
    if os.uname().sysname == "Darwin":
        return 1
    return -1


def build_regression_feature_names(
    ling_cols: list[str],
    hidden: int,
    feature_mode: str,
    use_micro_prob: bool,
) -> list[str]:
    if feature_mode == "global":
        names = [f"bert_Global_{i}" for i in range(hidden)]
    elif feature_mode == "hierarchical":
        names = (
            [f"bert_E1_{i}" for i in range(hidden)]
            + [f"bert_E2_{i}" for i in range(hidden)]
            + [f"bert_E3_{i}" for i in range(hidden)]
            + [f"bert_Global_{i}" for i in range(hidden)]
        )
    else:
        raise ValueError(feature_mode)
    if use_micro_prob:
        for t in TASK_NAMES:
            names.append(f"micro_prob_{t}")
    names += list(ling_cols)
    return names


def build_regression_X(
    feats: dict[str, np.ndarray],
    ling_mat: np.ndarray,
    feature_mode: str,
    use_micro_prob: bool,
) -> np.ndarray:
    parts: list[np.ndarray] = [feats[feature_mode].astype(np.float32)]
    if use_micro_prob:
        parts.append(feats["micro_prob"].astype(np.float32))
    parts.append(ling_mat.astype(np.float32))
    return np.concatenate(parts, axis=1).astype(np.float64)


def _xgb_train_eval_classifier(
    X_train,
    y_train,
    X_test,
    y_test,
    feature_names,
    target_var,
    output_dir,
    model_prefix: str,
):
    y_train_c = np.clip(np.round(y_train).astype(int), 0, 3)
    y_test_c = np.clip(np.round(y_test).astype(int), 0, 3)
    params = dict(
        objective="multi:softmax",
        num_class=4,
        n_estimators=200,
        learning_rate=0.05,
        max_depth=4,
        reg_lambda=1.0,
        gamma=0.0,
        subsample=0.8,
        colsample_bytree=0.7,
        random_state=42,
        n_jobs=_xgb_n_jobs(),
    )
    model = xgb.XGBClassifier(**params)
    if os.environ.get("NARRO_SKIP_XGB_CV", "1") == "1":
        cv_acc = np.array([np.nan])
        print("  [CV 跳过] NARRO_SKIP_XGB_CV=1")
    else:
        cv = KFold(n_splits=5, shuffle=True, random_state=42)
        cv_acc = cross_val_score(
            model, X_train, y_train_c, cv=cv, scoring="accuracy", n_jobs=1
        )
        print(f"  5-fold CV Acc: {cv_acc.mean():.4f} ± {cv_acc.std():.4f}")
    model.fit(X_train, y_train_c)
    y_pred = model.predict(X_test).astype(int)
    acc = accuracy_score(y_test_c, y_pred)
    mae = float(np.mean(np.abs(y_test_c - y_pred)))
    print(f"  Test Acc={acc:.4f} MAE={mae:.4f}")
    path = os.path.join(output_dir, f"{model_prefix}_{target_var}.joblib")
    joblib.dump(model, path)
    print(f"  [保存] {path}")
    return y_pred, {
        "预测目标": target_var,
        "Test Acc": acc,
        "Test MAE": mae,
    }


def _run_one_suite(
    output_dir: str,
    model_prefix: str,
    use_micro: bool,
    ft,
    fe,
    ling_tr,
    ling_te,
    auto_names,
    ytr,
    yte,
    bd,
) -> pd.DataFrame:
    os.makedirs(output_dir, exist_ok=True)
    rows = []
    preds = {}
    for tv in TARGETS[:3]:
        print(f"\n{'=' * 20} {tv} (micro_prob={use_micro}) {'=' * 20}")
        mode = "hierarchical" if tv in HIER_TARGETS else "global"
        X_tr = build_regression_X(ft, ling_tr, mode, use_micro)
        X_te = build_regression_X(fe, ling_te, mode, use_micro)
        fn = build_regression_feature_names(auto_names, bd, mode, use_micro)
        yp, m = _xgb_train_eval_classifier(
            X_tr, ytr[tv].values, X_te, yte[tv].values, fn, tv, output_dir, model_prefix
        )
        preds[tv] = yp
        m["use_micro_prob"] = use_micro
        rows.append(m)
    y_sum = sum(preds[t] for t in TARGETS[:3])
    yt = yte["SC_Sum"].values
    mse = mean_squared_error(yt, y_sum)
    r2 = r2_score(yt, y_sum)
    pr, _ = pearsonr(yt, y_sum)
    sp, _ = spearmanr(yt, y_sum)
    acc = accuracy_score(yt.astype(int), np.round(y_sum).astype(int))
    print(f"\n  SC_Sum (推导) MSE={mse:.4f} R²={r2:.4f} r={pr:.4f} ρ={sp:.4f} Acc={acc:.4f}")
    rows.append(
        {
            "预测目标": "SC_Sum (推导)",
            "Test MSE": mse,
            "Test R²": r2,
            "Pearson r": pr,
            "Spearman ρ": sp,
            "Acc (rounded)": acc,
            "use_micro_prob": use_micro,
        }
    )
    df_out = pd.DataFrame(rows)
    df_out.to_csv(os.path.join(output_dir, f"summary_{model_prefix}.csv"), index=False)
    return df_out


def main() -> int:
    bundle = os.environ.get(
        "NARRO_MACRO_BUNDLE_CACHE", "data/macro_sc_dual_bundle.npz"
    ).strip()
    if not os.path.isfile(bundle):
        print(f"缺少 bundle: {bundle}")
        print("请先完成特征提取并写入 bundle。")
        return 1

    print(f"[bundle-only] 加载 {bundle}")
    z = np.load(bundle, allow_pickle=True)
    ft = z["ft"].item()
    fe = z["fe"].item()
    bd = int(z["bd"])
    lt = z["lt"]
    le = z["le"]
    auto_names = list(z["auto_names"].tolist())
    ytr = pd.DataFrame(z["ytr"], columns=TARGETS)
    yte = pd.DataFrame(z["yte"], columns=TARGETS)

    main_dir = os.environ.get("NARRO_SC_MAIN_DIR", "models/macro_sc_main")
    direct_dir = os.environ.get("NARRO_SC_DIRECT_DIR", "models/macro_sc_direct")

    print("\n=== 轨 A · MAIN（SS 概率 + 分幕序数）===")
    _run_one_suite(main_dir, "sc_main", True, ft, fe, lt, le, auto_names, ytr, yte, bd)

    print("\n=== 轨 B · 直接 SC（无 SS 概率）===")
    _run_one_suite(
        direct_dir, "sc_direct", False, ft, fe, lt, le, auto_names, ytr, yte, bd
    )

    print(f"\n✅ 双轨 XGB 训练完成 → {main_dir} , {direct_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
