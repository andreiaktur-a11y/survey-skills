# ARA Survey Skills

A private set of Claude Agent Skills covering the full survey lifecycle for member-satisfaction and other **3MC** (multinational, multicultural, multiregional) surveys, built for healthcare Health Home / Care Management Agency (CMA) work.

Structured like Anthropic's `anthropics/skills`: one folder per skill under `skills/`, plus a `shared/` layer that every skill reads.

## Skills
| Skill | Does |
|---|---|
| `survey-orchestrator` | Sequences the lifecycle and routes to the others; applies the shared lens. |
| `survey-instrument-design` | Builds questionnaires from scratch. |
| `survey-instrument-review` | Audits an existing questionnaire → findings report. |
| `survey-translation-adaptation` | TRAPD translation + cultural adaptation + harmonization. |
| `survey-sampling` | Frames, sample size, per-group coverage, weighting. |
| `survey-fielding` | Mode selection, multilingual delivery, AI voice (Retell). |
| `survey-analysis` | Scoring, drivers, significance, measurement equivalence. |
| `survey-reporting` | Report/dashboard deliverable. |


## Agent integration
See `AGENTS.md` for the map of which agent loads which skills (bridges the AI Agent Architecture v2.0 harness to this repo).

## Domain modules (`skills/domain-*`)
One domain-agnostic methodological core + a thin domain "hat" per survey direction. See `DOMAINS.md` for the module contract and roster.
- `domain-healthcare-cma` (built) — CMA member satisfaction; CAHPS; HIPAA.
- `domain-hr-employee` (built) — employee/engagement surveys; confidentiality + anonymity thresholds.
- `domain-marketing` (built) — customer/brand research; CSAT/NPS/CES/pricing; CAN-SPAM/TCPA/GDPR consent.
- `domain-legal` (built) — trademark/IP survey evidence; recognized formats; admissibility (methodology, not legal advice).
- `domain-social-survey` (stub) — general sociological/social research of the public.
- `domain-public-opinion` (future) — politics/public opinion; documented in DOMAINS.md, build when real.

## Shared layer (`shared/`)
- `3mc-considerations.md` — cross-group comparability lens (used everywhere).
- `tse-framework.md` — Total Survey Error / quality framework.
- `pricing-model.md` — cost-estimate model for proposals (RF survey/legal line; internal levers). Asset, not methodology.
- `instrument-library/` — tagged catalog of validated items (CAHPS/CG-CAHPS, ARA's own). **Asset, not a skill.** No PHI.

## Design principles
- **Progressive disclosure:** thin `SKILL.md` (always-loaded triggering layer) → `references/` loaded on demand → `assets/`/`scripts/` as needed. Methodological depth lives in references, not in the always-loaded body.
- **One shared source of truth** for the instrument library and the 3MC/TSE lens, so the skills don't fork.
- **No PHI anywhere.** Build and test on synthetic or de-identified data.

## Install (private)
Skills here are **not** self-contained: most read the `shared/` layer via relative paths (e.g. `../../shared/question-quality.md`), and the legal references reach `../../../shared/`. So **do not upload a single skill folder as `.zip`** to Claude.ai — `shared/` won't be inside the archive and those references break.

Use one of:
- **Claude Code plugin (recommended):** register the **whole repo** as a marketplace (see `.claude-plugin/marketplace.json`); all skills + `shared/` install together and the relative paths resolve.
- **Claude.ai upload:** build a **self-contained bundle** per skill — a `.zip` whose root contains that skill's `SKILL.md` + `references/` **plus** the specific `shared/` files it references — or package a single "survey-suite" skill that vendors the shared files it needs. Verify every `../shared/...` path resolves inside the zip before uploading.

## Status
**v1 scaffold (private) — structure complete; legal/RF near-deliverable, other paths stubbed.** 13 skills (8 core + 5 domain) with valid frontmatter; shared layer = question-quality, 3mc, tse, instrument-library, pricing-model; governance = DOMAINS.md, AGENTS.md. Legal (RF) is the most developed domain: admissibility (SIP СП-21/15 + Rospatent Guideline), constructs→indicators→thresholds, formats (Eveready/Squirt/Teflon/Thermos + triangle rule + jurisdictional control-group note), two report templates + completeness checklist, pricing tied to geography. Healthcare/CMA path now runs end-to-end (evals: sample-plan + build-bilingual both PASS): instrument-library seeded with 32 tier-A items covering a full member-satisfaction instrument: CG-CAHPS (experience: access/communication/coordination/provider rating/overall, 20 items), ACS demographics (8), CDC HRQOL-4 health status (4) — all with full provenance; RU drafts flagged for TRAPD), plus translation-adaptation and instrument-flow references. Remaining stubs to populate from ARA material and public sources (ACS demographics, NHIS/BRFSS, AAPOR, CCSG concepts, official Rospatent/SIP texts). No PHI anywhere.
