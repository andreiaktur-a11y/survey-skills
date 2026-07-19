# Measure & Meaning — Employee Domain

## Field Questionnaire · Annual Engagement & Retention Census · v0.1

**Status:** draft for owner review · **Repo target:** `skills/domain-hr-employee/references/questionnaire-employee-census.md`
**Configuration:** CORE + NPS + GAP (18 core) + BRN + STAY + OPEN + segmentation — the "annual engagement census" row of the module map (§1 of `module-framework.md` v0.3).
**Companion artifacts:** `module-framework.md` v0.3 (item bank & rationale) · `codebook-employee-census.md` (variables, indices, screening) · `Employee_Engagement_Retention_SAMPLE_v3.docx` (what the client receives).

**All items are original Measure & Meaning formulations (IP tier A).** No wording is taken from Gallup Q12, UWES, MBI, OLBI, PCQ, or any vendor instrument.

**Length:** 60 closed items + 3 open-ends ≈ 13–16 minutes median (budget rule: 4–6 closed items/minute; ~45–60 s per open-end). This sits at the top of the 12–15-minute census budget — if the client adds site-specific items, trim BRN to 4 items or drop `OPN-03` rather than exceeding it.

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
| **Devices** | Mobile-first rendering required; GAP matrix must reflow to a card layout on narrow screens (see §3 note). |
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
> **Your answers are anonymous.** The survey is run by Measure & Meaning Research, an independent research firm. [Organization] receives grouped results only — never individual responses. **No result is ever reported for a group of fewer than 5 people**, so small teams cannot be identified by subtraction.
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

*Programming note:* "Prefer not to say" is offered here and nowhere else in the instrument. Intent to leave is the single most identity-exposing question in an employee survey; refusing it must be easier than lying on it. Treated as missing, and its rate is reported.

---

## 8 · Block G — Open-ended (OPEN)

*One screen, three boxes. Placed after the closed items so it does not prime them, and before segmentation so break-off does not cost the qualitative data.*

| ID | Item |
|---|---|
| OPN-01 | What is the single most important thing this organization could change to make it a better place to work? |
| OPN-02 | What should this organization be careful **not** to change? |
| OPN-03 | *(need-specific slot — omitted in the standard census; activated per engagement, e.g. post-change: "What about the recent changes is still unclear to you?")* |

**Screen text above the boxes:**

> Please avoid naming individual colleagues. Comments are read by the research team, grouped into themes, and reported to [Organization] as themes with example quotations. Quotations are paraphrased where the exact wording could identify who wrote it.

---

## 9 · Block H — About you (segmentation)

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

## 10 · Closing screen

> ### Thank you.
>
> Your answers are in. Results are grouped, analyzed independently by Measure & Meaning Research, and reported to [Organization] as themes and group-level figures — never as individual responses.
>
> [Organization] expects to share the findings with employees in **[timeframe]**.
>
> If this survey raised something you want to talk through with someone, [Organization]'s support resources are here: **[client-supplied link / EAP contact]**.

*Programming note:* the support-resources line is **required** in any configuration that includes the BRN block. A burnout screen that ends with nothing but "thanks" is poor practice — the instrument asked about sleep and health and should point somewhere.

---

## 11 · Block order rationale (documented, per the reporting standard)

1. **SAT-00 first** — a global judgment collected before the 18 specific conditions build it up piecewise.
2. **CORE, then NPS** — warm, non-sensitive, quick momentum.
3. **GAP in the middle** — the heavy 36-rating block sits where commitment is highest and fatigue has not yet peaked.
4. **BRN, then STAY** — sensitive items after rapport is established.
5. **OPEN before segmentation** — verbatims are the most valuable content per respondent-minute; they should not be lost to demographic-wall break-off.
6. **Segmentation last** — anonymity-protective (see §9).

*Known limitation:* placing STAY after the driver batteries risks priming the criterion with the content of the predictors. The alternative — criterion first — primes in the other direction. There is no placement that removes the effect; the order is fixed across waves so that whatever effect exists is constant and does not contaminate trend comparison. This is stated in the technical appendix.

---

## 12 · Open flags (owner decision required)

1. **Extended GAP categories (MEN, EVT).** Not included in this census configuration — 18 pairs already consume 6–8 minutes and the census budget is 12–15. Include only in EVP-focused engagements where CORE/BRN are trimmed? → *pending (carried from `module-framework.md` §11.1).*
2. **Trade-off block (MaxDiff-lite).** Not included. Confirm "design-on-request" status for v1? → *pending (carried from §11.1).*
3. **`OPN-03` in the standard census.** Currently an empty slot. Leave empty by default, or make it a standing third question? → *new flag.*
4. **Consistency with the sample report.** The report's method section states "74 closed items"; this instrument as specified contains **60** (53 substantive + 5 segmentation + 2 attention checks). One of the two must change — recommend updating the report text to 60 (and median time from 13.4 to a figure consistent with the 13–16-minute estimate). → *new flag.*

---

*Document owner: A. Akhtyrskii · Prepared with Claude · v0.1 · 2026-07-19*
