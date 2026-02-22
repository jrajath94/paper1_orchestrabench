#!/usr/bin/env python3
"""
Figure 1: DIT Task Space
Scatter plot of all 82 tasks in the D-I plane, with marker size proportional to T.
Color by category, topology priors shown as stars.
"""
import json
import os
import numpy as np

# Robust style setup
try:
    import scienceplots
    import matplotlib.pyplot as plt
    plt.style.use(['science', 'ieee'])
except Exception:
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 10,
        'axes.linewidth': 0.8,
        'xtick.direction': 'in',
        'ytick.direction': 'in',
    })

# Force non-interactive backend for PDF generation
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

# Disable LaTeX if it causes issues, fall back to mathtext
plt.rcParams['text.usetex'] = False
plt.rcParams['font.size'] = 10

BASE = '/Users/rj/eb-paper-claude/paper/experiments'

# Load all tasks
with open(os.path.join(BASE, 'pilot_tasks.json')) as f:
    pilot = json.load(f)
with open(os.path.join(BASE, 'scaled_tasks.json')) as f:
    scaled = json.load(f)
with open(os.path.join(BASE, 'extended_tasks.json')) as f:
    extended = json.load(f)

# Parse tasks into arrays
tasks = []
for t in pilot['tasks']:
    cat = t['category']
    if cat == 'multi-domain':
        cat = 'research'
    tasks.append({
        'D': t['D'], 'I': t['I'], 'T': t['T'],
        'category': cat, 'difficulty': 'easy', 'id': t['task_id']
    })

for t in scaled['tasks']:
    cat = t['category']
    if cat == 'multi-domain':
        cat = 'research'
    tasks.append({
        'D': t['dit']['D'], 'I': t['dit']['I'], 'T': t['dit']['T'],
        'category': cat, 'difficulty': 'hard', 'id': t['task_id']
    })

for t in extended['tasks']:
    cat = t['category']
    if cat == 'multi-domain':
        cat = 'research'
    tasks.append({
        'D': t['dit']['D'], 'I': t['dit']['I'], 'T': t['dit']['T'],
        'category': cat, 'difficulty': 'hard', 'id': t['task_id']
    })

# Colorblind-safe colors
cat_colors = {
    'coding': '#0077BB',     # blue
    'research': '#EE7733',   # orange
    'reasoning': '#009988',  # teal/green
}
cat_markers = {
    'coding': 'o',
    'research': 's',
    'reasoning': '^',
}
cat_hatches = {
    'coding': None,
    'research': None,
    'reasoning': None,
}

fig, ax = plt.subplots(figsize=(6.5, 4.5))

# Plot tasks by category
for cat in ['coding', 'research', 'reasoning']:
    cat_tasks = [t for t in tasks if t['category'] == cat]
    D_vals = [t['D'] for t in cat_tasks]
    I_vals = [t['I'] for t in cat_tasks]
    T_vals = [t['T'] for t in cat_tasks]
    # Size proportional to T (scale for visibility)
    sizes = [20 + 25 * t for t in T_vals]

    ax.scatter(D_vals, I_vals, s=sizes, c=cat_colors[cat],
               marker=cat_markers[cat], alpha=0.7,
               edgecolors='black', linewidths=0.4,
               label=f'{cat.capitalize()} (n={len(cat_tasks)})', zorder=3)

# Topology priors as stars
topo_priors = {
    'Flat':  (0.2, 0.8),
    'Hier':  (0.8, 0.2),
    'Debate': (0.3, 0.7),
}
topo_colors_stars = {
    'Flat': '#CC3311',     # red
    'Hier': '#33BBEE',     # cyan
    'Debate': '#EE3377',   # magenta
}

for name, (d, i) in topo_priors.items():
    ax.scatter(d, i, s=200, c=topo_colors_stars[name], marker='*',
               edgecolors='black', linewidths=0.8, zorder=5)
    # Offset labels to avoid overlap with data points
    offsets = {'Flat': (-0.12, 0.05), 'Hier': (0.08, -0.07), 'Debate': (-0.12, -0.03)}
    haligns = {'Flat': 'center', 'Hier': 'center', 'Debate': 'center'}
    dx, dy = offsets[name]
    ax.annotate(name, (d, i), xytext=(d + dx, i + dy),
                fontsize=9, fontweight='bold', color=topo_colors_stars[name],
                ha=haligns[name], va='bottom', zorder=6,
                arrowprops=dict(arrowstyle='->', color=topo_colors_stars[name],
                                lw=0.8, alpha=0.6))

# Add a few example alignment dashed lines (from illustrative tasks to nearest topology)
# Pick 3 representative tasks
example_tasks = [
    ('H01', 0.95, 0.15, 'Hier'),   # high-D coding -> Hier
    ('H09', 0.25, 0.84, 'Debate'), # high-I reasoning -> Debate
    ('E01', 0.3, 0.1, 'Flat'),     # easy coding -> low complexity
]
for tid, d, i, topo in example_tasks:
    td, ti = topo_priors[topo]
    ax.plot([d, td], [i, ti], 'k--', alpha=0.3, linewidth=0.8, zorder=2)

# Size legend
for tval, label in [(1, 'T=1'), (3, 'T=3'), (5, 'T=5')]:
    ax.scatter([], [], s=20 + 25 * tval, c='gray', alpha=0.5,
               edgecolors='black', linewidths=0.4, label=label)

ax.set_xlabel('Decomposability (D)', fontsize=11)
ax.set_ylabel('Iterativeness (I)', fontsize=11)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)

# Light grid
ax.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Legend
legend = ax.legend(loc='lower right', fontsize=8, framealpha=0.9,
                   edgecolor='gray', ncol=2,
                   columnspacing=1.0, handletextpad=0.5)

# Quadrant annotations
ax.text(0.85, 0.85, 'High D + I\n(hardest)', fontsize=7, ha='center',
        va='center', alpha=0.4, style='italic')
ax.text(0.15, 0.15, 'Low D + I\n(easiest)', fontsize=7, ha='center',
        va='center', alpha=0.4, style='italic')

plt.tight_layout()

OUT = '/Users/rj/eb-paper-claude/paper/output/figures'
fig.savefig(os.path.join(OUT, 'fig1_dit_space.pdf'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(OUT, 'fig1_dit_space.png'), bbox_inches='tight', dpi=300)
print(f"Saved fig1_dit_space to {OUT}")
plt.close()
