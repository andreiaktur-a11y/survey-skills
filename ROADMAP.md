# Measure & Meaning — Lab & Report Library · ROADMAP

**Single source of truth for this initiative.** Read this at the start of every session;
update the STATUS block at the end of every session. Mirror this file into the GitHub
repo (`survey-skills`) so it can be fetched from any new chat or project.

- **Owner:** Andrei Akhtyrskii, PhD — Measure & Meaning Research (measuremeaning.com)
- **Repo (source of truth for artifacts):** https://github.com/andreiaktur-a11y/survey-skills
- **Language:** conversation in Russian; artifacts (skills, templates, code) in English
- **Last updated:** 2026-07-30

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
| **CX / Member Experience (Health Home)** — vertical: NYS Medicaid Health Home care management · **buyer = Lead Health Home (LHH)**, not the CMA | ⬜ | 🟡 module framework **v0.3** (`module-framework-cx.md`, owner sign-off applied) + tier B source reference **v0.2** (`tier-b-source-items.md`, verbatim EN/ES); questionnaire v0.1 unblocked (`D-CX-17`/`D-CX-18`/`D-CX-19`), codebook still needs `O-CX-6` | ⬜ | ⬜ |
| **Brand / Market** | ⬜ (awareness, associations, share) | ⬜ | ⬜ | ⬜ |

Module frameworks (item bank + methodological rationale): Employee `module-framework.md` **v0.4** ·
CX `skills/domain-healthcare-cma/references/module-framework-cx.md` **v0.3**.

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
- **2026-07-28** **Tier B source assembled** (CX session 3). `skills/domain-healthcare-cma/references/tier-b-source-items.md` v0.1: source version-stamped (HCBS CAHPS 1.0, adult, 2017-01-19) and currency-checked against AHRQ and the CAHPS Database; seven response scales and four administrative fills transcribed **verbatim in English and Spanish**; every framework slot determined item by item; dropped-items register built for the provenance appendix. Seven flags raised for owner sign-off (Claude).
- **2026-07-30** **D-CX-10 — verbatim rationale corrected.** Verbatim use of a tier B item buys **attribution, format familiarity and freedom from the borrowed-paraphrase defect**; it does **not** buy comparability with published HCBS CAHPS results or the CAHPS Database. Grounds, all from the source's own administration guidance: the instrument is validated in its entirety and not in parts; a sponsor adding items beyond the core set and approved supplements cannot submit to the Database; and the published mode is interviewer-administered while ours is not. **A fourth prohibited claim** is added to the CX claim-discipline block ("comparable to HCBS CAHPS benchmarks"), and the false comparability ground is struck from the §9.2 criterion argument and the §12 benchmarking note. The verbatim-or-nothing rule itself is unchanged (owner).
- **2026-07-30** **D-CX-11 — bright line adopted.** Determination *transfers* → the slot is filled verbatim; determination *transfers in part* → the slot becomes an original tier A item. **The tier B set is closed at six items** (`RAT-B-01`, `RAT-B-02`, `CMH-B-00`, `CMH-B-01`, `POC-B-01`, `POC-B-02`). Adopted as a **rule** rather than as a series of item-level outcomes: after D-CX-10 every "in part" case was being paid for with a comparability we do not have, and a verbatim item behind a screen we wrote ourselves retains wording only. Consequences: `CMH-B-02` dropped, `CMH-B-03` → tier A `CMH-03`, **`UNM-TRN` resolved as tier A — closing old §5 item 3** (owner).
- **2026-07-30** **D-CX-12 — language.** Official Spanish used **verbatim** for tier B slots; TRAPD applies to tier A items only; our reconciliation review runs as a documented quality check, never as a licence to amend. Every language beyond EN/ES is **tier A throughout**, since the Database excludes independently translated versions — so a bilingual and a seven-language instrument are not the same instrument with respect to tier B (owner).
- **2026-07-30** **D-CX-13 — COM module rebuilt as tier A.** The source contains **no care-manager-referenced communication item at all**: the entire communication battery is anchored to paid in-home staff and homemakers, and the *Your Case Manager* section has no communication item. The care-manager-referenced subset is empty, not small. Re-pointing a staff item by fill substitution explicitly rejected — it changes the item's population and produces exactly the borrowed-paraphrase defect (owner).
- **2026-07-30** **D-CX-14 — `RAT-B-01` relabelled** to "rating of the **help received from** the care manager". The published anchors run *worst / best help from {care manager} possible* and the stem asks the member to rate the help, not the person. Bears directly on §5 item 1; the relabel is **consistent with** the exclusion of care-manager-level reporting rather than in tension with it (owner).
- **2026-07-30** **D-CX-15 — `CMH-B-00` adopted** (source Q48) as the gate for the whole care-manager block. Without it five denominators change. Reported as a standalone rate, excluded from the composite; substantively it is a first-order Health Home finding in its own right (owner).
- **2026-07-30** **D-CX-16 — reference-layer file naming.** Internal reference files carry neutral names; the instrument is named in full inside the file, not in the filename, because filenames propagate into commit messages and directory listings by accident (owner).
- **2026-07-30** **Open-item IDs stabilised.** The framework's §13.1 and this file's §5 numbered the same items differently, so a reference to "item 2" meant two things depending on which file was open. CX open items now carry stable `O-CX-n` IDs, never reused, with the mapping printed in both files (Claude, mechanical).
- **2026-07-30** **D-CX-17 — mode changed to telephone, conversational mode; supersedes D-CX-5.** The CMA member survey is administered as a **telephone interview**, conversational. ⚑ *"Conversational" carries three distinct methods; the choice among them is `O-CX-18` and it is not cosmetic.* Consequences recorded now: **(a)** one of D-CX-10's three grounds **falls away** — the published instrument is interviewer-administered by telephone, so our mode now matches it. The conclusion survives untouched on grounds 1 and 2 (validated only in its entirety; database submission requires the full core set with no additions) and the fourth prohibited claim stands — but `module-framework-cx.md` §2.5 and §0.1 must be edited so they stop printing a superseded argument in support of a correct conclusion. **(b)** `O-CX-7` unblocked and `POC-B-02`'s mode caveat removed: the source's alternate version, its `UNCLEAR RESPONSE` code and its unprompted "anyone else?" probe are meaningful again. **(c)** **None of the four bright-line conversions reopens** — `CMH-B-02`, `CMH-B-03`, `UNM-TRN` and `COM-B-01…03` each failed on content or structure, not on mode. **(d)** `O-CX-5` becomes acute: a telephone census is the most expensive design in the set. **(e)** **Frame coverage is now mode-determined** — a member without a working roster number is excluded by the instrument rather than by choice, and that rate is printed as a coverage figure on the §8.5 language precedent. **(f)** D-CX-7 becomes a **staffing** constraint: 95% coverage by phone means multilingual interviewers, not translated forms (owner).
- **2026-07-30** **D-CX-18 — administration register: mixed, biased to standard.** Reading (b) of `O-CX-18`, with the owner's qualifier *"closer to the standard"* operationalised so it is a rule an interviewer can follow rather than a disposition. **Tier B items: fully standardised, no exception** — read exactly as published, one verbatim re-read on request, then the source's own probing rules, then `UNCLEAR`. The interviewer never rephrases a tier B item, which is what keeps the six verbatim slots delivered as published. **Tier A items: standardised first reading, clarification only on the respondent's signal, and only from a pre-scripted clarification bank** — one approved alternative phrasing per item, written and tested at drafting, printed in the instrument. Clarification is never improvised. Consequences: every tier A item now carries **two texts**, which is added drafting work; **use of a clarification is logged per item**, giving a per-item clarification rate that is free comprehension diagnostics and a wave-2 rewrite signal; the rate is **reported, never adjusted for**, since its correlation with respondent characteristics is a finding rather than a nuisance. Design note: the care-manager block (`CMH-B-00` → `CMH-B-01` → `RAT-B-01` → `RAT-B-02`) is administered **contiguously**, which matches the source's own section structure and means the interviewer changes register between blocks rather than between items (owner + Claude).
- **2026-07-30** **D-CX-19 — questionnaire v0.1 configuration.** The QMP evidence-base configuration is drafted first; the ceiling is raised modestly from 10 minutes; the **criterion layer is never cut**. ⚑ **Correction carried into drafting:** the recommendation as put to the owner said "cut `LNG` and `RSP`", but those two modules are **not in the QMP configuration to begin with**, so cutting them frees nothing. The configuration is 26 closed items *before* `SEF` + `ENG`, which brings it to **32 against a ceiling of 26**. The reduction therefore has to come from inside the configuration — resolving `O-CX-8` and `O-CX-9` in the direction of cutting, and treating `UNM-OTH` as an open follow-up rather than a closed item, lands it near 29. **And `D-CX-18` lengthens interviews**, so a nominal 12-minute budget should be planned against roughly 15 achieved, which is at the edge of tolerable for a phone interview with this population. The exact cut list is settled at drafting; the direction is not reopened (owner, with Claude's correction to the arithmetic).

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

**CX — stable IDs, mirrored in `module-framework-cx.md` §13.1.** The old positional numbering
diverged between the two files; these IDs are authoritative and are never reused.

| ID | Open item | State |
|---|---|---|
| `O-CX-1` | **§9.2 dual criterion** — primary `RAT-B-01` (rating of the help received from the care manager), secondary `SEF`. `EXIT_TYPE` is settled; this is not. | **Blocks the questionnaire.** Both standing objections cleared 2026-07-30 (label corrected, false comparability ground struck) |
| `O-CX-2` | **Counsel review** of the §10.3 BAA structure and the §8.4.1 mandatory-reporting question | **Blocks member-facing text.** Mode no longer depends on it (D-CX-17). ⚑ Owner: does "no instrument text before counsel" bind the item bank, or only the introduction, consent and disclosure language? Recommended: only the latter |
| `O-CX-3` | **SPA measure table currency** — confirm no version newer than November 2017 before the "Experience of Care is empty" sentence is used with a client | Open |
| `O-CX-4` | **LHH disenrollment fields** and granularity, before wave-2 `EXIT_TYPE` validation is promised in a proposal | Open |
| `O-CX-5` | **Per-agency completes target.** Now a **design** question, not a budget one — the source developer's own field test puts the care-manager composite at an effective sample size of 376 against a recommended target of 400, so at ~100 completes that composite is not reliably reportable at agency level, which is the level the LHH wants it at. What is reported at which level, and at what n? | Open — answer before fieldwork is quoted |
| `O-CX-6` | **Top-box definition for the 0–10 global rating** as the source defines it. Not stated in either uploaded source document, and §2.1 forbids supplying it from memory | Open, narrow — needed before the codebook session |
| `O-CX-7` | **Alternate scales and mode artefacts** — the source's cognitive-accommodation alternate is a separate version of the whole survey, not a per-item fallback | **Unblocked by D-CX-17.** Decide in session 5: carry the alternate as the source specifies, or exclude it and state the exclusion |
| `O-CX-8` | **`ACC-01` × `CMH-B-01`** — same construct, different scales; one goes | At questionnaire drafting |
| `O-CX-9` | **`POC-02` × `POC-B-01`** — stated distinction required, or `POC-02` goes | At questionnaire drafting |
| `O-CX-10` | **`COM-02…04` wording** — tier A originals, written without reaching for the source's staff battery | At questionnaire drafting |
| `O-CX-11` | **`CMH-03` wording and its need screen** — tier A original replacing the dropped Q52+Q53 pair | At questionnaire drafting |
| `O-CX-12` | **`UNM-DME`** — adopt an equipment-access unmet-need item as tier A in `UNM`, or leave the content out | At questionnaire drafting |
| `O-CX-13` | **IP tier propagation.** `shared/instrument-library/index.json` and all four instrument banks still carry `reuse_tier: "A"` on CAHPS-derived material; `README.md`, `CONTINUE.md` and the `DOMAINS.md` roster row repeat it in prose. Mechanical but six files — its own short session. Until it lands, `SKILL.md` §3 is the authority on tier, not the library | Open |
| `O-CX-14` | **CG-CAHPS retention** — keep in the healthcare module as a general patient-experience source under tier B rules, or retire it from this module | Open |
| `O-CX-15` | **Tier legend.** Does "own/**official**" cover federal statistical instruments (ACS, NHIS/BRFSS, CDC HRQOL-4)? Proposed reading: **no** — tier A is original synthesis only. `module-framework-cx.md` §2.5 already applies the narrow reading to HCBS CAHPS | Open — library-wide |
| `O-CX-16` | **Automated voice** — confirm the exclusion, or keep it open | Open |
| `O-CX-17` | **"ARA" vs "Measure & Meaning"** across the skill library | Open — library-wide sweep, not a CX decision |
| `O-CX-18` | ~~What "conversational" means~~ | **Closed 2026-07-30 → `D-CX-18`** (mixed register, biased to standard; scripted clarification bank) |
| `O-CX-19` | ~~Configuration and length budget for questionnaire v0.1~~ | **Closed 2026-07-30 → `D-CX-19`** (QMP configuration; criterion layer intact; cut list settled at drafting) |
| `O-CX-20` | **Clarification bank** — one approved alternative phrasing per tier A item, from `D-CX-18`. Written and cognitively tested at drafting; declared in the codebook; its per-item use rate carried into the report as a coverage statistic | At questionnaire drafting |
**Closed 2026-07-30:** old §5 item 3 (`UNM-TRN` → tier A) · old §5 item 10 (framework header
repo path corrected to `skills/domain-healthcare-cma/…`) · all seven flags raised in
`tier-b-source-items.md` v0.1 §9 · `O-CX-18` and `O-CX-19`. **Session 5 has no remaining
precondition.**

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

**Session of 2026-07-30 — CX domain, session 4: owner sign-off applied; framework at v0.3.**
*(Same day, after the framework was built: mode decision `D-CX-17` taken; register and configuration settled as `D-CX-18` and `D-CX-19`; session 5 brief issued; GitHub write access attempted and refused. See the closing bullets.)*

- **Done:**
  - **Seven flags from `tier-b-source-items.md` v0.1 signed off and applied**, plus five decisions
    the file surfaced outside the flag list. Recorded as **D-CX-10 … D-CX-16** in §4.
  - **The framing decision was taken as a rule, not as a series of outcomes (D-CX-11).** After the
    verbatim rationale was corrected, every remaining item-level trade-off had the tier B side being
    paid for with a comparability that no longer exists — so deciding them one at a time would have
    produced a predictable sequence of "tier A" outcomes that the next session could re-open
    individually. The bright line (*transfers* → verbatim, *transfers in part* → tier A) disposes of
    `CMH-B-02`, `CMH-B-03` and `UNM-TRN` at once and **closes the tier B set at six items.**
  - **A false claim was found inside a blocking open item.** §9.2 justified the primary criterion
    partly as "comparable to the national database" — the exact statement D-CX-10 falsifies. Struck;
    the two surviving grounds carry the criterion, and `O-CX-1` is now decidable on its merits.
  - **`module-framework-cx.md` v0.3 built and validated**: §0.1 fourth prohibited claim · §2.1 anchor
    flag resolved and top-box rule qualified · §2.2 reliability argument strengthened with the
    developer's own ESS figures · §2.4 `-B-` ID set closed · §2.5 rewritten (corrected rationale,
    bright line, language rule, closed tier B table, source→questionnaire route, file-naming rule) ·
    §3 relabelled · §4 rebuilt with the gate item · §5 rebuilt as four tier A items · §6, §7 overlaps
    registered · §8.2 `UNM-TRN` resolved · §9.2 corrected · §12 benchmarking note repaired ·
    §13 renumbered to `O-CX-n`.
  - **Header repo path corrected** (old §5 item 10 closed) and the stale `D-CX-6` cross-reference
    repaired — it read "excluded pending confirmation of item 13.1.2", which pointed at the
    `UNM-TRN` flag and implied the care-manager-reporting exclusion was conditional. It never was.
  - **Open-item numbering stabilised** to `O-CX-n` across both files, ending a divergence that had
    the same item numbered 2 in one file and 3 in the other.

- **Not done, deliberately:** `tier-b-source-items.md` is **not re-transcribed**. Its flag table and
  changelog need a two-block status patch to v0.2; re-emitting the whole file would mean
  re-transcribing verbatim source text, which is the one operation §2.5 exists to prevent. The patch
  blocks were supplied to the owner for paste-in.

- **⚠ Repo state — write access attempted and refused; uploads then completed by the owner.** The
  connector exposed write tools this session and a push was authorised and attempted; it failed with
  `403 Resource not accessible by integration`, the same refusal as the previous three sessions.
  **Visible tools are not a permitted App**: the GitHub App must be installed on
  `andreiaktur-a11y/survey-skills` itself rather than only on the account, any new-permissions
  notification accepted, and the connector re-authorised in Claude Settings → Connectors. Read
  access works throughout and was used to verify every statement in this block.

  **Verified state at session close:** `ROADMAP.md` ✅ · `module-framework-cx.md` v0.3 ✅ ·
  `compliance.md` v0.2 ✅ · `SKILL.md` v0.2 ✅ · `session-brief-cx-05.md` ✅ ·
  `tier-b-source-items.md` **uploaded at v0.1, patch not applied** · the orphan PATCH file deleted ✅.

  **The v0.2 patch was then applied without re-transcription.** Because the file is now in the repo,
  it was **fetched and patched programmatically** rather than retyped — the objection that blocked
  this earlier was never about effort, it was about having no independent source to verify against,
  and the repo copy is that source. Diff verified: §1–§8 and §10 byte-identical to the uploaded file;
  only the status line, the flag-F sentence, §9 and the changelog changed. **`tier-b-source-items.md`
  v0.2 is the last file pending upload.**

  *(A ROADMAP regression happened this day and is repaired by this file: the superseded 2026-07-15
  project copy was uploaded over the current one, reverting §4 and §5 by two weeks. Git history holds
  the intermediate 07-27 state.)*

- **Next — session 5: questionnaire v0.1, no preconditions remaining.** Brief at
  `references/session-brief-cx-05.md`; its §1 and §3 are answered by `D-CX-18` and `D-CX-19`. The
  session opens by applying `D-CX-17` and `D-CX-18` as a scoped patch to `module-framework-cx.md`
  → **v0.4**, then drafts. Deliverable is shaped for the owner's own edit pass: two visual registers
  (`[LOCKED · TIER B · VERBATIM]` vs `[DRAFT · TIER A]`), a reasoning line on every editable item,
  a scripted clarification beneath every tier A item (`O-CX-20`), and English first with Spanish
  deferred until the edits settle. `O-CX-1` stays open but does not stop the draft: `SEF` is marked
  provisional, and if the dual criterion is later declined, three items come out and nothing else
  moves.

  **Short alternatives if session 5 is deferred:** `O-CX-6` + `O-CX-3` (two narrow source questions,
  external lookup) or `O-CX-13` (shared-layer IP tier sweep, mechanical, six files — the last place
  in the repo where the superseded tier A claim on CAHPS survives).

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

- **Note for the next session:** open a fresh chat and attach `session-brief-cx-05.md`,
  `module-framework-cx.md` v0.3, `tier-b-source-items.md` **v0.2** and `SKILL.md` v0.2. Fetch the ROADMAP
  from the repo rather than attaching a local copy — the local-copy route is what caused this day's
  regression:
  `curl -sS https://raw.githubusercontent.com/andreiaktur-a11y/survey-skills/main/ROADMAP.md`
  `Employee_Engagement_Retention_SAMPLE_v3_2.docx` is also still not in the repo.
