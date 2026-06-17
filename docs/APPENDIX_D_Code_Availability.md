# Appendix D. Code Availability and Reproducibility

To support reproducibility, all model implementations, preprocessing pipelines, and evaluation scripts are made available in a public code repository. The repository includes the following components:

1. **Preprocessing and shallow features**  
   - Jieba-based tokenization and calculable linguistic features (`linguistic_feature_extractor.py`).  
   - Ten-dimensional automated feature extraction combining BART-generated cues and keyword-based internal-state counts (`automated_feature_extractor.py`).

2. **BART-based cue generation (Module B)**  
   - Training script for the sequence-to-sequence cue generator (`bart_train_cue_generator.py`).  
   - Inference wrapper for generating `predicted_ist_words` from new narratives (`bart_cue_predictor.py`).

3. **Cue-enhanced BERT micro-structural classifier (Module E)**  
   - Training scripts for the multi-task (A2–A16) classifier with LoRA, including the schema-guided QA template set aligned with the study protocol (`train.py`, `train_multitask_cue_augmented.py`, and ablation variants `train_multitask_ablation_no_qa.py`, `train_multitask_ablation_no_ist.py`).  
   - Question templates per story type (`cat`, `dog`, `bird`, `goat`) are defined in code and match Appendix B of the manuscript.

4. **XGBoost-based macro-structural regression (Module D)**  
   - Expert-cue regression: micro-aligned BERT [CLS] features plus pre-computed linguistic columns from `narratives.csv` (`regression_expert_xgb_m4.py`; shared encoding in `regression_m4_bert_encoder.py`).  
   - Fully automated pipeline: BART-predicted cues + 10-D auto features + the same micro-aligned BERT encoder (`regression_automated_xgb_m4.py`), consumed by the end-to-end predictor.

5. **End-to-end prediction and reporting (Module 4)**  
   - Single entry point: BART → Jieba/auto features → BERT multitask → XGBoost regression → norm-referenced benchmarks → optional per-participant parent-facing reports (`predict_and_report.py`).

6. **Evaluation and analysis**  
   - Micro-structural classification: error analysis and supplementary analyses (`analyze_multitask_errors.py`, `analyze_multitask_metadata.py`).  
   - Macro-structural regression: held-out performance and error-case export (`analyze_regression_errors.py`); metadata and subgroup summaries (`analyze_regression_metadata.py`). Shared implementation: `regression_macro_analysis_core.py`.

7. **Norm-referenced comparison**  
   - Benchmark CSV paths are configurable in `predict_and_report.py` (regression and multitask reference databases). Percentile or group-mean comparisons are computed in-script against these references (see Appendix E in the manuscript for the norm construction).

**Data and ethics.** Raw narrative transcripts and identifiable participant metadata are **not** included in the repository, in accordance with ethical approval and confidentiality requirements. A **minimal anonymized template** illustrating the required CSV columns for batch prediction is provided as `sample_new_data_template.csv` (synthetic placeholder text only).

**Repository.**  
- Public repository (post-acceptance / attribution): **https://github.com/Joey629/BERT**  
- For double-blind review, replace the URL above with the anonymized link supplied by the journal or **https://anonymous.4open.science/r/XXXX** as required.

**Reproducibility notes.**  
- Pretrained multitask weights (`models/micro_narro_v4.pth`), BART checkpoint (`models/bart_narro_v4/`), and XGBoost joblib files under `models/macro_xgb_narro_v4/` are large binary artifacts. They may be distributed via release assets, institutional storage, or Git LFS; expected paths are in `configs/model_registry.json`, `src/pipeline_predict_report.py`, and `Annotation.md`.  
- Python dependencies follow standard `transformers`, `torch`, `jieba`, `xgboost`, `peft`, and `pandas` usage; a `requirements.txt` is provided in the repository root.

**Script index.** A concise map of all Python entry points is maintained in **`Annotation.md`** at the repository root.

---

## Copy-paste block for the manuscript (English)

**Appendix D. Code Availability and Reproducibility**

To support reproducibility, all model implementations, preprocessing pipelines, and evaluation scripts are made available via a public repository. The repository includes: (i) Jieba-based tokenization and ten-dimensional automated feature extraction (`linguistic_feature_extractor.py`, `automated_feature_extractor.py`); (ii) training and inference for the BART-based cue generation module (`bart_train_cue_generator.py`, `bart_cue_predictor.py`); (iii) training scripts for the cue-enhanced BERT micro-structural classifier with the complete schema-guided QA template set (`train.py`, `train_multitask_cue_augmented.py`, and ablations); (iv) training scripts for XGBoost-based macro-structural regression aligned with the micro-classifier (`regression_expert_xgb_m4.py`, `regression_automated_xgb_m4.py`, `regression_m4_bert_encoder.py`); (v) end-to-end prediction and norm-referenced reporting (`predict_and_report.py`); and (vi) evaluation and error-analysis utilities (`analyze_multitask_metadata.py`, `analyze_multitask_errors.py`, `analyze_regression_errors.py`, `analyze_regression_metadata.py`). Raw narrative transcripts are not included in order to protect participant confidentiality in accordance with ethical approval. A minimal anonymized CSV template (`sample_new_data_template.csv`) illustrates the required input format.

**Public repository:** https://github.com/Joey629/BERT  

For double-blind review, substitute the URL above with the anonymized repository link required by the venue (e.g. https://anonymous.4open.science/r/XXXX). The repository will retain full author attribution upon acceptance.
