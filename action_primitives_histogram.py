import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Data organized by category
data = {
    "Contact / Grasp": [
        ("reach", 6.0),
        ("touch", 5.0),
        ("grasp_power", 8.0),
        ("grasp_precision", 9.0),
        ("regrasp", 5.0),
        ("release", 4.5),
    ],
    "Place / Move": [
        ("lift", 7.0),
        ("place", 8.0),
        ("move", 6.0),
        ("slide", 4.0),
    ],
    "Tool Use": [
        ("use_tool", 4.5),
        ("cut", 3.0),
        ("rotate", 2.5),
        ("press", 2.5),
        ("scrape", 2.0),
        ("pull", 2.0),
        ("push", 2.0),
    ],
    "Assembly": [
        ("align", 2.5),
        ("insert", 2.5),
        ("remove", 2.0),
        ("tighten", 1.5),
        ("loosen", 1.0),
    ],
    "Deform": [
        ("fold", 2.5),
        ("deform", 1.5),
        ("stretch", 1.5),
        ("compress", 1.5),
    ],
    "Fluid / Granular": [
        ("pour", 2.0),
        ("scoop", 2.0),
        ("dump", 1.5),
        ("spread", 1.5),
    ],
    "Other /\nUncategorized": [
        ("—", 5.0),
    ],
}

# Color palettes for each category (different shades of blue)
blue_ranges = {
    "Contact / Grasp": (0.25, 0.75),
    "Place / Move": (0.30, 0.70),
    "Tool Use": (0.25, 0.75),
    "Assembly": (0.25, 0.75),
    "Deform": (0.30, 0.70),
    "Fluid / Granular": (0.30, 0.70),
    "Other /\nUncategorized": (0.40, 0.65),
}
color_palettes = {
    cat: plt.cm.Purples(np.linspace(lo, hi, len(data[cat])))
    for cat, (lo, hi) in blue_ranges.items()
}

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.85
x_positions = np.arange(len(data))
cat_names = list(data.keys())

for i, cat in enumerate(cat_names):
    sub_items = data[cat]
    colors = color_palettes[cat]
    bottom = 0.0

    for j, (sub_name, pct) in enumerate(reversed(sub_items)):
        color_idx = len(sub_items) - 1 - j
        bar = ax.bar(
            x_positions[i],
            pct,
            bar_width,
            bottom=bottom,
            color=colors[color_idx],
            edgecolor="white",
            linewidth=0.5,
        )

        # Add label inside the bar segment
        mid_y = bottom + pct / 2
        label = f"{sub_name} {pct}%"
        ax.text(
            x_positions[i],
            mid_y,
            label,
            ha="center",
            va="center",
            fontsize=8.5,
            fontweight="bold",
            color="black",
            clip_on=True,
        )

        bottom += pct

    # Add total percentage on top of each bar
    total = sum(p for _, p in sub_items)
    ax.text(
        x_positions[i],
        bottom + 0.5,
        f"{total:.1f}%",
        ha="center",
        va="bottom",
        fontsize=11.5,
        fontweight="bold",
        color="#333333",
    )

ax.set_xticks(x_positions)
ax.set_xticklabels(cat_names, fontsize=10.5, fontweight="bold")
ax.set_ylabel("")
ax.set_title(
    "Distribution of Action-Interaction Primitives",
    fontsize=17.5,
    fontweight="bold",
    pad=15,
)
ax.tick_params(axis="y", labelsize=10.5)
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.set_ylim(0, 42)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig(
    "/home/user/mahek-samples/action_primitives_histogram.png",
    dpi=150,
    bbox_inches="tight",
)
print("Saved to action_primitives_histogram.png")
