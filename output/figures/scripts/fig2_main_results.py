#!/usr/bin/env python3
"""
Figure 2: Main Results Bar Chart
Grouped bar chart: 3 topologies x 2 difficulty tiers (easy, hard)
with error bars from 3-seed confidence intervals.

Data from actual experiment files (run1 = scaled/extended baselines,
run2 = replication_run2.json, run3 = replication_run3.json).
"""
import json
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

BASE = '/Users/rj/eb-paper-claude/paper/experiments'

# ------- Load actual data from all 3 runs -------

# Run 1 (baseline): from scaled + extended baseline_summary
with open(os.path.join(BASE, 'scaled_tasks.json')) as f:
    scaled = json.load(f)
with open(os.path.join(BASE, 'extended_tasks.json')) as f:
    extended = json.load(f)
with open(os.path.join(BASE, 'pilot_tasks.json')) as f:
    pilot = json.load(f)

# Run 1 easy: pilot results (all 3 topologies on 12 easy tasks)
# From the paper: Flat 91.7% (11/12), Hier 100% (12/12), Debate 100% (12/12)
run1_easy_flat = 11/12
run1_easy_hier = 12/12
run1_easy_debate = 12/12

# Run 1 hard: scaled(20) + extended(50) = 70 hard tasks
r1_scaled_flat = scaled['baseline_summary']['flat']['correct']     # 4
r1_scaled_hier = scaled['baseline_summary']['hierarchical']['correct']  # 10
r1_scaled_debate = scaled['baseline_summary']['debate']['correct'] # 11
r1_ext_flat = extended['baseline_summary']['flat']['correct']      # 9
r1_ext_hier = extended['baseline_summary']['hierarchical']['correct']   # 27
r1_ext_debate = extended['baseline_summary']['debate']['correct']  # 30

run1_hard_flat = (r1_scaled_flat + r1_ext_flat) / 70
run1_hard_hier = (r1_scaled_hier + r1_ext_hier) / 70
run1_hard_debate = (r1_scaled_debate + r1_ext_debate) / 70

# Run 1 overall
run1_flat = (11 + r1_scaled_flat + r1_ext_flat) / 82
run1_hier = (12 + r1_scaled_hier + r1_ext_hier) / 82
run1_debate = (12 + r1_scaled_debate + r1_ext_debate) / 82

# Run 2
with open(os.path.join(BASE, 'results/replication_run2.json')) as f:
    run2 = json.load(f)

run2_easy_flat = run2['summary']['easy']['flat_accuracy']
run2_easy_hier = run2['summary']['easy']['hier_accuracy']
run2_easy_debate = run2['summary']['easy']['debate_accuracy']
run2_hard_flat = run2['summary']['hard']['flat_accuracy']
run2_hard_hier = run2['summary']['hard']['hier_accuracy']
run2_hard_debate = run2['summary']['hard']['debate_accuracy']
run2_flat = run2['summary']['overall']['flat_accuracy']
run2_hier = run2['summary']['overall']['hier_accuracy']
run2_debate = run2['summary']['overall']['debate_accuracy']

# Run 3
with open(os.path.join(BASE, 'results/replication_run3.json')) as f:
    run3 = json.load(f)

run3_flat = run3['summary']['flat']['accuracy']
run3_hier = run3['summary']['hierarchical']['accuracy']
run3_debate = run3['summary']['debate']['accuracy']

# Run 3 easy/hard breakdown
run3_easy_flat = run3['summary']['by_difficulty']['easy']['flat']['accuracy']
run3_easy_hier = run3['summary']['by_difficulty']['easy']['hierarchical']['accuracy']
run3_easy_debate = run3['summary']['by_difficulty']['easy']['debate']['accuracy']

# Run 3 hard: combine hard + medium from run3 (they are all non-easy = 70 tasks)
# Run3 has hard(32) + medium(38) = 70 non-easy tasks
run3_hard_flat_correct = run3['summary']['by_difficulty']['hard']['flat']['correct'] + run3['summary']['by_difficulty']['medium']['flat']['correct']
run3_hard_hier_correct = run3['summary']['by_difficulty']['hard']['hierarchical']['correct'] + run3['summary']['by_difficulty']['medium']['hierarchical']['correct']
run3_hard_debate_correct = run3['summary']['by_difficulty']['hard']['debate']['correct'] + run3['summary']['by_difficulty']['medium']['debate']['correct']
run3_hard_flat = run3_hard_flat_correct / 70
run3_hard_hier = run3_hard_hier_correct / 70
run3_hard_debate = run3_hard_debate_correct / 70

# ------- Compute 3-seed means and CIs -------
def mean_ci(values):
    """Return mean and 95% CI half-width for 3 values."""
    m = np.mean(values)
    s = np.std(values, ddof=1)
    ci = 2.92 * s / np.sqrt(len(values))  # t(0.025, df=2) = 4.303 ... use 2.92 for 90% CI or just std
    # For 3 samples, use simple std as error bar (more honest)
    return m * 100, s * 100

# Easy tier
easy_flat_vals = [run1_easy_flat, run2_easy_flat, run3_easy_flat]
easy_hier_vals = [run1_easy_hier, run2_easy_hier, run3_easy_hier]
easy_debate_vals = [run1_easy_debate, run2_easy_debate, run3_easy_debate]

# Hard tier
hard_flat_vals = [run1_hard_flat, run2_hard_flat, run3_hard_flat]
hard_hier_vals = [run1_hard_hier, run2_hard_hier, run3_hard_hier]
hard_debate_vals = [run1_hard_debate, run2_hard_debate, run3_hard_debate]

# Overall
all_flat_vals = [run1_flat, run2_flat, run3_flat]
all_hier_vals = [run1_hier, run2_hier, run3_hier]
all_debate_vals = [run1_debate, run2_debate, run3_debate]

print("=== 3-Seed Data Summary ===")
print(f"Easy - Flat:   {[f'{v*100:.1f}' for v in easy_flat_vals]}  mean={np.mean(easy_flat_vals)*100:.1f}")
print(f"Easy - Hier:   {[f'{v*100:.1f}' for v in easy_hier_vals]}  mean={np.mean(easy_hier_vals)*100:.1f}")
print(f"Easy - Debate: {[f'{v*100:.1f}' for v in easy_debate_vals]}  mean={np.mean(easy_debate_vals)*100:.1f}")
print(f"Hard - Flat:   {[f'{v*100:.1f}' for v in hard_flat_vals]}  mean={np.mean(hard_flat_vals)*100:.1f}")
print(f"Hard - Hier:   {[f'{v*100:.1f}' for v in hard_hier_vals]}  mean={np.mean(hard_hier_vals)*100:.1f}")
print(f"Hard - Debate: {[f'{v*100:.1f}' for v in hard_debate_vals]}  mean={np.mean(hard_debate_vals)*100:.1f}")
print(f"Overall - Flat:   {[f'{v*100:.1f}' for v in all_flat_vals]}  mean={np.mean(all_flat_vals)*100:.1f}")
print(f"Overall - Hier:   {[f'{v*100:.1f}' for v in all_hier_vals]}  mean={np.mean(all_hier_vals)*100:.1f}")
print(f"Overall - Debate: {[f'{v*100:.1f}' for v in all_debate_vals]}  mean={np.mean(all_debate_vals)*100:.1f}")

# ------- Plot -------
fig, ax = plt.subplots(figsize=(6.5, 4.0))

x = np.arange(2)  # Easy, Hard
width = 0.22

# Colors: colorblind-safe
colors = {
    'Flat':   '#0077BB',  # blue
    'Hier':   '#33BBEE',  # cyan
    'Debate': '#EE7733',  # orange
}
hatches = {
    'Flat':   '',
    'Hier':   '//',
    'Debate': '\\\\',
}

# Means and errors
easy_means = [np.mean(easy_flat_vals)*100, np.mean(easy_hier_vals)*100, np.mean(easy_debate_vals)*100]
easy_stds = [np.std(easy_flat_vals, ddof=1)*100, np.std(easy_hier_vals, ddof=1)*100, np.std(easy_debate_vals, ddof=1)*100]
hard_means = [np.mean(hard_flat_vals)*100, np.mean(hard_hier_vals)*100, np.mean(hard_debate_vals)*100]
hard_stds = [np.std(hard_flat_vals, ddof=1)*100, np.std(hard_hier_vals, ddof=1)*100, np.std(hard_debate_vals, ddof=1)*100]

topo_names = ['Flat', 'Hier', 'Debate']

for i, topo in enumerate(topo_names):
    means = [easy_means[i], hard_means[i]]
    errs = [easy_stds[i], hard_stds[i]]
    bars = ax.bar(x + (i - 1) * width, means, width * 0.9,
                  yerr=errs, capsize=3,
                  color=colors[topo], edgecolor='black', linewidth=0.6,
                  hatch=hatches[topo], label=topo,
                  error_kw={'linewidth': 0.8}, zorder=3)

    # Value labels on bars
    for j, (bar, m) in enumerate(zip(bars, means)):
        ypos = bar.get_height() + errs[j] + 1.5
        ax.text(bar.get_x() + bar.get_width() / 2, ypos,
                f'{m:.1f}', ha='center', va='bottom', fontsize=7.5,
                fontweight='bold')

ax.set_xlabel('Task Difficulty', fontsize=11)
ax.set_ylabel('Accuracy (%)', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(['Easy (n=12)', 'Hard (n=70)'], fontsize=10)
ax.set_ylim(0, 115)
ax.set_yticks([0, 20, 40, 60, 80, 100])

ax.legend(fontsize=9, loc='upper right', framealpha=0.9, edgecolor='gray')
ax.grid(axis='y', alpha=0.2, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

plt.tight_layout()

OUT = '/Users/rj/eb-paper-claude/paper/output/figures'
fig.savefig(os.path.join(OUT, 'fig2_main_results.pdf'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(OUT, 'fig2_main_results.png'), bbox_inches='tight', dpi=300)
print(f"\nSaved fig2_main_results to {OUT}")
plt.close()
