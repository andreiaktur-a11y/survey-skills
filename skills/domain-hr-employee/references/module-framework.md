# Measure & Meaning — Employee Domain

## Module Framework & Question Bank · v0.4

**Status:** owner-reviewed draft (v0.4 — segmentation bands fixed; instrument and codebook now exist as separate artifacts) · **Repo target:** `skills/domain-hr-employee/references/module-framework.md` **All example items are original Measure & Meaning formulations (IP tier A) unless marked otherwise. All sample figures, thresholds, and org names in this document are illustrative \+ synthetic.**

**IP tier legend** (per standing rules):

- **A** — own/official: original synthesis, safe to publish and reuse.  
- **B** — public/academic: paraphrase \+ attribute \+ verify license per instrument.  
- **C** — proprietary vendor (e.g., Gallup Q12, MBI, PCQ/PsyCap, vendor burnout tools): **never copied.** Structural inspiration only.

**Changelog v0.4 (supersedes v0.3):**

- **§10 tenure bands replaced.** The previous 1–3 / 3–7 grid double-assigned employees at exactly 3 and 7 years. New non-overlapping grid: **Less than 1 year · 1–2 years · 3–6 years · 7 years or more** (owner decision, 2026-07-19).
- **§5 quadrant boundaries reconfirmed as within-survey medians** — the scale-midpoint alternative was reviewed and rejected; rationale (ceiling effect on stated importance) now documented in-line.
- **Companion artifacts added:** the fielded instrument and the variable definitions have moved out of this document into `questionnaire-employee-census.md` v0.1 and `codebook-employee-census.md` v0.1. This file remains the item bank and methodological rationale; those files govern fielding and analysis.

**Changelog v0.3 (superseded by v0.4):**

- **GAP scale changed 6-point no-midpoint → 7-point fully verbalized, with an off-scale "Not applicable" option on satisfaction items.** This reverses the v0.2 "signature" decision — rationale in §2.1.  
- CRS resolved: organizational-support wording retained; self-efficacy variant excluded under the §9 guardrail.

*Carried from v0.2:* PSY module dropped \+ PsyCap guardrail; GAP set 18 core \+ 2 extended; SAT-00 anchor added; FLX reframed to "schedule fit".

---

## 1 · How modules combine: need → study design map

Each client engagement is assembled from modules. The Decision Lab (Phase 2\) will route to these same combinations.

| Client need (trigger) | Modules | Target length | Primary deliverable focus |
| :---- | :---- | :---- | :---- |
| Rising voluntary turnover | CORE \+ NPS \+ GAP \+ STAY (driver model) | 10–12 min | What predicts leaving; cheapest levers first |
| Burnout / overload concern | CORE \+ BRN \+ workload GAP items \+ OPEN | 8–10 min | Risk concentration by segment; workload math |
| EVP development / employer brand | GAP (core 18 \+ extended) \+ trade-offs \+ segments | 12–15 min | Segment-level value profiles → EVP messaging |
| Annual engagement census | CORE \+ NPS \+ GAP \+ BRN \+ STAY \+ OPEN | 12–15 min | Full picture \+ year-over-year tracking baseline |
| Quarterly pulse | CORE-short (5 items) \+ NPS \+ 1 OPEN | 3–5 min | Movement vs. baseline, not new diagnosis |
| Post-change check (reorg, leadership change, M\&A) | CORE \+ change/communication add-on \+ OPEN | 6–8 min | Trust & clarity gaps by affected unit |

Length budget rule of thumb: respondents process \~4–6 closed items per minute; every open-ended question ≈ 45–60 seconds. Anything over 15 minutes measurably increases speeding and straightlining (see §2.3). **Length note for GAP:** 18 core pairs \= 36 rated items ≈ 6–8 min on their own. Engagements that run the full census should either use the 18-pair set with no extended categories, or trim CORE/BRN — the module map above already reflects this budget.

---

## 2 · Cross-cutting standards (apply to every module)

### 2.1 Scales

- **Agreement items:** 5-point Likert (Strongly disagree … Strongly agree), US-market convention; midpoint retained.  
- **Importance × Satisfaction pairs (GAP module):** **7-point, fully verbalized (every point labeled, not just the poles), midpoint retained.**  
  - *Importance* (unipolar): Not at all important · Slightly important · Somewhat important · Moderately important · Important · Very important · Extremely important.  
  - *Satisfaction* (bipolar): Very dissatisfied · Dissatisfied · Somewhat dissatisfied · Neither satisfied nor dissatisfied · Somewhat satisfied · Satisfied · Very satisfied.  
  - **"Not applicable / no experience with this" is offered off-scale on satisfaction items only** (e.g., an employee who has never used tuition support). N/A responses are excluded from means and reported as a coverage statistic, never recoded to the midpoint.  
  - *Rationale (documented in every technical appendix):* satisfaction is bipolar, so a neutral state is a real position and forcing a direction manufactures signal; importance is unipolar, where the middle point is a level ("moderately important"), not an escape hatch — full verbalization is what keeps it a level. An odd number of categories also yields a stable within-survey **median**, which is what defines the GAP quadrant boundaries (§5); on an even scale those boundaries fall between categories and drift between waves. 7 points align with prevailing US practice (5- and 7-point Likert, 0–10 for NPS) and with clean top-2-box reporting (6–7).  
  - *Quality monitoring:* midpoint share is tracked as a data-quality indicator alongside straightlining — an anomalously high midpoint rate across the whole matrix is treated as a satisficing signal (§2.3).  
- **eNPS:** 0–10, canonical anchors ("Not at all likely" … "Extremely likely"). Never 1–10: promoter/detractor cutoffs (9–10 / 0–6) are defined on the 0–10 scale, and clients benchmark against them.  
- **Overall satisfaction anchor (SAT-00):** 5-point (Very dissatisfied … Very satisfied), asked once before the GAP matrix.  
- Scale direction is uniform within a matrix; reverse-keyed items are flagged in the codebook, never mixed silently.

### 2.2 Anonymity & reporting thresholds

- **No breakout reported for any group of N \< 5** (standing rule). Suppressed cells are shown as "n/a (below reporting threshold)" — never silently dropped.  
- Open-ended quotes are paraphrased or lightly edited if verbatim text could identify the author; role \+ tenure metadata attached to quotes only when the cell exceeds threshold.

### 2.3 Data quality screening (differentiator — disclose in every report)

Screening rules are pre-registered in the technical appendix and applied before any analysis:

- **Speeders:** completion time \< 1/3 of the median → flag; \< 2 s per item sustained → exclude.  
- **Straightliners:** zero variance across ≥ 20 consecutive matrix items → flag; combined with speeding → exclude.  
- **Attention check** (1 per \~50 items): "For data quality purposes, please select 'Agree' for this statement." Failure → flag; two failures → exclude.  
- **Shared devices/kiosks** (common on production floors): identical device signatures are acceptable by design, but response-time clustering is reviewed for proxy completion.  
- Report always states: N collected → N after screening → screening rate, by major segment.

### 2.4 Item ID convention (automation-ready)

Every item carries a stable ID (`ENG-01`, `GAP-PAY-I`, `GAP-PAY-S` …) used in the codebook, crosstab workbook, and the future `{{braces}}` report template. IDs never change meaning between waves; revised wording gets a new ID with a suffix (`ENG-01b`).

---

## 3 · Module CORE — Engagement

**Decision question:** How engaged is the workforce, and where is engagement uneven? **Index:** mean of ENG-01…06 rescaled to 0–100; reported by segment vs. org average. **Signature visualization:** horizontal bars by unit with dashed org-average line (as in sample report Fig. 1).

| ID | Item (5-pt agreement) |
| :---- | :---- |
| ENG-01 | Most days, my work gives me more energy than it takes. |
| ENG-02 | I am proud to tell people where I work. |
| ENG-03 | My work gives me a real sense of accomplishment. |
| ENG-04 | When my team needs extra effort, I am willing to give it. |
| ENG-05 | I can see a future for myself at this organization. |
| ENG-06 | I care about what this organization is trying to achieve. |

**CORE-short (pulse):** ENG-01, ENG-02, ENG-05 \+ NPS-01 \+ one open-end. **Caveats disclosed:** engagement indices are formative composites, not clinical measures; comparisons across waves require identical wording and comparable fielding windows. **IP note:** Gallup Q12 and UWES occupy this space — tier C and tier B respectively; no wording overlap permitted.

---

## 4 · Module NPS — Employee Net Promoter Score

**Decision question:** Would employees recommend us — and what moves that willingness?

| ID | Item |
| :---- | :---- |
| NPS-01 | How likely are you to recommend \[Organization\] as a place to work to a friend or colleague? (0–10) |
| NPS-02 | What is the main reason for your score? (open) |

**Index:** % Promoters (9–10) − % Detractors (0–6). Mean score reported as a *secondary* statistic only. **Why both:** the mean and the index can move in opposite directions (e.g., detractors softening from 2→5 raises the mean, leaves eNPS unchanged). The report explains any divergence rather than hiding one number. **Signature visualization:** 100% stacked bar (detractor/passive/promoter) by segment, with eNPS value labeled; NPS-02 themes coded and cross-tabbed by promoter class. **Caveats disclosed:** eNPS is a blunt single-item metric — useful for tracking, weak for diagnosis; always pair with driver analysis. Small segments produce unstable eNPS (a 20-person unit moves ±10 pts on two changed answers) — confidence intervals shown.

---

## 5 · Module GAP — Importance × Satisfaction (quadrant analysis)

**Decision question:** Which conditions matter most to employees, and where does the organization under-deliver on what matters?

Methodological signature carried over from the principal's academic work: each value/condition rated twice — importance when choosing an employer (1–7) and satisfaction in the current role (1–7, plus off-scale N/A). Analysis plots the two against each other.

**Anchor item (before the matrix):**

| ID | Item |
| :---- | :---- |
| SAT-00 | Overall, how satisfied or dissatisfied are you with \[Organization\] as an employer? (5-pt) |

SAT-00 serves as a criterion variable for the driver model (alongside STY-01) and as a headline trend metric between waves.

### Core set v2 — 18 categories

Each category \= one importance item (`GAP-XXX-I`) \+ one satisfaction item (`GAP-XXX-S`).

| Code | Category | Wording (rated for importance and satisfaction) |
| :---- | :---- | :---- |
| PAY | Pay fairness | My total pay reflects my skills and what I contribute. |
| REC | Recognition | Good work here gets noticed and acknowledged. |
| MGR | Manager relationship | I can work with my direct manager openly and without friction. |
| GRW | Career growth | There is a realistic path to grow my career here. |
| LRN | Learning & development | I can build new professional skills through my work, including formal training and development programs. |
| FLX | Schedule fit | My work schedule fits my life — hours, predictability, and the flexibility available to me. |
| WKL | Sustainable workload | My workload is one I can sustain long-term without burning out. |
| BEN | Benefits & social support | The benefits package (health, retirement, family support) works for my real life. |
| MNG | Meaningful work | My work contributes to something I consider worthwhile. |
| AUT | Autonomy | I can decide how to do my own work. |
| TEA | Team relationships | I work with people I trust and enjoy working with. |
| SEC | Job security | I am confident in this organization's stability and future. |
| RES | Tools & resources | I have the tools, equipment, and resources I need to get my work done. |
| VOI | Voice & participation | My ideas can actually influence decisions in my area, and leaders are willing to hear them. |
| CRS | Support in difficult situations | If I run into a difficult situation — at work or in life — this organization will help me through it. |
| SAF | Workplace safety | I feel safe and protected while doing my job. |
| COM | Communication & information | I get the information I need about what is happening in the organization and how it affects me. |
| FDK | Feedback | I know how my work is evaluated and what I can do to improve. |

*Mapping notes (owner edits → v0.2/v0.3):* former CND (working conditions) split: physical/tooling side → **RES**; safety side → new **SAF**. Owner's "я могу говорить о проблемах и просить помощь" folded into **VOI** (leader receptiveness) and **CRS** (help-seeking). Owner's pension addition folded into **BEN** wording (retirement). FLX reframed per owner from "control over when/where" to "schedule fit" — deliberately inclusive of production/shift roles that have no scheduling control but can still have good or poor schedule fit.

### Extended set (optional, EVP-focused engagements)

| Code | Category | Wording |
| :---- | :---- | :---- |
| MEN | Mentoring & knowledge sharing | I can act as a mentor to newer colleagues and share my expertise. |
| EVT | Community & shared events | The organization regularly brings people together outside day-to-day work (events, teams, traditions). |

*Owner's other four candidates — mapped, not added, to avoid duplicate constructs:* participation in unit priorities → covered by **VOI**; corporate training programs → covered by **LRN** (wording extended); manager receptiveness to ideas → covered by **VOI** (wording extended); learning from an innovative team → covered by **LRN** \+ **TEA**. If any of these needs to be measured *separately* (e.g., for a specific EVP hypothesis), it can be activated per-engagement with its own ID — flag at design stage.

**Index & visualization:** quadrant map — X \= satisfaction, Y \= importance, quadrant boundaries at within-survey medians (not scale midpoints; disclosed). *Why medians and not the scale midpoint (reviewed and reconfirmed 2026-07-19):* stated importance has a ceiling — employees rarely call pay, safety, or growth unimportant, so in practice all categories sit above the scale midpoint and a midpoint-anchored cross leaves the lower quadrants permanently empty. Medians always split the field and answer the question the client actually asks (what to address first). The cost is that boundaries move between waves; it is offset by (a) the ranked gap chart, which is absolute and does not drift, and (b) from wave 2 onward, plotting the prior wave's medians as a grey reference cross so it is visible whether a category moved or the boundary did. Top-left quadrant (high importance, low satisfaction) \= **action zone**, labeled per segment. Gap score \= importance − satisfaction, ranked. **Caveats disclosed:** stated importance ≠ derived importance; the report shows both stated ranks and driver-model ranks side by side and explains disagreements (they are frequent and informative). **Extension (design-on-request):** trade-off block — forced-choice pairs between categories (MaxDiff-lite) with a **balanced design** (each category appears an equal number of times, pairs counterbalanced).

---

## 6 · Module BRN — Burnout risk (organizational, aggregate-only)

**Decision question:** Where is burnout risk concentrated, and is it demand-driven or recovery-driven? **Positioning:** an *organizational risk screen*, not a clinical assessment and not individual feedback — reported only at segment level, N ≥ 5\. (Individual percentile-feedback reports of the vendor type are a different product genre and out of scope.)

| ID | Item (5-pt agreement) |
| :---- | :---- |
| BRN-01 | By the end of a typical workday, I have little energy left for anything else. |
| BRN-02 | Evenings, weekends, and vacations are enough for me to recover from work. *(R)* |
| BRN-03 | I find it harder to get interested in my work than I used to. |
| BRN-04 | My current workload is sustainable for the long term. *(R)* |
| BRN-05 | I feel increasingly detached from what happens in this organization. |
| BRN-06 | In the past month, work stress has affected my sleep or health. |

**Index:** risk tiers (low / moderate / elevated) from summed score terciles or pre-set cutpoints — cutpoint logic disclosed; never diagnostic language. **Signature visualization:** 100% stacked tiers by tenure band / unit (as in sample report Fig. 3), plus a demand-vs-recovery 2×2 (BRN-01/04 vs BRN-02). **Caveats disclosed:** self-report screen; elevated tier \= priority for organizational intervention, not an individual label. **IP note:** MBI (tier C, Mind Garden), OLBI (tier B — free for research, verify for commercial use), vendor tools (tier C). Item set above is original tier-A wording; structural inspiration ("state → components → unmet needs → actions") acknowledged generically, no vendor named.

---

## 7 · Module STAY — Retention intent & driver model (the differentiator)

**Decision question:** What actually predicts intent to stay — and which levers give the most retention per dollar?

| ID | Item |
| :---- | :---- |
| STY-01 | I expect to still be working at this organization twelve months from now. (5-pt) |
| STY-02 | In the past six months, I have seriously considered leaving. (5-pt) |
| STY-03 | Which best describes your current plans? \[ Planning to stay / Open to outside offers / Actively looking \] |

**Analysis standard:**

1. Bivariate first: rank correlations of module indices & GAP satisfaction items with STY-01 and SAT-00 (transparent, client-readable).  
2. Then relative importance: dominance analysis or Shapley-value decomposition on the driver set — because predictors are intercorrelated and raw correlations over-credit redundant drivers.  
3. **Significance ≠ importance:** at census-scale N, nearly everything is "significant"; the report ranks by effect size and shows a stated-vs-derived importance comparison. No unadjusted full significance matrices in client-facing sections; the full matrix lives in the appendix with a multiple-comparison note.

**Signature visualization:** dot plot of driver strength vs. intent to stay (sample report Fig. 2), annotated with a cost-to-address tag (low/med/high) → the "retention per dollar" framing.

---

## 8 · Module OPEN — Open-ended & coding standard

| ID | Item |
| :---- | :---- |
| OPN-01 | What is the single most important thing this organization could change to make it a better place to work? |
| OPN-02 | What should this organization be careful **not** to change? |
| OPN-03 | (need-specific slot, e.g., post-change:) What about the recent changes is still unclear to you? |

**Standard:** thematic coding by two coders with adjudication; theme frequencies cross-tabbed by segment and promoter class; quotes only above anonymity threshold.

---

## 9 · Module PSY — ❌ dropped (owner decision, 2026-07-19)

PCQ/PsyCap is tier C (copyright F. Luthans et al.; licensed via Mind Garden). Owner decision: **module not used**; no license pursued, no tier-A substitute built for v1. **Guardrail:** PsyCap-style constructs (self-efficacy, hope/pathways, resilience, optimism) must not re-enter the library through other modules' wording. Any item phrased as *"I can find many ways to solve problems"* or similar self-referential capability statements is out of scope — see §11.2 decisions log on CRS.

---

## 10 · Segmentation block (asked once, drives all breakouts)

Asked once, at the **end** of the instrument (placement rationale and trade-off in `questionnaire-employee-census.md` §9).

| Field | Categories | Weighting cell |
| :---- | :---- | :---- |
| Tenure band | **Less than 1 year · 1–2 years · 3–6 years · 7 years or more** | yes |
| Function / direction | client-specific, mirrored from HRIS | yes |
| Role level | Individual contributor · Team lead/supervisor · Manager · Senior leadership | yes |
| Site / location | client-specific, mirrored from HRIS | no |
| Age band | Under 25 · 25–34 · 35–44 · 45–54 · 55 or older | no |
| *(optional per engagement)* | children/caregiving · education | no |

**Tenure bands are non-overlapping by construction** (owner decision, 2026-07-19). Bands stated in whole years with no shared boundary and no gap: an employee with 3 years of service has exactly one home. The retired 1–3 / 3–7 grid double-assigned everyone at 3 and at 7 years, and in a self-completion checkbox that resolves as a coin flip, not as a rule.

Category sets mirror payroll/HRIS categories so results can be **weighted to payroll records** (department × tenure × role) to correct nonresponse skew — the weighting scheme is disclosed in every report. If a client's HRIS uses different tenure bands, **re-band the HRIS extract, not this instrument**: changing the bands here re-introduces the boundary ambiguity and breaks comparability with every prior wave.

All segmentation fields carry an explicit "Prefer not to say" option, treated as missing for breakouts with the refusal rate reported. Standing anonymity threshold applies to every breakout: **no group of N < 5**.

## 11 · Flags & decisions

### 11.1 Open — needs owner input

1. **Extended set (MEN, EVT):** include in the standard EVP configuration, or keep strictly optional? *(Not included in the census configuration — 18 pairs already consume 6–8 min of a 12–15 min budget.)*  
2. **Trade-off block (MaxDiff-lite):** include in v1 of the library, or defer to "design-on-request"?  
3. **`OPN-03`:** leave as an empty need-specific slot, or promote to a standing third open-end?

*Further open flags now live in the companion artifacts and are tracked there, not duplicated here:* `questionnaire-employee-census.md` §12 (item-count consistency with the sample report) · `codebook-employee-census.md` §9 (`BRN_TIER` cutpoints, weight-trimming bounds, `STY-02` scoring).

### 11.1a Comparability note (not a blocker)

The 6→7 scale change is made **before** the first US wave, by design: after a baseline is fielded, any scale change breaks trend comparability and forces either a bridging study or a reset of the benchmark. Historical reference data collected on the 6-point instrument are **not** directly comparable to future M\&M waves; they remain a structural reference only, on a separate market and a deferred track.

### 11.2 Resolved (decisions log)

- **2026-07-19** Tenure bands replaced with a non-overlapping grid (Less than 1 year / 1–2 / 3–6 / 7 years or more); HRIS extracts re-banded to match, not the reverse (owner).
- **2026-07-19** GAP quadrant boundaries reconfirmed as **within-survey medians**; scale-midpoint anchoring reviewed and rejected on the ceiling-effect argument (owner).
- **2026-07-19** Sample-report disclaimer policy: the illustrative/synthetic label is mandatory on the **cover block and running header**; per-figure caption labels are optional (owner).
- **2026-07-19** Fielded instrument and codebook split out into separate repo artifacts (v0.1 each); this document remains the item bank and rationale (owner).
- **2026-07-19** PSY module dropped; PsyCap guardrail added (owner).  
- **2026-07-19** ~~6-point no-midpoint GAP scale confirmed as signature~~ — **superseded same day**: GAP scale set to **7-point fully verbalized \+ midpoint \+ off-scale N/A** on satisfaction (owner). Signature status transferred to the substantive differentiators (driver analysis, data-quality screening), not the scale format.  
- **2026-07-19** CRS resolved: organizational-support wording retained; self-efficacy variant excluded under §9 guardrail (owner).  
- **2026-07-19** GAP category set updated to 18 core \+ 2 extended; four candidate categories mapped into existing constructs (owner edits \+ methodological consolidation).  
- **2026-07-19** SAT-00 overall-satisfaction anchor added (owner).  
- **2026-07-19** FLX reframed to "schedule fit" (owner).

*Document owner: A. Akhtyrskii · Prepared with Claude · v0.4 · 2026-07-19*  
