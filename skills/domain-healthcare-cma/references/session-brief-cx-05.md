# Session brief — CX session 5: questionnaire v0.1

**Repo target:** `skills/domain-healthcare-cma/references/questionnaire-cx-member-experience.md`
**Prepared:** 2026-07-30 · **Governing artefact:** `module-framework-cx.md` **v0.3** (→ v0.4, see §2)
**Discipline:** one task per session · principal-led · flag-first · scope guards declared below.

---

## 0 · The task

Draft the fielded member-experience questionnaire, **v0.1, English**, from the item bank in `module-framework-cx.md` v0.3, in a form the owner can read item by item and rewrite.

The owner's stated purpose for this session is **to review and edit the questions himself.** The deliverable is therefore shaped for editing, not for fielding: see §6.

**This session is not transcription.** Two things stand between the item bank and a questionnaire, and both need the owner's answer before drafting starts. They are §1 and §3 below. Neither is Claude's to resolve.

---

## 1 · Precondition — what "conversational" means

**Owner decision, 2026-07-30:** the CMA survey is a **telephone survey in conversational mode.** This supersedes D-CX-5 (SMS/mail primary, phone fallback).

The word *conversational* carries three different methods, and they have different consequences for the tier B set. **One line from the owner settles it.**

| Reading | What it means | Consequence |
|---|---|---|
| **(a) Standardised administration, conversational in tone** | A human interviewer reads items as written, warm delivery, probing only within the source's own rules before coding `UNCLEAR` | **Tier B set survives intact.** This is how the source instrument is administered. Lowest friction |
| **(b) Mixed register** | Conversational interviewing on tier A items; strictly standardised delivery on the six tier B items | Workable, but the interviewer changes register mid-instrument. That has to be **scripted and trained**, not left to judgment, and it is itself a measurement risk |
| **(c) Fully conversational throughout** | Interviewer free to rephrase and clarify any item until the respondent understands it | **The tier B set empties.** An item delivered with clarification is not the item as published, so honesty requires converting all six to tier A. Everything gained from verbatim use is given back |

**Recommended: (a), or (b) if comprehension in this population is judged to require it.**

**A fourth reading must be ruled out explicitly.** If *conversational mode* meant an **automated conversational voice agent**, that is `O-CX-16` and it collides with two standing positions: §8.4.1 requires a disclosure and escalation protocol that an automated agent cannot execute, and §10.2 sells independent administration as the product. Recommend the exclusion is confirmed rather than left implicit.

---

## 2 · Precondition — the mode change is a framework change

The questionnaire cannot be drafted against a framework whose mode section is wrong. **Session 5 opens by applying the mode decision as a scoped patch to `module-framework-cx.md` → v0.4**, then drafts. This is declared as part of the one task, not a second task, because the patch exists only to make the drafting correct.

### 2.1 What the mode change removes

**One of the three grounds under D-CX-10 falls away.** The published instrument is interviewer-administered by telephone or in person. Ground 3 — *our mode is not the published mode* — no longer holds.

**The conclusion does not change; the argument does.** Grounds 1 and 2 are independent and survive untouched: the instrument is validated in its entirety and not in parts, and a sponsor adding items beyond the core set and approved supplements cannot submit to the CAHPS Database. Our instrument is still a subset plus a substantial tier A block. **Verbatim use still does not buy comparability, and the fourth prohibited claim in §0.1 still stands.**

⚑ **This must be edited, not left.** §2.5 and §0.1 currently print ground 3 as live. A document that carries a superseded argument in support of a correct conclusion is worse than one that carries neither — it invites the whole determination to be reopened by the first reader who notices.

### 2.2 What the mode change unblocks

- **`O-CX-7` is now decidable.** The source's cognitive-accommodation alternate (binary version of the whole survey) and its alternate 5-point rating have meaning again, as does the `UNCLEAR RESPONSE` code. Decide: carry the alternate as the source specifies — a **separate alternate version of the whole instrument**, not a per-item fallback — or exclude it and state the exclusion.
- **`POC-B-02`'s mode caveat disappears.** Its interviewer-coded multiple response and unprompted "anyone else?" probe now work as published.
- **`O-CX-8` becomes decidable** (`ACC-01` frequency vs `CMH-B-01` verbatim Yes/No). The trade has moved in both directions: a human interviewer makes 4-point gradation cheap by phone, which favours `ACC-01`; but our mode now matches the published mode, which makes verbatim `CMH-B-01` more defensible than it was. Genuine trade, decidable in session.

### 2.3 What the mode change does **not** reopen

**All four bright-line conversions hold.** Each failed on content or structure, not on mode:

| Converted | Why it stays converted |
|---|---|
| `CMH-B-02` | HCBS-shaped exemplar; screened base rate lands at 15–20 per agency and is unreportable |
| `CMH-B-03` | The screen carries fixed, non-fillable HCBS service content |
| `UNM-TRN` | 4-point frequency item with no need screen, inside a Yes/No module |
| `COM-B-01…03` | No care-manager-referenced communication item exists in the source at all |

`D-CX-11` therefore stands as written, and the tier B set stays closed at six.

### 2.4 What the mode change makes worse

- **`O-CX-5` becomes acute.** A telephone census is the most expensive design in the set, and §2.2 already shows the care-manager composite is not reliably reportable at agency level at ~100 completes. The completes target is now a budget question **and** a design question at once.
- **Frame coverage is now mode-determined.** Members without a working number on the roster are excluded by the instrument's mode, not by their own choice. That exclusion rate is printed as a coverage figure, on the §8.5 precedent for language — not buried in limitations.
- **`D-CX-7` becomes a staffing constraint.** Coverage to 95% of roster by phone means multilingual **interviewers**, not translated forms. The cost structure is different and the 95% rule needs re-pricing.
- **Interviewer effects become the primary data-quality threat.** §2.3 already carries the right rules for the phone branch; the self-administered branch becomes secondary rather than co-equal.

### 2.5 Sections to patch in v0.4

§0.1 (ground 3) · §1 (length budget re-check) · §2.1 (alternates, per `O-CX-7`) · §2.3 (branch priority) · §2.5 (D-CX-10 ground 3; note that mode alignment does **not** restore comparability) · §8.5 (interpreter/interviewer capacity) · §10.2 (rewritten) · §13 (`D-CX-17` recorded; `O-CX-7`, `O-CX-16` dispositions).

---

## 3 · Precondition — the questionnaire is over budget by roughly double

This is the finding most likely to derail the session if it is discovered mid-draft.

**Item bank, v0.3, distinct IDs:** RAT 3 · CMH 5 · COM 4 · ACC 4 · POC 5 · COORD 3 · UNM 5 · GRV 3 · RSP 2 · LNG 3 · SEF 3 · ENG 3 · OPN 3 → **43 closed items plus 3 open-ended**, before need screens.

**Budget, §1:** 20–26 closed items, ≤ 10 minutes by phone.

The framework already anticipates this: §1 maps **configurations**, not one universal instrument. So the question is not *what gets cut* but **which configuration is being drafted first.** Taking the §1 QMP configuration (RAT + CMH + COM + ACC + POC + UNM + OPN) gives 26 closed items — exactly at the ceiling, and that is **before** the criterion layer, which the driver model requires: `SEF` (3) and `ENG` (3) push it to 32.

⚑ **Owner decision required before drafting:**

1. **Which configuration is v0.1?** Recommended: the **QMP evidence base** configuration — it is the one the buyer's obligation names, and it exercises every module the other configurations draw from.
2. **What yields to fit the budget?** Three routes, and they are not equivalent:
   - **(i) Raise the ceiling.** A well-run conversational phone interview sustains more than 10 minutes with this population. Costs money per complete and raises break-off risk mid-instrument.
   - **(ii) Cut modules.** `LNG`, `RSP`, `GRV` are the candidates by configuration logic — but `GRV` is described in §8.3 as the module most likely to produce a finding the LHH acts on the same quarter.
   - **(iii) Cut the criterion layer.** Do not. Without `SEF` and `ENG` there is no driver model and no `EXIT_TYPE`, which is the analytical product.

   **Recommended: (i) modestly, plus (ii) on `LNG` and `RSP`** — `LNG` is partly recoverable from the roster and from achieved-mode data, and `RSP` at two items is the thinnest module in the set. Flagged, not decided.

---

## 4 · The two standing blockers, restated honestly

- **`O-CX-1` (dual criterion) is open.** It does not have to stop this session: both criteria's items are specified, so the questionnaire can be drafted with `SEF` marked **provisional**. If the owner declines the dual criterion later, three items come out and nothing else moves. **Confirm this is acceptable, or answer `O-CX-1` first.**
- **`O-CX-2` (counsel) is open**, and §10.3 says *counsel review before any instrument text is written.* That constraint was written when the mode was undecided and the PHI route drove the mode. The mode is now set independently. ⚑ **Owner: does the constraint bind the item bank, or only the member-facing text?** Recommended reading — **only the member-facing text**: the introduction script, the consent and notice language, and the disclosure protocol are drafted as **stubs** in v0.1 and filled after counsel. Item wording proceeds.

---

## 5 · Scope guards

**In scope:** the v0.4 mode patch (§2.5 list) · the configuration decision (§3) · English draft of every item in the chosen configuration · routing and screen logic · interviewer instructions for the tier B items as the source specifies them · the locked/editable separation (§6).

**Out of scope, explicitly:** the codebook (needs `O-CX-6`) · the Spanish version (see §6.4) · the report template · the sample report · fieldwork materials that depend on counsel · `O-CX-13` (shared-layer tier sweep) · anything in the Employee or Brand domains.

---

## 6 · Shape of the deliverable — this is the part that matters for the owner's edit pass

### 6.1 Two visual registers, never mixed

Every item is printed in one of two forms, and the difference is unmissable on the page:

```
[LOCKED · TIER B · VERBATIM — source Q54 — DO NOT EDIT]
```

```
[DRAFT · TIER A — editable]
```

**Rationale, and it is the reason this matters more than it looks.** The owner's stated intention is to rewrite questions. A locked item that reads awkwardly is exactly the kind of thing an editor improves — and improving it silently converts a tier B item into a lightly reworded CAHPS item, which §2.5 identifies as the **worst** available outcome: no comparability *and* a paraphrase that reads as borrowed. The registers exist so that the edit pass cannot do this by accident.

**QA rule to carry forward:** every locked string is checked byte-for-byte against `tier-b-source-items.md`. A mismatch is a defect, not a variant.

### 6.2 Every tier A item carries its reasoning

Each editable item is printed as: **ID · construct · proposed wording · scale · routing · one line on what the item is doing and why it is worded that way.**

The last field is the point. An edit pass without it produces wording changes that quietly change constructs — the item still reads well and no longer measures what the index needs.

### 6.3 Interviewer layer is part of the instrument, not a wrapper

In a phone instrument the interviewer instructions *are* the instrument. Section lead-ins, fills, `DON'T KNOW` / `REFUSED` / `UNCLEAR` handling, and skip instructions are printed inline with the items, in the source's own form where the item is tier B.

### 6.4 English first, Spanish after the edits settle

Tier B items carry the **official Spanish inline and locked** (`D-CX-12`) — that text is already final and cannot be edited anyway. Tier A items are drafted **English only** in v0.1. TRAPD runs after the owner's edits are settled, because translating text that is about to change wastes the translation and, worse, produces a Spanish version that silently tracks a superseded English original.

---

## 7 · Inputs to attach when opening the session

1. `ROADMAP.md` — **fetch from the repo**, do not attach a local copy:
   `curl -sS https://raw.githubusercontent.com/andreiaktur-a11y/survey-skills/main/ROADMAP.md`
2. `module-framework-cx.md` v0.3
3. `tier-b-source-items.md` — **the source of every locked string.** The questionnaire is copied from this file and never from the PDF or from memory (§2.5, route rule)
4. `domain-healthcare-cma/SKILL.md` v0.2
5. This brief

---

## 8 · Session close checklist

- [ ] `module-framework-cx.md` **v0.4** — mode patch applied, `D-CX-17` recorded, `O-CX-7` and `O-CX-16` disposed of
- [ ] `questionnaire-cx-member-experience.md` **v0.1** — chosen configuration, both registers, reasoning line on every tier A item
- [ ] Locked-string check run against `tier-b-source-items.md`, result recorded
- [ ] Item count against the §1 budget printed in the questionnaire header, with what was cut and why
- [ ] `ROADMAP.md` STATUS updated and **uploaded**
- [ ] Open items reconciled: `O-CX-n` list identical in both files

---

*Prepared with Claude · Measure & Meaning Research · one task per session · flag-first · owner decisions recorded with rationale, never resolved silently.*
