# Instrument Library (shared asset)

A tagged catalog of survey instruments and item banks, shared across all skills. This is an **asset layer, not a skill** — it holds data plus a light lookup, so design/review/analysis/compliance all read from one source of truth instead of keeping divergent copies.

## How it works
- `index.json` holds metadata for every instrument, tagged by `domain`, `language`, `scale_type`, `source`, and `validation_status` (vocabulary defined in the file).
- `instruments/` holds one file per instrument (item text, scales, per-language versions, scoring/crosswalk notes).
- Skills find what they need by reading `index.json` and filtering on tags — no vector DB or RAG needed at this scale (add it only if the corpus grows to hundreds of multilingual instruments).

## Reuse tiers (record `reuse_tier` on every entry)
- **A — public domain, reuse verbatim:** CAHPS/CG-CAHPS, ACS/Census, NHIS, BRFSS, MEPS, NHANES, plus ARA's own instruments. Store full item text. CAHPS caveat: deleting core items forfeits the CAHPS name and comparability.
- **B — attribution, consult/adapt:** Pew Research Center question wording, GSS, academic instruments. Reference patterns and attribute; do **not** redistribute the source's respondent-level datasets. Be conservative about lifting wholesale into the distributed product.
- **C — do NOT ingest:** Qualtrics library/QSF templates, Press Ganey, NRC Health, any licensed vendor instrument. Consult only for coverage ideas; never copy.

## Provenance (required per entry)
Every instrument records `reuse_tier`, `license`, `source_url`, `retrieved_date`, `attribution`, and `verbatim_ok` (see `provenance_fields` in `index.json`). Wording changes across survey waves, so always date what you pulled and link the official source — not an aggregator.

## How to populate
Don't transcribe from memory. Pull the current instrument from its official source (ahrq.gov, census.gov, pewresearch.org), verify, then store with provenance. Priority order for ARA: CAHPS/CG-CAHPS → ACS demographics → health-status (NHIS/BRFSS) → Pew/GSS for attitudinal wording patterns.

## What NOT to put here
- **No PHI / no respondent answers with identifiers.** Build and test on synthetic or de-identified data.
- No tier-C content. No source's raw datasets.
## Tagging vocabulary
The `domain`, `scale_type`, and question-type tags use the vocabulary defined in `../question-quality.md` (§1 question types, §3 scale forms). Tag every instrument with that vocabulary so design, review, and search all speak the same language.
