#!/usr/bin/env python3
"""
Figure 5: Agent-Count Control Experiment
Bar chart comparing: Flat-baseline (20%), Flat-2x-budget (35%), Multi-agent best (65%)
Annotated decomposition: 15pp from compute, 30pp from structure.

Data from flat_2x_budget.json (actual experiment results).
"""
import json
import os
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

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

BASE = '/Users/rj/eb-paper-claude/paper/experiments'

# Load actual data
with open(os.path.join(BASE, 'results/flat_2x_budget.json')) as f:
    control = json.load(f)

flat_baseline_acc = control['comparison']['flat_baseline']['accuracy'] * 100  # 20%
flat_2x_acc = control['comparison']['flat_2x_budget']['accuracy'] * 100      # 35%
hier_acc = control['comparison']['hierarchical']['accuracy'] * 100            # 65%
debate_acc = control['comparison']['debate']['accuracy'] * 100                # 65%

# Best multi-agent = max(hier, debate)
multi_agent_acc = max(hier_acc, debate_acc)

# Tokens per task
flat_tokens = control['comparison']['flat_baseline']['tokens_per_task']
flat_2x_tokens = control['comparison']['flat_2x_budget']['tokens_per_task']
hier_tokens = control['comparison']['hierarchical']['tokens_per_task']
debate_tokens = control['comparison']['debate']['tokens_per_task']

print(f"Flat baseline: {flat_baseline_acc:.0f}% ({flat_tokens} tok/task)")
print(f"Flat 2x:       {flat_2x_acc:.0f}% ({flat_2x_tokens} tok/task)")
print(f"Hierarchical:  {hier_acc:.0f}% ({hier_tokens} tok/task)")
print(f"Debate:        {debate_acc:.0f}% ({debate_tokens} tok/task)")
print(f"Multi-agent:   {multi_agent_acc:.0f}%")

# Decomposition
compute_pp = flat_2x_acc - flat_baseline_acc    # 15pp
structure_pp = multi_agent_acc - flat_2x_acc     # 30pp
total_pp = multi_agent_acc - flat_baseline_acc   # 45pp

print(f"\nDecomposition:")
print(f"  Compute contribution:   +{compute_pp:.0f}pp ({compute_pp/total_pp*100:.0f}% of total)")
print(f"  Structure contribution: +{structure_pp:.0f}pp ({structure_pp/total_pp*100:.0f}% of total)")

# ------- Plot -------
fig, ax = plt.subplots(figsize=(6.5, 4.0))

conditions = ['Flat\n(baseline)', 'Flat\n(2x budget)', 'Multi-agent\n(best)']
values = [flat_baseline_acc, flat_2x_acc, multi_agent_acc]
token_labels = [f'~{flat_tokens:,} tok', f'~{flat_2x_tokens:,} tok', f'~{max(hier_tokens,debate_tokens):,} tok']

# Colors and hatching
colors = ['#0077BB', '#77AADD', '#EE7733']
hatches = ['', '//', '\\\\']

x = np.arange(3)
bars = ax.bar(x, values, width=0.55,
              color=colors, edgecolor='black', linewidth=0.6,
              hatch=hatches, zorder=3)

# Value labels
for i, (bar, val, tok) in enumerate(zip(bars, values, token_labels)):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5,
            f'{val:.0f}%', ha='center', va='bottom',
            fontsize=11, fontweight='bold')
    # Token budget label below bars
    ax.text(bar.get_x() + bar.get_width() / 2, -4.5,
            tok, ha='center', va='top', fontsize=7.5, alpha=0.6)

# Bracket annotations for decomposition
bracket_y = 72

# Compute contribution arrow (bar 0 -> bar 1)
ax.annotate('', xy=(1, flat_2x_acc + 3), xytext=(0, flat_baseline_acc + 3),
            arrowprops=dict(arrowstyle='<->', color='#009988', lw=1.5))
mid_x_compute = 0.5
mid_y_compute = (flat_baseline_acc + flat_2x_acc) / 2 + 3
ax.text(mid_x_compute, mid_y_compute + 4,
        f'+{compute_pp:.0f}pp\ncompute', ha='center', va='bottom',
        fontsize=8, color='#009988', fontweight='bold')

# Structure contribution arrow (bar 1 -> bar 2)
ax.annotate('', xy=(2, multi_agent_acc + 3), xytext=(1, flat_2x_acc + 3),
            arrowprops=dict(arrowstyle='<->', color='#CC3311', lw=1.5))
mid_x_struct = 1.5
mid_y_struct = (flat_2x_acc + multi_agent_acc) / 2 + 3
ax.text(mid_x_struct, mid_y_struct + 4,
        f'+{structure_pp:.0f}pp\nstructure', ha='center', va='bottom',
        fontsize=8, color='#CC3311', fontweight='bold')

# Summary box
summary_text = (f'Total advantage: +{total_pp:.0f}pp\n'
                f'Compute: {compute_pp/total_pp*100:.0f}%  |  Structure: {structure_pp/total_pp*100:.0f}%')
ax.text(0.98, 0.95, summary_text,
        transform=ax.transAxes, fontsize=8,
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                  edgecolor='gray', alpha=0.9))

ax.set_ylabel('Accuracy (%)', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(conditions, fontsize=9.5)
ax.set_ylim(-8, 95)
ax.set_yticks([0, 20, 40, 60, 80])

ax.grid(axis='y', alpha=0.2, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Subtitle
ax.set_xlabel('Agent Configuration (20-task subset)', fontsize=10)

plt.tight_layout()

OUT = '/Users/rj/eb-paper-claude/paper/output/figures'
fig.savefig(os.path.join(OUT, 'fig5_agent_control.pdf'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(OUT, 'fig5_agent_control.png'), bbox_inches='tight', dpi=300)
print(f"\nSaved fig5_agent_control to {OUT}")
plt.close()
