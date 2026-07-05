---
name: survey-analysis
description: Analyze survey data — descriptive statistics, top-box/top-2-box satisfaction scoring, driver analysis, significance testing, trend over time, and benchmarking — AND test for measurement equivalence across language/cultural groups before comparing them. Use whenever a user has survey responses and wants results, scores, comparisons across groups or time, key-driver analysis, or statistical testing. Apply the shared 3MC lens — never compare groups until you've ruled out that a difference is a measurement or mode artefact rather than a real one. Work on de-identified/synthetic data only — no PHI.
---

# Survey Analysis

Turn responses into defensible estimates and comparisons.

## Load first
- `../../shared/tse-framework.md` — reason per statistic; know your dominant error source.
- `../../shared/3mc-considerations.md` — comparison error gates group comparisons.

## Data handling
Operate on de-identified or synthetic data. Do not ingest PHI or respondent identifiers.

## Workflow
1. **Prepare:** clean, code, apply weights from the sampling plan; document processing (processing error is real).
2. **Describe:** distributions, top-box/top-2-box for satisfaction, item nonresponse.
3. **Compare — with a gate:** before reporting any group or time difference, check **measurement equivalence** (`references/measurement-equivalence.md`). If items don't measure the same construct the same way across groups, the comparison is invalid; say so.
4. **Significance:** apply appropriate tests with survey weights/design; report uncertainty, not just point estimates.
5. **Drivers:** key-driver analysis linking item satisfaction to overall outcomes (note correlation ≠ cause).
6. **Trend & benchmark:** compare to prior waves and external benchmarks where comparable.

## Output
Analysis results with: weighted estimates and uncertainty, top-box scores, validated (or flagged) group comparisons, driver findings, and an explicit note on the dominant remaining error sources and their likely direction.

## References
- `references/core-analysis.md` — scoring, weighting, testing, drivers.
- `references/measurement-equivalence.md` — the gate before group comparison.
