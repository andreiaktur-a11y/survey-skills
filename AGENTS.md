# Agents ↔ Skills

Two layers, kept deliberately separate:
- **Agent harness** — the autonomy/plumbing (per the ARA *AI Agent Architecture v2.0* addendum: Claude API + n8n + PostgreSQL, scheduling, webhooks, state, audit log, human-in-the-loop gates). This is the body.
- **Skills** (this repo) — the versioned methodology each agent loads to do its task well. This is the brain.

This file is the bridge so the two don't drift. **Update it whenever an agent or skill changes.**

## The wiring rule
Every agent loads **(a) its own core skill(s) + (b) the active domain hat** the Orchestrator selected for the project. `shared/` (question-quality, 3mc, tse, instrument-library, pricing-model) is available to all. The domain hat = the market/product (RF legal, US marketing/HR/healthcare), so one agent set serves both countries — only the hat swaps.

## Map (11-agent addendum → skills)
| Agent | Loads |
|---|---|
| 0 — Orchestrator | `survey-orchestrator` (+ reads `DOMAINS.md` to route to the domain hat; `shared/pricing-model.md` at proposal stage) |
| 1 — Research Methodology | `survey-sampling`, `shared/3mc-considerations`, `shared/tse-framework`, `survey-fielding` (mode selection) |
| 2 — Survey Design | `survey-instrument-design`, `survey-instrument-review`, `survey-translation-adaptation`, `shared/question-quality`, `shared/instrument-library`; (legal: `domain-legal/references/constructs-and-indicators`, `survey-formats`) |
| 3 — Survey Analyst | `survey-analysis` (core-analysis, measurement-equivalence) |
| 4 — Sentiment Extractor | `survey-analysis` (open-text conventions), `shared/question-quality` — mostly its own NLP; skills give the conventions/guardrails |
| 5 — Prediction | `survey-analysis` (driver analysis) — predictive tooling is its own; skill supplies analysis conventions and the "correlation ≠ cause" guardrail |
| 6 — Report Generator | `survey-reporting` + the active domain's report template (e.g., `domain-legal/references/report-template.md`) |
| 7 — Compliance | the active domain's compliance layer: healthcare HIPAA · HR anonymity thresholds · marketing TCPA/CAN-SPAM · legal admissibility (SIP/Rospatent) |
| 8 — Sales | `shared/pricing-model.md` |
| 9 — HR (internal hiring/ops) | — none (internal operations, not survey methodology) |
| 10 — Client Communications | — none / light (message tone only) |

## Routing by country/product
The Orchestrator picks the domain hat = market: **RF → `domain-legal`**; **US → `domain-marketing` / `domain-hr-employee` / `domain-healthcare-cma`**. Every downstream agent then loads that same hat.

## Guardrails (the skills enforce what the addendum requires)
- Human-in-the-loop: no client-facing deliverable ships without founder/expert approval. Legal **заключение** must carry an expert signature — the agent prepares, the human signs.
- No PHI / no respondent identifiers in any artefact; de-identified or synthetic data only.
- "Confirm with counsel" / "confirm against current Rospatent-SIP practice" stays in the output for legal work.
- Versioning skills in git **is** the audit trail the Orchestrator's audit-log function needs.

## Not to confuse
- `domain-hr-employee` = a skill for running **HR surveys for clients**, NOT Agent 9 (ARA's internal hiring). Different things.
- Business-ops agents (9, 10) are intentionally skill-light — they aren't methodology.
