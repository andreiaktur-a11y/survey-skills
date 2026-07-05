# Sample Size & Frames

The **general, domain-agnostic** sampling methodology used on every project — standard survey practice (free to use; original synthesis, not copied). Size and frame logic are the same for healthcare/CMA, HR, marketing, and social work. **Domains add an overlay, never a different method**: the RF legal/evidentiary path additionally references Rospatent's geographic norms (see the overlay section). Apply with `../../../shared/3mc-considerations.md` (per-group coverage) and `../../../shared/tse-framework.md` (representation half). No PHI; use de-identified or aggregate frame/population data.

## 1. Sample size for a proportion (the workhorse)
For an estimate at confidence level z (95% → z≈1.96) and target margin of error e on a proportion p:

`n₀ = z² · p(1−p) / e²`

- Use **p = 0.5** when unknown (most conservative, largest n).
- Reference points at 95% (p=0.5): e=5% → **n≈385 (~400)**; e=3% → **n≈1067**; e=2.5% → **n≈1537 (~1600)**; e=2% → **n≈2401**. These are the universal anchors behind any "≈400 / ≈1600" rule of thumb.
- **Finite population correction (FPC)** when the frame is closed/known and the sample is a non-trivial fraction (≥~5%): `n = n₀ / (1 + (n₀−1)/N)`. Matters for finite rosters (e.g., a CMA member list, one employer's headcount) — it lowers the required n.

## 2. Precision, not just count
Size flows from the **precision the key estimate needs**, the confidence level, and the expected response rate — not from a target headcount. Invitations needed ≈ completed n / expected response rate. Headcount alone never proves adequacy; a large but biased sample is still biased.

## 3. Design effect & effective sample size
Clustering, unequal selection, and weighting reduce precision. Effective sample size:

`n_eff = n / DEFF`,  with weighting DEFF ≈ `1 + CV²(weights)` (CV = coefficient of variation of the weights).

Plan precision on **n_eff**, then inflate the fielded n by DEFF. Typical DEFF 1.2–2.0 for clustered/weighted designs; flag if you expect more.

## 4. Per-group / subgroup minimums (size for the smallest reportable cell)
Size for the **smallest group you must report on or compare**, not the total.
- Stable subgroup estimate: aim **~100 completes per reported cell**; ~30 is an absolute floor (wide intervals — caveat heavily).
- **Comparisons** need adequate n in *both* groups; a comparison is only as precise as the smaller cell.
- **3MC link:** set a **minimum n per language/cultural group up front** (`3mc-considerations.md`), or low-incidence groups silently collapse. Oversample small-but-required groups and correct with weights.

## 5. Frames & coverage
The frame is the operational list/mechanism from which you sample.
- Assess: **coverage** (who's systematically missing — coverage error), **accuracy** (bad/stale records), **duplication** (multiplicity → unequal selection), and per-group coverage (a frame can cover one language group well and another poorly → different frames/stages per `3mc-considerations.md`).
- Frame types: complete list (best — enables probability sampling and FPC), area/multistage, RDD/phone, online panel (document coverage/self-selection limits), or **the population itself when small** (a finite roster → census or FPC-adjusted sample).

## 6. Selection / randomization
Probability methods where feasible; document any deviation.
- SRS, **systematic** (random start + interval), **stratified** (precision on strata you must report), **cluster/multistage** (cheaper, raises DEFF).
- **Randomness at least at the final selection stage** is the minimum bar; record the method so selection is reproducible (it may be scrutinized).
- Stratify by the dimensions you must represent or compare (language, region, site, segment).

## 7. Weighting plan
Document before fielding (weighting trades bias for variance — it raises DEFF, §3).
1. **Design weights** — inverse of selection probability.
2. **Nonresponse adjustment** — by response propensity / known respondent characteristics.
3. **Calibration / post-stratification** — to known population margins. Use project census data for targets: **ACS/Census (US)**, **Rosstat (RF)**; client roster margins for closed populations.
Report unweighted n, weighted base, and DEFF.

---

## Domain overlays (same method + one extra layer)

**RF legal / evidentiary (Rospatent-SIP).** Use everything above, then **layer the RF geographic-distribution norms and the 400–2000 evidentiary band** — these are *additional* admissibility requirements, not a different formula. Do **not** duplicate the numbers here: see `../../domain-legal/references/admissibility.md` (universe → sample → geography: spread across the RF, the ~500-per-large-city / ~125-per-additional-city Rospatent orientation, final-stage randomness, durable-vs-everyday screening). Sampling note: control **questions** are a design matter (`../../domain-legal/references/survey-formats.md`); a control **group/cell** is an optional second arm sized like §1, case-specific in RF.

**Healthcare / CMA.** The de-identified **member roster is the frame** (finite, known) → census the small populations or FPC-adjust (§1); set per-language minimums (§4); never put PHI/identifiers in the frame artifact (`../../domain-healthcare-cma/references/compliance.md`).

**HR / employee.** Subgroup reporting interacts with the **small-group anonymity threshold** — do not report cells below the anonymity floor even if n is statistically usable (`../../domain-hr-employee/references/compliance.md`). Size and report at the level the threshold permits.

**Marketing / social.** Standard practice above, no extra legal overlay; choose frame/panel with documented coverage limits and weight to ACS/Census or the relevant population margins.
