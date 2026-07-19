# Measure & Meaning — Employee Domain

## Codebook · Annual Engagement & Retention Census · v0.1

**Status:** draft for owner review · **Repo target:** `skills/domain-hr-employee/references/codebook-employee-census.md`
**Companions:** `questionnaire-employee-census.md` v0.1 (field instrument) · `module-framework.md` v0.3 (item bank & rationale) · `codebook-employee-census.csv` (machine-readable variable list)

This codebook is the contract between fieldwork and analysis. Every rule below is **pre-registered** — fixed before data arrive, disclosed in the report's technical appendix, and applied without exception.

---

## 1 · ID convention

- IDs are **stable across waves** and never change meaning. Revised wording gets a new ID with a letter suffix (`ENG-01b`), and the old ID is retired, not reused.
- GAP items take the form `GAP-<CODE>-I` (importance) and `GAP-<CODE>-S` (satisfaction).
- The same IDs are used in the raw export, the crosstab workbook, and the `{{braces}}` report template. Renaming a variable anywhere breaks all three.

---

## 2 · Scales and value codes

| Scale | Codes | Labels |
|---|---|---|
| **AGREE-5** | 1–5 | 1 Strongly disagree · 2 Disagree · 3 Neither agree nor disagree · 4 Agree · 5 Strongly agree |
| **SAT-5** | 1–5 | 1 Very dissatisfied · 2 Dissatisfied · 3 Neither satisfied nor dissatisfied · 4 Satisfied · 5 Very satisfied |
| **IMP-7** | 1–7 | 1 Not at all important · 2 Slightly · 3 Somewhat · 4 Moderately · 5 Important · 6 Very · 7 Extremely important |
| **SAT-7** | 1–7 (+99) | 1 Very dissatisfied · 2 Dissatisfied · 3 Somewhat dissatisfied · 4 Neither satisfied nor dissatisfied · 5 Somewhat satisfied · 6 Satisfied · 7 Very satisfied · **99 Not applicable (off-scale)** |
| **NPS-11** | 0–10 | 0 Not at all likely … 10 Extremely likely |

**Missing-value codes (uniform across the instrument):**

| Code | Meaning | Treatment |
|---|---|---|
| `.` / blank | Item shown, not answered (skipped) | Excluded pairwise; skip rate reported per item |
| `99` | Not applicable / no experience — **`GAP-*-S` only** | Excluded from means; reported as coverage % |
| `98` | Prefer not to say — **`STY-03` and `SEG-*` only** | Treated as missing for breakouts; rate reported |
| `.n` | Item not shown (block not fielded in this configuration) | Distinguished from a skip in the export |

**The `99` rule.** `99` is never recoded to the scale midpoint (4) and never imputed. "No experience with this" and "neutral about this" are different states; collapsing them pulls means toward the centre on exactly the items with the thinnest coverage. *(Owner decision, 2026-07-19; rationale in `module-framework.md` §2.1.)*

---

## 3 · Variable list

### Block A — anchor

| ID | Scale | Notes |
|---|---|---|
| `SAT-00` | SAT-5 | Secondary criterion for the driver model; headline trend metric between waves. |

### Block B — CORE (engagement)

| ID | Scale | Reverse | Index |
|---|---|---|---|
| `ENG-01` … `ENG-06` | AGREE-5 | none | `IDX_ENG` |

### Block C — NPS

| ID | Scale | Notes |
|---|---|---|
| `NPS-01` | NPS-11 | Classification cutoffs are defined on 0–10; never rescale. |
| `NPS-02` | open text | Coded to themes; cross-tabbed by promoter class. |

### Block D — GAP (18 categories × 2)

| ID pattern | Scale | Notes |
|---|---|---|
| `GAP-<CODE>-I` | IMP-7 | No N/A option. |
| `GAP-<CODE>-S` | SAT-7 | N/A = 99, off-scale. |

Codes: `PAY REC MGR GRW LRN FLX WKL BEN MNG AUT TEA SEC RES VOI CRS SAF COM FDK`

Additional stored field: `GAP_ORDER` — the realized randomized display order of the 18 categories for that respondent (comma-separated codes). Required to test for order effects between waves.

### Block E — BRN (burnout screen)

| ID | Scale | Reverse | Index |
|---|---|---|---|
| `BRN-01` | AGREE-5 | no | `IDX_BRN` |
| `BRN-02` | AGREE-5 | **yes** | `IDX_BRN` |
| `BRN-03` | AGREE-5 | no | `IDX_BRN` |
| `BRN-04` | AGREE-5 | **yes** | `IDX_BRN` |
| `BRN-05` | AGREE-5 | no | `IDX_BRN` |
| `BRN-06` | AGREE-5 | no | `IDX_BRN` |

### Block F — STAY

| ID | Scale | Notes |
|---|---|---|
| `STY-01` | AGREE-5 | **Primary criterion** for the driver model. |
| `STY-02` | AGREE-5 | Higher = more leaving consideration; reported, not summed with STY-01. |
| `STY-03` | categorical 1–3, 98 | 1 Planning to stay · 2 Open to outside offers · 3 Actively looking · 98 Prefer not to say |

### Block G — OPEN

| ID | Type | Notes |
|---|---|---|
| `OPN-01`, `OPN-02` | open text | Standard census pair. |
| `OPN-03` | open text | Slot; `.n` when not fielded. |

### Block H — segmentation

| ID | Type | Categories |
|---|---|---|
| `SEG-TEN` | categorical 1–4 | 1 Less than 1 year · 2 1–2 years · 3 3–6 years · 4 7 years or more |
| `SEG-FUN` | categorical, client-specific, 98 | Mirrors HRIS department list. |
| `SEG-ROL` | categorical 1–4, 98 | 1 IC · 2 Team lead/supervisor · 3 Manager · 4 Senior leadership |
| `SEG-SIT` | categorical, client-specific, 98 | Mirrors HRIS site list. |
| `SEG-AGE` | categorical 1–5, 98 | 1 Under 25 · 2 25–34 · 3 35–44 · 4 45–54 · 5 55 or older |
| `SEG-CAR`, `SEG-EDU` | optional | `.n` when not fielded. |

**Tenure bands are non-overlapping by construction** (owner decision, 2026-07-19). The previous 1–3 / 3–7 grid is retired: it double-assigned employees at exactly 3 and 7 years. HRIS extracts must be re-banded to match this codebook, not the reverse.

### Quality & paradata

| ID | Type | Notes |
|---|---|---|
| `AC-01`, `AC-02` | AGREE-5 / SAT-7 | Attention checks. Pass = the instructed value. |
| `T_TOTAL` | seconds | Total completion time. |
| `T_<BLOCK>` | seconds | Page-level time per screen. |
| `DEVICE` | categorical | desktop / mobile / tablet / kiosk. |
| `SOURCE` | categorical | link / QR / kiosk. |

---

## 4 · Derived variables

### 4.1 Reverse-keying

Applied at scoring, **not** on screen:

```
BRN-02r = 6 − BRN-02
BRN-04r = 6 − BRN-04
```

General form for AGREE-5: `x_r = (min + max) − x = 6 − x`.

### 4.2 Indices

| Index | Definition | Conditions |
|---|---|---|
| `IDX_ENG` | Mean of `ENG-01…06`, rescaled 0–100: `(mean − 1) / 4 × 100` | Computed only if ≥ 4 of 6 items answered. |
| `IDX_BRN` | Sum of `BRN-01, BRN-02r, BRN-03, BRN-04r, BRN-05, BRN-06` (range 6–30) | Computed only if ≥ 5 of 6 items answered. |
| `BRN_TIER` | 6–13 = Low · 14–21 = Moderate · 22–30 = Elevated | **Pre-set cutpoints**, not sample terciles — so tiers are comparable across waves and clients. Disclosed in every report. |
| `NPS_CLASS` | 0–6 Detractor · 7–8 Passive · 9–10 Promoter | — |
| `ENPS` | % Promoters − % Detractors (percentage points) | Mean of `NPS-01` reported as a **secondary** statistic only. |
| `GAP_<CODE>` | `mean(GAP-<CODE>-I) − mean(GAP-<CODE>-S)` | Satisfaction mean excludes `99`. |
| `COV_<CODE>` | % of respondents answering `99` on `GAP-<CODE>-S` | Reported alongside every satisfaction mean. |
| `IMP_MED`, `SAT_MED` | Within-survey medians across the 18 category means | Define the GAP quadrant boundaries. **Recomputed each wave**; from wave 2 the prior wave's medians are also plotted for reference. *(Owner decision, 2026-07-19: medians, not scale midpoints.)* |

### 4.3 Driver model

- **Criterion:** `STY-01` (primary), `SAT-00` (secondary/validation).
- **Predictors:** the 18 `GAP-<CODE>-S` items plus `IDX_ENG` and `IDX_BRN`.
- **Step 1:** Spearman rank correlations, criterion × each predictor — transparent, client-readable.
- **Step 2:** Shapley-value decomposition of model R² across the predictor set, because predictors are intercorrelated and raw correlations over-credit redundant drivers.
- **Reporting rule — significance ≠ importance:** at census N nearly everything is significant. Rank by effect size. No unadjusted significance matrices in client-facing sections; the full matrix with Holm-adjusted p-values lives in the appendix.
- **Stated vs. derived:** report the stated-importance rank (`GAP-*-I`) and the model-derived rank side by side, and explain divergences — they are frequent and informative.

---

## 5 · Data-quality screening (pre-registered, applied before any analysis)

Applied in this order; a respondent excluded by any rule is excluded from all analyses.

| # | Screen | Flag | Exclude |
|---|---|---|---|
| 1 | **Speeding** | `T_TOTAL` < ⅓ of the sample median | Sustained < 2 s per item across a block |
| 2 | **Straightlining** | Zero variance across ≥ 20 consecutive matrix items | Straightlining **and** flagged for speeding |
| 3 | **Attention checks** | One failure (`AC-01` or `AC-02`) | Both failed |
| 4 | **Kiosk proxy review** | Response-time clustering on a shared device signature | Manual review only — never auto-excluded |

**Reported in every report:** N collected → N after screening → screening rate, broken out by major segment. If the screening rate differs by more than ~3 pp between segments, that is itself a finding and is stated.

*Note on the GAP matrix:* straightlining detection runs on the importance and satisfaction columns **separately**. A respondent who legitimately rates everything "Very important" is not straightlining if their satisfaction column varies.

*Note on the midpoint:* the share of midpoint responses across the whole matrix is monitored as a satisficing indicator alongside straightlining — an anomalously high rate is treated as a data-quality signal, not as substantive neutrality.

---

## 6 · Weighting

- **Scheme:** rim weighting to payroll records on **department × tenure band × role level**.
- **Requirement:** `SEG-FUN`, `SEG-TEN`, `SEG-ROL` category sets must match the HRIS extract exactly. If they do not, weighting cannot be executed as specified and the report says so.
- **Trimming:** weights capped at 0.4–2.5; the realized range and the design effect are reported.
- **Effective N:** reported alongside nominal N wherever margins of error are given.
- Respondents who abandoned before Block H carry no segment values and are therefore **unweighted**; they are retained in org-level unweighted tallies and excluded from weighted and segment analyses. Their share is reported.

---

## 7 · Anonymity and suppression

- **No breakout for any group of N < 5.** Suppressed cells appear as "n/a (below reporting threshold)" — never silently dropped, because a blank invites reconstruction by subtraction.
- **Complement check:** if suppressing one cell in a table allows it to be derived from the row total and the remaining cells, suppress the next-smallest cell as well.
- Open-ended quotations are paraphrased where verbatim wording could identify the author. Role and tenure metadata are attached to a quotation only when that cell exceeds the threshold.
- No IP address, email, or employee identifier is stored with responses. The raw export contains no free-text field that was auto-populated from the invitation.

---

## 8 · Deliverable file set (per engagement)

| File | Contents |
|---|---|
| `<client>_raw.csv` | One row per respondent, all IDs as column names, codes per §2. |
| `<client>_screened.csv` | Post-screening analysis file, plus `WT` (weight) and all §4 derived variables. |
| `<client>_crosstabs.xlsx` | Full banner tables; suppression applied; full significance matrix. |
| `<client>_report.docx` | Client deliverable — built from the report template. |
| `codebook.md` | This file, versioned to the engagement. |

---

## 9 · Open flags (owner decision required)

1. **`BRN_TIER` cutpoints.** Set here at 6–13 / 14–21 / 22–30 (equal thirds of the 6–30 range). These are defensible and stable but not empirically anchored — no normative sample exists behind them. Options: (a) keep as documented arbitrary bands, clearly labeled; (b) anchor them after 3–5 engagements against observed distributions and freeze; (c) drop tier language and report the index continuously. → *pending.*
2. **Weight trimming bounds** (0.4–2.5) are a convention, not a rule. Confirm or set client-specific. → *pending.*
3. **`STY-02` scoring.** Currently reported alone. Alternative: a two-item retention-risk composite with reverse-keyed `STY-01`. Recommend keeping them separate — they behave differently and the composite hides that. → *pending.*

---

*Document owner: A. Akhtyrskii · Prepared with Claude · v0.1 · 2026-07-19*
