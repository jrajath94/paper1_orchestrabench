#!/usr/bin/env python3
"""
Figure 4: DIT Routing Accuracy Ablation
Bar chart showing routing accuracy by DIT feature subset.
Horizontal dashed line at 33% (random baseline).

Feature importance ablation: which DIT dimensions matter most for routing.
Values from the paper's routing accuracy analysis across the 82-task benchmark.
"""
import os
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

try:
    import scienceplots
    plt.style.use(['science', 'ieee'])
except Exception:
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 10,
        'axes.linewidth': 0.8,
    })

plt.rcParams['text.usetex'] = False
plt.rcParams['font.size'] = 10

# ------- Data: Routing accuracy by feature subset -------
# These values represent how accurately the DIT framework can route
# tasks to the optimal topology using subsets of the DIT features.
# Computed as leave-one-out oracle routing accuracy on the 82-task benchmark.
feature_subsets = {
    'D only':   69.5,
    'I only':   56.1,
    'T only':   41.5,
    'D+I':      82.9,
    'D+T':      74.4,
    'I+T':      61.0,
    'D+I+T':    90.2,
}

labels = list(feature_subsets.keys())
values = list(feature_subsets.values())
random_baseline = 33.3

# Color gradient: darker = more features
n = len(labels)
# Use a sequential colorblind-safe palette
cmap_colors = ['#BBBBBB', '#BBBBBB', '#BBBBBB',  # singles: gray
               '#77AADD', '#77AADD', '#77AADD',   # pairs: light blue
               '#0077BB']                           # full: dark blue

# Hatching to distinguish in grayscale
hatch_list = ['', '//', '\\\\',   # singles
              '', '//', '\\\\',    # pairs
              'xx']                 # full

fig, ax = plt.subplots(figsize=(6.5, 3.8))

bars = ax.bar(np.arange(n), values, width=0.65,
              color=cmap_colors, edgecolor='black', linewidth=0.6,
              hatch=hatch_list, zorder=3)

# Random baseline
ax.axhline(y=random_baseline, color='#CC3311', linestyle='--',
           linewidth=1.2, label='Random baseline (33.3%)', zorder=2)

# Value labels on bars
for i, (bar, val) in enumerate(zip(bars, values)):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 1.2,
            f'{val:.1f}%', ha='center', va='bottom',
            fontsize=8.5, fontweight='bold')

# Feature group brackets (positioned via axes transform to avoid overlap with xlabel)
ax.text(1, -7, 'Single features', ha='center', fontsize=7.5, alpha=0.5, style='italic')
ax.text(4, -7, 'Feature pairs', ha='center', fontsize=7.5, alpha=0.5, style='italic')
ax.text(6, -7, 'All', ha='center', fontsize=7.5, alpha=0.5, style='italic')

# Separator lines between groups
ax.axvline(x=2.5, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
ax.axvline(x=5.5, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)

ax.set_xlabel('DIT Feature Subset', fontsize=11)
ax.set_ylabel('Routing Accuracy (%)', fontsize=11)
ax.set_xticks(np.arange(n))
ax.set_xticklabels(labels, fontsize=9, rotation=0)
ax.set_ylim(0, 105)
ax.set_yticks([0, 20, 40, 60, 80, 100])

ax.legend(fontsize=9, loc='upper left', framealpha=0.9, edgecolor='gray')
ax.grid(axis='y', alpha=0.2, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Annotate key insight
ax.annotate('D is the most\ninformative\nsingle feature',
            xy=(0, 69.5), xytext=(0.8, 85),
            fontsize=7.5, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=0.8),
            alpha=0.7)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

OUT = '/Users/rj/eb-paper-claude/paper/output/figures'
fig.savefig(os.path.join(OUT, 'fig4_routing_ablation.pdf'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(OUT, 'fig4_routing_ablation.png'), bbox_inches='tight', dpi=300)
print(f"Saved fig4_routing_ablation to {OUT}")
plt.close()
