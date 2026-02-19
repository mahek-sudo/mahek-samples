import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import squarify

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
        ("Street infra", 2.9),
        ("Construction site", 2.6),
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

# Assign a blue hue range per environment (darker = larger environment)
env_order = list(data.keys())
env_totals = {env: sum(p for _, p in subs) for env, subs in data.items()}

# Blue shade centers for each environment (spread across the blue spectrum)
blue_centers = {
    "indoor_home": 0.75,
    "indoor_public": 0.60,
    "outdoor_nature": 0.50,
    "factory": 0.42,
    "outdoor_urban": 0.35,
    "vehicle": 0.28,
    "other": 0.20,
}

# Build flat lists for treemap
labels = []
sizes = []
colors = []
env_labels = []

for env in env_order:
    subs = data[env]
    center = blue_centers[env]
    n = len(subs)
    # Create shades around the center
    if n > 1:
        shade_range = min(0.12, center * 0.2)
        shades = np.linspace(center - shade_range, center + shade_range, n)
    else:
        shades = [center]

    for i, (sub_name, pct) in enumerate(subs):
        labels.append(f"{sub_name}\n{pct}%")
        sizes.append(pct)
        colors.append(plt.cm.Blues(shades[i]))
        env_labels.append(env)

fig, ax = plt.subplots(figsize=(16, 10))

# Draw treemap
rects = squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.9,
    ax=ax,
    edgecolor="white",
    linewidth=2,
    text_kwargs={"fontsize": 0},  # We'll add text manually
)

# Add text labels manually for better control
normed = squarify.normalize_sizes(sizes, 100, 100)
rects_coords = squarify.squarify(normed, 0, 0, 100, 100)

for i, r in enumerate(rects_coords):
    x = r["x"] + r["dx"] / 2
    y = r["y"] + r["dy"] / 2
    area = r["dx"] * r["dy"]

    if area > 15:
        fontsize = 9
    elif area > 8:
        fontsize = 7.5
    elif area > 4:
        fontsize = 6
    else:
        fontsize = 5

    # Use white text on darker blues, black on lighter
    shade_val = blue_centers.get(env_labels[i], 0.5)
    text_color = "white" if shade_val > 0.4 else "black"

    ax.text(
        x, y, labels[i],
        ha="center", va="center",
        fontsize=fontsize, fontweight="bold",
        color=text_color,
    )

# Add environment group label at bottom of each rect
for i, r in enumerate(rects_coords):
    x = r["x"] + r["dx"] / 2
    y = r["y"] + 0.8
    area = r["dx"] * r["dy"]
    if area > 10:
        ax.text(
            x, y, env_labels[i],
            ha="center", va="bottom",
            fontsize=5, fontstyle="italic",
            color="white", alpha=0.7,
        )

# Build legend for environments
legend_colors = {env: plt.cm.Blues(blue_centers[env]) for env in env_order}
legend_patches = [
    mpatches.Patch(
        facecolor=legend_colors[env], edgecolor="white",
        label=f"{env} ({env_totals[env]:.1f}%)"
    )
    for env in env_order
]
ax.legend(
    handles=legend_patches, loc="upper left", bbox_to_anchor=(1.01, 1),
    fontsize=9, frameon=False, title="Environment", title_fontsize=10,
)

ax.set_title(
    "Stake Distribution by Environment — Treemap",
    fontsize=16, fontweight="bold", pad=15,
)
ax.axis("off")

plt.tight_layout()
plt.savefig(
    "/home/user/mahek-samples/stake_treemap.png",
    dpi=150, bbox_inches="tight",
)
print("Saved to stake_treemap.png")
