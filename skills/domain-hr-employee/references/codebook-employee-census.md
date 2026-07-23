# Measure & Meaning — Employee Domain

## Codebook · Annual Engagement & Retention Census · v0.3

**Status:** release per consolidated handoff 2026-07-22 (flags session C) — implements D1, D2, D3, D4, D7, D8, Block X rules, allowlist principle · **Repo target:** `skills/domain-hr-employee/references/codebook-employee-census.md`
**Companions:** `questionnaire-employee-census.md` v0.3 · `module-framework.md` v0.4 (item bank & rationale) · `codebook-employee-census.csv` v0.3 (machine-readable variable list + `driver_models`/`predictors` spec) · `report-template-employee-census.md` v1.2

This codebook is the contract between fieldwork and analysis. Every rule below is **pre-registered** — fixed before data arrive, disclosed in the report's technical appendix, and applied without exception.

---

## 1 · ID convention

- IDs are **stable across waves** and never change meaning. Revised wording gets a new ID with a letter suffix (`ENG-01b`), and the old ID is retired, not reused.
- GAP items take the form `GAP-<CODE>-I` (importance) and `GAP-<CODE>-S` (satisfaction).
- The same IDs are used in the raw export, the crosstab workbook, and the `{{braces}}` report template. Renaming a variable anywhere breaks all three.
- The `CUS-` prefix is **reserved** for client add-on items (Block X, §10) and cannot collide with core blocks A–H.

### 1.1 Pipeline contract — the allowlist principle

> **The pipeline reads by allowlist, not by scanning.** Only canonical variable IDs declared in this codebook (and, per engagement, in the engagement codebook addendum) are parsed. Any unrecognised column in the raw export is ignored silently — not an error, not a warning.

This is what makes client add-ons safe: the principal can add columns freely and the standard report builds unchanged. Rows in the CSV whose `block` value carries the `spec_` prefix (`spec_driver_models`, `spec_predictors`) are machine-readable analysis specifications, not respondent variables, and are never expected in the raw export.

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
| `SAT-00` | SAT-5 | **Validation criterion** for the driver models (§4.3); headline trend metric between waves. Never promoted to a standalone driver ranking. |

### Block B — CORE (engagement)

| ID | Scale | Reverse | Index |
|---|---|---|---|
| `ENG-01` … `ENG-04`, `ENG-06` | AGREE-5 | none | `IDX_ENG`, `IDX_ENG_DRIVER` |
| `ENG-05` | AGREE-5 | none | `IDX_ENG` only — excluded from `IDX_ENG_DRIVER` (§4.3, criterion adjacency) |

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

Raw `BRN-*` items enter the driver models **only through `IDX_BRN`** — they are not individual predictors (tagging both would double-count burnout; §4.3).

### Block F — STAY

| ID | Scale | Notes |
|---|---|---|
| `STY-01` | AGREE-5 | **Primary criterion** — headline driver model (§4.3); feeds `STAY_TYPE` (§4.4). |
| `STY-02` | AGREE-5 | **Divergence criterion** (§4.3) — reported as a contrast exhibit and in prose, never as a second ranked list. Higher = more leaving consideration; not summed with STY-01. Feeds `STAY_TYPE`. |
| `STY-03` | categorical 1–3, 98 | 1 Planning to stay · 2 Open to outside offers · 3 Actively looking · 98 Prefer not to say |

### Block G — OPEN

| ID | Type | Notes |
|---|---|---|
| `OPN-01`, `OPN-02` | open text | Standard census pair. |
| `OPN-03` | open text | Slot; `.n` when not fielded. Serves as the open-ended custom slot for Block X (§10). |

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

### Block X — client add-on module (CUS)

Optional per engagement; descriptive only. IDs `CUS-01`, `CUS-02`, … Full rules in §10; declared in the per-engagement codebook addendum, never in this canonical codebook.

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
| `IDX_ENG` | Mean of `ENG-01…06`, rescaled 0–100: `(mean − 1) / 4 × 100` | Computed only if ≥ 4 of 6 items answered. Headline engagement metric and wave-over-wave trend variable. **Not a model predictor** (see `IDX_ENG_DRIVER`). |
| `IDX_ENG_DRIVER` | Mean of `ENG-01, ENG-02, ENG-03, ENG-04, ENG-06`, rescaled 0–100: `(mean − 1) / 4 × 100` | Computed only if ≥ 4 of 5 items answered. **Never reported as a number** — exists only inside the driver models (§4.3). *(Owner-delegated decision, 2026-07-22, D3.)* |
| `IDX_BRN` | `mean(BRN-01, BRN-02r, BRN-03, BRN-04r, BRN-05, BRN-06 \| valid) × 6` — prorated, range 6–30 | Computed only if ≥ 5 of 6 items answered. **Rounded to one decimal before tier assignment.** *(Owner decision, 2026-07-22, D1 — replaces the raw sum, which let 5-item cases score 5–25: below the scale floor and unable to reach the top tier.)* |
| `BRN_TIER` | 6–13 = Low · 14–21 = Moderate · 22–30 = Elevated | Assigned from the rounded `IDX_BRN`. **Pre-set cutpoints**, not sample terciles — so tiers are comparable across waves and clients. Not normatively anchored; disclosed in every report (technical appendix). **Recorded intent: re-anchor once against observed distributions after 3–5 engagements, then freeze** *(owner decision, 2026-07-19)*. |
| `NPS_CLASS` | 0–6 Detractor · 7–8 Passive · 9–10 Promoter | — |
| `ENPS` | % Promoters − % Detractors (percentage points) | Mean of `NPS-01` reported as a **secondary** statistic only. |
| `STAY_TYPE` | 2×2 stay/leave typology from `STY-01` × `STY-02` (top-2-box) | See §4.4. *(Owner decision, 2026-07-22, D7.)* |
| `GAP_<CODE>` | `mean(GAP-<CODE>-I) − mean(GAP-<CODE>-S)` | Satisfaction mean excludes `99`. |
| `COV_<CODE>` | % of respondents answering `99` on `GAP-<CODE>-S` | Reported alongside every satisfaction mean. |
| `IMP_MED`, `SAT_MED` | Within-survey medians across the 18 category means | Define the GAP quadrant boundaries. **Recomputed each wave**; from wave 2 the prior wave's medians are also plotted for reference. *(Owner decision, 2026-07-19: medians, not scale midpoints.)* |

### 4.3 Driver models

The specification is carried machine-readably in `codebook-employee-census.csv` (rows with block `spec_driver_models` and `spec_predictors`); this section is its human-readable contract.

**Models (all share the same predictor set):**

| id | Criterion | Role | Presentation rule |
|---|---|---|---|
| `DM_HEADLINE` | `STY-01` | Primary ranking | The **only** model rendered as a ranked priority list. |
| `DM_DIVERGENCE` | `STY-02` | Contrast exhibit | Reported as a **divergence exhibit and in prose — never as a second ranked list**. Two ranked lists force the client to ask which one to act on. *(Owner decision, 2026-07-22, D8.)* |
| `DM_VALIDATION` | `SAT-00` | Robustness check | Never reported as a ranking. Overall satisfaction is largely constituted by satisfaction with the 18 conditions — a part-whole relationship that would yield a flattering R² and a circular finding. |

**Canonical predictor set (fixed, identical across engagements):** the 18 `GAP-<CODE>-S` items + `IDX_ENG_DRIVER` + `IDX_BRN` — **20 predictors**. The count `{{n_predictors}}` is always computed from the `spec_predictors` row at render time, never hard-coded. *(Owner decision, 2026-07-22, D4 — three documents previously stated three different counts, none computed.)*

- Raw `BRN-01…06` are **not** individual predictors — burnout enters only through `IDX_BRN`; tagging both would double-count it.
- `CUS-*` items **never** enter any driver model (§10).

**Method:**

- **Step 1:** Spearman rank correlations, criterion × each predictor — transparent, client-readable.
- **Step 2:** Shapley-value decomposition of model R² across the predictor set, because predictors are intercorrelated and raw correlations over-credit redundant drivers.

**Reporting rules:**

- **Significance ≠ importance:** at census N nearly everything is significant. Rank by effect size. No unadjusted significance matrices in client-facing sections; the full matrix with Holm-adjusted p-values lives in the appendix.
- **Stated vs. derived:** report the stated-importance rank (`GAP-*-I`) and the model-derived rank side by side, and explain divergences — they are frequent and informative.
- **What the divergence model is for:** "considered leaving" (`STY-02`) is a retrospective emotional event driven by push factors (manager, workload, recognition, burnout); "expect to still be here" (`STY-01`) is a forecast bounded by external constraints (labour market, alternatives). A condition that ranks high on `STY-02` and low on `STY-01` reads as a source of quiet disengagement rather than turnover — actionable, and invisible in a conventional report.

**Disclosures (technical appendix, every report):**

1. `ENG-05` ("I can see a future for myself at this organization") is conceptually adjacent to the criterion `STY-01` and is therefore excluded from `IDX_ENG_DRIVER`. Including it inflates the engagement index's share of explained variance at the expense of the actionable conditions. `IDX_ENG` (six items) remains the headline metric and trend variable, untouched.
2. `BRN-03` and `BRN-05` sit conceptually closer to `STY-02` than to `STY-01`. Not a tautology on the `ENG-05` scale, but it is stated once the divergence model exists.

### 4.4 Stay/leave typology (`STAY_TYPE`)

Pre-registered dichotomization, **fixed across waves**:

- `STY-01` ∈ {4, 5} (Agree / Strongly agree) → **expects to stay**; {1, 2, 3} → does not.
- `STY-02` ∈ {4, 5} → **considered leaving**; {1, 2, 3} → did not.

|  | Did not consider leaving | Considered leaving |
|---|---|---|
| **Expects to stay** | 1 · Settled | 2 · **Reluctant stayers** |
| **Does not expect to stay** | 3 · Uncertain | 4 · Leaving |

Rules:

- The midpoint (3) share is reported separately for **both** items — it is a real position, not a rounding error, and collapsing it into the negative side silently inflates the risk quadrants.
- Respondents missing either item are **excluded** from the 2×2; their share is reported.
- Cells are weighted, consistent with the rest of the report. Standard N < 5 suppression and the complement check (§7) apply.

*Why it earns its place: reluctant stayers sit inside the healthy headline statistic — they answered "yes, I'll be here in a year" — while having seriously considered leaving within the past six months. They stay because of external constraints, not because conditions are good, and they leave the moment the constraint lifts. A conventional engagement report never surfaces them.*

---

## 5 · Data-quality screening (pre-registered, applied before any analysis)

Applied in this order; a respondent excluded by any rule is excluded from all analyses.

| # | Screen | Flag | Exclude |
|---|---|---|---|
| 1 | **Speeding** | `T_TOTAL` < ⅓ of the sample median | Sustained < 2 s per item across a block |
| 2 | **Straightlining** | Zero variance across all 18 ratings within a single GAP column (importance or satisfaction), evaluated per column | Straightlining **and** flagged for speeding |
| 3 | **Attention checks** | One failure (`AC-01` or `AC-02`) | Both failed |
| 4 | **Kiosk proxy review** | Response-time clustering on a shared device signature | Manual review only — never auto-excluded |

*(Straightlining rule revised 2026-07-22, D2 — the previous "≥ 20 consecutive matrix items" could never fire: the longest single run in this configuration is 18. Leftover from an earlier, longer configuration.)*

**Reported in every report:** N collected → N after screening → screening rate, broken out by major segment. If the screening rate differs by more than ~3 pp between segments, that is itself a finding and is stated.

*Note on the GAP matrix:* straightlining detection runs on the importance and satisfaction columns **separately**. A respondent who legitimately rates everything "Very important" is not straightlining if their satisfaction column varies.

*Note on the midpoint:* the share of midpoint responses across the whole matrix is monitored as a satisficing indicator alongside straightlining — an anomalously high rate is treated as a data-quality signal, not as substantive neutrality.

*Note on Block X:* `CUS-*` items are **excluded** from the straightlining and speeding screens — variable block length would make the rules non-comparable across engagements (§10).

---

## 6 · Weighting

- **Scheme:** rim weighting to payroll records on **department × tenure band × role level**.
- **Requirement:** `SEG-FUN`, `SEG-TEN`, `SEG-ROL` category sets must match the HRIS extract exactly. If they do not, weighting cannot be executed as specified and the report says so.
- **Trimming:** weights capped at 0.4–2.5 — **confirmed as the default convention** *(owner decision, 2026-07-19)*. A client-specific override is allowed and must be documented in the engagement codebook. The realized range and the design effect are reported as before.
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
| `<client>_raw.csv` | One row per respondent, all IDs as column names, codes per §2. Unrecognised columns permitted (allowlist principle, §1.1). |
| `<client>_screened.csv` | Post-screening analysis file, plus `WT` (weight) and all §4 derived variables. |
| `<client>_crosstabs.xlsx` | Full banner tables; suppression applied; full significance matrix. |
| `<client>_report.docx` | Client deliverable — built from the report template. |
| `codebook.md` | This file, versioned to the engagement, plus the Block X addendum when fielded (§10). |

---

## 9 · Decision log

### Flags session B — 2026-07-19 (all resolved)

1. **`BRN_TIER` cutpoints — resolved: option (b), staged.** Keep the pre-set bands 6–13 / 14–21 / 22–30, explicitly disclosed as pre-set (not normative) in every report's technical appendix. Recorded intent: re-anchor once against observed distributions after 3–5 engagements, then freeze. See §4.2.
2. **Weight trimming bounds — resolved.** 0.4–2.5 confirmed as the default convention; client-specific override allowed, documented in the engagement codebook. See §6.
3. **`STY-02` scoring — resolved.** `STY-01` and `STY-02` are reported separately; no composite. The stay/leave asymmetry is diagnostic, and the driver model is built on separate criteria. See §3 Block F and §4.3.

### Flags session C — 2026-07-22 (consolidated handoff; all resolved)

- **D1** `IDX_BRN` missing-data rule → prorated mean × 6; range 6–30 restored; one-decimal rounding before tier assignment. §4.2.
- **D2** Straightlining flag → zero variance across a full GAP column, per column; the impossible "≥ 20 consecutive" rule retired. §5.
- **D3** Criterion contamination → `IDX_ENG_DRIVER` (5 items, ENG-05 excluded) used inside models only; `IDX_ENG` unchanged as headline metric. §4.2–4.3. *(Owner delegated the call; Option A adopted.)*
- **D4** Canonical predictor set → 20, computed not typed; raw `BRN-*` de-tagged; `spec_predictors` row is the single source. §4.3.
- **D7** Stay/leave 2×2 → `STAY_TYPE`, top-2-box, pre-registered. §4.4.
- **D8** `STY-02` divergence model adopted with a hard presentation rule (never a second ranked list); BRN-03/BRN-05 adjacency disclosed. §4.3.
- **Block X** Client add-on module (CUS) adopted, descriptive only; allowlist principle recorded as the enabling invariant. §1.1, §10.
- **Not adopted (recorded so it is not silently revived):** a branching follow-up after `STY-03` asking at-risk respondents what pulls them toward leaving. If revisited: it would quantify what share of attrition risk is addressable at all, at a cost of one item shown to a minority; and it carries an anonymity flag, since relocation × site × tenure approaches identification.

*No open flags remain in this document.*

---

## 10 · Block X — client add-on module (CUS)

Client-requested items (e.g. evaluating an internal programme or event) can be added per engagement with **no effect on automation**. Such items are **descriptive only** — a quick section; charts may be produced manually. The enabling invariant is the allowlist principle (§1.1).

| Rule | Specification |
|---|---|
| **ID convention** | `CUS-01`, `CUS-02`, … Prefix reserved; cannot collide with core blocks A–H. |
| **Index isolation** | Never enter `IDX_ENG`, `IDX_ENG_DRIVER`, `IDX_BRN`, `GAP_*`, `IMP_MED`/`SAT_MED`, `ENPS`. |
| **Models** | **Never** enter any driver model. *(Simplified from the earlier opt-in design at owner's direction — custom items are descriptive only.)* The canonical 20-predictor set is therefore identical across every engagement. |
| **Placement** | Closed custom items: after Block F (STAY), before Block G (OPEN), so verbatims are not lost to break-off. Open-ended custom item: the existing `OPN-03` slot. |
| **Scales** | Must reuse an existing scale from §2. New scale types require an owner decision — they break shared rendering and screening logic. |
| **Screening** | Excluded from straightlining and speeding screens (variable block length would make the rules non-comparable across engagements). |
| **Documentation** | Declared in the per-engagement codebook addendum (`codebook.md` versioned to the engagement) — never in this canonical codebook. |
| **Reporting** | Conditional section **§4.6 Engagement-specific questions**, `{{#if custom_module}}`. Absent → does not render; the report is structurally identical to the standard. Frequencies and a chart per item; no modelling, no driver claims. |
| **Crosstabs** | Banner-crossed by standard segments and promoter class like any other variable. |
| **Suppression** | Standard N < 5 rule and complement check (§7) apply unchanged. |

---

*Document owner: A. Akhtyrskii · Prepared with Claude · v0.3 · 2026-07-22*
