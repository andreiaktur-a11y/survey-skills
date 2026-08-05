# Session brief — CX **thaw** brief, written at the freeze

**Repo target:** `skills/domain-healthcare-cma/references/session-brief-cx-07.md`
**Prepared:** 2026-08-05, at the close of CX session 7 · **Governing artefacts at freeze:** `module-framework-cx.md` **v0.6** · `questionnaire-cx-member-experience.md` **v0.3**
**Discipline:** one task per session · principal-led · flag-first.

> ⏸ **This brief is different from the ones before it.** Sessions 5 and 6 were briefed *forward* into a known task. This one is written **into an unknown gap**, because the CX domain is parked (`D-CX-26`) while the Employee domain is finalised, and nobody knows how long that will be. It is therefore written for a reader who has forgotten the context — including a future Claude with none of it — and its first job is to make the state recoverable, not to plan a task.

---

## 0 · Where this stands, in five sentences

The CX domain builds a member-experience instrument for NYS Medicaid Health Home care management, sold to the **Lead Health Home**, measuring care-manager performance at **programme level and never at individual level**. Six items are reproduced verbatim from a published CMS instrument under a **verbatim-or-nothing** rule; everything else is original. The questionnaire is at **v0.3, 19 closed bank items, ≈35 questions on the expected path**, drafted and edited twice by the owner but **never cognitively tested, never translated beyond the locked strings, and never fielded** — and it runs on a **single criterion** since `D-CX-24` withdrew the capacity module. Two structural blockers stand: **counsel has not reviewed the PHI and disclosure structure** (`O-CX-2`), so no member-facing text exists at all; and the **codebook does not exist**. The domain is frozen at this point by owner decision, with every unresolved question written down rather than assumed away.

---

## 1 · Open the session this way — the sequence matters

1. **Fetch from the repo, never from a local or uploaded copy.**
   ```
   curl -sS https://raw.githubusercontent.com/andreiaktur-a11y/survey-skills/main/<path>
   ```
   ⚑ **This is not pedantry.** A local `ROADMAP.md` copy once rolled the repo back by two weeks. The repo file is the single source of truth; anything on disk is a snapshot of unknown age.
2. **Fetch, in this order:** `ROADMAP.md` → `skills/domain-healthcare-cma/references/module-framework-cx.md` → `.../questionnaire-cx-member-experience.md` → `.../tier-b-source-items.md` → this brief.
3. **Read ROADMAP §7 STATUS first.** If its date is later than 2026-08-05, this brief is stale — trust STATUS.
4. **Confirm the versions match** what §0 above states. A mismatch means work happened that this brief does not know about; find it before doing anything.

---

## 2 · The five decisions waiting — none of them Claude's

Each carries a recommendation. **A recommendation is not a decision, and it does not become one by sitting in a file for a few months.** If the owner does not answer, the item stays open and is re-raised — it is not absorbed.

| ID | Decision | Recommendation | Cost of getting it wrong |
|---|---|---|---|
| `O-CX-2` | Does *"no instrument text before counsel"* bind the item bank, or only the introduction, consent, disclosure and close? | **Only the latter** — as all three questionnaire versions assume | Low if wrong: only questionnaire §3 is affected, and §3 is empty |
| `O-CX-26` | How the member is told who we mean — programme term, role description, or the care manager's name | **The §2.6 sequence rule**: agency + role before the gate, name only *after* a `NO` is recorded | ⚑ **High.** Naming the person before A1 silently destroys A1's finding, and nothing in the data would show it had happened |
| `O-CX-27` | Which member characteristics are asked, and which come from the LHH file | **Ask only what administrative data holds badly** — race and ethnicity above all. Take DOB, sex, language from the file | Medium: over-asking costs 3–4 minutes and, through §2.2 suppression, *fewer* reportable findings rather than more |
| `O-CX-25` | `EXIT_TYPE` *Constrained continuing* after the `SEF` withdrawal (`D-CX-24`) | **Rename the type to what it now measures** | Medium: the label currently promises a capacity reading the instrument cannot deliver |
| `O-CX-29` | A2 has no *did not need to make contact* option | **Code `-7`, excluded from the `CMH` denominator, reported as a rate** | ⚑ **Settle before the codebook.** It changes a composite denominator, and a denominator changed after the codebook is written is a re-run, not an edit |

`O-CX-28` (A1 `YES` with no contact) also stands, with the recommendation to **change nothing** — see questionnaire §A1.

---

## 3 · The first task at thaw — and it needs none of the above answered

**Extract the *about you* and interviewer blocks into `tier-b-source-items.md` v0.3.**

This is deliberately chosen as the entry point because it is the one substantial piece of CX work that is **not blocked by any open decision**. It can run the moment the domain thaws, while the owner is still deciding the five items in §2.

**What it involves, and why it is a session of its own:**

- The source PDFs in the project are **page images, not text**. Every string has to be read off the page and transcribed by hand under the same discipline as the existing six locked items — then byte-verified, in **both EN and ES**.
- Each item needs a **transferability determination** — *transfers / transfers in part / does not transfer* — with the ground stated, exactly as `tier-b-source-items.md` §5 does for the existing slots. Demographic items are not automatically transferable: an HCBS-shaped item about living arrangements may not fit a Health Home roster.
- ⚑ **Verbatim or nothing. There is no third option.** If a string cannot be read confidently off the page, it is recorded as unreadable and the item is left out — **never reconstructed from what it probably says.** A demographic item is the easiest thing in the world to write from memory and the hardest place to notice that you have.

**Only after the extraction** can questionnaire sections I and J be drafted, and only after `O-CX-27` decides which of the extracted items are actually used.

---

## 4 · Everything that must be true before this instrument is fielded

Written as a list because at thaw it will be tempting to treat v0.3 as nearly finished. **It is not.** In rough dependency order:

1. `O-CX-2` answered → questionnaire §3.1–§3.5 drafted (advance contact, introduction and notice, proxy and assisted completion, disclosure and escalation protocol, close). **There is currently no text a member would ever hear.**
2. `O-CX-26` decided → the sample-file specification written, including whether care-manager name and title are transferred. **This changes the counsel package, so it belongs with item 1, not after it.**
3. `O-CX-6` obtained (source's top-box definition for the 0–10 rating) and `O-CX-29` decided → **codebook v0.1**.
4. `tier-b-source-items.md` v0.3 + `O-CX-27` → sections I and J drafted.
5. **Cognitive testing** — the pretest register is at questionnaire §7 and already names what to watch: `SC-10` option 4, `ACC-02` option 6 self-classification, `ACC-03` where no contact frequency was ever agreed, `RAT-B-02`'s conditional clause, A3's placement, and whether members can place `{agency name}` at all.
6. **Spanish for tier A items** — TRAPD, run **once**, on text that has survived cognitive testing. Running it earlier means running it twice.
7. `O-CX-5` (per-agency completes) → fieldwork costed.
8. One committed locked-string extractor, replacing the three that have each reported a different count.

---

## 5 · The rules that survive the freeze — do not re-derive these

- **Verbatim-or-nothing on tier B.** Verbatim use buys attribution, format familiarity, and freedom from the borrowed-paraphrase defect. It does **not** buy comparability with published results or the CAHPS Database, and the deliverable is never named "…CAHPS…".
- **Locked means locked in both directions** — wording, options, order, punctuation, the trailing `. . .`, the doubled Spanish `¿`. A locked item that reads awkwardly stays awkward.
- **No care-manager-level reporting.** Excluded on measurement-validity grounds, not feasibility. Stated to the member, in the report, and in the contract.
- **No external benchmark database.** Cross-agency within-network comparison is the standing comparison frame.
- **Suppression:** N < 5 with complement check; N ≥ 10 for within-agency subgroups.
- **Flag-first.** Construct-level changes are surfaced and approved before application, never applied silently. **Decisions once logged with rationale are not re-litigated** unless explicitly reopened.
- **Self-correction is explicit.** When Claude finds an error in its own prior work it is flagged to the owner, not quietly fixed. Two such corrections are recorded in the v0.3 change log.

---

## 6 · Two known defects carried into the freeze

1. ⚑ **The RU reading copy of v0.2 is wrong at A2**, rendering a locked Yes/No contact item as a 4-point frequency item about how often help was given when asked. **The working file was always correct.** The reading copy is superseded; at thaw it is **regenerated mechanically from the working file**, never hand-edited. The rule this produced: *a reading copy is generated, not written.*
2. ⚑ **The locked-string count has been reported three times and three ways** — 91, 70, 58 — each time because the extractor changed, never because a string changed. Every string all three extractors agree is locked has been byte-identical throughout. **One committed extractor before the codebook**, so the figure means something.

---

## 7 · Session close checklist (for whatever the thaw session turns out to be)

- [ ] Every construct-level change flagged and approved **before** application — none silent.
- [ ] Locked strings byte-verified against `tier-b-source-items.md`; result recorded in the questionnaire's QA section.
- [ ] All decisions logged in `ROADMAP.md` §4 with rationale; open items as `O-CX-n`, closed as `D-CX-n`.
- [ ] `ROADMAP.md`, `module-framework-cx.md` and the questionnaire left **mutually consistent** — no superseded argument left printed in support of a live conclusion.
- [ ] Version stamps updated **including the footer** (it has gone stale once).
- [ ] STATUS block written into ROADMAP §7.
- [ ] A brief prepared for the next session.
- [ ] All artefacts delivered to `/mnt/user-data/outputs/` for manual upload — **GitHub write access still fails with `403 Resource not accessible by integration`**. Fix: install the GitHub App on the *repository* (not only the account), accept the new-permissions notification, then reconnect the connector in Claude Settings → Connectors.

---

*Document owner: A. Akhtyrskii · Measure & Meaning Research · Prepared with Claude · 2026-08-05 · written at the freeze point, for a reader who has lost the context · illustrative + synthetic.*
