# Measure & Meaning — Employee Domain

## Field Questionnaire · Annual Engagement & Retention Census · v0.3

**Status:** release per consolidated handoff 2026-07-22 (flags session C) — implements F1, F2, D6, Block X placement · **Repo target:** `skills/domain-hr-employee/references/questionnaire-employee-census.md`
**Configuration:** CORE + NPS + GAP (18 core) + BRN + STAY + OPEN + segmentation — the "annual engagement census" row of the module map (§1 of `module-framework.md` v0.4) — plus an optional per-engagement Block X (client add-on items, §8).
**Companion artifacts:** `module-framework.md` v0.4 (item bank & rationale) · `codebook-employee-census.md` v0.3 + `codebook-employee-census.csv` v0.3 (variables, indices, screening, machine-readable model spec) · `report-template-employee-census.md` v1.2 (deliverable template) · `Employee_Engagement_Retention_SAMPLE_v3_2.docx` (what the client receives).

**All items are original Measure & Meaning formulations (IP tier A).** No wording is taken from Gallup Q12, UWES, MBI, OLBI, PCQ, or any vendor instrument.

**Length:** 60 closed items + 3 open-ends ≈ 13–16 minutes median (budget rule: 4–6 closed items/minute; ~45–60 s per open-end). Client add-on items are **additive and budgeted**, never traded against the core (owner decision 2026-07-22, D6): custom closed items are capped at **8** (≈ +1.5–2 minutes), and in that configuration the instrument runs **~15–17 minutes** — a figure stated in the report's method section. **BRN is never trimmed** while the burnout tier is a deliverable — `IDX_BRN` and `BRN_TIER` require ≥ 5 of 6 items answered (codebook §4.2). **The 18-category GAP set is never trimmed** — fewer categories move `IMP_MED`/`SAT_MED` and break quadrant comparability across waves and clients. `OPN-03` is the free custom open-end slot and costs nothing when left unfielded.

---

## 0 · Programming specification (read before building)

| Setting | Specification |
|---|---|
| **Platform** | Any (Qualtrics / SurveyMonkey / Forms). Block structure below maps 1:1 to platform blocks. |
| **Piping** | `[Organization]` is piped from a single survey-level field. Set once; never hard-code per screen. |
| **Forced response** | **Never force.** Employee surveys run on trust; forcing answers raises break-off and undermines the anonymity promise. Use one soft prompt ("You skipped some items — continue anyway?") per screen, then allow continuation. |
| **Back button** | Enabled through the end of the OPEN block; disabled after the segmentation block begins. |
| **Progress bar** | Shown. Employees over-estimate length in matrix-heavy instruments. |
| **Save & resume** | Enabled (production shift workers may be interrupted). |
| **Devices** | Mobile-first rendering required; GAP matrix must reflow to a card layout on narrow screens (see §5 note). |
| **Kiosk mode** | Shared production-floor stations: clear session on submit; no autofill; no device fingerprint used for identification. Identical device signatures are expected by design. |
| **Timing capture** | Record page-level timestamps for every screen — required for the speeder screen (§ codebook). |
| **Display order capture** | Where category order is randomized, store the realized order per respondent. |
| **Anonymity** | No IP address, no email, no employee ID stored with responses. |

---

## 1 · Welcome screen

> ### [Organization] Employee Survey
>
> This survey asks how it is to work at [Organization] — what is working, what is not, and what would make the biggest difference. It takes about 15 minutes.
>
> **Your answers are anonymous.** The survey is run by Measure & Meaning Research, an independent research firm. [Organization] receives grouped results only — never individual responses. **No result is ever reported for a group of fewer than 5 people, and additional results are withheld whenever a small group could be worked out from the ones that are shown.**
>
> There are no right answers, and nothing here is a test of you. Please answer for how things actually are, not how they are supposed to be.
>
> You can pause and return using the same link. If you would rather not answer a question, you can skip it.
>
> [ Start the survey → ]

*Programming note:* no consent checkbox — proceeding constitutes participation, which is standard for anonymous workplace surveys and avoids the impression that consent is being logged against a person. If client counsel requires an explicit affirmative consent step, add it here and record it as a survey-level flag (`CONSENT`), never joined to responses.

---

## 2 · Block A — Overall satisfaction anchor

*One screen. Asked before the detailed matrix so the global judgment is not built up from — or contaminated by — the 18 specific conditions.*

**SAT-00.** Overall, how satisfied or dissatisfied are you with [Organization] as an employer?

☐ Very dissatisfied ☐ Dissatisfied ☐ Neither satisfied nor dissatisfied ☐ Satisfied ☐ Very satisfied

---

## 3 · Block B — Engagement (CORE)

*One screen, 6 items, matrix. Item order fixed (not randomized) so wave-over-wave order effects stay constant.*

**Instruction:** How much do you agree or disagree with each statement?
**Scale (all items):** Strongly disagree · Disagree · Neither agree nor disagree · Agree · Strongly agree

| ID | Item |
|---|---|
| ENG-01 | Most days, my work gives me more energy than it takes. |
| ENG-02 | I am proud to tell people where I work. |
| ENG-03 | My work gives me a real sense of accomplishment. |
| ENG-04 | When my team needs extra effort, I am willing to give it. |
| ENG-05 | I can see a future for myself at this organization. |
| ENG-06 | I care about what this organization is trying to achieve. |

---

## 4 · Block C — Recommendation (NPS)

*Two screens: the score, then the reason. Splitting them prevents the open-end from being skipped as part of the same visual block.*

**NPS-01.** How likely are you to recommend [Organization] as a place to work to a friend or colleague?

`0` Not at all likely — `1` — `2` — `3` — `4` — `5` — `6` — `7` — `8` — `9` — `10` Extremely likely

*Programming note:* **0–10 only.** Never 1–10 — the promoter (9–10) and detractor (0–6) cutoffs are defined on the 0–10 scale.

**NPS-02.** What is the main reason for your score? *(open text, ~500 char)*

---

## 5 · Block D — What matters and how we deliver (GAP)

*Three screens of 6 categories each. Both ratings for a category appear together on the same row — pairing must stay visible, or respondents rate importance and satisfaction as two unrelated batteries.*

**Screen instruction (repeated on each of the 3 screens):**

> For each item below, please give us two ratings:
> **left** — how important it is to you when choosing an employer;
> **right** — how satisfied you are with it in your current role at [Organization].

**Importance scale (unipolar, 7 points, every point labeled):**
Not at all important · Slightly important · Somewhat important · Moderately important · Important · Very important · Extremely important

**Satisfaction scale (bipolar, 7 points, every point labeled):**
Very dissatisfied · Dissatisfied · Somewhat dissatisfied · Neither satisfied nor dissatisfied · Somewhat satisfied · Satisfied · Very satisfied
**+ off-scale option, satisfaction only:** ⟂ Not applicable / no experience with this

*Programming notes for the N/A option:*
1. It is **not an eighth scale point.** Render it separated by a vertical rule or gap, visually outside the 7-point track.
2. Stored as a distinct code (`99`), never as a scale value.
3. Offered on **satisfaction only** — every employee can judge how important pay is; not every employee has used tuition support.
4. Excluded from all means; reported as a coverage statistic per category.

*Order:* the 18 categories are randomized across respondents (blocked so that each screen of 6 is drawn from the full set); realized order is stored. Wording is fixed.

### The 18 categories

| Code | Category | Wording (rated twice: importance, then satisfaction) |
|---|---|---|
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

### Attention check 1

*Placed on GAP screen 2, in the satisfaction column, styled identically to a real row.*

**AC-01.** For data quality purposes, please select "Satisfied" for this row.

*Mobile layout note:* below ~600 px the side-by-side row layout fails. Reflow to one card per category: category wording on top, importance scale, then satisfaction scale with the N/A option below a divider. Never collapse to two separate 18-item batteries.

---

## 6 · Block E — Burnout risk screen (BRN)

*One screen, 6 items, matrix. Positioned after the GAP block so the more sensitive material comes once the respondent is committed, and before the retention questions.*

**Instruction:** How much do you agree or disagree with each statement?
**Scale (all items):** Strongly disagree · Disagree · Neither agree nor disagree · Agree · Strongly agree

| ID | Item | Keying |
|---|---|---|
| BRN-01 | By the end of a typical workday, I have little energy left for anything else. | + |
| BRN-02 | Evenings, weekends, and vacations are enough for me to recover from work. | **reverse** |
| BRN-03 | I find it harder to get interested in my work than I used to. | + |
| BRN-04 | My current workload is sustainable for the long term. | **reverse** |
| BRN-05 | I feel increasingly detached from what happens in this organization. | + |
| BRN-06 | In the past month, work stress has affected my sleep or health. | + |

*Programming note:* reverse-keyed items are presented in the same scale direction as the rest of the matrix — **never flip the scale on screen.** Reversal happens at scoring, and is flagged in the codebook.

### Attention check 2

**AC-02.** For data quality purposes, please select "Agree" for this statement.

*Placed as the 4th row of this matrix.*

---

## 7 · Block F — Retention intent (STAY)

*One screen. This block supplies the criterion variable for the driver model.*

**Instruction:** How much do you agree or disagree?
**Scale:** Strongly disagree · Disagree · Neither agree nor disagree · Agree · Strongly agree

| ID | Item |
|---|---|
| STY-01 | I expect to still be working at this organization twelve months from now. |
| STY-02 | In the past six months, I have seriously considered leaving. |

**STY-03.** Which best describes your current plans?

☐ Planning to stay ☐ Open to outside offers ☐ Actively looking ☐ Prefer not to say

*Programming note:* "Prefer not to say" is offered here and on the segmentation items — nowhere among the attitudinal items. Intent to leave is the single most identity-exposing attitudinal question in an employee survey; refusing it must be easier than lying on it. Treated as missing for breakouts, and its rate is reported.

---

## 8 · Block X — Client add-on items (optional, per engagement)

*Fielded only when the engagement adds client-requested items (e.g. evaluating an internal programme or event). Absent from the standard census — when absent, the instrument proceeds directly from Block F to Block G.*

- **Placement:** closed `CUS-*` items sit here — **after Block F (STAY), before Block G (OPEN)** — so the open-ended verbatims are not lost to break-off. The open-ended custom item uses the existing `OPN-03` slot (§9); no additional open-end screen is created.
- **Scales:** must reuse an existing scale from codebook §2 (AGREE-5, SAT-5, IMP-7, SAT-7, NPS-11). New scale types require an owner decision — they break shared rendering and screening logic.
- **Budget:** capped at 8 closed items (≈ +1.5–2 minutes; see the length note in the header, D6).
- **Screening:** `CUS-*` items are **excluded** from the straightlining and speeding screens — variable block length would make those rules non-comparable across engagements.
- **Everything else** — the `CUS-` ID convention, index and driver-model isolation, per-engagement documentation in the codebook addendum, and conditional reporting as §4.6 of the deliverable — is governed by **codebook v0.3 §10**; the rules are deliberately not duplicated here.

---

## 9 · Block G — Open-ended (OPEN)

*One screen, three boxes. Placed after the closed items so it does not prime them, and before segmentation so break-off does not cost the qualitative data.*

| ID | Item |
|---|---|
| OPN-01 | What is the single most important thing this organization could change to make it a better place to work? |
| OPN-02 | What should this organization be careful **not** to change? |
| OPN-03 | *(need-specific slot — omitted in the standard census; activated per engagement, e.g. post-change: "What about the recent changes is still unclear to you?")* |

**Screen text above the boxes:**

> Please avoid naming individual colleagues. Comments are read by the research team, grouped into themes, and reported to [Organization] as themes with example quotations. Quotations are paraphrased where the exact wording could identify who wrote it.

---

## 10 · Block H — About you (segmentation)

*Placed last, deliberately — see the trade-off note below. One screen.*

**Screen text:**

> These last questions let us compare results between groups — for example, whether new hires see things differently from long-tenured employees. **No group smaller than 5 people is ever reported separately.**

| ID | Question | Categories |
|---|---|---|
| SEG-TEN | How long have you worked at [Organization]? | Less than 1 year · 1–2 years · 3–6 years · 7 years or more |
| SEG-FUN | Which best describes your area? | *(client-specific list, mirrored from HRIS)* · Prefer not to say |
| SEG-ROL | Which best describes your role level? | Individual contributor · Team lead / supervisor · Manager · Senior leadership · Prefer not to say |
| SEG-SIT | Which site do you work at most of the time? | *(client-specific list)* · Prefer not to say |
| SEG-AGE | Which age group are you in? | Under 25 · 25–34 · 35–44 · 45–54 · 55 or older · Prefer not to say |
| SEG-CAR | *(optional, per engagement)* Do you regularly care for children or another dependent? | Yes · No · Prefer not to say |
| SEG-EDU | *(optional, per engagement)* What is the highest level of education you have completed? | *(client-specific list)* · Prefer not to say |

**Category-set rule:** `SEG-TEN`, `SEG-FUN`, `SEG-ROL`, and `SEG-SIT` must mirror payroll/HRIS categories exactly. This is what makes weighting to payroll records (department × tenure × role) possible. If the client's HRIS uses different tenure bands, **change the HRIS-side extract, not this instrument** — the bands above are non-overlapping by construction (owner decision, 2026-07-19) and altering them re-introduces the boundary ambiguity.

**Placement trade-off (disclosed design choice):** segmentation is asked last. Asking it first raises break-off in employee surveys — a demographics wall reads as "they are working out who I am." The cost is that respondents who abandon before this block cannot be assigned to a segment or weighted. Expect 2–4% of completes to be segment-unassignable; they are retained in org-level results and excluded from breakouts, and this is stated in the report.

---

## 11 · Closing screen

> ### Thank you.
>
> Your answers are in. Results are grouped, analyzed independently by Measure & Meaning Research, and reported to [Organization] as themes and group-level figures — never as individual responses.
>
> [Organization] expects to share the findings with employees in **[timeframe]**.
>
> If this survey raised something you want to talk through with someone, [Organization]'s support resources are here: **[client-supplied link / EAP contact]**.

*Programming note:* the support-resources line is **required** in any configuration that includes the BRN block. A burnout screen that ends with nothing but "thanks" is poor practice — the instrument asked about sleep and health and should point somewhere.

---

## 12 · Block order rationale (documented, per the reporting standard)

1. **SAT-00 first** — a global judgment collected before the 18 specific conditions build it up piecewise.
2. **CORE, then NPS** — warm, non-sensitive, quick momentum.
3. **GAP in the middle** — the heavy 36-rating block sits where commitment is highest and fatigue has not yet peaked.
4. **BRN, then STAY** — sensitive items after rapport is established.
5. **Block X (when fielded) after STAY, before OPEN** — custom closed items ride on established commitment without displacing the verbatims (codebook §10).
6. **OPEN before segmentation** — verbatims are the most valuable content per respondent-minute; they should not be lost to demographic-wall break-off.
7. **Segmentation last** — anonymity-protective (see §10).

*Known limitation:* placing STAY after the driver batteries risks priming the criterion with the content of the predictors. The alternative — criterion first — primes in the other direction. There is no placement that removes the effect; the order is fixed across waves so that whatever effect exists is constant and does not contaminate trend comparison. This is stated in the technical appendix.

---

## 13 · Flags — all resolved (owner decisions, 2026-07-19, flags session B)

1. **Extended GAP categories (MEN, EVT) — resolved.** They stay in the item bank (`module-framework.md`) and are fielded **only in EVP-focused configurations where CORE/BRN are trimmed**. Not part of the standard census — the 18-pair set already consumes 6–8 of the 12–15-minute budget. *(v0.3 note, per D6: trimming CORE/BRN applies only to configurations where the burnout tier is not a deliverable. In the standard census BRN is never trimmed — `IDX_BRN`/`BRN_TIER` require ≥ 5 of 6 items — and client add-ons are handled additively via Block X, §8, not by trading away core modules.)*
2. **Trade-off block (MaxDiff-lite) — resolved.** **Design-on-request for v1**; not part of the standard deliverable or the report template.
3. **`OPN-03` — resolved.** Remains an **empty per-engagement slot** (codebook code `.n` when not fielded); no standing third open-end.
4. **Consistency with the sample report — resolved, in the report's favor of modularity.** The report and template **do not state a fixed closed-item count**: the census is modular (client add-ons possible; pulse surveys are subset configurations), so the method section describes modules, not counts. The sample report's method section was rewritten accordingly (v3.1). **Median completion time 13.4 minutes stays** — consistent with a ~60-item instrument at 4–6 items/minute. The template carries an *optional* `{{n_closed_items}}` field, **empty by default**, for engagements where a contract requires a stated count. This questionnaire's own header may state its configuration count (60 closed + 3 open) — the rule applies to the client-facing report, not to the field instrument spec.

*No open flags remain in this document.*

---

*Document owner: A. Akhtyrskii · Prepared with Claude · v0.3 · 2026-07-22*
