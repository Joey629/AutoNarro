# Appendix E. Norm-Referenced Percentile Distributions for Narrative Performance

This appendix presents percentile distributions for **micro-structural** and **macro-structural** narrative scores derived from the full annotated corpus (**N = 564**; update *N* to your final sample size after exclusions), stratified by **age group** (4, 5, and 6 years) and **task type** (storytelling vs. retelling). These distributions constitute the reference database used by the Predictor/Report Generator module to situate individual children’s automated scores within age- and task-matched normative comparisons (see Section 3.2).

**Percentile ranks** were computed from raw scores using the **nearest-rank** method (or equivalent empirical CDF as implemented in your analysis software). The norm-referenced system positions an individual child’s score at the corresponding percentile within the matched subgroup, enabling interpretable reporting of the form: *“This child’s narrative performance falls at approximately the Xth percentile for [age]-year-old children in the [task type] condition.”*

**Micro-structural scores** reflect the total number of narrative elements (A2–A16) coded as present (**range: 0–15**).

**Macro-structural scores** reflect the summed episode-level complexity across three episodes (**SC_Sum = SC_E1 + SC_E2 + SC_E3**), with each episode scored **0–3** in the annotation scheme, hence **SC_Sum range: 0–9** (theoretical minimum 0; empirical max in the reference corpus may be slightly below 9 depending on coding rules).

All scores used for **norm construction** were based on **expert annotations** rather than model predictions, ensuring that the reference distributions reflect ground-truth developmental benchmarks. Model-based predictions are compared *to* these norms at inference time.

---

## Optional: alignment with repository scripts

Benchmark CSVs used in `predict_and_report.py` (e.g. multitask predictions with expert labels **A2–A16** and **SC_Sum**) can be used to **reproduce** subgroup descriptive statistics; see `appendix_e_compute_norms.py` in this repository for a template `pandas` workflow (stratify by `age` and `task_type`, compute percentiles for micro and macro columns).
