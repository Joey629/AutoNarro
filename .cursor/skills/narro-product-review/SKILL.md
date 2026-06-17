---
name: narro-product-review
description: >-
  Runs a structured Narro/AutoNarro product review across architecture, code
  security, and UX. Use when the user asks for a full product review, architecture
  audit, UX walkthrough, security pass, or to compare fixes against the Top-10
  baseline checklist.
---

# Narro Product Review

## When to use

- Full-stack review before release or after major refactors
- Re-audit after implementing Top-10 fixes (compare to [BASELINE_CHECKLIST.md](BASELINE_CHECKLIST.md))
- Onboarding: understand Narro POC boundaries (single-tenant appliance vs SaaS)

## Review workflow

Run **three passes** (can use parallel subagents), then **one summary**:

1. **Architecture** — `backend/`, `src/`, `configs/`, `run_web.py`, deployment docs  
2. **Code & security** — auth, store, ML pipeline, frontend XSS, Docker, tests  
3. **UX** — `frontend/index.html`, `frontend/static/js/app.js`, `frontend/static/css/narro.css`

### Required reading (architecture)

| Path | Focus |
|------|--------|
| `backend/api/main.py` + `backend/api/routers/` | API surface, auth deps |
| `backend/evaluation_service.py` | Inference orchestration, locks |
| `src/pipeline_predict_report.py` | ML pipeline |
| `backend/evaluation_store.py` | SQLite, `tenant_id` |
| `configs/model_registry.json` | Model versions |

### Required reading (UX)

| Path | Focus |
|------|--------|
| `frontend/index.html` | IA: session vs history, profile, mobile |
| `frontend/static/js/app.js` | Flows, dialogs, evaluation |
| `frontend/static/js/narro-ui.js` | Shared escape/download helpers |

## Output template

```markdown
# Narro Product Review — [date]

## Executive summary
- 3–5 bullets

## P0 / P1 / P2
| ID | Area | Issue | Path | Status vs baseline |

## Top-10 action items (track)
| # | Item | Status: done / partial / open |

## Recommendations (ordered)
1. …
```

## Severity rules

- **P0**: Data leak, auth bypass, wrong scores, blocked primary user path  
- **P1**: Security hardening, major UX friction, maintainability debt  
- **P2**: Polish, docs, nice-to-have refactors  

## Baseline comparison

After each fix batch, open [BASELINE_CHECKLIST.md](BASELINE_CHECKLIST.md) and update item status.  
Optional: run `python .cursor/skills/narro-product-review/scripts/check_baseline.py` (if present).

## Product constraints (do not forget)

- Target users: caregivers, children 4–6, Chinese picture-story narratives  
- **Not** a clinical diagnosis tool — disclaimers must stay visible  
- Default deployment model: **one tenant per process** (`NARRO_TENANT_ID`), optional API keys  
- ML path: BART → features → quality gate → BERT micro + XGB macro → norms → report  

## Additional resources

- Full checklist with file hints: [BASELINE_CHECKLIST.md](BASELINE_CHECKLIST.md)
- Machine-readable status: [baseline-status.json](baseline-status.json)
