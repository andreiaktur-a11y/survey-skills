# Measure & Meaning — Lab & Report Library · ROADMAP

**Single source of truth for this initiative.** Read this at the start of every session;
update the STATUS block at the end of every session. Mirror this file into the GitHub
repo (`survey-skills`) so it can be fetched from any new chat or project.

- **Owner:** Andrei Akhtyrskii, PhD — Measure & Meaning Research (measuremeaning.com)
- **Repo (source of truth for artifacts):** https://github.com/andreiaktur-a11y/survey-skills
- **Language:** conversation in Russian; artifacts (skills, templates, code) in English
- **Last updated:** 2026-07-22

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
| **Employee / HR** | ✅ **v3.2** (`Employee_Engagement_Retention_SAMPLE_v3_2.docx`) — 17 pp, 11 figures incl. STAY_TYPE 2×2 and STY-02 divergence exhibit, three-model driver section, per-column screening funnel | ✅ **v0.3** — `questionnaire-employee-census.md` + `codebook-employee-census.md` / `.csv` (incl. `spec_driver_models` / `spec_predictors` machine-readable model spec) | ✅ **v1.2** — `report-template-employee-census.md` (D1–D8/F1–F2 release; `{{n_predictors}}` computed; Block X conditional §4.6) | ⬜ |
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
- **2026-07-19** Flags session B (external analytical review, 14 points → 9 confirmed defects): triage recorded in `external-review-triage-2026-07-22.md` (superseded by the consolidated handoff).
- **2026-07-22** Flags session C — **v0.3 release decided** (consolidated handoff `employee-handoff-2026-07-22.md`): **D1** IDX_BRN prorated (≥ 5 of 6, range 6–30 restored) · **D2** straightlining = zero variance across a full 18-item GAP column, per column · **D3** ENG-05 criterion contamination → `IDX_ENG_DRIVER` (5 items, model-internal only; `IDX_ENG` unchanged as headline/trend) · **D4** canonical 20-predictor set, `{{n_predictors}}` computed, never typed · **D5** "retention impact per dollar" → "retention leverage" (no ROI modeling) · **D6** custom closed items capped at 8; BRN and GAP never trimmed · **D7** STAY_TYPE 2×2 (top-2-box, pre-registered; reluctant stayers) · **D8** STY-02 divergence model — exhibit + prose only, never a second ranked list · **F1/F2** PNTS wording and anonymity statement fixed.
- **2026-07-22** **Block X** (client add-on module, `CUS-*` prefix) adopted: descriptive only, never enters any index or driver model; excluded from screening rules; declared in per-engagement codebook addendum; conditional §4.6 in the template. Enabled by the **allowlist parsing principle**: the pipeline reads only canonical variable IDs declared in the codebook; unrecognised columns are ignored silently.
- **2026-07-22** Next-build-step decision (old §5) resolved as **B, then A**: flags cleared (07-19 / 07-22), then the automation template built — `report-template-employee-census.md` v1.2 now in the repo. *(Owner confirmation recorded in Session C.)*
- **2026-07-22** Session C sign-offs closed: next-build-step = **path A confirmed by owner**; push of the release commit **confirmed by owner**; items delegated by owner to Claude and decided as follows — F1 note in questionnaire §7 **keeps** the operational sentence "Treated as missing for breakouts, and its rate is reported" (consistent with codebook §2, code 98); questionnaire §13 flag 1 *(v0.3 note, per D6)* interpretation **confirmed** (CORE/BRN trimming applies only where the burnout tier is not a deliverable — the only reading consistent with D1); SAMPLE v3.2 **keeps** the rendered D7/D8 exhibits and the template v1.2 figure numbering.
- **2026-07-22** v0.3 release executed across Sessions A–C: codebook v0.3 (.md + .csv), questionnaire v0.3, template v1.2, SAMPLE v3.2; single release commit to `survey-skills@main`.

---

## 5. Open decisions (waiting on owner)

None from the v0.3 release — all Session C sign-offs are closed and recorded in the decisions log (2026-07-22; items 3–5 were delegated by the owner to Claude and are reversible on request).

Carried: `module-framework.md` §11.1 still lists as open the three flags resolved 2026-07-19 and recorded in questionnaire v0.3 §13 (MEN/EVT = EVP-only configurations; MaxDiff-lite = design-on-request; `OPN-03` = empty per-engagement slot) — sync the framework doc next time it is edited (not part of this release).

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

**Sessions A–C of 2026-07-22 — Employee domain v0.3 release.**

- **Done:**
  - **Codebook v0.3** (.md + .csv) — D1 prorated IDX_BRN, D2 per-column straightlining, D3 `IDX_ENG_DRIVER`, D4 canonical 20-predictor set with machine-readable `spec_driver_models` / `spec_predictors` rows, D7 `STAY_TYPE`, D8 divergence model, Block X rules, allowlist principle.
  - **Questionnaire v0.3** — F1/F2 wording, Block X placement (§8, before OPEN), D6 length budget, "trim BRN" guidance deleted.
  - **Template v1.2** — three-model §05 with STAY_TYPE 2×2 (Fig. 8) and divergence exhibit (Fig. 11), retention-leverage wording, `{{n_predictors}}` computed, conditional §4.6, Appendix A/D disclosures.
  - **SAMPLE v3.2** — rendered reference of template v1.2: D7/D8 exhibits added, figures renumbered (Shapley → Fig. 9, stated-vs-derived → Fig. 10), per-column screening funnel (flags 26: importance 15 / satisfaction 8 / both 3; excluded 11; totals 1,022 → 987 unchanged), Appendix D rebuilt on the 20-predictor / three-model spec, retention-leverage wording, Appendix A burnout-index boilerplate per D1, trimming bounds disclosed. Numeric-leftover sweep clean (one extra "summed score" leftover found in §4.3 and fixed).
  - Single release commit to `survey-skills@main` (this commit).

- **Next (Phase 1-A, pipeline — recorded backlog, not artifact edits):** deterministic `driver_models` spec (predictor missing-data rule, `WT` usage, exact Shapley procedure incl. R² baseline over 2²⁰ subsets); psychometric evidence base (alpha/omega, item-total, dimensionality — internal, feeds `BRN_TIER` re-anchoring after 3–5 engagements); deterministic/interpretation split (`analysis_results.json` + `report_content.json` + template → DOCX); Northgate regression fixture as the permanent pipeline test case; automated QA layer (unresolved `{{braces}}`, cross-section number reconciliation, predictor count vs. model, suppression leakage, sample-mode language).

- **Open:** none from this release; carried module-framework flags listed in §5.

- **Note for the next session:** open a fresh chat, attach `ROADMAP.md`, `employee-handoff-2026-07-22.md`, and the four v0.3/v1.2 artifacts from the repo. The project-knowledge copy of ROADMAP.md is stale (2026-07-15) — replace it with this version.
