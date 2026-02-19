import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Data organized by category
data = {
    "Contact / Grasp": [
        ("grasp_power", 7.0),
        ("grasp_precision", 6.0),
        ("reach", 5.5),
        ("release", 3.5),
        ("other", 8.0),
    ],
    "Place / Move": [
        ("lift", 6.5),
        ("place", 6.0),
        ("move", 5.5),
        ("other", 4.0),
    ],
    "Tool Use": [
        ("press", 3.5),
        ("rotate", 3.0),
        ("cut", 3.0),
        ("push", 2.5),
        ("other", 6.0),
    ],
    "Assembly": [
        ("insert", 3.0),
        ("align", 3.0),
        ("remove", 2.5),
        ("tighten", 2.0),
        ("other", 1.5),
    ],
    "Fluid": [
        ("pour", 2.5),
        ("scoop", 2.0),
        ("dump", 1.5),
        ("other", 1.0),
    ],
    "Bimanual": [
        ("two_hand_hold", 2.5),
        ("anchor_and_act", 2.0),
        ("two_hand_align", 1.5),
        ("other", 0.5),
    ],
    "Deform": [
        ("fold", 1.5),
        ("compress", 1.5),
        ("stretch", 1.0),
        ("other", 1.0),
    ],
}

# Color palettes for each category (different shades of blue)
blue_ranges = {
    "Contact / Grasp": (0.25, 0.75),
    "Place / Move": (0.30, 0.70),
    "Tool Use": (0.25, 0.75),
    "Assembly": (0.25, 0.75),
    "Fluid": (0.30, 0.70),
    "Bimanual": (0.35, 0.75),
    "Deform": (0.30, 0.70),
}
color_palettes = {
    cat: plt.cm.Blues(np.linspace(lo, hi, len(data[cat])))
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
ax.set_ylim(0, 35)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig(
    "/home/user/mahek-samples/action_primitives_histogram.png",
    dpi=150,
    bbox_inches="tight",
)
print("Saved to action_primitives_histogram.png")
