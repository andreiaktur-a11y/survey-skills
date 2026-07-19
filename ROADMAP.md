# Measure & Meaning — Lab & Report Library · ROADMAP

**Single source of truth for this initiative.** Read this at the start of every session;
update the STATUS block at the end of every session. Mirror this file into the GitHub
repo (`survey-skills`) so it can be fetched from any new chat or project.

- **Owner:** Andrei Akhtyrskii, PhD — Measure & Meaning Research (measuremeaning.com)
- **Repo (source of truth for artifacts):** https://github.com/andreiaktur-a11y/survey-skills
- **Language:** conversation in Russian; artifacts (skills, templates, code) in English
- **Last updated:** 2026-07-19

---

## 0. What we are building (scope)

A two-part product initiative that makes ARA's methodological expertise **visible,
standardized, and sellable** — without becoming a software company:

1. **Report Library** — a small set of exemplar, decision-first sample reports, one per
   priority domain, that (a) prove what a client receives, (b) double as reusable delivery
   templates, and (c) become the destinations the Decision Lab points to.
2. **Research Decision Lab** — a *static* (client-side, no backend) diagnostic on
   `measuremeaning.com/lab`: 10–12 questions → recommended approach + methodological risks
   + deliverables + next step, with lead capture via Formspree.

**Market for v1:** US / M&M (English, USD). RF trademark/sociology practice is a separate
future "domain brain" on the same frame — deferred.

---

## 1. Standing rules (non-negotiable)

- Never name KPMG — refer only to "a top-5 global consulting firm."
- No fabricated clients, metrics, testimonials, or photography-as-team/client.
- Every sample labeled **illustrative + synthetic**; fictional org names only.
- MVP is **fully static** — no backend, no monthly cost. Leads via Formspree.
- The "one input → many internal documents" (proposal engine) is run **by the principal**
  in Claude (Cowork/Code), not by a server-side API. Principal-led judgment.
- IP tiering for instruments: **A** = own/official (original synthesis) · **B** = public/
  academic (paraphrase, attribute, check each) · **C** = proprietary vendor (never copied).
- Ambiguous factual claims → flag for owner sign-off, don't change unilaterally.
- Anonymity threshold in employee work: no breakout for a group of N < 5.

---

## 2. Phase plan

| Phase | What | Status |
|---|---|---|
| **0** | Decisions: market, build order, static MVP, rules | ✅ Done |
| **1** | **Report Library** — exemplar sample reports per domain (Employee → CX/Patient → Brand/Market) + turn each into an automation-ready `{{braces}}` template in the repo | 🟡 In progress |
| **2** | **Decision Lab MVP** — static 10–12-Q diagnostic on /lab; rule-based routing from skills; Formspree; client-side PDF | ⬜ Not started |
| **3** | **Internal Proposal Engine** — principal-run Claude workflow: brief → lead summary, discovery agenda, risk memo, service rec, proposal draft | ⬜ Not started |
| **4** | **Survey Quality Checker** — internal first (from skills); public shows 3–5 flags; full audit paid | ⬜ Not started |
| **5** | **Defer:** backend (Supabase/CRM/Stripe), client portal, RF branch (152-ФЗ + OFAC gating) | ⏸ Deferred |

---

## 3. Report Library tracker (Phase 1 detail)

Shared skeleton across domains: Executive summary (decision-first) → Objectives →
Method (brief) → Sample & coverage → Results by objective → **Driver analysis (the
differentiator)** → Recommended actions → Limitations → Appendix (instrument provenance).

| Domain | Sample report (.docx) | Instrument (questionnaire + codebook) | Automation template in repo | Website "what you receive" |
|---|---|---|---|---|
| **Employee / HR** | ✅ **v3** (`Employee_Engagement_Retention_SAMPLE_v3.docx`) — 15 pp, 9 per-module visualizations, driver model, screening funnel, payroll weighting | ✅ v0.1 — `questionnaire-employee-census.md` (60 closed + 3 open, full programming spec) + `codebook-employee-census.md` / `.csv` | ⬜ **next candidate (A)** — build from v3 + codebook CSV | ⬜ |
| **CX / Patient** | ⬜ (top-box, coordination-of-care, CAHPS-style) | ⬜ | ⬜ | ⬜ |
| **Brand / Market** | ⬜ (awareness, associations, share) | ⬜ | ⬜ | ⬜ |

Module framework (item bank + methodological rationale): `module-framework.md` **v0.4**.

Repo anchors: `skills/domain-hr-employee/`, `skills/survey-reporting/references/report-structure.md`,
`skills/domain-legal/references/report-template.md` (pattern for the `{{braces}}` automation).

---

## 4. Decisions log

- **2026-07-15** Market for v1 Lab = **US / M&M**.
- **2026-07-15** Build order = **Report Library first**, then Decision Lab.
- **2026-07-15** Priority domains = **Employee, CX/Patient, Brand/Market**.
- **2026-07-15** MVP = **fully static**, leads via Formspree, no backend.
- **2026-07-15** Standing content rules confirmed apply to all report templates.
- **2026-07-15** Employee sample report v1 produced (fully synthetic, labeled illustrative).
- **2026-07-19** PSY module dropped (PCQ/PsyCap = tier C); PsyCap guardrail added to the framework.
- **2026-07-19** GAP scale = **7-point fully verbalized**, midpoint retained, with an **off-scale "Not applicable"** on satisfaction items only. N/A is coded `99`, excluded from means, reported as a coverage statistic — **never recoded to the midpoint** (no-experience ≠ neutral).
- **2026-07-19** GAP quadrant boundaries = **within-survey medians**, not the scale midpoint. Reviewed and reconfirmed: stated importance has a ceiling, so a midpoint-anchored cross leaves the lower quadrants permanently empty. Drift is offset by the absolute gap-rank chart and, from wave 2, a grey reference cross at the prior wave's medians.
- **2026-07-19** Tenure bands replaced with a **non-overlapping grid**: Less than 1 year / 1–2 / 3–6 / 7 years or more. The retired 1–3 / 3–7 grid double-assigned employees at exactly 3 and 7 years. HRIS extracts are re-banded to match the instrument, not the reverse.
- **2026-07-19** Sample-report **disclaimer policy**: the illustrative/synthetic label is mandatory on the **cover block and running header**; per-figure caption labels are optional.
- **2026-07-19** Employee sample report **v3** issued (owner layout + agreed corrections). Fielded instrument and codebook split out as separate repo artifacts.
- **2026-07-19** Open decision §5.1 closed: real project data are used as a **structural reference only**; all public samples stay synthetic + illustrative.

---

## 5. Open decisions (waiting on owner)

**Next build step.** (A) `{{braces}}` automation template from the v3 report + codebook CSV, (B) clear the eight flags below in one short session, or (C) start the CX/Patient domain. → *recommended: B, then A — several flags land directly in the report text, so clearing them after the template is built means rebuilding it.*

Carried flags, tracked in the artifacts that own them:

| # | Flag | Lives in |
|---|---|---|
| 1 | Extended GAP categories (MEN, EVT) — standard in EVP configuration or strictly optional? | `module-framework.md` §11.1 |
| 2 | Trade-off block (MaxDiff-lite) — in v1 or design-on-request? | `module-framework.md` §11.1 |
| 3 | `OPN-03` — empty slot or standing third open-end? | `module-framework.md` §11.1 |
| 4 | Sample report states "74 closed items"; the instrument has **60**. Recommend correcting the report. | `questionnaire-employee-census.md` §12 |
| 5 | `BRN_TIER` cutpoints (6–13 / 14–21 / 22–30) are documented but arbitrary — no normative sample behind them. Keep labeled-arbitrary, anchor after 3–5 engagements, or drop tier language? | `codebook-employee-census.md` §9 |
| 6 | Weight-trimming bounds (0.4–2.5) — confirm or set per client. | `codebook-employee-census.md` §9 |
| 7 | `STY-02` — report separately (current) or as a composite with `STY-01`? Recommend separate. | `codebook-employee-census.md` §9 |
| 8 | Fig. 2 caption in v3 still carries the per-figure synthetic label the other eight lost — remove for consistency? | v3 report |

---

## 6. How we work (per-session ritual)

1. Start a **new chat per single task** (one report, or one template) — long threads get
   expensive; split work across sessions.
2. Open the session by pointing Claude at this ROADMAP ("работаем по ROADMAP, фаза X"),
   or let Claude fetch it from the repo.
3. Do the one focused chunk.
4. Claude ends with a **STATUS block** (Done / Next / Open decisions) → paste it into this
   file's Decisions/Status and, optionally, commit to the repo.

---

## 7. STATUS (latest)

**Session of 2026-07-19 — Employee domain build-out.**

- **Done:**
  - `module-framework.md` **v0.4** — 18-category GAP set, 7-point verbalized scales with off-scale N/A, non-overlapping tenure bands, quadrant-boundary rationale, decisions log.
  - **Sample report v3** — 15 pp, nine per-module visualizations (engagement bars, eNPS stacks with CIs, importance × satisfaction quadrant map, ranked gaps, burnout tiers, demand-vs-recovery 2×2, open-end themes, Shapley driver dot plot with cost tags, stated-vs-derived slope chart). Built on the owner's own layout and logo; XSD-validated.
  - **Field questionnaire v0.1** — 60 closed + 3 open items, ≈13–16 min, full programming spec (no forced response, N/A rendered off-scale, reverse-keyed items never flipped on screen, segmentation last with the trade-off disclosed, support-resources link mandatory whenever the burnout block is fielded).
  - **Codebook v0.1** — human-readable (`.md`) and machine-readable (`.csv`, 81 variables) plus its generator; index formulas, reverse-keying, missing-code system, pre-registered screening funnel, weighting scheme, suppression rules.
  - Figure generation scripts (`make_figs.py`, `make_fig5_v3.py`) and the v2 document builder (`build_report.js`).

- **Next:** clear the eight flags in §5 (short session), then build the `{{braces}}` automation template from the v3 report + codebook CSV. That closes the Employee domain end-to-end: instrument → codebook → report template → website "what you receive".

- **Open:** the eight flags in §5.

- **Note for the next session:** open a fresh chat, attach `ROADMAP.md`, `module-framework.md` v0.4, `codebook-employee-census-v0_1.csv`, and the v3 report. That is enough context to resume without re-explaining anything.
