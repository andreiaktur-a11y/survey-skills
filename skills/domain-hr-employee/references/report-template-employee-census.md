# Measure & Meaning — Employee Domain

## Report Template · Annual Engagement & Retention Census · v1.2

**Status:** release per consolidated handoff 2026-07-22 (flags session C) — implements D1 (Appendix A), D2 (§03 + Appendix B), D3/D8 disclosures (Appendix D), D4 (`{{n_predictors}}` computed), D5 (retention leverage), D7 (STAY_TYPE exhibit), D8 (divergence exhibit), Block X (§4.6 conditional + `custom` field group) · **Repo target:** `skills/domain-hr-employee/references/report-template-employee-census.md`
**Companions:** `codebook-employee-census.md` v0.3 + `codebook-employee-census.csv` v0.3 (variable IDs — placeholder names are keyed to them; `spec_driver_models`/`spec_predictors` rows are the model spec) · `questionnaire-employee-census.md` v0.3 · `module-framework.md` v0.4 · sample report v3.2 (the rendered reference of what this template produces) · `scripts/build_report.js` (v2 hardcoded builder — to be refactored to consume this template's field schema)

---

### Template conventions (read before filling — this block is never rendered)

| Convention | Rule |
|---|---|
| `{{snake_case}}` | Scalar placeholder (Mustache/Handlebars, per the `domain-legal` pattern). Names are keyed to codebook variable/derived-variable IDs where one exists (`{{idx_eng_org}}` ← `IDX_ENG`; `{{enps_org}}` ← `ENPS`; `{{gap_pay}}` ← `GAP_PAY`). Renaming a variable in the codebook breaks the template — see codebook §1. |
| `{{#each list}} … {{/each}}` | Repeating block; fields inside via `{{this.field}}`. Pairs with the Node + `docx` generator. |
| `{{#if flag}} … {{/if}}` | Conditional block, rendered only when the flag/field is set. |
| `<!-- INSTRUCTION: … -->` | Fill-in guidance for the principal/Claude. Delete before delivery; never render. |
| **[BOILERPLATE — DO NOT EDIT]** | Standing methodological disclosure. Identical wording in every deliverable; changes require an owner decision logged in the ROADMAP. |
| Empty-by-default fields | `{{n_closed_items}}` is **optional and empty by default** (owner decision, 2026-07-19): the census is modular, so the method section describes modules, not counts. Fill only when a client contract requires a stated count. |
| Computed fields | `{{n_predictors}}` is **computed at render time** from the codebook CSV `spec_predictors` row — never hard-coded (owner decision 2026-07-22, D4). `{{n_custom_items}}` is computed as the length of `custom_items[]`. |
| Suppression | Any cell with N < 5 renders as `n/a (below reporting threshold)` — never blank, never dropped (codebook §7). |
| Standing content rules | No fabricated benchmarks or testimonials; no vendor-instrument wording (IP tier C); ambiguous claims → flag for owner sign-off, don't resolve silently. |

---

<!-- ============ COVER ============ -->

# {{report_type_label}}
<!-- INSTRUCTION: "SAMPLE REPORT" for the public exemplar; omit for client deliverables. -->

**Employee Engagement & Retention**
{{study_design_label}} <!-- e.g. "Annual census, all-employee population." -->

| | |
|---|---|
| Prepared for | {{client_name}}{{#if sample_mode}} — {{client_descriptor}} (illustrative){{/if}} |
| Prepared by | Andrei Akhtyrskii, PhD — Measure & Meaning Research |

{{#if sample_mode}}
> **About this document**
> **This is a sample deliverable.** Every number, chart, organization name, and quotation in it is synthetic — generated to illustrate the structure, analysis standards, and decision framing of a Measure & Meaning employee census report. No real client data appear anywhere in this document.
> *Instrumentation: all survey items referenced here are original Measure & Meaning formulations (IP tier A).*
{{/if}}

{{report_month_year}}

---

# 01 Executive summary

**The decision this study supports:** {{decision_context}}
<!-- INSTRUCTION: 2–4 sentences. Name the business problem with its magnitude, who must decide, and what this census resolves that other evidence (exit interviews, escalations) cannot. Decision-first: this paragraph is why the report exists. -->

{{#each key_findings}}
- **{{this.headline}}.** {{this.body}} ({{this.figure_ref}})
{{/each}}
<!-- INSTRUCTION: 4–6 bullets, one per objective. Each bullet = bolded verdict + evidence + figure reference. Lead with the distribution/concentration story, not the average. -->

> **Recommendation**
> {{headline_recommendation}}
<!-- INSTRUCTION: sequenced, numbered tiers by cost (low-cost levers now → structural fixes → evidence-before-spending), plus the re-measurement plan. Mirrors §06. -->

# 02 Background and objectives

{{background_narrative}}
<!-- INSTRUCTION: org size, sites, the trigger event, why prior evidence was insufficient, and what decision the study feeds. -->

The study was designed to resolve {{n_objectives}} questions, each mapped to a survey module:

| # | Objective (question the analysis resolves) | Module |
|---|---|---|
{{#each objectives}}
| {{this.num}} | {{this.question}} | {{this.module}} |
{{/each}}

Open-ended responses (module OPEN) cut across all objectives and are reported in §4.5.

# 03 Method and sample

## Design and instrument

{{fielding_mode_sentence}} <!-- e.g. "Anonymous online census of all employees; kiosk stations provided on production floors for employees without company email." --> Median completion time {{median_completion_min}} minutes. The instrument combined {{n_modules}} modules — {{module_list}} — assembled from the Measure & Meaning employee item bank; the census is modular, and the fielded configuration is engagement-specific.{{#if n_closed_items}} The fielded configuration comprised {{n_closed_items}} closed items plus {{n_open_ends}} open-ends.{{/if}}{{#if custom_module}} The engagement additionally fielded {{n_custom_items}} engagement-specific closed items (Block X; reported in §4.6, documented in Appendix A). Custom items are capped at eight by design, holding the instrument to approximately 15–17 minutes in that configuration.{{/if}} All items are original Measure & Meaning formulations; item IDs, scales, and provenance are documented in Appendix A.
<!-- INSTRUCTION: {{n_closed_items}} is EMPTY BY DEFAULT — the conditional sentence renders only if a count is contractually required (owner decision, 2026-07-19). Do not reintroduce a fixed count into the base sentence. -->

**[BOILERPLATE — DO NOT EDIT] Scales.** Agreement items use a 5-point Likert scale. Importance and satisfaction are each rated on 7-point, fully verbalized scales; satisfaction items offer an off-scale "Not applicable / no experience with this" option, excluded from means and reported as a coverage statistic (Appendix A explains the rationale). eNPS uses the canonical 0–10 scale.

## Sample and coverage

| Unit | Invited | Completed | After screening | Response rate | MoE (95%) |
|---|---|---|---|---|---|
{{#each units}}
| {{this.name}} | {{this.invited}} | {{this.completed}} | {{this.screened}} | {{this.rr}} | ±{{this.moe}} pp |
{{/each}}
| **Total** | **{{n_invited}}** | **{{n_completed}}** | **{{n_analyzed}}** | **{{response_rate}}** | **±{{moe_org}} pp** |

Exhibit 1. Achieved sample by unit

**Weighting.** Results are weighted to payroll records by department × tenure band × role level to correct nonresponse skew{{weighting_skew_note}}. Weights range {{weight_min}}–{{weight_max}}; the scheme is documented in Appendix C. All figures in this report are weighted unless labeled otherwise.

## Data-quality screening (applied before any analysis)

**[BOILERPLATE — DO NOT EDIT]** Screening rules were pre-registered in the technical appendix and applied uniformly. This disclosure is standard in every Measure & Meaning report:

| Screen | Rule | Flagged | Excluded |
|---|---|---|---|
| Speeding | < ⅓ of median completion time flag; sustained < 2 s/item exclude | {{scr_speed_flag}} | {{scr_speed_excl}} |
| Straightlining | Zero variance across all 18 ratings within a single GAP column (importance or satisfaction), assessed per column, flag; + speeding exclude | {{scr_straight_flag}} | {{scr_straight_excl}} |
| Attention checks | 2 embedded items; one failure flag, two exclude | {{scr_ac_flag}} | {{scr_ac_excl}} |
| Kiosk proxy review | Response-time clustering on shared devices reviewed manually | {{scr_kiosk_flag}} | {{scr_kiosk_excl}} |
| **Total excluded (unique respondents)** | | | **{{scr_total_excl}} ({{scr_rate}}%)** |

Exhibit 2. Screening funnel: {{n_completed}} completed → {{n_analyzed}} analyzed
<!-- INSTRUCTION: if the screening rate differs by > ~3 pp between major segments, state it here as a finding (codebook §5). -->

> **[BOILERPLATE — DO NOT EDIT] Anonymity threshold**
> **No result is reported for any group of fewer than 5 respondents.** Suppressed cells are shown as "n/a (below reporting threshold)" — never silently dropped. Open-ended quotations are paraphrased where verbatim wording could identify the author.

# 04 Results by objective

## 4.1 · Engagement: {{core_section_verdict}} — CORE

The engagement index (mean of six agreement items, rescaled 0–100) averages {{idx_eng_org}} weighted. {{core_narrative}}
<!-- INSTRUCTION: lead with the spread, not the average — name units above/below and tie to the decision context. Per-unit values in units[].idx_eng. -->

*Fig. 1. Engagement index by unit vs. organization average (weighted, n={{n_analyzed}})*

## 4.2 · Willingness to recommend: eNPS {{enps_org}} — NPS

Employee Net Promoter Score is % promoters (9–10) minus % detractors (0–6) on the 0–10 recommendation scale. The organization scores {{enps_org}}: {{enps_narrative}}.

*Fig. 2. Promoter / passive / detractor shares and eNPS by unit (weighted)*

**[BOILERPLATE — DO NOT EDIT] Two disclosures we make in every report.** First, the mean score ({{nps_mean_org}}) is reported only as a secondary statistic — the mean and the index can move in opposite directions (detractors softening from 2 to 5 raises the mean and leaves eNPS unchanged), and any divergence is explained, not hidden. Second, small segments produce unstable eNPS: a {{small_unit_example_n}}-person unit moves ±{{small_unit_swing}} points on one changed answer, which is why every segment score carries a confidence interval.

## 4.3 · What matters vs. what we deliver: the gap map — GAP

Each of {{n_gap_conditions}} working conditions was rated twice — importance when choosing an employer, and satisfaction in the current role (7-point scales; "not applicable" available on satisfaction and excluded from means). Plotting the two against each other separates what to fix from what to protect. **[BOILERPLATE — DO NOT EDIT]** Quadrant boundaries are the within-survey medians, not scale midpoints — this is disclosed because it affects interpretation: quadrants describe relative position in this workforce, this wave.

*Fig. 3. Importance × satisfaction, {{n_gap_conditions}} conditions (weighted means; codes in Appendix A)*

**{{n_action_zone}} conditions land in the action zone:** {{#each action_zone}}{{this.label}} ({{this.code}}); {{/each}}. {{gap_narrative}}
<!-- INSTRUCTION: name strengths-to-protect explicitly; the recommendation section treats them as assets, not targets. Gap scores come from GAP_<CODE>; e.g. {{gap_pay}}, {{gap_wkl}}. -->

*Fig. 4. Gap score (importance − satisfaction), ranked; gaps ≥ {{gap_highlight_threshold}} highlighted*

**Coverage note:** {{#each coverage_notes}}{{this.share}}% of respondents selected "not applicable" on the {{this.condition}} satisfaction item{{this.reason}}; {{/each}}. These responses are excluded from the means above and reported here rather than recoded to the midpoint. <!-- COV_<CODE> per codebook §4.2 -->

## 4.4 · Burnout risk: {{brn_section_verdict}} — BRN

The burnout module is an organizational risk screen — six items covering exhaustion, recovery, disengagement, and sustainability — reported only at segment level. Respondents are assigned to low / moderate / elevated tiers by pre-set cutpoints on the burnout index (index formula and cutpoint logic in Appendix A).

*Fig. 5. Burnout risk tiers by tenure band (weighted)*
<!-- INSTRUCTION: tenure bands are the non-overlapping SEG-TEN grid: <1 / 1–2 / 3–6 / 7+ yrs (owner decision, 2026-07-19). -->

{{brn_narrative}}
<!-- INSTRUCTION: report elevated-tier share by tenure (brn_by_tenure[]) and by unit; state the demand-vs-recovery mechanism split and its intervention consequence (structural workload vs. wellness programming). Suppress cells N < 5. -->

*Fig. 6. Demand load vs. recovery adequacy by unit (bubble size = n)*

## 4.5 · What employees say in their own words — OPEN

{{n_open_ends}} open-ended items were coded thematically by two coders with adjudication ({{coder_agreement}}% initial agreement). Themes are cross-tabulated by promoter class — what detractors want changed, and what promoters insist must not change:

*Fig. 7. Theme frequency among detractors vs. promoters (multi-code)*

> **From the open-ended responses (paraphrased{{quote_mode_label}})**
{{#each quotes}}
> "{{this.text}}" — {{this.segment}}
{{/each}}
<!-- INSTRUCTION: paraphrase to protect anonymity; attach role/tenure metadata only where the cell exceeds the reporting threshold (codebook §7). -->

{{#if custom_module}}
## 4.6 · Engagement-specific questions — Block X

{{custom_section_intro}}
<!-- INSTRUCTION: 1–3 sentences naming what the client asked to evaluate and why. HARD RULES (codebook §10): custom items are DESCRIPTIVE ONLY — frequencies and one chart per item; no modelling, no driver claims, no entry into any index or into the predictor set. Banner-crossed by standard segments and promoter class in the crosstab workbook. Standard N < 5 suppression and the complement check apply unchanged. When custom_module is false this entire section does not render and the report is structurally identical to the standard deliverable. -->

{{#each custom_items}}
**{{this.id}} · {{this.label}}** ({{this.scale}}). {{this.result_summary}} ({{this.figure_ref}})
{{/each}}
{{/if}}

# 05 Driver analysis: what actually predicts staying

**[BOILERPLATE — DO NOT EDIT] This section is the differentiator of the report.** The descriptive sections describe the workforce; this section models it. Three pre-registered models share one canonical predictor set (codebook §4.3): the **headline model** on intent to stay (STY-01) — the only model reported as a ranked priority list; the **divergence model** on "seriously considered leaving" (STY-02) — reported as a contrast exhibit and in prose; and the **validation model** on overall satisfaction (SAT-00) — a robustness check, never reported as a ranking.
<!-- INSTRUCTION: STY-01 and STY-02 are reported separately, never composited — the stay/leave asymmetry is diagnostic (owner decisions 2026-07-19 and 2026-07-22, D8). Model roles are fixed in codebook §4.3 and the CSV spec_driver_models rows; do not add, remove, or re-role models here. -->

## The stay/leave landscape

Before any modelling, respondents are classified directly on the two retention items, using the pre-registered top-2-box rule fixed across waves (codebook §4.4):

| | Did not consider leaving | Considered leaving |
|---|---|---|
| **Expects to stay** | Settled — {{stay_settled_pct}}% | **Reluctant stayers — {{stay_reluctant_pct}}%** |
| **Does not expect to stay** | Uncertain — {{stay_uncertain_pct}}% | Leaving — {{stay_leaving_pct}}% |

*Fig. 8. Stay/leave typology (STAY_TYPE), weighted shares (n={{n_analyzed}})*

The midpoint ("neither agree nor disagree") is a real position, not a rounding error, and is reported separately for both items rather than collapsed into the negative side: {{sty01_mid_pct}}% on the expect-to-stay item, {{sty02_mid_pct}}% on the considered-leaving item. {{stay_excluded_pct}}% of respondents answered fewer than both items and are excluded from the typology. {{stay_type_narrative}}
<!-- INSTRUCTION: the reluctant-stayer cell is the finding a conventional report misses — inside the healthy headline statistic, yet having seriously considered leaving within six months; they stay because of external constraints and leave when the constraint lifts. Read the cell against segments in the crosstab workbook. Cells are weighted; N < 5 suppression and the complement check apply (codebook §7). -->

The analysis proceeds in two disclosed steps. First, transparent bivariate rank correlations between each condition and intent to stay — readable by any stakeholder. Second, because the predictors are intercorrelated, raw correlations over-credit redundant drivers; a Shapley-value decomposition allocates the model's explained variance fairly across correlated predictors.

*Fig. 9. Share of explained variance in intent to stay, with cost-to-address tags (model R² = {{r2_driver_model}})*

> **[BOILERPLATE — DO NOT EDIT] Significance ≠ importance**
> At census scale (n={{n_analyzed}}), nearly every correlation is statistically significant — significance is a function of sample size, not practical relevance. **This report therefore ranks drivers by effect size and never presents unadjusted significance matrices in client-facing sections; the full matrix, with a multiple-comparison note, lives in Appendix D.**

{{stated_vs_derived_narrative}}
<!-- INSTRUCTION: show both rankings and explain the divergences — they are frequent and informative, not errors. Driver shares in drivers[].shap_share. -->

*Fig. 10. Stated importance rank vs. model-derived driver rank (top {{n_drivers_shown}})*

## Divergence check: pressure to leave vs. expectation to stay

**[BOILERPLATE — DO NOT EDIT]** A second model over the same {{n_predictors}} predictors takes "In the past six months, I have seriously considered leaving" (STY-02) as its criterion. The two criteria measure different things: considered-leaving is a retrospective emotional event driven by push factors (manager, workload, recognition, burnout); expect-to-stay is a forecast bounded by external constraints (labour market, alternatives). A condition that weighs heavily on considered-leaving but lightly on expect-to-stay reads as a source of quiet disengagement rather than imminent turnover — actionable, and invisible in a conventional report.

*Fig. 11. Driver divergence: share of explained variance under STY-02 vs. STY-01, per condition (divergence model R² = {{r2_divergence_model}})*

{{divergence_reading}}
<!-- INSTRUCTION — HARD PRESENTATION RULE (owner decision 2026-07-22, D8, non-negotiable): the divergence model is NEVER rendered as a second ranked priority list — divergence exhibit and prose only. Two ranked lists force the client to ask which one to act on; the headline priority ranking stays on STY-01. Name the 2–3 conditions with the largest STY-02 − STY-01 contrast and interpret them as quiet-disengagement sources. Data in divergence_points[]. -->

{{retention_leverage_reading}}
<!-- INSTRUCTION: group drivers by cost-to-address; name the cheapest levers and their joint variance share; state where perception data end and further study (e.g. pay benchmarking) begins. -->

# 06 Recommended actions

Sequenced by retention leverage — driver strength weighed against cost-to-address — using the driver model (Fig. 9), the gap map (Fig. 3), and the burnout mechanism split (Fig. 6). Each action names its evidence.

## Now — low-cost levers ({{horizon_now}})
{{#each actions_now}}
- **{{this.headline}}** ({{this.evidence}}). {{this.detail}}
{{/each}}

## Next — structural fixes ({{horizon_next}})
{{#each actions_next}}
- **{{this.headline}}** ({{this.evidence}}). {{this.detail}}
{{/each}}

## Then — evidence before spending ({{horizon_then}})
{{#each actions_then}}
- **{{this.headline}}** ({{this.evidence}}). {{this.detail}}
{{/each}}

> **Measurement follow-up**
> {{followup_plan}}
<!-- INSTRUCTION: pulse configuration = subset of this census module map (identical wording), timing, and the noise threshold for reading movement. -->

# 07 Limitations

**[BOILERPLATE — adapt bracketed spans only]**

- Cross-sectional design: the driver model identifies predictive association at one point in time, not proven causation. {{longitudinal_plan}}
- Intent to stay is a proxy for retention. It is the strongest survey-measurable predictor of voluntary turnover, but linkage to actual exit records ({{linkage_option}}, subject to the anonymity protocol) would strengthen the model.
- Self-report burnout screen: tiers indicate where organizational intervention should be prioritized; they are not diagnoses and are never reported below segment level.
- Stated importance reflects what employees can and will articulate; derived importance reflects statistical association. Both are shown; neither is treated as ground truth alone.
- {{small_unit_limitation}}
- {{trend_baseline_limitation}} External benchmarks are not used — cross-vendor benchmark databases differ in items, scales, and populations, and comparisons against them are not defensible. The baseline standard here is internal comparison across units and waves.

# A–D Appendices

## Appendix A · Instrument provenance and scales (summary)

All items fielded in this study are original Measure & Meaning formulations.

| Module | Items | Scale | Index rule (disclosed) |
|---|---|---|---|
{{#each modules}}
| {{this.name}} | {{this.items}} | {{this.scale}} | {{this.rule}} |
{{/each}}
{{#if custom_module}}
| Engagement-specific (Block X) | {{#each custom_items}}{{this.id}} {{/each}} | Reused from the standard scale set (codebook §2) | Descriptive only — never enters any index or driver model; excluded from straightlining/speeding screens; declared in the per-engagement codebook addendum (codebook §10) |
{{/if}}

**[BOILERPLATE — DO NOT EDIT] Why 7-point verbalized scales for the GAP matrix:** satisfaction is bipolar — a neutral state is a real position, and forcing a direction manufactures signal; importance is unipolar — the fully labeled midpoint ("moderately important") is a level, not an escape hatch. An odd scale also yields a stable within-survey median, which defines the quadrant boundaries; on an even scale those boundaries fall between categories and drift between waves. Midpoint share is monitored as a satisficing indicator alongside straightlining.

**[BOILERPLATE — DO NOT EDIT] Burnout index and tier cutpoints (disclosed):** the burnout index is the prorated mean of the six burnout items (reverse-keyed items rescored at scoring), multiplied by 6 — computed when at least five of the six items are answered, with a range of 6–30 for every valid case, and rounded to one decimal before tier assignment. Respondents are assigned to Low / Moderate / Elevated tiers by pre-set cutpoints on the index: 6–13 / 14–21 / 22–30. The bands are pre-set — equal thirds of the 6–30 score range — and are not normatively anchored: no external benchmark sample stands behind them. They are held fixed by design so that tiers remain comparable across waves and across organizations; the tiers indicate where organizational intervention should be prioritized and are not clinical diagnoses.

## Appendix B · Screening rules (pre-registered)

**[BOILERPLATE — DO NOT EDIT]** Speeders: completion < ⅓ of median → flag; sustained < 2 s per item → exclude. Straightliners: zero variance across all 18 ratings within a single GAP column (importance or satisfaction), assessed per column → flag; combined with speeding → exclude. Attention checks: two embedded checks; one failure → flag, two → exclude. Engagement-specific (Block X) items, when fielded, are excluded from the straightlining and speeding screens. Shared kiosk devices: identical device signatures acceptable by design; response-time clustering reviewed for proxy completion. Funnel: {{n_completed}} → {{n_analyzed}} ({{scr_rate}}% excluded), reported by segment in Exhibit 2.

## Appendix C · Weighting

Rim weighting to payroll records on department × tenure band × role level. Category sets mirror HRIS categories by design, which is what makes payroll weighting possible. Trimming bounds {{trim_lo}}–{{trim_hi}} <!-- default convention 0.4–2.5; client-specific override documented in the engagement codebook (owner decision, 2026-07-19) -->; realized weight range {{weight_min}}–{{weight_max}}; design effect {{deff}}; effective n = {{n_effective}}. Unweighted results available in the crosstab workbook.

## Appendix D · Statistical notes

**Driver models.** OLS on standardized predictors. Three pre-registered models share the canonical predictor set — the 18 GAP satisfaction items plus the engagement driver index (`IDX_ENG_DRIVER`) and the burnout index (`IDX_BRN`): {{n_predictors}} predictors, with the count computed at render time from the codebook CSV `spec_predictors` row, never hard-coded. **Headline model** — criterion STY-01; R² = {{r2_driver_model}}; Shapley decomposition of explained variance across the predictor set ({{n_drivers_shown}} shown, remainder pooled); the only model reported as a ranked list. **Divergence model** — criterion STY-02; R² = {{r2_divergence_model}}; reported as a contrast exhibit and in prose only (Fig. 11). **Validation model** — criterion SAT-00; robustness check, never reported as a ranking: overall satisfaction stands in a part-whole relationship with the 18 condition-satisfaction predictors, so its R² is structurally flattered and a ranking built on it would be circular.

**Disclosures.** (1) ENG-05 ("I can see a future for myself at this organization") is conceptually adjacent to the criterion STY-01 and is therefore excluded from the engagement index used inside the models (`IDX_ENG_DRIVER`, five items, never reported as a number); including it would inflate the engagement index's share of explained variance at the expense of the actionable conditions. The six-item headline index `IDX_ENG` is unchanged and remains the trend variable. (2) BRN-03 and BRN-05 sit conceptually closer to STY-02 than to STY-01 — not a tautology of the ENG-05 kind, but stated because the divergence model exists.

Full bivariate matrix with Holm-adjusted p-values in the crosstab workbook — omitted from the body per the significance ≠ importance standard. eNPS intervals: Wald 95% on the promoter–detractor difference. Suppression: all cells n < 5, with the complement check (codebook §7).

---

Measure & Meaning Research · measuremeaning.com{{#if sample_mode}} · This sample report contains only illustrative, synthetic data and a fictional organization.{{/if}}

---

## Automation field schema

Generate from the structured engagement record (screened data file + crosstab workbook + engagement codebook), then render with the Node + `docx` pipeline (refactor target: `scripts/build_report.js`). Groups:

- **engagement:** report_type_label, study_design_label, client_name, client_descriptor, sample_mode (bool), report_month_year
- **framing:** decision_context, key_findings[]{headline, body, figure_ref}, headline_recommendation, background_narrative, n_objectives, objectives[]{num, question, module}
- **method:** fielding_mode_sentence, median_completion_min, n_modules, module_list, n_closed_items (optional, empty by default), n_open_ends, weighting_skew_note
- **sample:** units[]{name, invited, completed, screened, rr, moe, idx_eng}, n_invited, n_completed, n_analyzed, response_rate, moe_org
- **screening:** scr_speed_flag, scr_speed_excl, scr_straight_flag, scr_straight_excl, scr_ac_flag, scr_ac_excl, scr_kiosk_flag, scr_kiosk_excl, scr_total_excl, scr_rate
- **core (← IDX_ENG):** core_section_verdict, idx_eng_org, core_narrative
- **nps (← ENPS, NPS_CLASS):** enps_org, enps_narrative, nps_mean_org, small_unit_example_n, small_unit_swing
- **gap (← GAP_*, COV_*, IMP_MED/SAT_MED):** n_gap_conditions, n_action_zone, action_zone[]{label, code}, gap_narrative, gap_highlight_threshold, gap_pay … gap_fdk (18 scalars by code), coverage_notes[]{share, condition, reason}
- **brn (← IDX_BRN, BRN_TIER):** brn_section_verdict, brn_narrative, brn_by_tenure[]{band, elevated_share}
- **open:** coder_agreement, quote_mode_label, quotes[]{text, segment}
- **driver (← spec_driver_models, spec_predictors):** r2_driver_model, r2_divergence_model, n_predictors (computed from the CSV `spec_predictors` row at render time — never typed), n_drivers_shown, drivers[]{code, label, shap_share, cost_tag}, divergence_points[]{code, label, share_sty01, share_sty02}, divergence_reading, stated_vs_derived_narrative, retention_leverage_reading
- **staytype (← STAY_TYPE):** stay_settled_pct, stay_reluctant_pct, stay_uncertain_pct, stay_leaving_pct, sty01_mid_pct, sty02_mid_pct, stay_excluded_pct, stay_type_narrative
- **custom (← Block X, per-engagement codebook addendum):** custom_module (bool, false by default), custom_section_intro, custom_items[]{id, label, scale, result_summary, figure_ref}, n_custom_items (computed as length of custom_items[])
- **actions:** horizon_now/next/then, actions_now[] / actions_next[] / actions_then[] {headline, evidence, detail}, followup_plan
- **limitations:** longitudinal_plan, linkage_option, small_unit_limitation, trend_baseline_limitation
- **appendix:** modules[]{name, items, scale, rule}, trim_lo, trim_hi, weight_min, weight_max, deff, n_effective

## Notes

- The BOILERPLATE blocks are the automation anchors and the audit trail: the anonymity threshold, the significance ≠ importance rule, the scale rationale, and the BRN_TIER cutpoint disclosure appear verbatim in every deliverable. If a client engagement pressures any of them, that is an owner decision, not a template edit.
- `{{n_closed_items}}` stays empty unless a contract requires a count — the census is modular; pulse surveys are subset configurations of the same module map, filled from the same schema.
- `{{n_predictors}}` and `{{n_custom_items}}` are computed, never typed (owner decision 2026-07-22, D4 — three documents previously stated three different predictor counts, none computed).
- With `custom_module` false, §4.6 and all Block X conditionals collapse and the rendered report is structurally identical to the standard deliverable — the allowlist principle (codebook §1.1) guarantees the pipeline side of the same invariant.
- The divergence model's presentation rule (exhibit + prose, never a second ranked list) is non-negotiable (owner decision 2026-07-22, D8); a renderer that produces two ranked lists is a bug, not a style choice.
- Placeholder ↔ codebook coupling is deliberate (codebook §1): the same IDs run through the raw export, the crosstab workbook, and this template.

---

*Document owner: A. Akhtyrskii · Prepared with Claude · Template v1.2 · 2026-07-22*
