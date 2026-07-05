# Validated Instruments (how to reuse them)

Reuse validated items instead of inventing wording — it buys comparability, established reliability/validity, and defensibility. The items themselves live in `../../../shared/instrument-library/`; this file is the **how-to-reuse** guide.

## Workflow
1. **Find** — read `shared/instrument-library/index.json`, filter by `domain` / `source` / `language` / `scale_type`.
2. **Check the tier** — `reuse_tier` A/B/C governs what you may do (below).
3. **Pull current wording from the official source**, not memory — instruments change across waves; honor `retrieved_date` and re-verify if stale.
4. **Keep composites intact** — validated scales are validated as sets; dropping/altering core items breaks comparability (and, for CAHPS, forfeits the name).
5. **Assemble** per `instrument-flow.md`; **adapt other languages** per the translation references (mark non-validated languages `draft`/`adapted`).
6. **Attribute** — carry the source attribution string; never imply endorsement by the source agency.

## Tier rules (from the library README)
- **A — public domain, verbatim OK** (CAHPS/CG-CAHPS, ACS/Census, NHIS, BRFSS, MEPS, NHANES; ARA's own). Store/use full text with provenance.
- **B — attribution, adapt conservatively** (Pew wording, GSS, academic). Reference patterns and attribute; don't redistribute the source's respondent datasets.
- **C — do NOT ingest** (Qualtrics/QSF, Press Ganey, NRC Health, any licensed vendor instrument). Consult for coverage ideas only; never copy.

## Provenance you must preserve
`reuse_tier`, `license`, `source_url`, `retrieved_date`, `attribution`, `verbatim_ok`. A new-language rendering you produce is `verbatim_ok=false` until it clears TRAPD.

## For the CMA path specifically
Backbone = **CG-CAHPS** (access, communication, care coordination, provider rating, overall) + **CAHPS supplemental** sets; **ACS** for demographics; **NHIS/BRFSS** for health status. All tier A. No PHI in any stored artefact.
