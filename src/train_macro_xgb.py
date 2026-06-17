"""
train_macro_xgb.py
==============================
宏观 SC 回归 · **自动化版**：BART → predicted_ist_words → Jieba/A+B 特征（+auto_TTR）→ 宏观 SS 编码器。
与专家版共用 micro_encoder（含 split .npz、CV、Pearson/Spearman、可选 micro 概率）。
宏观 SC 划分与宏观 SS 一致：``load_or_create_macro_split`` → 70/10/20 分层，XGB 用 train∪val / test。

输出目录默认 models/macro_xgb_narro_v4/，joblib 名与 pipeline 一致：auto_xgb_model_SC_E*.joblib

运行：python3 train_macro_xgb.py

Apple Silicon：须在 matplotlib / xgboost **之前** import bart_infer，否则 BART
``from_pretrained`` 在 MPS 上可能段错误（exit 139）。本文件已固定 import 顺序。
宏观批推理默认 CPU（``NARRO_BART_FORCE_CPU=1``，见 bart_infer）；可设 ``0`` 尝试 MPS。
"""

from __future__ import annotations

import os
import warnings

# 必须在 matplotlib / xgboost 之前（macOS MPS 段错误规避）
import bart_infer  # noqa: F401
from bart_infer import BARTCuePredictor

import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np
import pandas as pd
import xgboost as xgb
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score
from tqdm import tqdm

try:
    from features_automated import analyze_automated_features
except ImportError as e:
    raise SystemExit(f"❌ 缺少 features_automated: {e}") from e

import micro_encoder as rfe
import train_micro_shared as msh
import train_micro as micro

warnings.filterwarnings("ignore")
plt.rcParams["font.sans-serif"] = ["Heiti TC", "Arial Unicode MS", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

CONFIG = {
    "data_path": micro.FILE_PATH,
    "model_name": os.environ.get("NARRO_MICRO_MODEL", micro.MODEL_NAME),
    "micro_checkpoint": os.environ.get("NARRO_MICRO_CKPT", "models/micro_narro_v4.pth"),
    "bart_model_dir": os.environ.get(
        "NARRO_BART_DIR", "models/bart_narro_v4"
    ),
    "split_seed": 42,
    "split_cache": "data/regression_macro_split_narro_v4_701020_seed42.npz",
    "cv_folds": 5,
    "target_variables": ["SC_E1", "SC_E2", "SC_E3"],
    "hier_targets": {"SC_E2"},
    "use_micro_prob_in_xgb": False,
    "run_micro_ablation": False,
    "xgb_n_estimators": 200,
    "xgb_learning_rate": 0.05,
    "xgb_max_depth": 4,
    "xgb_reg_lambda": 1.0,
    "xgb_gamma": 0.0,
    "xgb_subsample": 0.8,
    "xgb_colsample_bytree": 0.7,
    "automated_linguistic_columns": [
        "auto_TNU", "auto_MLU", "auto_TNW", "auto_TDW",
        "auto_IS_Per_count", "auto_IS_Phy_count", "auto_IS_Con_count",
        "auto_IS_Emo_count", "auto_IS_Men_count", "auto_IS_Ling_count",
    ],
    "output_dir": os.environ.get(
        "NARRO_MACRO_OUTPUT_DIR", "models/macro_xgb_narro_v4"
    ),
}


def _prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.rename(columns={df.columns[0]: "text"}, inplace=True)
    if "story_type" not in df.columns:
        raise ValueError("缺少列 story_type")
    msh.coerce_task_label_columns(df, micro.TASK_NAMES)
    return df


def _append_auto_ttr(ling: np.ndarray, base_cols: list[str]) -> tuple[np.ndarray, list[str]]:
    ic_nw = base_cols.index("auto_TNW")
    ic_dw = base_cols.index("auto_TDW")
    with np.errstate(divide="ignore", invalid="ignore"):
        ttr = ling[:, ic_dw] / (ling[:, ic_nw] + 1e-9)
    ttr = np.nan_to_num(ttr, nan=0.0, posinf=0.0, neginf=0.0)
    return np.hstack([ling, ttr.reshape(-1, 1)]), list(base_cols) + ["auto_TTR"]


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
        n_estimators=CONFIG["xgb_n_estimators"],
        learning_rate=CONFIG["xgb_learning_rate"],
        max_depth=CONFIG["xgb_max_depth"],
        reg_lambda=CONFIG["xgb_reg_lambda"],
        gamma=CONFIG["xgb_gamma"],
        subsample=CONFIG["xgb_subsample"],
        colsample_bytree=CONFIG["xgb_colsample_bytree"],
        random_state=CONFIG["split_seed"],
        n_jobs=-1,
    )
    model = xgb.XGBClassifier(**params)
    cv = KFold(n_splits=CONFIG["cv_folds"], shuffle=True, random_state=CONFIG["split_seed"])
    cv_acc = cross_val_score(model, X_train, y_train_c, cv=cv, scoring="accuracy")
    print(
        f"  {CONFIG['cv_folds']}-fold CV Acc: {cv_acc.mean():.4f} ± {cv_acc.std():.4f}"
    )
    model.fit(X_train, y_train_c)
    y_pred = model.predict(X_test).astype(int)
    acc = accuracy_score(y_test_c, y_pred)
    mae = float(np.mean(np.abs(y_test_c - y_pred)))
    print(f"  Test Acc={acc:.4f} MAE={mae:.4f}")
    path = os.path.join(output_dir, f"{model_prefix}_{target_var}.joblib")
    joblib.dump(model, path)
    print(f"  [保存] {path}")
    if feature_names and len(feature_names) == X_train.shape[1]:
        rfe.report_xgb_feature_importance(
            model,
            feature_names,
            target_var,
            output_csv=os.path.join(
                output_dir, f"feat_imp_{model_prefix}_{target_var}.csv"
            ),
            top_k=20,
        )
    return y_pred, {
        "预测目标": target_var,
        f"CV Acc ({CONFIG['cv_folds']}-fold mean)": cv_acc.mean(),
        f"CV Acc ({CONFIG['cv_folds']}-fold std)": cv_acc.std(),
        "Test Acc": acc,
        "Test MAE": mae,
    }


def _xgb_train_eval(
    X_train,
    y_train,
    X_test,
    y_test,
    feature_names,
    target_var,
    output_dir,
    model_prefix: str,
):
    params = dict(
        objective="reg:squarederror",
        n_estimators=CONFIG["xgb_n_estimators"],
        learning_rate=CONFIG["xgb_learning_rate"],
        max_depth=CONFIG["xgb_max_depth"],
        reg_lambda=CONFIG["xgb_reg_lambda"],
        gamma=CONFIG["xgb_gamma"],
        subsample=CONFIG["xgb_subsample"],
        colsample_bytree=CONFIG["xgb_colsample_bytree"],
        random_state=CONFIG["split_seed"],
        n_jobs=-1,
    )
    model = xgb.XGBRegressor(**params)
    cv = KFold(n_splits=CONFIG["cv_folds"], shuffle=True, random_state=CONFIG["split_seed"])
    cv_r2 = cross_val_score(model, X_train, y_train, cv=cv, scoring="r2")
    cv_mse = -cross_val_score(
        model, X_train, y_train, cv=cv, scoring="neg_mean_squared_error"
    )
    print(
        f"  {CONFIG['cv_folds']}-fold CV  R²: {cv_r2.mean():.4f} ± {cv_r2.std():.4f} | "
        f"MSE: {cv_mse.mean():.4f} ± {cv_mse.std():.4f}"
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    pr, _ = pearsonr(y_test, y_pred)
    sp, _ = spearmanr(y_test, y_pred)
    acc = accuracy_score(y_test.astype(int), np.round(y_pred).astype(int))
    print(f"  Test MSE={mse:.4f} R²={r2:.4f} Pearson r={pr:.4f} Spearman ρ={sp:.4f} Acc={acc:.4f}")
    path = os.path.join(output_dir, f"{model_prefix}_{target_var}.joblib")
    joblib.dump(model, path)
    print(f"  [保存] {path}")
    if feature_names and len(feature_names) == X_train.shape[1]:
        rfe.report_xgb_feature_importance(
            model,
            feature_names,
            target_var,
            output_csv=os.path.join(
                output_dir, f"feat_imp_{model_prefix}_{target_var}.csv"
            ),
            top_k=20,
        )
    return y_pred, {
        "预测目标": target_var,
        f"CV R² ({CONFIG['cv_folds']}-fold mean)": cv_r2.mean(),
        f"CV R² ({CONFIG['cv_folds']}-fold std)": cv_r2.std(),
        "Test MSE": mse,
        "Test R²": r2,
        "Pearson r": pr,
        "Spearman ρ": sp,
        "Acc (rounded)": acc,
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
    *,
    use_classifier: bool = False,
) -> pd.DataFrame:
    os.makedirs(output_dir, exist_ok=True)
    rows = []
    preds = {}
    k = CONFIG["cv_folds"]
    for tv in CONFIG["target_variables"]:
        print(f"\n{'=' * 20} {tv} (micro_prob={use_micro}) {'=' * 20}")
        mode = "hierarchical" if tv in CONFIG["hier_targets"] else "global"
        X_tr = rfe.build_regression_X(ft, ling_tr, mode, use_micro)
        X_te = rfe.build_regression_X(fe, ling_te, mode, use_micro)
        fn = rfe.build_regression_feature_names(auto_names, bd, mode, use_micro)
        train_fn = _xgb_train_eval_classifier if use_classifier else _xgb_train_eval
        yp, m = train_fn(
            X_tr,
            ytr[tv].values,
            X_te,
            yte[tv].values,
            fn,
            tv,
            output_dir,
            model_prefix,
        )
        preds[tv] = yp
        m["use_micro_prob"] = use_micro
        rows.append(m)
    y_sum = sum(preds[t] for t in CONFIG["target_variables"])
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
            f"CV R² ({k}-fold mean)": np.nan,
            f"CV R² ({k}-fold std)": np.nan,
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


if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    msh.set_seed(CONFIG["split_seed"])

    df = pd.read_csv(CONFIG["data_path"])
    df = _prepare_dataframe(df)
    targets = CONFIG["target_variables"] + ["SC_Sum"]
    for c in targets:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)

    tr, te = rfe.load_or_create_macro_split(
        df, CONFIG.get("split_cache") or None, CONFIG["split_seed"]
    )
    dtr = df.iloc[tr].reset_index(drop=True)
    dte = df.iloc[te].reset_index(drop=True)

    ckpt = CONFIG["micro_checkpoint"]
    if not os.path.isfile(ckpt):
        raise SystemExit(f"❌ 缺少宏观 SS 权重: {ckpt}")
    bart = BARTCuePredictor(model_dir=CONFIG["bart_model_dir"])
    dtr["predicted_ist_words"] = [
        bart.predict_ist_words(str(t)) for t in tqdm(dtr["text"], desc="BART train")
    ]
    dte["predicted_ist_words"] = [
        bart.predict_ist_words(str(t)) for t in tqdm(dte["text"], desc="BART test")
    ]

    base_cols = CONFIG["automated_linguistic_columns"]

    def rv(r):
        return analyze_automated_features(r["text"], r["predicted_ist_words"])[0]

    tqdm.pandas(desc="A+B train")
    lt = np.array(dtr.progress_apply(rv, axis=1).tolist(), dtype=np.float64)
    tqdm.pandas(desc="A+B test")
    le = np.array(dte.progress_apply(rv, axis=1).tolist(), dtype=np.float64)
    lt, auto_names = _append_auto_ttr(lt, base_cols)
    le, _ = _append_auto_ttr(le, base_cols)

    tok, bert, dev = rfe.load_micro_encoder(ckpt, CONFIG["model_name"])
    bd = bert.bert.config.hidden_size
    ft = rfe.extract_all_micro_features(
        dtr, bert, tok, dev, "predicted_ist_words", micro.MAX_LENGTH, True, "auto train"
    )
    fe = rfe.extract_all_micro_features(
        dte, bert, tok, dev, "predicted_ist_words", micro.MAX_LENGTH, True, "auto test"
    )
    ytr = dtr[targets]
    yte = dte[targets]

    dual_train = os.environ.get("NARRO_SC_DUAL_TRAIN", "1") == "1"
    if dual_train:
        main_dir = os.environ.get("NARRO_SC_MAIN_DIR", "models/macro_sc_main")
        direct_dir = os.environ.get("NARRO_SC_DIRECT_DIR", "models/macro_sc_direct")
        print("\n=== 轨 A · MAIN（SS 概率 + 分幕序数）===")
        df_a = _run_one_suite(
            main_dir,
            "sc_main",
            True,
            ft,
            fe,
            lt,
            le,
            auto_names,
            ytr,
            yte,
            bd,
            use_classifier=True,
        )
        df_a.to_csv(os.path.join(main_dir, "summary_sc_main.csv"), index=False)
        print("\n=== 轨 B · 直接 SC（无 SS 概率）===")
        df_b = _run_one_suite(
            direct_dir,
            "sc_direct",
            False,
            ft,
            fe,
            lt,
            le,
            auto_names,
            ytr,
            yte,
            bd,
            use_classifier=True,
        )
        df_b.to_csv(os.path.join(direct_dir, "summary_sc_direct.csv"), index=False)
        print(f"\n✅ 双轨训练完成 → {main_dir} , {direct_dir}")
    else:
        out = CONFIG["output_dir"]
        df_main = _run_one_suite(
            out,
            "auto_xgb_model",
            CONFIG["use_micro_prob_in_xgb"],
            ft,
            fe,
            lt,
            le,
            auto_names,
            ytr,
            yte,
            bd,
            use_classifier=False,
        )
        df_main.to_csv(os.path.join(out, "summary_performance_automated.csv"), index=False)
        print(f"\n✅ 主实验完成 → {out}")

    if (
        not dual_train
        and CONFIG["run_micro_ablation"]
        and not CONFIG["use_micro_prob_in_xgb"]
    ):
        out_ab = os.path.join(CONFIG["output_dir"], "ablation_micro_prob")
        _run_one_suite(
            out_ab,
            "auto_xgb_model_micro",
            True,
            ft,
            fe,
            lt,
            le,
            auto_names,
            ytr,
            yte,
            bd,
        )
        print(f"✅ Micro 概率消融 → {out_ab}")

    manifest_dir = (
        os.environ.get("NARRO_SC_MAIN_DIR", "models/macro_sc_main")
        if dual_train
        else CONFIG["output_dir"]
    )
    pd.DataFrame(
        [
            {
                "script": "train_macro_xgb",
                "dual_train": dual_train,
                "micro_checkpoint": ckpt,
                "split_cache": CONFIG.get("split_cache"),
                "automated_linguistic_columns": ",".join(CONFIG["automated_linguistic_columns"]),
                "use_micro_prob": CONFIG["use_micro_prob_in_xgb"],
                "micro_ist_sep": micro.MICRO_IST_INLINE_SEPARATOR,
            }
        ]
    ).to_csv(os.path.join(manifest_dir, "run_manifest.csv"), index=False)
