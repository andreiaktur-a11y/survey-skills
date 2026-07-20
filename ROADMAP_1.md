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

| Domain | Sample report (.docx) | Automation template in repo | Website "what you receive" |
|---|---|---|---|
| **Employee / HR** | ✅ v1 built (`Employee_Engagement_Retention_SAMPLE.docx`) — eNPS, satisfaction, burnout by segment, PsyCap, values, stay-vs-leave driver model | ⬜ next candidate (A) | ⬜ |
| **CX / Patient** | ⬜ (top-box, coordination-of-care, CAHPS-style) | ⬜ | ⬜ |
| **Brand / Market** | ⬜ (awareness, associations, share) | ⬜ | ⬜ |

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
- **2026-07-19** Non-overlapping tenure bands adopted (SEG-TEN: <1 / 1–2 / 3–6 / 7+ yrs); Fig. 5 rebuilt to match.
- **2026-07-19** Seven open flags resolved in one session (flags session "B"):
  1. **MEN/EVT extended GAP categories** — stay in the item bank; fielded only in EVP-focused configurations where CORE/BRN are trimmed. Not in the standard census.
  2. **MaxDiff-lite trade-off block** — design-on-request for v1; not part of the standard deliverable or report template.
  3. **OPN-03** — remains an empty per-engagement slot (codebook `.n` when not fielded); no standing third open-end.
  4. **Item count in report text** — do **not** state a fixed closed-item count in the sample report or template. The census is modular (client add-ons possible; pulse surveys will be subset configurations). Method section describes modules, not counts. Median completion time 13.4 min stays (consistent with a ~60-item instrument at 4–6 items/min). Template gets an *optional* `{{n_closed_items}}` field, empty by default.
  5. **BRN_TIER cutpoints** — keep pre-set bands 6–13 / 14–21 / 22–30, explicitly disclosed as pre-set (not normative). Recorded intent: re-anchor once against observed distributions after 3–5 engagements, then freeze. Disclosure to be mirrored in the report's technical appendix.
  6. **Weight trimming** — 0.4–2.5 confirmed as the default convention; client-specific override allowed, documented in the engagement codebook. Realized range + design effect reported as before.
  7. **STY-01 / STY-02** — reported separately, no composite. The stay/leave asymmetry is diagnostic; the driver model is built on separate criteria.
- **2026-07-19** Pulse surveys noted as future configurations = subsets of the census module map, not separate instruments.

---

## 5. Open decisions (waiting on owner)

1. **Real vs. synthetic data for report templates.** Default = synthetic. If anonymizable
   real outputs exist (e.g. the Engage motivation report), prepare a working template
   variant on that basis. → *pending answer.*

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

## 7. STATUS (latest — 2026-07-19, flags session)

- **Done:** Employee domain artifact chain drafted — questionnaire v0.1 (60 closed + 3 open,
  IP tier A), codebook v0.1 (md + CSV), sample report v3 (.docx), Fig. 5 rebuilt on
  non-overlapping tenure bands. All seven open flags resolved (see Decisions log,
  2026-07-19). Pulse-survey concept recorded: subset configurations of the census map.
- **Next:** session (A) — build the `{{braces}}` automation template from v3 + CSV codebook,
  applying the session-B edits:
  1. Method section: remove "74 closed items" (single instance in the method section only —
     "74" also appears twice as an Engineering score in results; do not touch those).
     Rewrite around module names; keep "median completion time 13.4 minutes".
  2. Add optional `{{n_closed_items}}` field to the template, empty by default.
  3. Mirror the BRN_TIER pre-set-cutpoints disclosure into the report technical appendix
     (source wording: codebook §5 / §9.1).
  4. Bump codebook §9 and questionnaire §12: all flags → resolved, with the decisions above;
     codebook gains the "re-anchor after 3–5 engagements, then freeze" note on BRN_TIER.
  After (A), the Employee domain is closed end-to-end (questionnaire → codebook → template)
  and ready for the website "what you receive" slot.
- **Open:** §5.1 (real vs. synthetic template variant) — the only remaining owner decision.
