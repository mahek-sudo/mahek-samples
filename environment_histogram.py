import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Data organized by environment
data = {
    "Indoor Home": [
        ("Kitchen", 14.0),
        ("Living Room", 10.0),
        ("Bedroom", 7.5),
        ("Garage", 4.0),
        ("Other", 5.0),
    ],
    "Indoor Public": [
        ("Retail", 5.0),
        ("Warehouse", 3.0),
        ("Office", 2.5),
        ("Restaurant", 2.0),
        ("Other", 1.5),
    ],
    "Outdoor Nature": [
        ("Garden", 8.5),
        ("Trail", 6.0),
        ("Farm", 3.0),
        ("Other", 3.5),
    ],
    "Outdoor Urban": [
        ("Neighborhood", 5.0),
        ("Street Infra", 4.0),
        ("Construction", 2.0),
        ("Other", 2.0),
    ],
    "Factory": [
        ("Assembly Line", 2.0),
        ("Packaging", 1.5),
        ("Machine Shop", 1.5),
        ("Other", 1.5),
    ],
    "Vehicle": [
        ("Car Cabin", 2.0),
        ("Other", 1.0),
    ],
    "Other": [
        ("Other", 2.0),
    ],
}

# Color palettes for each environment (different shades of blue)
blue_ranges = {
    "Indoor Home": (0.25, 0.75),
    "Indoor Public": (0.30, 0.70),
    "Outdoor Nature": (0.35, 0.75),
    "Outdoor Urban": (0.30, 0.70),
    "Factory": (0.30, 0.70),
    "Vehicle": (0.35, 0.70),
    "Other": (0.40, 0.65),
}
color_palettes = {
    env: plt.cm.Blues(np.linspace(lo, hi, len(data[env])))
    for env, (lo, hi) in blue_ranges.items()
}

fig, ax = plt.subplots(figsize=(18, 8))

bar_width = 0.85
x_positions = np.arange(len(data))
env_names = list(data.keys())

for i, env in enumerate(env_names):
    sub_envs = data[env]
    colors = color_palettes[env]
    bottom = 0.0

    for j, (sub_name, pct) in enumerate(reversed(sub_envs)):
        color_idx = len(sub_envs) - 1 - j
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
    total = sum(p for _, p in sub_envs)
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
ax.set_xticklabels(env_names, fontsize=11.5, fontweight="bold")
ax.set_ylabel("")
ax.set_title("Distribution of Environment Types", fontsize=17.5, fontweight="bold", pad=15)
ax.tick_params(axis="y", labelsize=10.5)
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.set_ylim(0, 45)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("/home/user/mahek-samples/environment_histogram.png", dpi=150, bbox_inches="tight")
print("Saved to environment_histogram.png")
