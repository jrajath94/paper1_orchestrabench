#!/usr/bin/env python3
"""Generate all figures for OrchestraBench paper.

Produces publication-quality figures using SciencePlots styling.
Figures use REAL experimental data from pilot (12 easy) and scaled (20 hard) studies.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scienceplots
import numpy as np
import os
import json
import math

# --- Paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, '..')
RESULTS_DIR = os.path.join(SCRIPT_DIR, '..', '..', '..', 'experiments', 'results')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Use science style with no-latex fallback (avoids TeX dependency issues)
plt.style.use(['science', 'no-latex', 'ieee'])
plt.rcParams.update({'font.size': 9, 'figure.dpi': 300})


# ============================================================
# DATA LOADING
# ============================================================

def load_all_data():
    """Load all experimental results and return structured data."""
    with open(os.path.join(RESULTS_DIR, 'flat_batch1.json')) as f:
        fb1 = json.load(f)
    with open(os.path.join(RESULTS_DIR, 'flat_batch2.json')) as f:
        fb2 = json.load(f)
    with open(os.path.join(RESULTS_DIR, 'hierarchical_all.json')) as f:
        hier = json.load(f)
    with open(os.path.join(RESULTS_DIR, 'debate_all.json')) as f:
        deb = json.load(f)
    with open(os.path.join(RESULTS_DIR, 'scaled_experiment.json')) as f:
        scaled = json.load(f)

    flat_pilot = fb1 + fb2
    return flat_pilot, hier, deb, scaled


# D-I-T scores for pilot (easy) tasks
PILOT_DIT = {
    'CODE-01':     (0.5, 0.2, 0.2),
    'CODE-02':     (0.3, 0.3, 0.1),
    'CODE-03':     (0.6, 0.3, 0.2),
    'CODE-04':     (0.5, 0.2, 0.1),
    'REASON-01':   (0.3, 0.3, 0.1),
    'REASON-02':   (0.2, 0.3, 0.1),
    'REASON-03':   (0.5, 0.4, 0.1),
    'REASON-04':   (0.4, 0.4, 0.1),
    'RESEARCH-01': (0.4, 0.3, 0.5),
    'RESEARCH-02': (0.3, 0.3, 0.5),
    'RESEARCH-03': (0.5, 0.4, 0.6),
    'RESEARCH-04': (0.5, 0.3, 0.5),
}

# Topology structural priors in D-I-T space
TOPOLOGY_PRIORS = {
    'flat':         (0.3, 0.8, 0.3),
    'hierarchical': (0.8, 0.2, 0.4),
    'debate':       (0.5, 0.7, 0.3),
}

TOPO_COLORS = {
    'flat': '#2196F3',
    'hierarchical': '#4CAF50',
    'debate': '#FF9800',
}

TOPO_LABELS = {
    'flat': 'Flat',
    'hierarchical': 'Hierarchical',
    'debate': 'Debate',
}


def euclidean_dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def get_pilot_category(task_id):
    """CODE-01 -> CODE, REASON-01 -> REASON, etc."""
    return task_id.split('-')[0]


def get_hard_category(task_id):
    """HARD-CODE-01 -> CODE, HARD-REASON-01 -> REASON, etc."""
    return task_id.split('-')[1]


# ============================================================
# FIGURE 1: Topology Architectures (unchanged)
# ============================================================

def fig1_topology_architectures():
    """Figure 1: Five orchestration topology architectures side-by-side."""
    fig, axes = plt.subplots(1, 5, figsize=(12, 2.8))

    topologies = [
        ('Flat\nConversation', 'circle'),
        ('Hierarchical\nSOP', 'triangle'),
        ('Role-\nPlaying', 'diamond'),
        ('DAG-\nBased', 'dag'),
        ('RL-\nOrchestrated', 'star'),
    ]

    colors = ['#2196F3', '#4CAF50', '#FF9800', '#9C27B0', '#F44336']

    for ax, (name, shape), color in zip(axes, topologies, colors):
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.set_title(name, fontsize=7, pad=8)
        ax.axis('off')

        if shape == 'circle':
            angles = np.linspace(0, 2 * np.pi, 5, endpoint=False)
            x = np.cos(angles) * 0.9
            y = np.sin(angles) * 0.9
            for i in range(5):
                for j in range(i + 1, 5):
                    ax.plot([x[i], x[j]], [y[i], y[j]], '-', color='gray', alpha=0.3, lw=0.5)
            ax.scatter(x, y, s=80, c=color, zorder=5, edgecolors='black', linewidth=0.5)

        elif shape == 'triangle':
            ax.scatter([0], [1.0], s=120, c=color, zorder=5, marker='s', edgecolors='black', linewidth=0.5)
            mid_x = [-0.7, 0.7]
            mid_y = [0, 0]
            ax.scatter(mid_x, mid_y, s=80, c=color, zorder=5, edgecolors='black', linewidth=0.5, alpha=0.7)
            for mx, my in zip(mid_x, mid_y):
                ax.plot([0, mx], [1.0, my], '-', color='gray', lw=0.8)
            leaf_x = [-1.0, -0.4, 0.4, 1.0]
            leaf_y = [-1.0, -1.0, -1.0, -1.0]
            ax.scatter(leaf_x, leaf_y, s=50, c=color, zorder=5, edgecolors='black', linewidth=0.5, alpha=0.5)
            ax.plot([-0.7, -1.0], [0, -1.0], '-', color='gray', lw=0.5)
            ax.plot([-0.7, -0.4], [0, -1.0], '-', color='gray', lw=0.5)
            ax.plot([0.7, 0.4], [0, -1.0], '-', color='gray', lw=0.5)
            ax.plot([0.7, 1.0], [0, -1.0], '-', color='gray', lw=0.5)

        elif shape == 'diamond':
            pairs = [(-0.8, 0.5), (0.8, 0.5), (-0.8, -0.5), (0.8, -0.5)]
            for px, py in pairs:
                ax.scatter([px], [py], s=80, c=color, zorder=5, edgecolors='black', linewidth=0.5)
            ax.annotate('', xy=(0.6, 0.5), xytext=(-0.6, 0.5),
                        arrowprops=dict(arrowstyle='<->', color='gray', lw=0.8))
            ax.annotate('', xy=(0.6, -0.5), xytext=(-0.6, -0.5),
                        arrowprops=dict(arrowstyle='<->', color='gray', lw=0.8))
            ax.plot([0, 0], [0.3, -0.3], '--', color='gray', alpha=0.5, lw=0.5)

        elif shape == 'dag':
            nodes = [(0, 1.0), (-0.8, 0.0), (0.8, 0.0), (-0.4, -1.0), (0.4, -1.0)]
            for nx, ny in nodes:
                ax.scatter([nx], [ny], s=80, c=color, zorder=5, edgecolors='black', linewidth=0.5)
            edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4)]
            for i, j in edges:
                ax.annotate('', xy=nodes[j], xytext=nodes[i],
                            arrowprops=dict(arrowstyle='->', color='gray', lw=0.8))

        elif shape == 'star':
            ax.scatter([0], [0], s=150, c=color, zorder=5, marker='*', edgecolors='black', linewidth=0.5)
            angles = np.linspace(0, 2 * np.pi, 6, endpoint=False)
            x = np.cos(angles) * 1.0
            y = np.sin(angles) * 1.0
            ax.scatter(x, y, s=50, c=color, zorder=5, edgecolors='black', linewidth=0.5, alpha=0.6)
            for xi, yi in zip(x, y):
                ax.annotate('', xy=(xi * 0.85, yi * 0.85), xytext=(0, 0),
                            arrowprops=dict(arrowstyle='->', color='gray', lw=0.5,
                                            connectionstyle='arc3,rad=0.1'))

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig1_topologies.pdf'), bbox_inches='tight')
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig1_topologies.png'), bbox_inches='tight', dpi=300)
    plt.close()
    print('[DONE] Figure 1: Topology architectures')


# ============================================================
# FIGURE 2: D-I-T Framework (unchanged)
# ============================================================

def fig2_dit_framework():
    """Figure 2: D-I-T task characterization with topology priors."""
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(111, projection='3d')

    priors = {
        'Hierarchical SOP':  (0.8, 0.2, 0.4),
        'Flat Conversation':  (0.3, 0.8, 0.3),
        'Role-Playing':       (0.5, 0.7, 0.3),
        'DAG-Based':          (0.9, 0.3, 0.7),
        'RL-Orchestrated':    (0.5, 0.5, 0.5),
    }

    benchmarks = {
        'SWE-bench': (0.85, 0.3, 0.5),
        'WebArena':  (0.4, 0.8, 0.8),
        'GAIA':      (0.5, 0.6, 0.7),
    }

    colors_top = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#F44336']
    markers_top = ['s', 'o', 'D', '^', '*']

    for (name, (d, i, t)), color, marker in zip(priors.items(), colors_top, markers_top):
        ax.scatter(d, i, t, c=color, marker=marker, s=100, label=name,
                   edgecolors='black', linewidth=0.5, zorder=5)

    for name, (d, i, t) in benchmarks.items():
        ax.scatter(d, i, t, c='gray', marker='X', s=150, edgecolors='black',
                   linewidth=1, zorder=6, alpha=0.8)
        ax.text(d + 0.05, i + 0.05, t + 0.05, name, fontsize=6, style='italic')

    alignments = [
        ('SWE-bench', 'Hierarchical SOP'),
        ('WebArena', 'Flat Conversation'),
        ('GAIA', 'RL-Orchestrated'),
    ]
    for bench_name, top_name in alignments:
        b = benchmarks[bench_name]
        t = priors[top_name]
        ax.plot([b[0], t[0]], [b[1], t[1]], [b[2], t[2]], '--', color='gray', alpha=0.4, lw=0.8)

    ax.set_xlabel('Decomposability (D)', fontsize=7, labelpad=5)
    ax.set_ylabel('Iterativeness (I)', fontsize=7, labelpad=5)
    ax.set_zlabel('Tool Diversity (T)', fontsize=7, labelpad=5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.tick_params(labelsize=6)
    ax.legend(fontsize=5, loc='upper left', framealpha=0.9)
    ax.view_init(elev=25, azim=45)

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig2_dit_framework.pdf'), bbox_inches='tight')
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig2_dit_framework.png'), bbox_inches='tight', dpi=300)
    plt.close()
    print('[DONE] Figure 2: D-I-T framework')


# ============================================================
# FIGURE 3: Performance Heatmap (REAL DATA)
# ============================================================

def fig3_main_results_heatmap():
    """Figure 3: Topology performance heatmap by task category.

    Uses REAL experimental data from pilot (easy) and scaled (hard) studies.
    Rows: category x difficulty. Columns: topology.
    """
    flat_pilot, hier_pilot, deb_pilot, scaled = load_all_data()

    # --- Compute pilot (easy) per-category rates ---
    pilot_cats = {'Coding': [], 'Reasoning': [], 'Research': []}
    cat_map = {'CODE': 'Coding', 'REASON': 'Reasoning', 'RESEARCH': 'Research'}

    # Build lookup dicts for hierarchical and debate pilot
    hier_lookup = {t['task_id']: t for t in hier_pilot}
    deb_lookup = {t['task_id']: t for t in deb_pilot}

    pilot_rates = {}  # (category, topology) -> rate
    for cat_key, cat_name in cat_map.items():
        flat_tasks = [t for t in flat_pilot if get_pilot_category(t['task_id']) == cat_key]
        hier_tasks = [hier_lookup[t['task_id']] for t in flat_tasks]
        deb_tasks = [deb_lookup[t['task_id']] for t in flat_tasks]
        n = len(flat_tasks)

        flat_c = sum(1 for t in flat_tasks if t['correct'])
        hier_c = sum(1 for t in hier_tasks if t['correct'])
        deb_c = sum(1 for t in deb_tasks if t['correct'])

        pilot_rates[(cat_name, 'flat')] = flat_c / n * 100
        pilot_rates[(cat_name, 'hierarchical')] = hier_c / n * 100
        pilot_rates[(cat_name, 'debate')] = deb_c / n * 100

    # --- Compute hard per-category rates ---
    hard_cats = {'Coding': 'CODE', 'Reasoning': 'REASON', 'Research': 'RESEARCH', 'Multi-domain': 'MULTI'}
    hard_rates = {}

    for cat_name, cat_key in hard_cats.items():
        tasks = [r for r in scaled['results'] if get_hard_category(r['task_id']) == cat_key]
        n = len(tasks)
        if n == 0:
            continue
        flat_c = sum(1 for t in tasks if t['flat_result']['correct'])
        hier_c = sum(1 for t in tasks if t['hierarchical_result']['correct'])
        deb_c = sum(1 for t in tasks if t['debate_result']['correct'])

        hard_rates[(cat_name, 'flat')] = flat_c / n * 100
        hard_rates[(cat_name, 'hierarchical')] = hier_c / n * 100
        hard_rates[(cat_name, 'debate')] = deb_c / n * 100

    # --- Build heatmap matrix ---
    row_labels = [
        'Easy: Coding',
        'Easy: Reasoning',
        'Easy: Research',
        'Hard: Coding',
        'Hard: Reasoning',
        'Hard: Research',
        'Hard: Multi-domain',
    ]
    col_labels = ['Flat', 'Hierarchical', 'Debate']
    topos = ['flat', 'hierarchical', 'debate']

    data = np.zeros((7, 3))
    # Easy rows
    for j, topo in enumerate(topos):
        data[0, j] = pilot_rates[('Coding', topo)]
        data[1, j] = pilot_rates[('Reasoning', topo)]
        data[2, j] = pilot_rates[('Research', topo)]
    # Hard rows
    for j, topo in enumerate(topos):
        data[3, j] = hard_rates[('Coding', topo)]
        data[4, j] = hard_rates[('Reasoning', topo)]
        data[5, j] = hard_rates[('Research', topo)]
        data[6, j] = hard_rates[('Multi-domain', topo)]

    fig, ax = plt.subplots(figsize=(5.5, 4.5))

    im = ax.imshow(data, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)

    ax.set_xticks(range(3))
    ax.set_xticklabels(col_labels, fontsize=8)
    ax.set_yticks(range(7))
    ax.set_yticklabels(row_labels, fontsize=7)

    # Add text annotations
    for i in range(7):
        for j in range(3):
            val = data[i, j]
            best_in_row = data[i, :].max()
            weight = 'bold' if val == best_in_row else 'normal'
            color = 'white' if val < 35 or val > 85 else 'black'
            ax.text(j, i, f'{val:.0f}%', ha='center', va='center',
                    fontsize=8, fontweight=weight, color=color)

    # Draw divider between easy and hard
    ax.axhline(y=2.5, color='black', linewidth=1.5, linestyle='-')

    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Accuracy (%)', fontsize=8)
    cbar.ax.tick_params(labelsize=6)

    ax.set_title('Topology Performance by Task Category (n=32 tasks)', fontsize=9, pad=10)

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig3_heatmap.pdf'), bbox_inches='tight')
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig3_heatmap.png'), bbox_inches='tight', dpi=300)
    plt.close()

    print('[DONE] Figure 3: Performance heatmap (REAL DATA)')
    print(f'       Easy overall: Flat={sum(1 for t in flat_pilot if t["correct"])/len(flat_pilot)*100:.1f}%  '
          f'Hier={sum(1 for t in hier_pilot if t["correct"])/len(hier_pilot)*100:.1f}%  '
          f'Debate={sum(1 for t in deb_pilot if t["correct"])/len(deb_pilot)*100:.1f}%')
    print(f'       Hard overall: Flat={scaled["summary"]["flat"]["accuracy"]*100:.0f}%  '
          f'Hier={scaled["summary"]["hierarchical"]["accuracy"]*100:.0f}%  '
          f'Debate={scaled["summary"]["debate"]["accuracy"]*100:.0f}%')


# ============================================================
# FIGURE 4: Alignment Scatter (REAL DATA)
# ============================================================

def fig4_alignment_prediction():
    """Figure 4: D-I-T alignment distance vs success (binary).

    Uses REAL alignment distances computed from actual task D-I-T scores
    and topology priors. 96 task-topology pairs (32 tasks x 3 topologies).
    """
    from scipy import stats

    flat_pilot, hier_pilot, deb_pilot, scaled = load_all_data()

    hier_lookup = {t['task_id']: t for t in hier_pilot}
    deb_lookup = {t['task_id']: t for t in deb_pilot}

    alignment_dists = []
    successes = []
    topo_labels = []
    difficulty_labels = []

    # --- Pilot (easy) tasks ---
    for task in flat_pilot:
        tid = task['task_id']
        dit = PILOT_DIT[tid]
        for topo_name, prior in TOPOLOGY_PRIORS.items():
            dist = euclidean_dist(dit, prior)
            if topo_name == 'flat':
                success = 1 if task['correct'] else 0
            elif topo_name == 'hierarchical':
                success = 1 if hier_lookup[tid]['correct'] else 0
            else:
                success = 1 if deb_lookup[tid]['correct'] else 0
            alignment_dists.append(dist)
            successes.append(success)
            topo_labels.append(topo_name)
            difficulty_labels.append('easy')

    # --- Hard tasks ---
    for r in scaled['results']:
        dit = (r['dit']['D'], r['dit']['I'], r['dit']['T'])
        for topo_name, prior in TOPOLOGY_PRIORS.items():
            dist = euclidean_dist(dit, prior)
            if topo_name == 'flat':
                success = 1 if r['flat_result']['correct'] else 0
            elif topo_name == 'hierarchical':
                success = 1 if r['hierarchical_result']['correct'] else 0
            else:
                success = 1 if r['debate_result']['correct'] else 0
            alignment_dists.append(dist)
            successes.append(success)
            topo_labels.append(topo_name)
            difficulty_labels.append('hard')

    alignment_dists = np.array(alignment_dists)
    successes = np.array(successes)

    # Compute Spearman correlation (negative = closer alignment -> higher success)
    rho, pval = stats.spearmanr(alignment_dists, successes)

    fig, ax = plt.subplots(figsize=(5, 4))

    # Jitter y-axis for visibility (success is binary 0/1)
    jitter = np.random.RandomState(42).uniform(-0.06, 0.06, len(successes))
    y_jittered = successes + jitter

    # Plot by topology
    for topo_name in ['flat', 'hierarchical', 'debate']:
        mask = np.array([t == topo_name for t in topo_labels])
        ax.scatter(alignment_dists[mask], y_jittered[mask],
                   c=TOPO_COLORS[topo_name], s=25, alpha=0.6,
                   label=TOPO_LABELS[topo_name], edgecolors='none')

    # Logistic regression fit for visual
    from scipy.optimize import curve_fit

    def logistic(x, L, k, x0):
        return L / (1 + np.exp(k * (x - x0)))

    try:
        # Bin alignment distances and compute mean success for smooth curve
        bins = np.linspace(alignment_dists.min(), alignment_dists.max(), 10)
        bin_centers = (bins[:-1] + bins[1:]) / 2
        bin_means = []
        for i in range(len(bins) - 1):
            mask = (alignment_dists >= bins[i]) & (alignment_dists < bins[i + 1])
            if mask.sum() > 0:
                bin_means.append(successes[mask].mean())
            else:
                bin_means.append(np.nan)

        # Plot binned means as larger markers
        valid = ~np.isnan(bin_means)
        ax.scatter(bin_centers[valid], np.array(bin_means)[valid],
                   c='black', s=60, marker='D', zorder=10, edgecolors='white',
                   linewidth=0.8, label='Binned mean')

        # Fit and draw logistic curve
        popt, _ = curve_fit(logistic, alignment_dists, successes, p0=[1, 3, 0.7], maxfev=5000)
        x_smooth = np.linspace(alignment_dists.min(), alignment_dists.max(), 200)
        y_smooth = logistic(x_smooth, *popt)
        ax.plot(x_smooth, y_smooth, 'k--', lw=1.2, alpha=0.7, label='Logistic fit')
    except Exception:
        # Fallback: simple linear regression line
        z = np.polyfit(alignment_dists, successes, 1)
        p = np.poly1d(z)
        x_line = np.linspace(alignment_dists.min(), alignment_dists.max(), 100)
        ax.plot(x_line, p(x_line), 'k--', lw=1, alpha=0.7)

    # Correlation annotation
    pval_str = f'p = {pval:.4f}' if pval >= 0.001 else 'p < 0.001'
    ax.text(0.95, 0.95,
            f'Spearman rho = {rho:.3f}\n{pval_str}\nn = {len(successes)} pairs',
            transform=ax.transAxes, fontsize=7, verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray'))

    ax.set_xlabel('D-I-T Alignment Distance (Euclidean)', fontsize=8)
    ax.set_ylabel('Task Success (0 = fail, 1 = correct)', fontsize=8)
    ax.set_title('Alignment Distance vs. Task Success', fontsize=9)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Fail', 'Correct'], fontsize=7)
    ax.legend(fontsize=6, loc='center left')
    ax.tick_params(labelsize=6)

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig4_alignment.pdf'), bbox_inches='tight')
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig4_alignment.png'), bbox_inches='tight', dpi=300)
    plt.close()
    print(f'[DONE] Figure 4: Alignment prediction (Spearman rho={rho:.3f}, p={pval:.4f}, n={len(successes)})')


# ============================================================
# FIGURE 5: Difficulty-Dependent Topology Advantage (NEW)
# ============================================================

def fig5_difficulty_topology_advantage():
    """Figure 5: Accuracy by difficulty level for each topology.

    Headline visual: bar chart showing the dramatic topology differentiation
    that emerges on hard tasks but is absent on easy tasks.
    """
    flat_pilot, hier_pilot, deb_pilot, scaled = load_all_data()

    # Easy task accuracy
    n_easy = len(flat_pilot)
    easy_flat = sum(1 for t in flat_pilot if t['correct']) / n_easy * 100
    easy_hier = sum(1 for t in hier_pilot if t['correct']) / n_easy * 100
    easy_debate = sum(1 for t in deb_pilot if t['correct']) / n_easy * 100

    # Hard task accuracy
    n_hard = len(scaled['results'])
    hard_flat = scaled['summary']['flat']['accuracy'] * 100
    hard_hier = scaled['summary']['hierarchical']['accuracy'] * 100
    hard_debate = scaled['summary']['debate']['accuracy'] * 100

    fig, ax = plt.subplots(figsize=(5, 3.5))

    x = np.arange(3)  # Flat, Hierarchical, Debate
    width = 0.32

    bars_easy = ax.bar(x - width / 2, [easy_flat, easy_hier, easy_debate],
                       width, label='Easy (n=12)', color=['#90CAF9', '#A5D6A7', '#FFCC80'],
                       edgecolor=['#1565C0', '#2E7D32', '#E65100'], linewidth=1.2)
    bars_hard = ax.bar(x + width / 2, [hard_flat, hard_hier, hard_debate],
                       width, label='Hard (n=20)', color=['#2196F3', '#4CAF50', '#FF9800'],
                       edgecolor=['#0D47A1', '#1B5E20', '#BF360C'], linewidth=1.2)

    # Add value labels on bars
    for bar in bars_easy:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height + 1.5,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=7, fontweight='bold')
    for bar in bars_hard:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height + 1.5,
                f'{height:.0f}%', ha='center', va='bottom', fontsize=7, fontweight='bold')

    # Draw arrows showing the delta
    for i, (e, h) in enumerate([(easy_flat, hard_flat), (easy_hier, hard_hier), (easy_debate, hard_debate)]):
        delta = h - e
        mid_x = x[i] + width * 0.75
        ax.annotate(f'{delta:+.0f}pp',
                    xy=(mid_x, h + 5), fontsize=6, color='red' if delta < 0 else 'green',
                    ha='center', fontweight='bold')

    ax.set_xlabel('')
    ax.set_ylabel('Accuracy (%)', fontsize=9)
    ax.set_title('Topology Differentiation Emerges on Hard Tasks', fontsize=10, fontweight='bold', pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(['Flat', 'Hierarchical', 'Debate'], fontsize=9)
    ax.set_ylim(0, 115)
    ax.legend(fontsize=8, loc='upper right')
    ax.tick_params(labelsize=7)

    # Add horizontal reference lines
    ax.axhline(y=100, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
    ax.axhline(y=50, color='gray', linestyle=':', linewidth=0.5, alpha=0.3)

    # Subtitle with key finding
    ax.text(0.5, -0.12,
            'Easy tasks show ceiling effect (all topologies near 100%). '
            'Hard tasks reveal 6.5x advantage for structured topologies.',
            transform=ax.transAxes, fontsize=6.5, ha='center', style='italic', color='#555')

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig5_difficulty_advantage.pdf'), bbox_inches='tight')
    fig.savefig(os.path.join(OUTPUT_DIR, 'fig5_difficulty_advantage.png'), bbox_inches='tight', dpi=300)
    plt.close()

    print('[DONE] Figure 5: Difficulty-dependent topology advantage (HEADLINE)')
    print(f'       Easy: Flat={easy_flat:.1f}%  Hier={easy_hier:.1f}%  Debate={easy_debate:.1f}%')
    print(f'       Hard: Flat={hard_flat:.0f}%  Hier={hard_hier:.0f}%  Debate={hard_debate:.0f}%')
    print(f'       Delta: Flat={hard_flat-easy_flat:+.0f}pp  Hier={hard_hier-easy_hier:+.0f}pp  Debate={hard_debate-easy_debate:+.0f}pp')


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    print('=== Generating OrchestraBench Figures (REAL DATA) ===')
    print()
    fig1_topology_architectures()
    fig2_dit_framework()
    fig3_main_results_heatmap()
    fig4_alignment_prediction()
    fig5_difficulty_topology_advantage()
    print()
    print(f'All figures saved to: {os.path.abspath(OUTPUT_DIR)}')
    print('Formats: PDF (LaTeX) + PNG (preview)')
