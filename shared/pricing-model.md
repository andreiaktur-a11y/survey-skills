# Pricing Model (shared)

A pricing layer the orchestrator uses to produce cost estimates and proposals. **Asset/reference, not methodology.** First encoded model below is the **RF survey / expert-survey line** (model #1); add other markets/domains (e.g., US marketing) as new sections later — same way the domain modules extend.

Calibrated to authoritative anchors (v05): **1500 mass-consumer = 573 321 ₽** and **500 professional = 435 745 ₽**. Prices in ₽, client-facing (quote) level. Re-confirm periodically — these drift.

> **Internal.** Some levers below (×2 for large clients, showcase markup) are commercial strategy. Keep in the private repo; never expose the levers or internal cost in client-facing output — only the final quote.

---

## Model #1 — RF survey / expert-survey line

### 1. Base quote — mass consumer (МКТУ groups 1–3), online, client-facing
| Sample (resp.) | Quote (₽) |
|---|---|
| 500 | ~305 000 |
| 700 | ~371 000 *(house rule: average of 500 and 1000)* |
| 1000 | ~436 000 |
| 1500 | **573 321** *(anchor)* |
| 2200 | ~737 000 |

Interpolation for non-standard sizes ≈ **171 000 + 268 ₽ × respondents** (approximate; tapers above 1500 — prefer the table for standard sizes).

### 2. Specialized / professional audience (groups 4–5)
Take the mass quote at the same sample size and **add the specialized uplift ≈ +130 000** (= +100 000 specialized + offline field ≈30 000). Calibrated so **500 professional = 435 745 ₽** (≈ ×1.5 of mass at small N). One anchor only — tighten the curve as more professional jobs land.

### 3. Modifiers (apply to the base, in this order)
- **Offline collection:** + field cost **+ 50 000** (mass). For groups 3–5 the field+uplift is already in §2.
- **Urgency:** standard 30 days = ×1; **3 weeks +40%**; **2 weeks +70%**.
- **Multiple tasks:** **+20% per additional questionnaire** (+ offline field per task if applicable).
- **Large / premium client** (e.g., alcohol, FMCG majors): **×2** — internal lever; quote high, adjust in negotiation.
- **Control cell (optional):** for legal confusion surveys, a test/control design adds a second sample arm → + its share of the per-respondent cost. **Standard in US** practice; **case-specific in RF** (not required by the SIP note — use when netting out baseline noise adds probative value). Off by default; turn on per case.
- **Showcase markup:** the quote is already padded (~+70 000 at 1500 vs internal cost) so a discount can be offered without going below cost.

### 4. Volume discount
If total ≥ 500 000 ₽: `discount% = min(30, total/1000 × 0.005 + 5)`, then `price = total × (1 − discount/100)`.
(Example: 700 000 → 8.5% → 640 500 ₽.)

### 5. Add-ons (priced separately, × number of objects; **+20% per additional object**)
| Add-on | ~Price (₽) |
|---|---|
| Market-share sociological study | ~616 500 |
| Information-analytical review | ~330 000 |
| Statistical review | ~330 000 |
| Qualitative content analysis | ~130 000 *(better sold as a pair, ~160 000)* |
| Quantitative content analysis | ~130 000 |
| Bibliographic study | ~550 000 |
| Archival-bibliographic study | ~940 000 |
| Natural experiment | ~830 000 |
| Online experiment | +20% of base |
| Tachistoscopic experiment | ~130 000 |
| Review (рецензия) | 80 000–240 000 *(depends on signatory)* |

*(Listed prices already include the +50 000 the calculator adds per add-on.)*

### 6. Sample × geography (ties to admissibility)
Optimal RF sample **2200 = 1500 in 6 cities (Rospatent benchmark) + 700 across ≥50 settlements** → satisfies both formal Rospatent compliance and all-Russia coverage. This is the pricing reflection of the geographic requirement in `../skills/domain-legal/references/admissibility.md` (SIP note) — pricing and defensibility line up here.

### Worked example
1500 mass, online, standard timing, single task, + market-share add-on:
573 321 + 616 500 = 1 189 821 → total ≥ 500 000 → discount min(30, 1189.821×0.005 + 5) = 10.95% → **≈ 1 059 500 ₽**.

---

## How the orchestrator uses this
When a project scope is set (audience type, sample size, mode, timing, tasks, add-ons), compute: base (§1/§2) → modifiers (§3) → sum add-ons (§5) → volume discount (§4) → final quote. Show the client only the final quote (and optionally an itemized scope), never the internal levers or cost.

> Source: ARA cost calculator v05, calibrated to the two authoritative anchors above. Re-validate figures before quoting.
