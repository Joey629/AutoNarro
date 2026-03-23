# Narrative micro- & macro-structure assessment (BERT + BART + XGBoost)

Code for cue-enhanced BERT multi-task classification (A2–A16), BART-based cue generation, XGBoost macro-structural regression (SC_E1/E2/E3), and norm-referenced prediction reports.

## Quick start (inference)

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Place **trained weights** where `predict_and_report.py` expects them (see `MODEL_PATHS` in that file): multitask `.pth`, BART folder `model_b_bart_structured_generator/`, and XGBoost models under `automated_champion_models/` or `champion_models_*`.
3. Prepare input CSV from `sample_new_data_template.csv` (required columns: `text` or `Text`, `story_type`, `age`, `left_behind`; optional `task_type`, `participants`). Save as `new_data.csv` locally (**not committed**).
4. Run:
   ```bash
   python predict_and_report.py
   ```
   Outputs: `batch_predictions_summary.csv`, `batch_reports/participant_reports/` (if `participants` column present).

## Documentation

- **`Annotation.md`** — index of all Python scripts and their roles.  
- **`docs/APPENDIX_D_Code_Availability.md`** — manuscript-style appendix (code availability & reproducibility).

**Script naming:** `train_*` = training; `analyze_*` = analysis & diagnostics; `bart_cue_*` = BART cue pipeline; `*_ablation_*` = multitask ablations. See `Annotation.md` for the full map (legacy names like `train_model_b_t5_generator` / `analysis_reg_update_12` were renamed for clarity).

## Data policy

**Raw transcripts and study CSVs (`narratives.csv`, `new_data.csv`, etc.) are git-ignored** to protect participants. Only the anonymized column template `sample_new_data_template.csv` is versioned.

## License / citation

Add your license and citation text after manuscript acceptance.
