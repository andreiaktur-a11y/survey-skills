# Patch blocks — `tier-b-source-items.md` v0.1 → v0.2

**Purpose.** The owner signed off all seven flags on 2026-07-30 and the decisions are applied in `module-framework-cx.md` v0.3. The source file must stop describing itself as a draft awaiting sign-off, or the two files contradict each other on the record.

**Method.** Two blocks are replaced and nothing else is touched. **The verbatim source text in §3 and §5 is not re-emitted**, because re-transcribing published item wording is precisely the operation §2.5 exists to prevent — a copy is not the source, and a copy of a copy is a defect waiting to happen. Paste over the two blocks below; leave every other line as it stands.

---

## Block 1 — replaces the version/status line under the title

**Find:**

> **Version:** 0.1 · 2026-07-28 · **Status:** draft — three determinations and six flags require owner sign-off before any questionnaire line is written.

**Replace with:**

> **Version:** 0.2 · 2026-07-30 · **Status:** signed off. All seven flags resolved by the owner on 2026-07-30 and applied in `module-framework-cx.md` **v0.3** (decisions `D-CX-10` … `D-CX-16`). Verbatim source text unchanged from v0.1 — this revision touches the status line, §9 and §11 only.
>
> **Governs:** every `-B-` slot in `references/module-framework-cx.md` **v0.3**. The tier B set is now **closed at six items**; the determinations recorded here are the record of how it was closed, and the dropped-items register in §7 is the record of what was declined and why.

*(The naming note immediately below it stands as written — flag F was adopted as `D-CX-16`; strike only the trailing sentence "⚑ **Flag F, owner:** confirm the naming convention so it can be applied to the rest of the reference layer." and replace it with: "Adopted as `D-CX-16`, 2026-07-30, and extended to the whole reference layer.")*

---

## Block 2 — replaces §9 in full

**Find:** the section beginning `## 9 · Flags for owner sign-off` and running to the end of the paragraph beginning `**Additional finding for ROADMAP §5 item 6…**`.

**Replace with:**

```markdown
## 9 · Flag dispositions — all resolved 2026-07-30

Every flag raised in v0.1 was signed off by the owner on 2026-07-30. Recorded here as dispositions rather than deleted, because the provenance appendix must be able to show a reader a decision.

| # | Flag | Disposition | Recorded as |
|---|---|---|---|
| **A** | Spanish = a tier B question, not a translation question | **Adopted.** Official Spanish verbatim for tier B slots; TRAPD for tier A only. Every language beyond EN/ES is tier A throughout | `D-CX-12` · framework §2.5 constraint 4 |
| **B** | Slots with no usable source text become tier A — materialised at COM, all three slots | **Adopted.** Module COM rebuilt as four tier A items; framework §5 rewritten | `D-CX-13` · framework §5 |
| **C** | Alternate scales, `UNCLEAR RESPONSE`, and the "anyone else?" probe have no self-administered meaning | **Registered as open, blocked.** Not decidable until the mode is fixed | `O-CX-7`, blocked by `O-CX-2` |
| **D** | Corrected rationale for verbatim use; proposed fourth prohibited claim | **Adopted, both parts.** Verbatim buys attribution, format familiarity and freedom from the borrowed-paraphrase defect — not comparability. Fourth prohibited claim added | `D-CX-10` · framework §0.1, §2.5, §9.2, §12 |
| **E** | `RAT-B-01` is a rating of *help received*, not of the care manager | **Adopted.** Framework label corrected; §9.2 criterion argument corrected with it | `D-CX-14` · framework §3, §9.2 |
| **F** | Naming convention for reference-layer files | **Adopted** and extended to the whole reference layer | `D-CX-16` · framework §2.5 |
| **G** | The measure specification is a document we do not hold | **Scope reduced, then registered as open.** Under the bright line (`D-CX-11`) no tier B *composite* survives — every remaining tier B slot is a single item whose most positive option is unambiguous. The residue is one question: the source's own top-box definition for the 0–10 global rating | `O-CX-6` |

### 9.1 The framing decision the flags produced

The owner's disposition of flag D forced a decision the flag list did not contain. Once verbatim use no longer buys comparability, **every remaining item-level trade-off had the tier B side being paid for with a currency we no longer hold** — so deciding the slots one at a time would have produced a predictable run of tier A outcomes, each individually re-openable in a later session.

A rule was adopted instead (`D-CX-11`): a determination of **transfers** fills the slot verbatim; a determination of **transfers in part** converts it to an original tier A item. Applied to §4 and §5.5 of this file, it disposes of `CMH-B-02`, `CMH-B-03` and `UNM-TRN` together and closes the tier B set at six items — `RAT-B-01`, `RAT-B-02`, `CMH-B-00`, `CMH-B-01`, `POC-B-01`, `POC-B-02`.

`CMH-B-00` (§5.2) was adopted as recommended (`D-CX-15`): it is the gate for the whole care-manager block, and taking the block without it changes five denominators.

**`UNM-TRN` is resolved as the tier A item**, closing ROADMAP §5 item 3.

### 9.2 The hard input to `O-CX-5` (per-agency completes)

The TA guide reports effective sample sizes from the field test ranging from **70 completes** for the *Choosing the Services That Matter to You* composite to **376** for the *Case Manager Is Helpful* composite, against a **recommended target ESS of 400**. Our planning figure is ~100 per agency.

This does not invalidate the design — at network level, ten agencies at 100 clears 400 comfortably — but the composite the instrument is built around is the one requiring 376, so **it is not reliably reportable at agency level at the current planning target**, which is the level the LHH will want it at. It strengthens framework §2.2's reliability argument, and it turns `O-CX-5` from a budget question into a design question: *what is reported at which level, and at what n.* Answer it before the fieldwork budget is quoted.
```

---

## Block 3 — appends to §11 · Change log

**Insert above the existing v0.1 entry:**

```markdown
**v0.2 · 2026-07-30 —** Status only; no verbatim source text altered. All seven flags disposed of by owner sign-off and recorded in §9 as dispositions rather than deleted. §9.1 records the framing decision the sign-off produced (`D-CX-11`, the bright line) and the resulting closed tier B set of six items. Flag G's scope reduced to a single question and re-registered as `O-CX-6`; flag C re-registered as `O-CX-7`, blocked. §9.2 carries the effective-sample-size finding through to `O-CX-5`. Governing framework version advanced to v0.3.
```

---

## One consistency note, not a patch

§4 of the source file records the count correction ("ten fixed slots plus one conditional, eleven in total"). That correction stands and needs no edit — but note that after `D-CX-11` the *live* count is **six**, and §4's table is now a record of determinations rather than an inventory of slots. If the file is ever revised for content, say so in §4's lead-in. It is not worth a revision on its own.
