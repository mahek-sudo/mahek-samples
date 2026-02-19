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
        ("Workshop", 3.2),
        ("Utility room", 2.8),
    ],
    "indoor_public": [
        ("Retail", 5.9),
        ("Office", 5.9),
        ("Warehouse", 4.4),
        ("Restaurant", 3.9),
        ("Classroom", 3.0),
        ("Lab", 1.5),
    ],
    "outdoor_nature": [
        ("Garden", 4.1),
        ("Farm", 3.4),
        ("Trail", 2.4),
        ("Orchard", 1.6),
        ("Forest", 1.2),
        ("Campsite", 0.8),
    ],
    "factory": [
        ("Assembly line", 2.7),
        ("Packaging", 2.2),
        ("Machine shop", 1.8),
        ("Welding bay", 1.4),
        ("Clean room", 1.0),
    ],
    "outdoor_urban": [
        ("Street infrastructure", 2.9),
        ("Construction site", 2.6),
        ("Loading dock", 1.8),
    ],
    "vehicle": [
        ("Car cabin", 2.4),
        ("Truck cabin", 0.5),
        ("Forklift", 0.4),
        ("Crane", 0.2),
        ("Excavator", 0.2),
    ],
    "other": [
        ("\u2014", 1.8),
    ],
}

# Color palettes for each environment (light to dark shades)
color_palettes = {
    "indoor_home": plt.cm.Blues(np.linspace(0.35, 0.85, len(data["indoor_home"]))),
    "indoor_public": plt.cm.Oranges(np.linspace(0.35, 0.85, len(data["indoor_public"]))),
    "outdoor_nature": plt.cm.Greens(np.linspace(0.35, 0.85, len(data["outdoor_nature"]))),
    "factory": plt.cm.Reds(np.linspace(0.35, 0.85, len(data["factory"]))),
    "outdoor_urban": plt.cm.Purples(np.linspace(0.35, 0.85, len(data["outdoor_urban"]))),
    "vehicle": plt.cm.YlOrBr(np.linspace(0.35, 0.85, len(data["vehicle"]))),
    "other": plt.cm.Greys(np.linspace(0.45, 0.65, len(data["other"]))),
}

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.6
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

        # Add label inside the bar segment if tall enough
        mid_y = bottom + pct / 2
        if pct >= 1.5:
            ax.text(
                x_positions[i],
                mid_y,
                f"{sub_name}\n{pct}%",
                ha="center",
                va="center",
                fontsize=7,
                fontweight="bold",
                color="white" if pct >= 3.0 else "black",
            )
        elif pct >= 0.8:
            ax.text(
                x_positions[i],
                mid_y,
                f"{sub_name} {pct}%",
                ha="center",
                va="center",
                fontsize=5.5,
                color="black",
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
        fontsize=9,
        fontweight="bold",
        color="#333333",
    )

ax.set_xticks(x_positions)
ax.set_xticklabels(env_names, fontsize=10, fontweight="bold")
ax.set_ylabel("Percentage (%)", fontsize=12)
ax.set_title("Stake Distribution by Environment", fontsize=16, fontweight="bold", pad=15)
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.set_ylim(0, 45)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3, linestyle="--")

plt.tight_layout()
plt.savefig("/home/user/mahek-samples/stake_histogram.png", dpi=150, bbox_inches="tight")
print("Saved to stake_histogram.png")
