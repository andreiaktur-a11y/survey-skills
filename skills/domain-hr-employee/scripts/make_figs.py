#!/usr/bin/env python3
"""Measure & Meaning — Employee sample report v2 figures.
All data are ILLUSTRATIVE + SYNTHETIC (fictional org: Northgate Components, Inc.).
Brand palette per MM brand guidelines v1/2026."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ---- brand ----
NAVY   = "#0B1F3A"
TEAL   = "#0EA5A3"
TEALI  = "#0B7472"   # teal for text
CORAL  = "#FF6A5C"
CORALI = "#C7402F"   # coral for text
SAGE   = "#7FA58F"
PAPER  = "#F3F5F6"
STONE  = "#E2E7EB"

for f in ["fonts/Poppins-SemiBold.ttf", "fonts/Inter-Regular.ttf", "fonts/Inter-Medium.ttf"]:
    fm.fontManager.addfont(f)
plt.rcParams.update({
    "font.family": "Inter",
    "font.size": 10,
    "axes.edgecolor": STONE,
    "axes.linewidth": 0.8,
    "axes.labelcolor": NAVY,
    "text.color": NAVY,
    "xtick.color": NAVY,
    "ytick.color": NAVY,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "svg.fonttype": "none",
})
POP = fm.FontProperties(fname="fonts/Poppins-SemiBold.ttf")

def style_ax(ax, xgrid=False, ygrid=False):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    if xgrid:
        ax.xaxis.grid(True, color=STONE, lw=0.8)
        ax.set_axisbelow(True)
    if ygrid:
        ax.yaxis.grid(True, color=STONE, lw=0.8)
        ax.set_axisbelow(True)

def save(fig, name):
    fig.savefig(f"figs/{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", name)

# =====================================================================
# Fig 1 — CORE: Engagement index by unit, dashed org-average line
# =====================================================================
units = ["Engineering", "Finance & Admin", "Quality", "Sales & Customer Ops",
         "IT", "Production", "Warehouse & Logistics"]
n_by  = [94, 46, 52, 81, 24, 512, 168]
eng   = [74, 71, 70, 69, 66, 64, 61]
org_avg = 65.4  # weighted

fig, ax = plt.subplots(figsize=(7.4, 3.6))
order = np.argsort(eng)
y = np.arange(len(units))
cols = [CORAL if eng[i] < org_avg - 2 else TEAL for i in order]
ax.barh(y, [eng[i] for i in order], color=cols, height=0.62, zorder=3)
ax.set_yticks(y, [f"{units[i]}  (n={n_by[i]})" for i in order])
ax.axvline(org_avg, color=NAVY, ls=(0, (5, 3)), lw=1.4, zorder=4)
ax.text(org_avg + 0.6, len(units) - 0.28, f"Org average {org_avg:.0f}",
        fontsize=9, color=NAVY, fontweight="bold")
for yi, i in enumerate(order):
    ax.text(eng[i] - 1.2, yi, str(eng[i]), va="center", ha="right",
            color="white", fontsize=9.5, fontweight="bold", zorder=5)
ax.set_xlim(0, 100)
ax.set_xlabel("Engagement index (0–100)")
style_ax(ax, xgrid=True)
save(fig, "fig1_core")

# =====================================================================
# Fig 2 — eNPS: 100% stacked detractor / passive / promoter by segment
# =====================================================================
segs   = ["Org overall", "Engineering", "Quality", "Sales & Cust. Ops",
          "Finance & Admin", "IT", "Production", "Warehouse & Log."]
det    = [31, 20, 25, 27, 26, 33, 35, 38]
prom   = [28, 38, 33, 31, 30, 25, 23, 21]
pas    = [100 - d - p for d, p in zip(det, prom)]
enps   = [p - d for d, p in zip(det, prom)]
ci     = [4, 10, 13, 11, 14, 19, 5, 8]  # ±, wider for small n

fig, ax = plt.subplots(figsize=(7.4, 3.8))
y = np.arange(len(segs))[::-1]
ax.barh(y, det,  color=CORAL, height=0.6, label="Detractors (0–6)", zorder=3)
ax.barh(y, pas,  left=det, color=STONE, height=0.6, label="Passives (7–8)", zorder=3)
ax.barh(y, prom, left=[d + p for d, p in zip(det, pas)], color=TEAL,
        height=0.6, label="Promoters (9–10)", zorder=3)
for yi, (d, pa, pr, e, c) in zip(y, zip(det, pas, prom, enps, ci)):
    ax.text(d / 2, yi, f"{d}", va="center", ha="center", color="white", fontsize=8.5, fontweight="bold")
    ax.text(d + pa / 2, yi, f"{pa}", va="center", ha="center", color=NAVY, fontsize=8.5)
    ax.text(d + pa + pr / 2, yi, f"{pr}", va="center", ha="center", color="white", fontsize=8.5, fontweight="bold")
    ax.text(103, yi, f"{e:+d}  (±{c})", va="center", ha="left", fontsize=9,
            color=CORALI if e < 0 else TEALI, fontweight="bold")
labels = list(segs)
labels[0] = "Org overall (n=987)"
ax.set_yticks(y, labels)
ax.get_yticklabels()[0].set_fontweight("bold")
ax.set_xlim(0, 122)
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xlabel("% of respondents")
ax.text(103, len(segs) - 0.15, "eNPS (±95% CI)", fontsize=8.5, color=NAVY, fontweight="bold")
ax.legend(loc="upper center", bbox_to_anchor=(0.42, -0.18), ncol=3, frameon=False, fontsize=9)
style_ax(ax)
save(fig, "fig2_enps")

# =====================================================================
# GAP data — 18 categories, 7-pt scales
# =====================================================================
gap = {  # code: (importance mean, satisfaction mean, label)
 "PAY": (6.4, 4.1, "Pay fairness"),
 "REC": (5.6, 4.3, "Recognition"),
 "MGR": (5.9, 5.4, "Manager relationship"),
 "GRW": (5.8, 3.9, "Career growth"),
 "LRN": (5.4, 4.4, "Learning & development"),
 "FLX": (5.7, 4.8, "Schedule fit"),
 "WKL": (6.0, 4.2, "Sustainable workload"),
 "BEN": (6.1, 4.9, "Benefits & social support"),
 "MNG": (5.2, 5.0, "Meaningful work"),
 "AUT": (5.0, 5.1, "Autonomy"),
 "TEA": (5.5, 5.7, "Team relationships"),
 "SEC": (6.2, 5.2, "Job security"),
 "RES": (5.6, 4.6, "Tools & resources"),
 "VOI": (5.3, 4.0, "Voice & participation"),
 "CRS": (5.4, 4.7, "Support in difficult situations"),
 "SAF": (6.3, 5.8, "Workplace safety"),
 "COM": (5.7, 4.3, "Communication & information"),
 "FDK": (5.1, 4.4, "Feedback"),
}
imp_med, sat_med = 5.65, 4.65  # within-survey medians (synthetic)

# Fig 3 — quadrant map
fig, ax = plt.subplots(figsize=(7.2, 5.6))
ax.axvspan(2.8, sat_med, ymin=(imp_med-4.2)/(7.1-4.2), ymax=1, color=CORAL, alpha=0.08, zorder=0)
ax.axvline(sat_med, color=NAVY, ls=(0, (5, 3)), lw=1.2)
ax.axhline(imp_med, color=NAVY, ls=(0, (5, 3)), lw=1.2)
offsets = {"PAY":(-0.05,0.09),"WKL":(0.06,0.08),"GRW":(-0.05,-0.16),"COM":(-0.05,0.09),
           "VOI":(-0.05,-0.16),"REC":(0.06,-0.15),"RES":(0.07,0.07),"LRN":(-0.05,-0.16),
           "FDK":(0.06,0.06),"CRS":(0.06,0.07),"FLX":(0.06,0.07),"BEN":(0.06,0.07),
           "SEC":(0.06,0.07),"MGR":(0.06,-0.15),"TEA":(0.06,0.06),"SAF":(0.06,0.06),
           "MNG":(0.05,-0.16),"AUT":(0.05,0.07)}
for code, (i, s, lab) in gap.items():
    action = (i > imp_med and s < sat_med)
    ax.scatter(s, i, s=64, color=CORAL if action else TEAL, zorder=4,
               edgecolor="white", linewidth=1)
    dx, dy = offsets.get(code, (0.06, 0.06))
    ax.text(s + dx, i + dy, code, fontsize=8.5, color=CORALI if action else NAVY,
            fontweight="bold" if action else "normal",
            ha="right" if dx < 0 else "left")
ax.text(2.92, 7.02, "ACTION ZONE", fontsize=10, color=CORALI, fontweight="bold", fontproperties=POP)
ax.text(2.92, 6.82, "high importance · low satisfaction", fontsize=8, color=CORALI)
ax.text(7.0, 7.02, "STRENGTHS — protect", fontsize=9, color=TEALI, fontweight="bold", ha="right")
ax.text(7.0, 4.28, "monitor", fontsize=9, color=NAVY, alpha=0.6, ha="right")
ax.text(2.92, 4.28, "low priority", fontsize=9, color=NAVY, alpha=0.6)
ax.set_xlim(2.8, 7.1); ax.set_ylim(4.2, 7.1)
ax.set_xlabel("Satisfaction (mean, 1–7; N/A excluded)")
ax.set_ylabel("Importance (mean, 1–7)")
ax.text(sat_med + 0.03, 4.3, "survey median", fontsize=7.5, color=NAVY, alpha=0.7, rotation=90, va="bottom")
style_ax(ax)
save(fig, "fig3_gap_quadrant")

# Fig 4 — ranked gap scores
codes = sorted(gap, key=lambda c: gap[c][0] - gap[c][1], reverse=True)
vals  = [gap[c][0] - gap[c][1] for c in codes]
fig, ax = plt.subplots(figsize=(7.4, 5.0))
y = np.arange(len(codes))[::-1]
cols = [CORAL if v >= 1.3 else (TEAL if v > 0 else SAGE) for v in vals]
ax.barh(y, vals, color=cols, height=0.62, zorder=3)
ax.set_yticks(y, [f"{gap[c][2]}  ({c})" for c in codes], fontsize=9)
for yi, v in zip(y, vals):
    ax.text(v + (0.04 if v >= 0 else -0.04), yi, f"{v:+.1f}", va="center",
            ha="left" if v >= 0 else "right", fontsize=8.5,
            color=CORALI if v >= 1.3 else NAVY)
ax.axvline(0, color=NAVY, lw=1)
ax.set_xlim(-0.5, 2.6)
ax.set_xlabel("Gap = importance − satisfaction (7-pt scales)")
style_ax(ax, xgrid=True)
save(fig, "fig4_gap_rank")

# =====================================================================
# Fig 5 — BRN: 100% stacked risk tiers by tenure band
# =====================================================================
bands = ["< 1 year\n(n=142)", "1–3 years\n(n=289)", "3–7 years\n(n=331)", "7+ years\n(n=225)"]
low   = [58, 44, 38, 47]
mod   = [28, 32, 31, 31]
elev  = [14, 24, 31, 22]
fig, ax = plt.subplots(figsize=(6.8, 3.4))
x = np.arange(len(bands))
ax.bar(x, low, color=TEAL, width=0.58, label="Low risk", zorder=3)
ax.bar(x, mod, bottom=low, color=STONE, width=0.58, label="Moderate", zorder=3)
ax.bar(x, elev, bottom=[l + m for l, m in zip(low, mod)], color=CORAL, width=0.58, label="Elevated", zorder=3)
for xi, (l, m, e) in zip(x, zip(low, mod, elev)):
    ax.text(xi, l / 2, f"{l}%", ha="center", va="center", color="white", fontsize=9, fontweight="bold")
    ax.text(xi, l + m / 2, f"{m}%", ha="center", va="center", color=NAVY, fontsize=9)
    ax.text(xi, l + m + e / 2, f"{e}%", ha="center", va="center", color="white", fontsize=9, fontweight="bold")
ax.set_xticks(x, bands)
ax.set_ylim(0, 100)
ax.set_ylabel("% of respondents")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=3, frameon=False, fontsize=9)
style_ax(ax)
save(fig, "fig5_brn_tiers")

# =====================================================================
# Fig 6 — BRN demand vs recovery 2×2 by unit
# =====================================================================
# x = demand load (BRN-01 + reversed BRN-04), y = recovery adequacy (BRN-02)
brn_units = {
 "Production":            (3.6, 2.6, 512),
 "Warehouse & Logistics": (3.4, 2.8, 168),
 "Engineering":           (3.3, 3.4, 94),
 "Sales & Customer Ops":  (3.1, 3.1, 81),
 "Quality":               (2.9, 3.3, 52),
 "Finance & Admin":       (2.7, 3.5, 46),
 "IT":                    (3.2, 3.0, 24),
}
fig, ax = plt.subplots(figsize=(6.8, 5.2))
ax.axvline(3.0, color=NAVY, ls=(0, (5, 3)), lw=1.1)
ax.axhline(3.0, color=NAVY, ls=(0, (5, 3)), lw=1.1)
ax.axvspan(3.0, 4.0, ymin=0, ymax=(3.0-2.2)/(4.0-2.2), color=CORAL, alpha=0.08, zorder=0)
for u, (d, r, n) in brn_units.items():
    risk = d > 3.0 and r < 3.0
    ax.scatter(d, r, s=np.sqrt(n) * 14, color=CORAL if risk else TEAL,
               alpha=0.85, edgecolor="white", linewidth=1.2, zorder=4)
    va = "bottom" if u not in ("Warehouse & Logistics",) else "top"
    dy = 0.06 if va == "bottom" else -0.06
    dy = dy * (2.2 if u == "Production" else 1)
    ax.text(d, r + dy + (0.06 if u == "Production" else 0), u, fontsize=8.5,
            ha="center", va=va, color=CORALI if risk else NAVY,
            fontweight="bold" if risk else "normal")
ax.text(3.97, 2.24, "HIGH DEMAND · LOW RECOVERY\n= structural risk (workload math, not resilience training)",
        fontsize=8, color=CORALI, ha="right", va="bottom", fontweight="bold")
ax.text(2.24, 3.92, "sustainable", fontsize=9, color=TEALI, va="top")
ax.set_xlim(2.2, 4.0); ax.set_ylim(2.2, 4.0)
ax.set_xlabel("Demand load (BRN-01, BRN-04ʀ mean, 1–5)")
ax.set_ylabel("Recovery adequacy (BRN-02, 1–5)")
ax.text(3.02, 3.94, "scale midpoint", fontsize=7.5, color=NAVY, alpha=0.7, rotation=90, va="top")
style_ax(ax)
save(fig, "fig6_brn_2x2")

# =====================================================================
# Fig 7 — STAY driver dot plot with cost-to-address tags
# =====================================================================
drivers = [  # (label, share of explained variance %, cost tag)
 ("Career growth (GRW)",          16.2, "med"),
 ("Pay fairness (PAY)",           14.1, "high"),
 ("Sustainable workload (WKL)",   11.8, "med–high"),
 ("Manager relationship (MGR)",    9.4, "med"),
 ("Recognition (REC)",             8.3, "low"),
 ("Communication & info (COM)",    6.9, "low"),
 ("Job security (SEC)",            6.1, "—"),
 ("Feedback (FDK)",                5.2, "low"),
 ("Schedule fit (FLX)",            4.8, "med"),
 ("Voice & participation (VOI)",   4.3, "low"),
 ("All remaining drivers",        12.9, ""),
]
tagcol = {"low": TEALI, "med": NAVY, "med–high": CORALI, "high": CORALI, "—": NAVY, "": NAVY}
fig, ax = plt.subplots(figsize=(7.4, 4.6))
y = np.arange(len(drivers))[::-1]
for yi, (lab, v, tag) in zip(y, drivers):
    grey = lab.startswith("All remaining")
    ax.plot([0, v], [yi, yi], color=STONE, lw=2, zorder=2)
    ax.scatter(v, yi, s=110, color=(STONE if grey else (TEAL if tag == "low" else NAVY)),
               zorder=4, edgecolor="white", linewidth=1.2)
    ax.text(v + 0.45, yi, f"{v:.1f}%", va="center", fontsize=9, color=NAVY,
            fontweight="bold" if not grey else "normal")
    if tag:
        ax.text(21.6, yi, f"cost: {tag}", va="center", fontsize=8.5, color=tagcol[tag],
                fontweight="bold" if tag == "low" else "normal")
ax.set_yticks(y, [d[0] for d in drivers], fontsize=9.5)
ax.set_xlim(0, 25.5)
ax.set_xlabel("Share of explained variance in intent to stay (Shapley decomposition, %)")
leg = ax.scatter([], [], s=110, color=TEAL, edgecolor="white")
ax.legend([leg], ["low-cost lever"], loc="lower right", frameon=False, fontsize=9)
style_ax(ax, xgrid=True)
save(fig, "fig7_stay_drivers")

# =====================================================================
# Fig 8 — stated vs derived importance (slope chart, top 10)
# =====================================================================
# stated rank from GAP importance means; derived rank from Shapley shares
stated  = ["PAY", "SAF", "SEC", "BEN", "WKL", "MGR", "GRW", "FLX", "COM", "REC"]
derived = ["GRW", "PAY", "WKL", "MGR", "REC", "COM", "SEC", "FDK", "FLX", "VOI"]
names = {c: gap[c][2] for c in gap}
fig, ax = plt.subplots(figsize=(7.0, 4.8))
n = 10
for c in set(stated) | set(derived):
    sr = stated.index(c) + 1 if c in stated else None
    dr = derived.index(c) + 1 if c in derived else None
    if sr and dr:
        moved_up = sr - dr >= 3
        col = CORALI if (c in ("GRW", "SEC")) else (TEAL if abs(sr - dr) <= 1 else NAVY)
        ax.plot([0, 1], [n + 1 - sr, n + 1 - dr], color=col, lw=2 if c in ("GRW", "SEC") else 1.2,
                alpha=0.9 if c in ("GRW", "SEC") else 0.55, zorder=3)
        ax.scatter([0, 1], [n + 1 - sr, n + 1 - dr], color=col, s=32, zorder=4)
    elif sr:
        ax.scatter([0], [n + 1 - sr], color=STONE, s=32, zorder=4)
    elif dr:
        ax.scatter([1], [n + 1 - dr], color=STONE, s=32, zorder=4)
for i, c in enumerate(stated):
    ax.text(-0.05, n - i, f"{i+1}. {names[c]}", ha="right", va="center", fontsize=9,
            color=CORALI if c in ("GRW", "SEC") else NAVY,
            fontweight="bold" if c in ("GRW", "SEC") else "normal")
for i, c in enumerate(derived):
    ax.text(1.05, n - i, f"{i+1}. {names[c]}", ha="left", va="center", fontsize=9,
            color=CORALI if c in ("GRW", "SEC") else NAVY,
            fontweight="bold" if c in ("GRW", "SEC") else "normal")
ax.text(0, n + 1.1, "STATED\n(what employees say matters)", ha="right", fontsize=9.5,
        fontweight="bold", color=NAVY, ma="right")
ax.text(1, n + 1.1, "DERIVED\n(what predicts staying)", ha="left", fontsize=9.5,
        fontweight="bold", color=NAVY)
ax.set_xlim(-1.35, 2.35); ax.set_ylim(0.4, n + 2.1)
ax.axis("off")
save(fig, "fig8_stated_derived")

# =====================================================================
# Fig 9 — OPEN: theme frequency by promoter class
# =====================================================================
themes = ["Pay & compensation", "Staffing levels / workload", "Career paths & promotion",
          "Communication from leadership", "Equipment & tooling", "Recognition",
          "Schedule predictability", "Keep: team culture", "Keep: safety practices"]
det_f  = [34, 29, 24, 21, 14, 12, 11, 8, 6]
prom_f = [15, 12, 14, 9, 8, 7, 6, 41, 22]
fig, ax = plt.subplots(figsize=(7.4, 4.0))
y = np.arange(len(themes))[::-1]
ax.barh(y + 0.19, det_f, height=0.36, color=CORAL, label="Detractors (n=306)", zorder=3)
ax.barh(y - 0.19, prom_f, height=0.36, color=TEAL, label="Promoters (n=276)", zorder=3)
for yi, (d, p) in zip(y, zip(det_f, prom_f)):
    ax.text(d + 0.6, yi + 0.19, f"{d}%", va="center", fontsize=8, color=CORALI)
    ax.text(p + 0.6, yi - 0.19, f"{p}%", va="center", fontsize=8, color=TEALI)
ax.set_yticks(y, themes, fontsize=9)
ax.set_xlim(0, 48)
ax.set_xlabel("% of open-ended responses mentioning theme (multi-code)")
ax.legend(loc="lower right", frameon=False, fontsize=9)
style_ax(ax, xgrid=True)
save(fig, "fig9_open_themes")

print("ALL FIGURES DONE")
