# pipeline_predict_report.py
# [目标]：
# 1. 接收一段新文本和元数据。
# 2. 全自动执行 B1 (Jieba) 和 B2 (BART) 预处理 [来自: 1, 2]。
# 3. 全自动执行 C (BERT) 特征提取。
# 4. 全自动执行 D (XGBoost) 回归预测。
# 5. 全自动执行 E (多任务) 分类预测 [来自: 3]。
# 6. 加载 F (基准数据库)，生成一份对比分析报告 [来自: 3]。
#
# [论文 / 仓库对应 — Jieba (B1)]
# - 原始叙事上的 A 类可计算特征：features_jieba.extract_calculable_features（jieba.lcut）
# - BART 线索串上的 B 类关键词计数：features_automated.extract_B_class_features（jieba.lcut）
# - 预测端统一入口：features_automated.analyze_automated_features（内部已调用上述逻辑）
#
# [全自动宏观回归 (D) — 核心脚本]
# - 训练与导出 joblib：train_macro_xgb.py → MODEL_PATHS['auto_xgb_folder']
#     （auto_xgb_model_SC_E{1,2,3}.joblib）
# - 宏观 XGB：`models/macro_xgb_narro_v4/`（由 train_macro_xgb.py 产出）。
#
# [V5 - 最终对比修复版]
# [V6 - 与论文模块 4 对齐] 支持 task_type 基准对比、报告增加发展水平定位。
# - 自动读取 "new_data.csv"（可选列 task_type：讲述/复述，用于更精确的常模对比）
# - 修复了 'age' 和 'left_behind' 列的 NaN/字符串转换错误
# - 修复了 'goat' 模板中的 'A4Masks' 拼写错误
# - 新增 '置信分数' 到报告和 CSV 中
# - [!] 修复1: 自动计算多任务基准库的 'calculated_SS_Sum'，启用对比。
# - [!] 修复2: 回归和多任务对比现在同时按 'age' 和 'story_type' 筛选。
# - [V6] 修复3: 若基准库与输入含 task_type，则按 task_type 筛选（与论文 4.2.3 一致）。
# - [V6] 新增: 报告增加「发展水平定位」摘要（论文 3.2 developmental stage indicators）。
# - [V7] 若 new_data.csv 含 participants 列，同数字视为同一人；predict 完成后自动按参与者生成汇总报告（batch_reports/participant_reports/）。

import pandas as pd
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm
import os
import joblib
import warnings
from pathlib import Path

import micro_encoder as micro_enc
from train_micro import (
    IST_TASKS,
    QUESTION_TEMPLATES,
    TASK_NAMES,
    format_micro_context_segment,
)

# --- 导入自动化工具 ---
try:
    # [来自: 1] (bart_infer.py)
    from bart_infer import BARTCuePredictor
except ImportError as e:
    print(f"❌ 错误: 找不到自动化脚本。 {e}")
    print("请确保 'bart_infer.py' 与 'features_automated.py' 在同一个文件夹中。")
    exit()

# [来自: 2] (features_automated.py)
from features_automated import EXPERT_KEYWORD_DB, analyze_automated_features
from calibration_microstructure_thresholds import multitask_threshold_for_task, resolve_thresholds

warnings.filterwarnings("ignore")

MICRO_MAX_LENGTH = 512
TASK_NAMES_GLOBAL = TASK_NAMES

# ==============================================================================
# --- ( ! ) 用户输入区 ( ! ) ---
# ==============================================================================

# [!] 注意：下面的文本和元数据仅作为备用，脚本现在会从 .csv 读取
# 1. 填入你想要分析的新文本
NEW_NARRATIVE_TEXT = "小猫想抓蝴蝶。它跳了起来，但是没有抓到。小猫很难过。"

# 2. 填入对应的元数据
NEW_META_DATA = {
    'story_type': 'cat', # 'cat', 'dog', 'bird', 'goat'
    'age': 5,            # 参与者年龄
    'left_behind': 0     # 0 = 非留守, 1 = 留守
}

try:
    from paths import default_model_paths

    MODEL_PATHS = default_model_paths()
except ImportError:
    MODEL_PATHS = {
        "bart_model_dir": "./models/bart_narro_v4",
        "macro_xgb_dir": "./models/macro_xgb_narro_v4",
        "auto_xgb_folder": "./models/macro_xgb_narro_v4",
        "micro_weights": "./models/micro_narro_v4.pth",
        "bert_classifier_weights": "./models/micro_narro_v4.pth",
        "bert_multitask_calibration_json": None,
        "benchmark_db_regression": "",
        "benchmark_db_multitask": "",
    }

# ==============================================================================
# --- 1. 核心组件 (BERT) ---
# ==============================================================================
CONFIG = {
    'model_name': 'Morton-Li/QiDeBERTa-base',
    # [新] 我们只使用 'features_automated.py' 能生成的特征
    'automated_linguistic_columns': [
        'auto_TNU', 'auto_MLU', 'auto_TNW', 'auto_TDW', 
        'auto_IS_Per_count', 'auto_IS_Phy_count', 'auto_IS_Con_count', 
        'auto_IS_Emo_count', 'auto_IS_Men_count', 'auto_IS_Ling_count'
    ],
}


def _append_auto_ttr_row(ling: np.ndarray, base_cols: list[str]) -> np.ndarray:
    """与 train_macro_xgb._append_auto_ttr 一致（单行）。"""
    ic_nw = base_cols.index("auto_TNW")
    ic_dw = base_cols.index("auto_TDW")
    with np.errstate(divide="ignore", invalid="ignore"):
        ttr = ling[:, ic_dw] / (ling[:, ic_nw] + 1e-9)
    ttr = np.nan_to_num(ttr, nan=0.0, posinf=0.0, neginf=0.0)
    return np.hstack([ling, ttr.reshape(-1, 1)])
# QUESTION_TEMPLATES / format_micro_context_segment 与 train_micro.py 共用（微观训练问法）

# ==============================================================================
# --- 2. 预测流程 ---
# ==============================================================================

class AutomatedNarrativePredictor:
    def __init__(self, model_paths):
        print("--- 正在初始化全自动叙事分析器 ---")
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif getattr(torch.backends, "mps", None) is not None and torch.backends.mps.is_available():
            self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")
        self.model_paths = model_paths
        
        # 1. 加载 T5 模型 (B2)
        try:
            self.bart_predictor = BARTCuePredictor(model_dir=model_paths['bart_model_dir'])
        except Exception as e:
            print("❌ 致命错误: 无法加载 BART 模型。")
            raise e

        # 2. 加载 QiDeBERTa-base 微观模型（micro_narro_v4.pth，含 LoRA）
        enc_name = model_paths.get("encoder_model", CONFIG["model_name"])
        micro_cfg = model_paths.get("micro_config")
        self.tokenizer, self.bert_model, _ = micro_enc.load_micro_encoder(
            model_paths["bert_classifier_weights"],
            enc_name,
            self.device,
            micro_config_path=micro_cfg,
        )
        print("  [✓] 宏观 SS 编码器 (多任务/特征) 模型加载成功。")

        self._mt_thr_telling, self._mt_thr_retelling, _thr_src = resolve_thresholds(
            model_paths["bert_classifier_weights"],
            model_paths.get("bert_multitask_calibration_json"),
        )
        print(
            f"  [✓] 多任务二值化阈值 ({_thr_src}): "
            f"Telling={self._mt_thr_telling:.2f}, Retelling={self._mt_thr_retelling:.2f}"
        )

        # 3. 加载宏观 SC 双轨模型 (D)
        from sc_dual_track import load_sc_dual_models, regression_ling_dim_for_bundle

        macro_xgb_dir = model_paths.get("macro_xgb_dir") or model_paths.get(
            "auto_xgb_folder", "./models/macro_xgb_narro_v4"
        )
        main_dir = model_paths.get("macro_sc_main_dir") or ""
        direct_dir = model_paths.get("macro_sc_direct_dir") or ""
        self._sc_models = load_sc_dual_models(main_dir, direct_dir, macro_xgb_dir)
        self._has_regression_models = (
            self._sc_models.has_main
            or self._sc_models.has_direct
            or self._sc_models.has_legacy
        )
        self._regression_ling_dim = (
            regression_ling_dim_for_bundle(self._sc_models)
            if self._has_regression_models
            else len(CONFIG["automated_linguistic_columns"])
        )
        if self._sc_models.has_main:
            print(f"  [✓] SC 轨 A (MAIN) 已加载 ({os.path.basename(main_dir)})")
        if self._sc_models.has_direct:
            print(f"  [✓] SC 轨 B (直接) 已加载 ({os.path.basename(direct_dir)})")
        if not self._sc_models.has_main and self._sc_models.has_legacy:
            print(
                f"  [✓] SC 使用 legacy 回归回退 ({os.path.basename(macro_xgb_dir)})"
            )
        if not self._has_regression_models:
            print(
                f"  [!] 未找到宏观 SC 模型（{main_dir} / {direct_dir} / {macro_xgb_dir}），"
                "宏观复杂度得分将显示为「未可用」。"
            )

        # 4. 加载基准数据库 (F)：显式 CSV → 否则 narratives.csv → 否则空表（仅输出分数，无常模对比）
        self.benchmark_db_reg, self.benchmark_db_multi, self._benchmark_source = (
            self._load_benchmark_databases(model_paths)
        )
        print(f"--- ✅ 分析器已就绪（常模来源: {self._benchmark_source}）---")

    @staticmethod
    def _load_benchmark_databases(model_paths: dict) -> tuple[pd.DataFrame, pd.DataFrame, str]:
        reg_path = model_paths.get("benchmark_db_regression")
        multi_path = model_paths.get("benchmark_db_multitask")
        for label, path in (("regression", reg_path), ("multitask", multi_path)):
            if path and os.path.isfile(path):
                continue
            if path:
                print(f"  [!] 未找到{label}基准文件: {path}")

        if reg_path and os.path.isfile(reg_path):
            reg_df = pd.read_csv(reg_path)
            multi_df = (
                pd.read_csv(multi_path)
                if multi_path and os.path.isfile(multi_path)
                else reg_df.copy()
            )
            source = "archived_csv"
        else:
            narr = None
            try:
                from paths import narratives_csv_path

                narr = narratives_csv_path()
            except ImportError:
                pass
            if narr is None:
                for candidate in (Path("data/narratives.csv"), Path("narratives.csv")):
                    if candidate.is_file():
                        narr = candidate
                        break
            if narr is not None and Path(narr).is_file():
                reg_df = multi_df = pd.read_csv(narr)
                if reg_df.columns[0].lower() not in ("text", "narrative"):
                    reg_df = reg_df.rename(columns={reg_df.columns[0]: "text"})
                source = str(narr)
                print(f"  [✓] 使用 {narr} 作为常模参照 (n={len(reg_df)})。")
            else:
                reg_df = pd.DataFrame(
                    columns=["age", "story_type", "left_behind", "pred_SC_Sum", "task_type"]
                )
                multi_df = pd.DataFrame(
                    columns=["age", "story_type", "left_behind", "task_type"] + TASK_NAMES_GLOBAL
                )
                source = "none"
                print("  [!] 无常模库：仅输出模型预测分，不进行同龄对比。")

        for df in (reg_df, multi_df):
            if "age" in df.columns:
                df["age"] = pd.to_numeric(df["age"], errors="coerce").fillna(0)
            if "left_behind" in df.columns:
                df["left_behind"] = pd.to_numeric(df["left_behind"], errors="coerce").fillna(0)

        if "pred_SC_Sum" not in reg_df.columns and "SC_Sum" in reg_df.columns:
            reg_df["pred_SC_Sum"] = pd.to_numeric(reg_df["SC_Sum"], errors="coerce")

        multi_task_cols = [c for c in TASK_NAMES_GLOBAL if c in multi_df.columns]
        if multi_task_cols and "calculated_SS_Sum" not in multi_df.columns:
            for c in multi_task_cols:
                multi_df[c] = pd.to_numeric(multi_df[c], errors="coerce").fillna(0)
            multi_df["calculated_SS_Sum"] = multi_df[multi_task_cols].sum(axis=1)

        from benchmark_norms import ensure_expert_norm_columns

        reg_df = ensure_expert_norm_columns(reg_df)
        multi_df = ensure_expert_norm_columns(multi_df)

        return reg_df, multi_df, source

    def predict(
        self,
        text,
        story_type,
        age,
        left_behind,
        task_type=None,
        predicted_ist_words: str | None = None,
    ):
        """
        对单篇新文本执行全流程分析。
        task_type: 可选，叙事类型（如 'storytelling'/'retelling' 或中文）。若提供且基准库含该列，则按同龄+同主题+同任务类型对比。
        predicted_ist_words: 可选，已算好的 BART 线索，避免重复推理。
        """
        if predicted_ist_words is None:
            predicted_ist_words = self.bart_predictor.predict_ist_words(text)
        # print(f"  [B2] 自动预测线索: \"{predicted_ist_words}\"")

        # B1 + B(扩展): A 类（Jieba 于原文）+ B 类（Jieba 于 BART 线索）[来自: features_automated]
        auto_features_vector, auto_feature_names = analyze_automated_features(text, predicted_ist_words)
        linguistic_features = np.array(auto_features_vector).reshape(1, -1)  # (1, 10)
        base_cols = CONFIG["automated_linguistic_columns"]
        if self._has_regression_models and linguistic_features.shape[1] < self._regression_ling_dim:
            if self._regression_ling_dim == linguistic_features.shape[1] + 1:
                linguistic_features = _append_auto_ttr_row(linguistic_features, base_cols)
            else:
                pad = np.zeros(
                    (1, self._regression_ling_dim - linguistic_features.shape[1]),
                    dtype=linguistic_features.dtype,
                )
                linguistic_features = np.concatenate([linguistic_features, pad], axis=1)

        from linguistic_metrics import (
            build_linguistic_metrics,
            format_linguistic_report_section,
            peer_linguistic_norms,
        )

        linguistic_metrics = build_linguistic_metrics(text, predicted_ist_words)
        peer_ling = peer_linguistic_norms(
            self.benchmark_db_reg, age, story_type, task_type
        )
        linguistic_metrics["peer_norms"] = peer_ling

        from narrative_quality_gate import (
            apply_regression_safeguards,
            assess_narrative_quality,
            null_regression,
        )

        narrative_quality = assess_narrative_quality(
            text, linguistic_metrics.get("core", {})
        )
        if narrative_quality["status"] == "insufficient":
            report_lines = [
                "--- 叙事自动分析报告 ---",
                "",
                f"【{narrative_quality['message']}】",
                "",
                "当前检测到的语言产出（仅供自检）：",
            ]
            report_lines.extend(
                format_linguistic_report_section(
                    linguistic_metrics, peer_ling, age, story_type, task_type
                )
            )
            report_lines.append(
                "\n说明：输入未达最短讲述要求时，不输出宏观 SC 与宏观 SS 模型分，"
                "以避免无意义分数（如仅说「你好」）。"
            )
            empty_tasks: dict = {"pred_MultiTask_Sum": None}
            return (
                "\n".join(report_lines),
                null_regression(),
                empty_tasks,
                linguistic_metrics,
                narrative_quality,
            )

        # --- 模块 C & E: 微观双句编码 + 多任务分类（与 train_micro 一致）---
        if story_type not in QUESTION_TEMPLATES:
            print(f"  [!] 警告: 未知的 story_type '{story_type}'。将使用 'cat' 作为模板。")
            story_type = "cat"

        qs, cs = [], []
        for task_name in TASK_NAMES_GLOBAL:
            qs.append(QUESTION_TEMPLATES[story_type][task_name])
            use_ist = bool(predicted_ist_words) and task_name in IST_TASKS
            cs.append(format_micro_context_segment(text, predicted_ist_words, use_ist))

        cls_np, micro_probs = micro_enc._forward_cls_and_micro_probs(
            self.bert_model,
            self.tokenizer,
            qs,
            cs,
            self.device,
            MICRO_MAX_LENGTH,
            compute_micro=True,
        )
        all_probs_flat = micro_probs.reshape(-1, 1)
        thr = multitask_threshold_for_task(
            task_type, story_type, self._mt_thr_telling, self._mt_thr_retelling
        )
        all_preds_binary_flat = np.where(all_probs_flat > thr, 1, 0)
        
        # --- [!! V4 修改 !!] ---
        # 同时存储 0/1 预测和概率
        task_predictions = {}
        for i, task_name in enumerate(TASK_NAMES_GLOBAL):
            binary_pred = all_preds_binary_flat[i][0]
            probability = float(all_probs_flat[i][0])
            task_predictions[task_name] = binary_pred
            task_predictions[f"{task_name}_prob"] = probability # [!] 新增此行
        # --- [!! V4 修改结束 !!] ---
            
        # 处理回归特征 (C)
        all_embeddings_flat = cls_np  # (15, 768)
        
        # C1: 全局特征
        bert_features_global = np.mean(all_embeddings_flat, axis=0, keepdims=True) # (1, 768)
        
        # C2: 层次化特征
        emb_E1 = np.mean(all_embeddings_flat[0:5], axis=0, keepdims=True) # A2-A6
        emb_E2 = np.mean(all_embeddings_flat[5:10], axis=0, keepdims=True) # A7-A11
        emb_E3 = np.mean(all_embeddings_flat[10:15], axis=0, keepdims=True) # A12-A16
        emb_Global = np.mean(np.stack([emb_E1, emb_E2, emb_E3]), axis=0)
        bert_features_hierarchical = np.concatenate([emb_E1, emb_E2, emb_E3, emb_Global], axis=1) # (1, 3072)
        
        # print("  [✓] BERT 特征提取与多任务分类完成。")

        # --- 模块 D: SC 双轨预测（MAIN + 直接 SC；缺权重时回退 legacy 回归）---
        if self._has_regression_models:
            from sc_dual_track import predict_sc_dual

            micro_prob = np.array(
                [[float(task_predictions[f"{n}_prob"]) for n in TASK_NAMES_GLOBAL]],
                dtype=np.float32,
            )
            regression_results = predict_sc_dual(
                self._sc_models,
                bert_features_global,
                bert_features_hierarchical,
                linguistic_features,
                micro_prob,
            )
            regression_results, narrative_quality = apply_regression_safeguards(
                regression_results,
                linguistic_metrics.get("core", {}),
                narrative_quality,
            )
            pred_sc_e1 = regression_results.get("pred_SC_E1")
            pred_sc_e2 = regression_results.get("pred_SC_E2")
            pred_sc_e3 = regression_results.get("pred_SC_E3")
            pred_sc_sum = regression_results.get("pred_SC_Sum")
        else:
            pred_sc_e1 = pred_sc_e2 = pred_sc_e3 = pred_sc_sum = None
            regression_results = {
                "pred_SC_E1": None,
                "pred_SC_E2": None,
                "pred_SC_E3": None,
                "pred_SC_Sum": None,
                "sc_main": None,
                "sc_direct": None,
                "sc_agreement": {"flag_review": False, "message": "模型未加载"},
            }
        
        # --- 模块 F: 生成分析报告 ---
        # print("  [F] 正在生成对比分析报告...")
        
        report_lines = []
        report_lines.append("--- 叙事自动分析报告 ---")
        report_lines.extend(
            format_linguistic_report_section(
                linguistic_metrics, peer_ling, age, story_type, task_type
            )
        )

        # 2. 回归得分
        report_lines.append("\n2. 复杂度回归得分 (模块 D)")
        if self._has_regression_models:
            report_lines.append(f"   - SC_E1 (情节 1) 得分: {pred_sc_e1:.2f}")
            report_lines.append(f"   - SC_E2 (情节 2) 得分: {pred_sc_e2:.2f}")
            report_lines.append(f"   - SC_E3 (情节 3) 得分: {pred_sc_e3:.2f}")
            report_lines.append("   ---------------------------------")
            report_lines.append(f"   - SC_Sum (总复杂度) 得分: {pred_sc_sum:.2f} (四舍五入: {np.round(pred_sc_sum):.0f})")
        else:
            report_lines.append(
                "   - [未可用] 请先运行 scripts/train_macro.py 生成 models/macro_sc_main/ 与 models/macro_sc_direct/；"
                " 或保留 legacy 回退 models/macro_xgb_narro_v4/。"
            )

        from benchmark_norms import EXPERT_MACRO_SUM_COL, EXPERT_MICRO_SUM_COL

        # --- [!! V5 修复 2 + V6 task_type !!] ---
        # 3. 回归基准对比：模型分 vs narratives.csv 专家 SC_Sum 常模
        report_lines.append("\n3. 复杂度基准对比 (模块 F - 回归 · 专家常模)")
        mask_reg = (self.benchmark_db_reg['age'] == age) & (self.benchmark_db_reg['story_type'] == story_type)
        if task_type is not None and 'task_type' in self.benchmark_db_reg.columns:
            t_ref = self.benchmark_db_reg['task_type'].astype(str).str.strip().str.lower()
            t_in = str(task_type).strip().lower()
            mask_reg = mask_reg & (t_ref == t_in)
        benchmark_df_reg_filtered = self.benchmark_db_reg[mask_reg]
        expert_sc_col = EXPERT_MACRO_SUM_COL if EXPERT_MACRO_SUM_COL in benchmark_df_reg_filtered.columns else "pred_SC_Sum"
        
        if not self._has_regression_models:
            report_lines.append("   - [未可用] 缺少回归模型，无法进行宏观基准对比。")
        else:
            report_lines.append(f"   - 模型预测 SC_Sum: {pred_sc_sum:.2f}")
            if not benchmark_df_reg_filtered.empty and expert_sc_col in benchmark_df_reg_filtered.columns:
                age_avg_sum = pd.to_numeric(benchmark_df_reg_filtered[expert_sc_col], errors="coerce").mean()
                peer_desc = f"专家常模 (narratives.csv · '{story_type}', 年龄 {age}"
                if task_type is not None and 'task_type' in self.benchmark_db_reg.columns:
                    peer_desc += f", {task_type}"
                peer_desc += ")"
                report_lines.append(f"\n   - [{peer_desc}]")
                report_lines.append(f"     - 模型预测: {pred_sc_sum:.2f}")
                report_lines.append(f"     - 专家 SC_Sum 常模均值: {age_avg_sum:.2f} (n={len(benchmark_df_reg_filtered)})")
                report_lines.append(f"     - {'高于专家常模均值' if pred_sc_sum > age_avg_sum else '低于或接近专家常模均值'}")
            else:
                report_lines.append(f"\n   - [!] 在基准库中未找到匹配的同类数据 (story_type={story_type}, age={age}" + (f", task_type={task_type}" if task_type else "") + ")，跳过对比。")
        # --- [!! V5 修复 2 + V6 结束 !!] ---

        
        # --- [!! V4 修改 !!] ---
        # 3. 多任务分类结果 (带置信度)
        report_lines.append("\n4. 多任务分类结果 (模块 E)")
        task_sum = 0
        for task_name in TASK_NAMES_GLOBAL: # [!] 遍历 A2-A16 的标准列表
            value = task_predictions[task_name]
            prob = task_predictions[f"{task_name}_prob"]
            report_lines.append(f"   - {task_name}: {value}  (置信度: {prob*100:.2f}%)") # [!] 修改
            task_sum += value
        report_lines.append(f"   ---------------------------------")
        report_lines.append(f"   - 多任务总分: {task_sum} / 15")
        # --- [!! V4 修改结束 !!] ---
        
        # [!] 添加一个 key 到 task_predictions 字典，用于汇总 CSV
        task_predictions['pred_MultiTask_Sum'] = task_sum

        # --- [!! V5 修复 3 + V6 task_type !!] ---
        # 4. 多任务基准对比 (按 age, story_type，若有则按 task_type)
        report_lines.append("\n5. 多任务基准对比 (模块 F - 多任务)")
        report_lines.append(f"   - 您的多任务总分: {task_sum}")
        
        multi_task_sum_col = (
            EXPERT_MICRO_SUM_COL
            if EXPERT_MICRO_SUM_COL in self.benchmark_db_multi.columns
            else "calculated_SS_Sum"
        )
        benchmark_df_multi_filtered = pd.DataFrame()  # 供后续发展水平定位使用
        if multi_task_sum_col not in self.benchmark_db_multi.columns:
            report_lines.append(f"  [F 警告] 在多任务基准库中未找到专家微观总分列，跳过多任务对比。")
        else:
            mask_multi = (self.benchmark_db_multi['age'] == age) & (self.benchmark_db_multi['story_type'] == story_type)
            if task_type is not None and 'task_type' in self.benchmark_db_multi.columns:
                t_ref = self.benchmark_db_multi['task_type'].astype(str).str.strip().str.lower()
                t_in = str(task_type).strip().lower()
                mask_multi = mask_multi & (t_ref == t_in)
            benchmark_df_multi_filtered = self.benchmark_db_multi[mask_multi]
            
            if not benchmark_df_multi_filtered.empty:
                age_avg_multi_sum = pd.to_numeric(
                    benchmark_df_multi_filtered[multi_task_sum_col], errors="coerce"
                ).mean()
                peer_desc = f"专家常模 (narratives.csv · '{story_type}', 年龄 {age}"
                if task_type is not None and 'task_type' in self.benchmark_db_multi.columns:
                    peer_desc += f", {task_type}"
                peer_desc += ")"
                report_lines.append(f"\n   - [{peer_desc}]")
                report_lines.append(f"     - 模型微观总分: {task_sum}")
                report_lines.append(f"     - 专家 A2–A16 总分常模均值: {age_avg_multi_sum:.2f} (n={len(benchmark_df_multi_filtered)})")
                report_lines.append(f"     - {'高于专家常模均值' if task_sum > age_avg_multi_sum else '低于或接近专家常模均值'}")
            else:
                report_lines.append(f"\n   - [!] 在基准库中未找到匹配的同类数据 (story_type={story_type}, age={age}" + (f", task_type={task_type}" if task_type else "") + ")，跳过对比。")
        # --- [!! V5 修复 3 + V6 结束 !!] ---
        
        # --- [!! V6: 发展水平定位 (Developmental stage indicators, 论文 3.2) !!] ---
        report_lines.append("\n6. 发展水平定位 (Developmental Stage)")
        above_reg = (
            self._has_regression_models
            and pred_sc_sum is not None
            and not benchmark_df_reg_filtered.empty
            and expert_sc_col in benchmark_df_reg_filtered.columns
            and pred_sc_sum > pd.to_numeric(benchmark_df_reg_filtered[expert_sc_col], errors="coerce").mean()
        )
        above_multi = (
            multi_task_sum_col in self.benchmark_db_multi.columns
            and not benchmark_df_multi_filtered.empty
            and task_sum > pd.to_numeric(benchmark_df_multi_filtered[multi_task_sum_col], errors="coerce").mean()
        )
        if self._has_regression_models and not benchmark_df_reg_filtered.empty:
            pos_reg = "高于同龄同组平均" if above_reg else "低于或接近同龄同组平均"
        else:
            pos_reg = "未可用（缺回归模型）" if not self._has_regression_models else "无同类参照"
        if multi_task_sum_col in self.benchmark_db_multi.columns and not benchmark_df_multi_filtered.empty:
            pos_multi = "高于同龄同组平均" if above_multi else "低于或接近同龄同组平均"
        else:
            pos_multi = "无同类参照"
        report_lines.append(f"   - 宏观 SC（情节完整性）: {pos_reg}。")
        report_lines.append(f"   - 宏观 SS（故事结构）完整性: {pos_multi}。")
        if not benchmark_df_reg_filtered.empty or (multi_task_sum_col in self.benchmark_db_multi.columns and not benchmark_df_multi_filtered.empty):
            report_lines.append(f"   - 综合: 该叙事在「年龄 {age} 岁、主题 {story_type}" + (f"、任务 {task_type}" if task_type else "") + "」的参照组中，整体处于" + ("较好" if (above_reg or above_multi) else "中等或待提升") + "水平。")
        else:
            report_lines.append("   - 暂无同类参照数据，无法给出发展水平定位；请确认基准库包含匹配的 age / story_type / task_type。")
        # --- [!! V6 结束 !!] ---
        
        if narrative_quality.get("status") == "low_quality":
            report_lines.append(f"\n【质量提示】{narrative_quality.get('message', '')}")
        if narrative_quality.get("sc_capped"):
            report_lines.append(
                "【SC 约束】语言产出偏少或质量偏低，宏观总分已按规则上限收敛（beta）。"
            )

        report_lines.append("\n--- 报告结束 ---")
        
        return (
            "\n".join(report_lines),
            regression_results,
            task_predictions,
            linguistic_metrics,
            narrative_quality,
        )

# ==============================================================================
# --- ( ! ) [新] 主程序入口 (批量处理版 V3 - 最终修复) ( ! ) ---
# ==============================================================================

if __name__ == "__main__":
    
    # --- 批量配置 ---
    NEW_DATA_FILE = "new_data.csv"
    OUTPUT_REPORT_DIR = "batch_reports"  # 与 participant_reports 的父目录（已不再生成单条 report_index_* 文件）
    OUTPUT_PARTICIPANT_REPORT_DIR = "batch_reports/participant_reports"  # 按参与者汇总的融合报告（含各故事完整分析）
    OUTPUT_CSV_FILE = "batch_predictions_summary.csv" # 包含所有预测结果的总表
    
    # 1. 创建输出文件夹
    os.makedirs(OUTPUT_REPORT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_PARTICIPANT_REPORT_DIR, exist_ok=True)
    
    # 2. 加载新数据
    try:
        df_new = pd.read_csv(NEW_DATA_FILE)
        
        # [!! 重要 !!] 检查 'text', 'story_type', 'age', 'left_behind' 列是否存在
        if 'text' not in df_new.columns and 'Text' in df_new.columns:
            df_new.rename(columns={'Text': 'text'}, inplace=True)
        elif 'text' not in df_new.columns:
            print("  [警告] 在 new_data.csv 中未找到 'text' 或 'Text' 列，正在将第一列重命名为 'text'。")
            df_new.rename(columns={df_new.columns[0]: 'text'}, inplace=True)
            
        # 检查其他必要的元数据列
        required_cols = ['story_type', 'age', 'left_behind']
        if not all(col in df_new.columns for col in required_cols):
            print(f"❌ 致命错误: 您的 '{NEW_DATA_FILE}' 必须包含以下列: {required_cols}")
            exit()
            
        print(f"--- 成功加载 '{NEW_DATA_FILE}', 准备分析 {len(df_new)} 条文本 ---")
    
    except FileNotFoundError:
        print(f"❌ 致命错误: 找不到数据文件 '{NEW_DATA_FILE}'。")
        exit()
    except Exception as e:
        print(f"❌ 致命错误: 加载 '{NEW_DATA_FILE}' 时出错: {e}")
        exit()

    all_regression_results = []
    all_task_predictions = []
    all_single_report_contents = {}  # index -> 单条报告全文（仅用于嵌入参与者报告，不再单独落盘）

    try:
        # 3. 初始化预测器 (只执行一次)
        predictor = AutomatedNarrativePredictor(MODEL_PATHS)
        
        print(f"\n--- 开始批量处理 {len(df_new)} 条文本 ---")
        
        # 4. 循环遍历 DataFrame 的每一行
        for index, row in tqdm(df_new.iterrows(), total=len(df_new), desc="批量分析中"):
            
            try:
                # 从行中获取数据
                text_to_analyze = str(row['text'])
                story_type = str(row['story_type'])
                
                # --- [!! 最终修复 !!] ---
                # 1. 尝试将 'age' 转换为数字
                age_val = pd.to_numeric(row['age'], errors='coerce')
                # 2. 如果是 NaN (空) 则设为0, 否则转为 int
                age = 0 if pd.isna(age_val) else int(age_val)
                
                # 1. 尝试将 'left_behind' 转换为数字 (这将对 "Partially Left-Behind" 返回 NaN)
                lb_val = pd.to_numeric(row['left_behind'], errors='coerce')
                # 2. 如果是 NaN (转换失败) 则设为0, 否则转为 int
                left_behind = 0 if pd.isna(lb_val) else int(lb_val)
                # --- [!! 修复结束 !!] ---
                
                # [V6] 可选: task_type（讲述/复述），用于与论文 4.2.3 一致的基准对比
                task_type = str(row['task_type']).strip() if 'task_type' in df_new.columns and pd.notna(row.get('task_type')) else None
                if task_type is not None and (task_type == '' or task_type.lower() == 'nan'):
                    task_type = None
                
                # 5. 执行预测
                final_report, regression_results, task_predictions, _ling, _q = predictor.predict(
                    text_to_analyze,
                    story_type,
                    age,
                    left_behind,
                    task_type=task_type
                )
                
                # 存储结果以便最后保存到总表
                all_regression_results.append(regression_results)
                all_task_predictions.append(task_predictions)
                
                # 6. 单条报告内容仅存入内存，用于嵌入参与者报告（不再单独写 report_index_* 文件）
                meta_line = "元数据: story_type={}, age={}, left_behind={}".format(story_type, age, left_behind)
                if task_type is not None:
                    meta_line += ", task_type={}".format(task_type)
                single_full = "分析索引: {}\n分析文本: {}\n{}\n{}".format(index, text_to_analyze, meta_line, final_report)
                all_single_report_contents[index] = single_full

            except Exception as e:
                print(f"--- ❌ 跳过第 {index} 行，发生错误: {e} ---")
                all_regression_results.append({}) # 添加空字典以保持行对应
                all_task_predictions.append({})   # 添加空字典以保持行对应

        print("\n--- 批量处理完成 ---")

        # 7. 保存汇总的 CSV 结果
        df_reg_results = pd.DataFrame(all_regression_results)
        df_task_results = pd.DataFrame(all_task_predictions)
        
        # 将原始数据与新预测合并
        # [!] V5 修复: 重置 df_new 的索引以确保 concat 对齐
        df_final_summary = pd.concat([df_new.reset_index(drop=True), df_reg_results.reset_index(drop=True), df_task_results.reset_index(drop=True)], axis=1)
        # 数值列统一保留小数点后 2 位再写入 CSV
        for c in df_final_summary.columns:
            if df_final_summary[c].dtype in (np.floating, 'float64', 'float32'):
                df_final_summary[c] = df_final_summary[c].round(2)
        
        df_final_summary.to_csv(OUTPUT_CSV_FILE, index=False, encoding='utf-8-sig')
        
        print(f"\n--- ✅ 汇总的 CSV 已保存到 '{OUTPUT_CSV_FILE}' ---")

        # 8. 按参与者汇总报告（若 new_data 中有 participants 列）：面向家长的可读版 + 常模对比
        STORY_NAMES = {'cat': '小猫与蝴蝶', 'dog': '小狗与香肠', 'bird': '小鸟一家', 'goat': '小羊与狐狸'}
        if 'participants' in df_final_summary.columns:
            bench_reg, bench_multi = None, None
            multi_col = 'calculated_SS_Sum'
            try:
                bench_reg = pd.read_csv(MODEL_PATHS['benchmark_db_regression'])
                bench_reg['age'] = pd.to_numeric(bench_reg['age'], errors='coerce').fillna(0)
                bench_multi = pd.read_csv(MODEL_PATHS['benchmark_db_multitask'])
                bench_multi['age'] = pd.to_numeric(bench_multi['age'], errors='coerce').fillna(0)
                if multi_col not in bench_multi.columns:
                    task_cols = [c for c in TASK_NAMES_GLOBAL if c in bench_multi.columns]
                    if task_cols:
                        bench_multi[multi_col] = bench_multi[task_cols].sum(axis=1)
            except Exception as e:
                print(f"  [!] 加载参照库失败: {e}")
            part_col = 'participants'
            for pid, grp in df_final_summary.groupby(part_col, sort=True):
                pid = pid if pd.notna(pid) else 'unknown'
                part_age = int(grp['age'].dropna().iloc[0]) if len(grp['age'].dropna()) > 0 else None
                has_reg = 'pred_SC_Sum' in grp.columns and grp['pred_SC_Sum'].notna().any()
                has_multi = 'pred_MultiTask_Sum' in grp.columns and grp['pred_MultiTask_Sum'].notna().any()
                part_mean_reg = float(grp['pred_SC_Sum'].dropna().mean()) if has_reg else None
                part_mean_m = float(grp['pred_MultiTask_Sum'].dropna().mean()) if has_multi else None
                # 宏观常模：优先用回归库 pred_SC_Sum；若全为 0 则用多任务库的 SC_Sum（专家评分）作参照
                ref_reg_mean, ref_reg_n, ref_reg_age_mean, ref_reg_age_n = None, 0, None, 0
                if bench_reg is not None and 'pred_SC_Sum' in bench_reg.columns:
                    ref_all = bench_reg['pred_SC_Sum'].dropna()
                    ref_reg_n = len(ref_all)
                    ref_reg_mean = float(ref_all.mean())
                    if part_age is not None and ref_reg_n > 0:
                        ref_age = bench_reg[bench_reg['age'] == part_age]['pred_SC_Sum'].dropna()
                        ref_reg_age_n = len(ref_age)
                        ref_reg_age_mean = float(ref_age.mean()) if ref_reg_age_n > 0 else ref_reg_mean
                if (ref_reg_mean is None or ref_reg_n == 0 or ref_reg_mean == 0) and bench_multi is not None and 'SC_Sum' in bench_multi.columns:
                    s = bench_multi['SC_Sum'].dropna()
                    ref_reg_n = len(s)
                    ref_reg_mean = float(s.mean())
                    if part_age is not None and ref_reg_n > 0:
                        sa = bench_multi[bench_multi['age'] == part_age]['SC_Sum'].dropna()
                        ref_reg_age_n = len(sa)
                        ref_reg_age_mean = float(sa.mean()) if ref_reg_age_n > 0 else ref_reg_mean
                ref_m_mean, ref_m_n, ref_m_age_mean, ref_m_age_n = None, 0, None, 0
                if bench_multi is not None and multi_col in bench_multi.columns:
                    rm = bench_multi[multi_col].dropna()
                    ref_m_n = len(rm)
                    ref_m_mean = float(rm.mean())
                    if part_age is not None and ref_m_n > 0:
                        rma = bench_multi[bench_multi['age'] == part_age][multi_col].dropna()
                        ref_m_age_n = len(rma)
                        ref_m_age_mean = float(rma.mean()) if ref_m_age_n > 0 else ref_m_mean
                # ----- 家长版报告：约 2 分钟阅读，篇幅适中、说清即可 -----
                lines = []
                lines.append("")
                lines.append("╔══════════════════════════════════════════════════════════════════════════╗")
                lines.append("║                    儿童叙事能力评估报告 · 家长版                           ║")
                lines.append("╚══════════════════════════════════════════════════════════════════════════╝")
                lines.append("")
                lines.append("本报告根据孩子完成的 {} 个叙事任务（四个主题故事）生成，得分已与参照库（约 564 名 4–6 岁儿童）对比，便于了解孩子在同龄人中的大致位置。".format(len(grp)))
                lines.append("")
                lines.append("一、本报告看什么")
                lines.append("  · 故事结构（满分 9 分）：孩子能否把故事的「开头—经过—结果」说清楚，有无起因、目标、行动和结局。")
                lines.append("  · 情节与细节（15 项）：是否提到「为什么」「心里怎么想」「结果怎样」等，项数越多说明表达越丰富。")
                lines.append("")
                lines.append("二、各故事表现")
                rows_list = list(grp.iterrows())
                for i, (idx, row) in enumerate(rows_list, 1):
                    st = str(row.get('story_type', '—'))
                    story_name = STORY_NAMES.get(st, st)
                    sc = row.get('pred_SC_Sum')
                    mt = row.get('pred_MultiTask_Sum')
                    sc_val = float(sc) if pd.notna(sc) else None
                    mt_val = int(mt) if pd.notna(mt) else None
                    lines.append("  （{}）《{}》 结构 {:.2f}/9 分，细节 {}/15 项。".format(
                        i, story_name,
                        sc_val if sc_val is not None else 0,
                        int(mt_val) if mt_val is not None else 0))
                    if sc_val is not None and mt_val is not None:
                        if sc_val >= 7.0 and mt_val >= 12:
                            lines.append("     本故事结构较完整、细节也较丰富。")
                        elif sc_val >= 5.0 and mt_val >= 8:
                            lines.append("     本故事脉络基本清楚，部分环节可再充实。")
                        else:
                            lines.append("     可多鼓励孩子说清「后来呢」「为什么」和角色感受。")
                lines.append("")
                lines.append("三、整体小结")
                if has_reg and part_mean_reg is not None:
                    s = grp['pred_SC_Sum'].dropna()
                    if len(s) > 0:
                        lines.append("  · 故事结构：平均 {:.2f} 分（最高 {:.2f}，最低 {:.2f}）。".format(part_mean_reg, s.max(), s.min()))
                    else:
                        lines.append("  · 故事结构：平均 {:.2f} 分。".format(part_mean_reg))
                if has_multi and part_mean_m is not None:
                    m = grp['pred_MultiTask_Sum'].dropna()
                    if len(m) > 0:
                        lines.append("  · 情节与细节：平均 {:.2f} 项/15 项（最多 {} 项，最少 {} 项）。".format(part_mean_m, int(m.max()), int(m.min())))
                    else:
                        lines.append("  · 情节与细节：平均 {:.2f} 项/15 项。".format(part_mean_m))
                lines.append("")
                lines.append("四、与同龄人对比")
                n_ref = ref_reg_n if ref_reg_n > 0 else ref_m_n
                lines.append("  参照库为约 {} 名 4–6 岁儿童，使用相同故事任务。".format(n_ref))
                if part_mean_reg is not None and ref_reg_mean is not None and ref_reg_n > 0:
                    above_reg = part_mean_reg > ref_reg_mean
                    lines.append("  · 故事结构：孩子平均 {:.2f} 分，同龄平均 {:.2f} 分 → 总体{}同龄水平。".format(
                        part_mean_reg, ref_reg_age_mean if ref_reg_age_mean is not None and ref_reg_age_n > 0 else ref_reg_mean,
                        "高于" if above_reg else "低于"))
                if part_mean_m is not None and ref_m_mean is not None and ref_m_n > 0:
                    above_m = part_mean_m > ref_m_mean
                    lines.append("  · 情节与细节：孩子平均 {:.2f} 项/15 项，同龄平均 {:.2f} 项 → 总体{}同龄水平。".format(
                        part_mean_m, ref_m_age_mean if ref_m_age_mean is not None and ref_m_age_n > 0 else ref_m_mean,
                        "高于" if above_m else "低于"))
                lines.append("")
                lines.append("五、使用说明")
                lines.append("  本报告仅供了解发展参考，不替代专业诊断；如有疑问请咨询实施方或专业人员。")
                lines.append("")
                lines.append("═══════════════════════════════════════════════════════════════════════════")
                out_path = os.path.join(OUTPUT_PARTICIPANT_REPORT_DIR, f"participant_report_{pid}.txt")
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(lines))
            n_part = df_final_summary['participants'].nunique()
            print(f"--- ✅ 已按参与者生成 {n_part} 份家长可读报告到 '{OUTPUT_PARTICIPANT_REPORT_DIR}'（含常模对比）---")

    except Exception as e:
        print(f"\n--- ❌ 预测过程中发生严重错误 ---")
        print(e)
        import traceback
        traceback.print_exc()