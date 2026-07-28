# Measure & Meaning — Lab & Report Library · ROADMAP

**Single source of truth for this initiative.** Read this at the start of every session;
update the STATUS block at the end of every session. Mirror this file into the GitHub
repo (`survey-skills`) so it can be fetched from any new chat or project.

- **Owner:** Andrei Akhtyrskii, PhD — Measure & Meaning Research (measuremeaning.com)
- **Repo (source of truth for artifacts):** https://github.com/andreiaktur-a11y/survey-skills
- **Language:** conversation in Russian; artifacts (skills, templates, code) in English
- **Last updated:** 2026-07-23

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
- **Regulatory-claim discipline (added 2026-07-23, from the CX domain; applies library-wide):**
  never claim that a survey improves a client's regulatory score where that score is computed
  from administrative data only; never describe a permitted method as a mandated one; never
  imply a deliverable substitutes for a state- or federally-procured instrument. Specific to
  the Health Home vertical: no "improves your redesignation score", no "required by NYSDOH",
  no CAHPS-substitution claim. See `module-framework-cx.md` §0.1.

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
| **CX / Member Experience (Health Home)** — vertical: NYS Medicaid Health Home care management · **buyer = Lead Health Home (LHH)**, not the CMA | ⬜ | 🟡 module framework **v0.2** (`module-framework-cx.md`); questionnaire + codebook not started | ⬜ | ⬜ |
| **Brand / Market** | ⬜ (awareness, associations, share) | ⬜ | ⬜ | ⬜ |

Module frameworks (item bank + methodological rationale): Employee `module-framework.md` **v0.4** ·
CX `skills/domain-cx-member-experience/references/module-framework-cx.md` **v0.2**.

Repo anchors: `skills/domain-hr-employee/`, `skills/domain-cx-member-experience/`,
`skills/survey-reporting/references/report-structure.md`,
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
- **2026-07-23** **CX domain verticalised** — built as member experience for NYS Medicaid Health Home care management rather than as a generic commercial CX exemplar. Rationale of record: a generic CX sample competes with the content marketing of the large platform vendors, where a boutique loses on volume by definition; a member-experience report for a Health Home network competes with essentially no one. The instrument core stays domain-general so the library retains transferability. **Buyer = the Lead Health Home**: the regulatory obligation and the budget sit with the LHH, and one engagement covers the whole CMA network, which yields cross-agency internal comparison — consistent with the standing refusal to use external vendor benchmark databases (owner).
- **2026-07-23** **Three-layer transfer rule** adopted, governing what moves between domains: (1) argument structure — carried; (2) methodological invariants — carried as `[BOILERPLATE — DO NOT EDIT]`; (3) domain content (items, indices, criterion, model set, exhibits, `{{braces}}` schema) — **rebuilt per domain, never forked**. A single field schema spanning all domains will therefore not exist; the surrounding infrastructure (DOCX rendering, QA layer, suppression logic, unresolved-`{{braces}}` check) is domain-neutral, and each domain feeds its own schema to one engine (owner).
- **2026-07-23** **Regulatory verification, CX domain.** HH0003 (*Health Home Quality Management Program*, effective 2017-06-01) is a **single programme-wide policy** covering adults and children — the presumed separate adult standard does not exist; **no recorded revision** (the "09/2017" date is a web-page footer, not a policy revision). Confirmed: Health Homes must collect and report data on care-coordination effectiveness **including member satisfaction**, with content areas named (timeliness of appointments, ease of access to information, quality of communication with care managers); member experience surveys are one **permitted** method among several; obtaining and applying member/family feedback is an **obligation** with the method left open. **Correction to the commercial argument:** no survey-derived measure enters the redesignation score — Domain 2 (20% of total) is computed from CMART and Medicaid claims/encounters only. The defensible statement is narrower and stronger: the state's own SPA measure framework names *Experience of Care* as a measure category and populates it with none (Claude, verified against NYSDOH sources).
- **2026-07-23** **D-CX-3** CX reporting convention = HCBS CAHPS response formats (4-point frequency, Yes/No, 4-point recommendation, 0–10 global ratings), **top-box reporting**, no agreement matrices. The Employee 7-point verbalized scale does not transfer (owner).
- **2026-07-23** **D-CX-4** Weighting frame = Health Home / agency **enrolled population**, rim weighting on agency × programme × age × sex × race, conditional on frame quality; race/ethnicity excluded from the scheme if roster missingness is material (owner + Claude).
- **2026-07-23** **D-CX-5** Mode = SMS/mail primary, phone fallback; **independent administration is the product**; contact list held by the LHH, never by the CMA; phone capacity resourced multilingually and achieved mode reported per agency (owner).
- **2026-07-23** **D-CX-6** Reporting units = network and agency. N < 5 suppression with complement check; **N ≥ 10 for within-agency subgroups**. **Care-manager-level reporting excluded by policy** — caseloads of 50–60 make it technically feasible, so the exclusion is argued on reliability, identification, and above all measurement validity: a performance-management instrument for individual staff and a QMP measurement instrument cannot be the same instrument. Caseload-characteristic breakouts offered instead (owner + Claude).
- **2026-07-23** **D-CX-7** Language rule = EN + ES baseline plus whatever covers 95% of the roster; back-translation and equivalence documented; **language-exclusion rate printed as a coverage figure**, not buried in limitations (owner).
- **2026-07-23** **D-CX-8** PHI route = M&M receives contact data and administers directly. **Correction:** this cannot be a HIPAA limited data set (an LDS excludes phone, email, and address — the fields fielding requires); the correct structure is a disclosure of PHI to a business associate for **health care operations** under a signed BAA, with minimum necessary, contact fields segregated from the analysis file, and destruction at fieldwork close with a written certificate. **Counsel review before any instrument text is written** (owner, with correction).
- **2026-07-23** **D-CX-9** HCBS CAHPS classified **tier B**, not C — developed by CMS for voluntary use by state Medicaid programmes, CAHPS trademark June 2016, 19 NQF-endorsed measures October 2016. Three governing rules: the deliverable is **not** named "…CAHPS…" (registered AHRQ trademark; permission is granted only against AHRQ's criteria) and is instead attributed in the provenance appendix; tier B items are used **verbatim or not at all** — the framework therefore carries **tier B slots, not tier B wording**, with exact text pulled at fielding; transferability is checked **item by item, never block by block** (owner + Claude).
- **2026-07-23** **`EXIT_TYPE` adopted** (owner's construction, replacing Claude's proposal to demote engagement intent to a descriptive item). Raw intent to stay is two-sided in this programme — disenrollment is frequently the *intended* outcome — so intent alone cannot carry a driver model. Intent **plus a pre-registered reason item** yields four types: Graduating / Disengaging / Constrained continuing / Committed continuing. It is a **profiling outcome, not the driver-model criterion**. Mandatory triangulation: a member claiming independence while scoring bottom-box on care-manager support and reporting unmet needs is a **masked disengagement** — an aggregate analytic category, **never an individual label**. Validated against realised disenrollment from wave 2 (owner).
- **2026-07-23** **Physical-safety items excluded** from every configuration of the CX instrument; a written disclosure and escalation protocol is required regardless, since removing the item does not remove the event. Mandatory-reporting exposure is a legal question, answered before the first call (owner).
- **2026-07-23** Census where an agency roster is ≤ ~800 members, stratified probability sample above; planning target ~100 completes per agency, mode and materials identical across both routes (Claude, from owner's caseload figures).

---

## 5. Open decisions (waiting on owner)

**Employee:** none from the v0.3 release — all Session C sign-offs are closed and recorded in
the decisions log (2026-07-22; items 3–5 were delegated by the owner to Claude and are
reversible on request).

Carried: `module-framework.md` §11.1 still lists as open the three flags resolved 2026-07-19
and recorded in questionnaire v0.3 §13 (MEN/EVT = EVP-only configurations; MaxDiff-lite =
design-on-request; `OPN-03` = empty per-engagement slot) — sync the framework doc next time
it is edited.

**CX (from `module-framework-cx.md` v0.2 §13.1):**

1. **§9.2 dual criterion** — primary `RAT-B-01` (global rating of the care manager) + secondary
   `SEF` (perceived capacity to manage one's own care). `EXIT_TYPE` is settled; this is not.
   **Blocks the questionnaire.**
2. **Counsel review** of the §10.3 BAA structure — this **also blocks the questionnaire**, because
   the mode determines the instrument's form (SMS, phone, and mail are three documents, not three
   layouts). Includes the mandatory-reporting question in §8.4.1.
3. `UNM-TRN` — tier B slot for comparability, or tier A item.
4. SPA measure table currency — confirm no version newer than November 2017 before the
   "Experience of Care is empty" sentence is used with a client.
5. LHH disenrollment fields and granularity — before wave-2 `EXIT_TYPE` validation is promised
   in a proposal.
6. Per-agency completes target — ~100 is a methodological planning figure, not a costed one.

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

**Session of 2026-07-23 — CX domain opened; module framework v0.2.**

- **Done:**
  - **Regulatory verification closed** (all four items of the session brief), with two corrections
    to the brief's premises: HH0003 is one programme-wide policy with no recorded revision, and no
    survey-derived measure enters the redesignation score. A stronger positioning anchor found in
    its place — the state's SPA measure framework names *Experience of Care* and populates it with
    none.
  - **D-CX-3 … D-CX-9 resolved and logged** (§4), including the IP determination on HCBS CAHPS
    (tier B; verbatim-or-not-at-all; tier B slots rather than tier B wording).
  - **`EXIT_TYPE`** — owner's construction adopted over Claude's narrower proposal; triangulation
    against experience composites made mandatory, with masked disengagement fixed as an aggregate
    category only.
  - **`module-framework-cx.md` v0.2** produced, target path
    `skills/domain-cx-member-experience/references/` — 13 sections, 12 modules, claim-discipline
    block (§0.1), three-layer transfer rule (§12).
  - **Standing rule added** to §1: regulatory-claim discipline, library-wide.

- **⚠ Not committed.** The GitHub connector is **read-only** — a push of this file and of
  `module-framework-cx.md` v0.2 failed with `403 Resource not accessible by integration`. Both
  files must be uploaded manually. This is the same limitation previously recorded for the binary
  sample report, and it is broader than assumed: it applies to text artifacts too. Until a
  write-capable token is configured, every session ends with manual upload.

- **Next:** `questionnaire-cx-member-experience.md` v0.1 — **in a fresh chat**, and only after the
  two blockers in §5 clear (driver-model criterion; counsel review of the PHI/BAA structure, which
  fixes the mode and therefore the instrument's form). Preparatory step that needs neither cleared:
  assemble the verbatim tier B item texts from the HCBS CAHPS source into a reference file, since
  §2.5 forbids drafting the instrument from paraphrase or memory.

- **Also open, unrelated to CX:** the Employee row's "Website *what you receive*" cell in §3 is the
  only unfilled Employee deliverable in Phase 1, and it sets the pattern for the other two domains.

- **Phase 1-A pipeline backlog** (unchanged, from the 2026-07-22 release): deterministic
  `driver_models` spec (predictor missing-data rule, `WT` usage, exact Shapley procedure incl. R²
  baseline over 2²⁰ subsets); psychometric evidence base (alpha/omega, item-total, dimensionality —
  internal, feeds `BRN_TIER` re-anchoring after 3–5 engagements); deterministic/interpretation split
  (`analysis_results.json` + `report_content.json` + template → DOCX); Northgate regression fixture
  as the permanent pipeline test case; automated QA layer (unresolved `{{braces}}`, cross-section
  number reconciliation, predictor count vs. model, suppression leakage, sample-mode language).
  **Trigger: the first real engagement, not a calendar date.**

- **Note for the next session:** open a fresh chat and attach `ROADMAP.md` (this version) plus
  `module-framework-cx.md` v0.2. `Employee_Engagement_Retention_SAMPLE_v3_2.docx` is also still not
  in the repo. Consider configuring a write-capable GitHub token so artifacts stop depending on
  manual upload.
