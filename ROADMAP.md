# Measure & Meaning — Lab & Report Library · ROADMAP

**Single source of truth for this initiative.** Read this at the start of every session;
update the STATUS block at the end of every session. Mirror this file into the GitHub
repo (`survey-skills`) so it can be fetched from any new chat or project.

- **Owner:** Andrei Akhtyrskii, PhD — Measure & Meaning Research (measuremeaning.com)
- **Repo (source of truth for artifacts):** https://github.com/andreiaktur-a11y/survey-skills
- **Language:** conversation in Russian; artifacts (skills, templates, code) in English
- **Last updated:** 2026-07-27

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
CX `skills/domain-healthcare-cma/references/module-framework-cx.md` **v0.2**.

Repo anchors: `skills/domain-hr-employee/`, `skills/domain-healthcare-cma/`,
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
- **2026-07-27** **Domain folder naming closed.** The CX artifacts live in **`skills/domain-healthcare-cma/`**; `skills/domain-cx-member-experience/` never existed and the references to it in §3 and §7 were stale. The existing folder is retained rather than renamed: `DOMAINS.md` (roster), `AGENTS.md` (country/product routing), the two `cma-*` evals and the skill's own frontmatter `name:` all key on it, and the module is the **healthcare hat**, of which Health Home member experience is the first worked-out vertical rather than the whole of it. Recorded here so the folder name stops being re-litigated (Claude, mechanical; reversible on owner's word — rename cost is 6 files).
- **2026-07-27** **Domain-module contract established** (read from `DOMAINS.md` + `AGENTS.md`). The domain `SKILL.md` is the **agent-facing routing layer** (the seven contract sections an agent reads before opening anything else); the Report Library artifacts in `references/` are the **delivery artifacts**. They are not alternatives: the skill is **not** superseded, and `module-framework-cx.md` is **normative for the Health Home vertical**. Precedence rule adopted and printed in the skill: *where the two disagree, the framework governs and the skill is corrected*; the skill points at framework sections rather than restating methodology (Claude).
- **2026-07-27** **`domain-healthcare-cma/SKILL.md` v0.2 and `references/compliance.md` v0.2 reconciled with the framework.** Four contradictions corrected: (1) CAHPS/CG-CAHPS reclassified **tier A → tier B** with the D-CX-9 rules carried into the skill (no "CAHPS" in the deliverable name, verbatim-or-not-at-all, slots not wording, per-item transferability, provenance attribution); (2) QMP monitoring reframed from "good practice / not a written state policy" to the **written HH0003 obligation**, with the caution it was protecting now carried precisely by the §0.1 claim-discipline block rather than by understatement; (3) default mode **voice/phone primary → SMS/mail primary with a fully resourced phone fallback**, achieved mode reported per agency; (4) benchmarks **CAHPS Database → cross-agency within network**, with database submission recorded as a separate owner decision out of scope for v1 (Claude, flag-first; every change proposed with rationale).
- **2026-07-27** **Incidentals in the same revision:** the named voice vendor removed from the domain module — phone in this vertical is **interviewer-administered**, since §2.3 screening assumes interviewer effects and §8.4.1 assumes a briefed human; vendor/stack choice returns to `survey-fielding`, where it belongs. Construct domain `disenrollment_reason` superseded by **`engagement_intent`** (ENG-01–03 → `EXIT_TYPE`, §9.1), and the construct list extended to match the 12 modules. `compliance.md` promoted from stub to the domain's compliance layer: HH0003 basis, claim discipline, BAA structure, respondent protection, and an evidence crosswalk rewritten against the obligation's actual elements (Claude).

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

**CX (added 2026-07-27, from the skill/framework reconciliation):**

7. **IP tier propagation — the tier A claim on CAHPS survives outside the two reconciled files.**
   `shared/instrument-library/index.json` and all four instrument banks (CG-CAHPS core, CG-CAHPS
   coordination of care, ACS demographics, CDC HRQOL-4) carry `reuse_tier: "A"`; `README.md`,
   `CONTINUE.md` and the `DOMAINS.md` roster row repeat it in prose. The library is otherwise
   already compatible with verbatim-or-nothing (it stores measure stems and tells the reader to pull
   field wording from the source). **The edit is mechanical — a tier field, a licence note and three
   prose lines — but it is six files, so it is proposed as its own short session rather than folded
   in silently.** Until it is done, `SKILL.md` §3 is the authority on tier, not the library.
8. **CG-CAHPS retention.** It is the wrong reference for the Health Home vertical (it measures
   clinician and group *visit* experience, not a member's relationship with a care manager). Keep it
   in the healthcare module as a general patient-experience source under tier B rules, or retire it
   from this module?
9. **Tier legend ambiguity.** The standing legend reads "**A** = own/official". Does "official"
   cover federal statistical instruments (ACS, NHIS/BRFSS, CDC HRQOL-4)? Proposed reading: **no** —
   tier A is original synthesis only, and these are tier B. The cost of the safe reading is
   attribution; the cost of the loose one is that "tier A" stops meaning anything.
10. `module-framework-cx.md` still carries **"Repo target: `skills/domain-cx-member-experience/…`"**
    in its header. Metadata-only correction to v0.2.1 — no content touched — or leave until the next
    content revision?
11. **Automated voice.** Not a default in this vertical after the §8.4.1 disclosure protocol; if it
    is ever proposed, the protocol has to be answered first. Confirm the exclusion, or keep it open.
12. **Naming: "ARA" vs "Measure & Meaning"** across the skill library. The revised CX files use M&M;
    the other domain skills still say ARA. Library-wide sweep, not a CX decision — flagged, not made.

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

**Session of 2026-07-27 — CX domain, session 2: domain skill reconciled with the framework.**

- **Done:**
  - **Architecture question answered first, as the brief required.** `DOMAINS.md` + `AGENTS.md`
    establish that a domain `SKILL.md` is the **agent-facing routing layer** and the `references/`
    artifacts are the **delivery layer**. The skill is therefore **not superseded**: it is corrected
    and made to point at the framework, with an explicit precedence rule — *framework governs,
    skill is corrected* — printed at the top of the file. This determined the shape of everything
    below.
  - **All four contradictions reconciled** in `domain-healthcare-cma/SKILL.md` **v0.2** and
    `references/compliance.md` **v0.2**: CAHPS tier A → **tier B** with the full D-CX-9 rule set;
    QMP "good practice" → the **written HH0003 obligation** plus the §0.1 claim-discipline block;
    voice-primary → **SMS/mail primary, phone fallback resourced as a full mode**; CAHPS Database
    → **cross-agency within network**. Both incidentals cleared (voice vendor removed,
    `disenrollment_reason` → `engagement_intent`/`EXIT_TYPE`).
  - **`compliance.md` promoted from stub** to the domain's compliance layer, with the two counsel
    items carried as live flags rather than settled statements, and a scope note that HH0003 is
    NYS-specific and is not assumed to transfer to another state.
  - **Path repair complete.** §3 and §7 now name `skills/domain-healthcare-cma/`; the folder-naming
    decision is recorded in §4 so it stops recurring. No second domain folder created.
  - **Six new open items registered** in §5 — the largest being that the **tier A claim on CAHPS
    survives in six other files**, including the four instrument banks the design agent actually
    reads for wording.

- **Not done, deliberately:** the shared-layer IP tier sweep (§5 item 7). It is mechanical but it is
  six files outside this session's scope, and flag-first discipline says a correction to `shared/`
  is proposed, not folded in. Until it lands, `SKILL.md` §3 is the authority on tier for those banks.

- **⚠ Not committed.** The GitHub connector remains **read-only** (`403 Resource not accessible by
  integration`). `SKILL.md` v0.2, `compliance.md` v0.2 and this ROADMAP require manual upload.
  A write-capable token remains the single highest-value piece of plumbing: three consecutive
  sessions have now ended with the repo and the artifacts out of sync, which is exactly the drift
  this session existed to repair.

- **Next:** the two questionnaire blockers are unchanged (§5 items 1–2), so the natural session 3 is
  the preparatory step that needs neither cleared: **assemble the verbatim tier B item texts from the
  HCBS CAHPS source into a reference file**, since §2.5 forbids drafting the instrument from
  paraphrase or memory. The IP tier sweep (§5 item 7) is a short alternative and would pair naturally
  with it — the sweep sets the tier field the new reference file will be read against.

- **Also open, unrelated to CX:** the Employee row's "Website *what you receive*" cell in §3 is the
  only unfilled Employee deliverable in Phase 1, and it sets the pattern for the other two domains.
  Carried: `module-framework.md` §11.1 still lists three flags resolved 2026-07-19.

- **Phase 1-A pipeline backlog** (unchanged, from the 2026-07-22 release): deterministic
  `driver_models` spec (predictor missing-data rule, `WT` usage, exact Shapley procedure incl. R²
  baseline over 2²⁰ subsets); psychometric evidence base (alpha/omega, item-total, dimensionality —
  internal, feeds `BRN_TIER` re-anchoring after 3–5 engagements); deterministic/interpretation split
  (`analysis_results.json` + `report_content.json` + template → DOCX); Northgate regression fixture
  as the permanent pipeline test case; automated QA layer (unresolved `{{braces}}`, cross-section
  number reconciliation, predictor count vs. model, suppression leakage, sample-mode language).
  **Trigger: the first real engagement, not a calendar date.**

- **Note for the next session:** open a fresh chat and attach this `ROADMAP.md`,
  `module-framework-cx.md` v0.2 and `SKILL.md` v0.2. `Employee_Engagement_Retention_SAMPLE_v3_2.docx`
  is also still not in the repo.
