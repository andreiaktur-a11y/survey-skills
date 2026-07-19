#!/usr/bin/env python3
"""Fig. 5 rebuild — non-overlapping tenure bands (owner decision, 2026-07-19).
Bands: Less than 1 year / 1–2 years / 3–6 years / 7 years or more.
Aspect matched to the placement in the owner's layout (5.1375in x 2.39375in = 2.146)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

NAVY, TEAL, CORAL, STONE = "#0B1F3A", "#0EA5A3", "#FF6A5C", "#E2E7EB"
for f in ["fonts/Poppins-SemiBold.ttf", "fonts/Inter-Regular.ttf", "fonts/Inter-Medium.ttf"]:
    fm.fontManager.addfont(f)
plt.rcParams.update({
    "font.family": "Inter", "font.size": 10, "axes.edgecolor": STONE,
    "axes.linewidth": 0.8, "axes.labelcolor": NAVY, "text.color": NAVY,
    "xtick.color": NAVY, "ytick.color": NAVY,
    "figure.facecolor": "white", "axes.facecolor": "white",
})

bands = ["Less than 1 year\n(n=142)", "1–2 years\n(n=289)",
         "3–6 years\n(n=331)", "7 years or more\n(n=225)"]
low  = [58, 44, 38, 47]
mod  = [28, 32, 31, 31]
elev = [14, 24, 31, 22]

fig, ax = plt.subplots(figsize=(8.3, 3.05))
x = np.arange(len(bands))
ax.bar(x, low, color=TEAL, width=0.58, label="Low risk", zorder=3)
ax.bar(x, mod, bottom=low, color=STONE, width=0.58, label="Moderate", zorder=3)
ax.bar(x, elev, bottom=[l + m for l, m in zip(low, mod)], color=CORAL,
       width=0.58, label="Elevated", zorder=3)
for xi, (l, m, e) in zip(x, zip(low, mod, elev)):
    ax.text(xi, l / 2, f"{l}%", ha="center", va="center", color="white", fontsize=9, fontweight="bold")
    ax.text(xi, l + m / 2, f"{m}%", ha="center", va="center", color=NAVY, fontsize=9)
    ax.text(xi, l + m + e / 2, f"{e}%", ha="center", va="center", color="white", fontsize=9, fontweight="bold")
ax.set_xticks(x, bands)
ax.set_ylim(0, 100)
ax.set_ylabel("% of respondents")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.20), ncol=3, frameon=False, fontsize=9)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
fig.savefig("figs/fig5_brn_tiers.png", dpi=200, bbox_inches="tight", facecolor="white")
print("saved fig5")

from PIL import Image
im = Image.open("figs/fig5_brn_tiers.png")
print("px:", im.size, "aspect:", round(im.width / im.height, 4))
