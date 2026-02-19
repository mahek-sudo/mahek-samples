import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Data organized by environment
data = {
    "indoor_home": [
        ("Kitchen", 11.2),
        ("Living room", 10.0),
        ("Bedroom", 8.0),
        ("Garage", 4.8),
        ("Other", 6.0),
    ],
    "indoor_public": [
        ("Retail", 5.9),
        ("Office", 5.9),
        ("Warehouse", 4.4),
        ("Restaurant", 3.9),
        ("Other", 4.5),
    ],
    "outdoor_nature": [
        ("Garden", 4.1),
        ("Farm", 3.4),
        ("Trail", 2.4),
        ("Other", 3.7),
    ],
    "factory": [
        ("Assembly line", 2.7),
        ("Packaging", 2.2),
        ("Machine shop", 1.8),
        ("Other", 2.4),
    ],
    "outdoor_urban": [
        ("Street Infra", 2.9),
        ("Construction Site", 2.6),
        ("Other", 1.8),
    ],
    "vehicle": [
        ("Car cabin", 2.4),
        ("Other", 1.3),
    ],
    "other": [
        ("\u2014", 1.8),
    ],
}

# Color palettes for each environment (different shades of blue)
blue_ranges = {
    "indoor_home": (0.25, 0.75),
    "indoor_public": (0.30, 0.70),
    "outdoor_nature": (0.35, 0.75),
    "factory": (0.30, 0.70),
    "outdoor_urban": (0.35, 0.75),
    "vehicle": (0.40, 0.70),
    "other": (0.45, 0.55),
}
color_palettes = {
    env: plt.cm.Blues(np.linspace(lo, hi, len(data[env])))
    for env, (lo, hi) in blue_ranges.items()
}

fig, ax = plt.subplots(figsize=(14, 8))

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
            fontsize=9,
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
        fontsize=12,
        fontweight="bold",
        color="#333333",
    )

ax.set_xticks(x_positions)
ax.set_xticklabels(env_names, fontsize=12, fontweight="bold")
ax.set_ylabel("Percentage (%)", fontsize=14)
ax.set_title("Stake Distribution by Environment", fontsize=18, fontweight="bold", pad=15)
ax.tick_params(axis="y", labelsize=11)
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.set_ylim(0, 45)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("/home/user/mahek-samples/stake_histogram.png", dpi=150, bbox_inches="tight")
print("Saved to stake_histogram.png")
