# Appendix D. Code Availability and Reproducibility

To support reproducibility, all model implementations, preprocessing pipelines, and evaluation scripts are made available in a public code repository. The repository includes the following components:

1. **Preprocessing and shallow features**  
   - Jieba-based tokenization and calculable linguistic features (`linguistic_feature_extractor.py`).  
   - Ten-dimensional automated feature extraction combining BART-generated cues and keyword-based internal-state counts (`automated_feature_extractor.py`).

2. **BART-based cue generation (Module B)**  
   - Training script for the sequence-to-sequence cue generator (`train_model_b_t5_generator.py`).  
   - Inference wrapper for generating `predicted_ist_words` from new narratives (`bart_predictor.py`).

3. **Cue-enhanced BERT micro-structural classifier (Module E)**  
   - Training scripts for the multi-task (A2–A16) classifier with LoRA, including the schema-guided QA template set aligned with the study protocol (`train.py`, `train_clue_augmented_model.py`, and ablation variants in `train_clue_augmented_noQA.py`, `train_clue_augmented_noist.py`).  
   - Question templates per story type (`cat`, `dog`, `bird`, `goat`) are defined in code and match Appendix B of the manuscript.

4. **XGBoost-based macro-structural regression (Module D)**  
   - Champion regression pipeline using BERT embeddings plus pre-computed linguistic columns from `narratives.csv` (`regression_analysis_final.py`).  
   - Fully automated regression pipeline using BART + 10-D auto features + BERT (`train_final_automated_model.py`), consumed by the end-to-end predictor.

5. **End-to-end prediction and reporting (Module 4)**  
   - Single entry point: BART → Jieba/auto features → BERT multitask → XGBoost regression → norm-referenced benchmarks → optional per-participant parent-facing reports (`predict_and_report.py`).

6. **Evaluation and analysis**  
   - Micro-structural classification: error analysis and supplementary analyses (`analyze_errors.py`, `analysis.py`).  
   - Macro-structural regression: error analysis (`analyze_errors_regression.py`), extended regression analytics (`analysis_reg.py`, `analysis_reg_update_12.py`).

7. **Norm-referenced comparison**  
   - Benchmark CSV paths are configurable in `predict_and_report.py` (regression and multitask reference databases). Percentile or group-mean comparisons are computed in-script against these references (see Appendix E in the manuscript for the norm construction).

**Data and ethics.** Raw narrative transcripts and identifiable participant metadata are **not** included in the repository, in accordance with ethical approval and confidentiality requirements. A **minimal anonymized template** illustrating the required CSV columns for batch prediction is provided as `sample_new_data_template.csv` (synthetic placeholder text only).

**Repository.**  
- Public repository (post-acceptance / attribution): **https://github.com/Joey629/BERT**  
- For double-blind review, replace the URL above with the anonymized link supplied by the journal or **https://anonymous.4open.science/r/XXXX** as required.

**Reproducibility notes.**  
- Pretrained BERT multitask weights (e.g. `best_model_*_macrof1_*.pth`), trained BART checkpoint directory (`model_b_bart_structured_generator/`), and XGBoost joblib files under `automated_champion_models/` or `champion_models_*` are large binary artifacts. They may be distributed via release assets, institutional storage, or Git LFS; the repository documents expected paths in `predict_and_report.py` and `Annotation.md`.  
- Python dependencies follow standard `transformers`, `torch`, `jieba`, `xgboost`, `peft`, and `pandas` usage; a `requirements.txt` is provided in the repository root.

**Script index.** A concise map of all Python entry points is maintained in **`Annotation.md`** at the repository root.
