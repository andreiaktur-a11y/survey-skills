# Evals

Representative tasks that exercise the skill set end-to-end, so we can tell whether a path actually works **before** filling content — and, when it doesn't, exactly *which* reference is load-bearing. This follows Anthropic's "start from representative tasks, iterate on observations" guidance.

## How to run one
1. Open a fresh Claude session with the relevant skills installed (or dogfood: load the domain `SKILL.md` + its `references/` + the `shared/` files they point to).
2. Paste the task prompt from `tasks/`.
3. Score against the task's **pass criteria**.
4. Log the result in `results/` as `YYYY-MM-DD-<task-id>.md`, and — critically — note every place the agent had to **improvise** because a reference was a stub. Those stubs are the load-bearing ones; fill them first.

## Scoring (per task)
- **PASS** — output meets all pass criteria from the agent's own knowledge + the populated references; no methodology invented.
- **PARTIAL** — structurally correct, but the agent filled a methodological gap from general memory because a reference was a stub (record which one).
- **FAIL** — wrong methodology, principle violation (e.g., US control-cell forced onto an RF case), or a broken/missing reference.

## Principle checks (run on every output)
- No PHI / no respondent identifiers.
- IP tiering respected (no verbatim tier-B/C; tier-A only with provenance).
- Legal: control **questions/stimulus** always; control **cell/group** not auto-applied to RF.
- Human-in-the-loop preserved (legal заключение marked "expert signature required"; "confirm with counsel / current Rospatent-SIP practice" retained).

## Roster (build files as we run them — YAGNI)
| id | path | task | status |
|---|---|---|---|
| `legal-rf-confusion-plan` | legal/RF | Plan an RF trademark likelihood-of-confusion survey. | **PASS** |
| `cma-sample-plan` | healthcare-CMA | Sample-size plan: 1,200 members, 5 language groups. | **PASS** |
| `cma-build-bilingual` | healthcare-CMA | Build a 12-item CMA member-satisfaction survey, EN/RU. | **PASS** — library seeded (20 tier-A CG-CAHPS items) + translation/flow refs filled |
| `review-anonymized` | core | Audit an anonymized member-satisfaction questionnaire → findings. | **PASS** |
| `analysis-comparability` | core | Decide whether language groups are comparable before pooling. | **PASS** |
