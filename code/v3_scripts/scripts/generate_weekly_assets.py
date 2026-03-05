import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from V3.acedcor_v3.conditional import conditional_dependence_report
from V3.acedcor_v3.core import acedcor_test


ROOT = Path('.')
IMG_DIR = ROOT / 'img'
OUT_DIR = ROOT / 'V3'
IMG_DIR.mkdir(exist_ok=True)
OUT_DIR.mkdir(exist_ok=True)


def _simulate_a1(n=180, repeats=25, B=99, alpha=0.05, seed=20260303):
    rng = np.random.default_rng(seed)

    scenarios = {
        'Independent': lambda x, e: rng.normal(0.0, 1.0, size=x.size),
        'Monotonic (x^3)': lambda x, e: 0.25 * (x**3) + 1.3 * e,
        'Symmetric (x^2)': lambda x, e: 0.25 * (x**2) + 1.3 * e,
    }

    rows = []
    for name, fn in scenarios.items():
        reject_raw = 0
        reject_after = 0
        for _ in range(repeats):
            x = rng.normal(0.0, 1.0, size=n)
            e = rng.normal(0.0, 1.0, size=n)
            y = fn(x, e)
            result = acedcor_test(x, y, B=B, random_state=int(rng.integers(1_000_000)))
            reject_raw += int(result['p_before'] < alpha)
            reject_after += int(result['p_after'] < alpha)

        rows.append({
            'scenario': name,
            'n': n,
            'repeats': repeats,
            'B': B,
            'alpha': alpha,
            'reject_rate_raw': reject_raw / repeats,
            'reject_rate_after_ace': reject_after / repeats,
        })

    csv_path = OUT_DIR / 'a1_type1_power_summary.csv'
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    labels = [r['scenario'] for r in rows]
    raw_vals = [r['reject_rate_raw'] for r in rows]
    ace_vals = [r['reject_rate_after_ace'] for r in rows]

    x = np.arange(len(labels))
    width = 0.36

    plt.figure(figsize=(8.2, 4.8))
    plt.bar(x - width / 2, raw_vals, width, label='Raw dCor test')
    plt.bar(x + width / 2, ace_vals, width, label='After-ACE dCor test')
    plt.axhline(alpha, color='red', linestyle='--', linewidth=1.2, label='alpha=0.05')
    plt.xticks(x, labels)
    plt.ylabel('Rejection rate')
    plt.title('A1: Type-I error / power by scenario (perm test)')
    plt.ylim(0, 1)
    plt.legend()
    plt.tight_layout()
    fig_path = IMG_DIR / 'a1_type1_power.png'
    plt.savefig(fig_path, dpi=170)
    plt.close()

    return rows


def _simulate_a2(n=500, seed=20260304):
    rng = np.random.default_rng(seed)
    z = rng.normal(0.0, 1.0, size=n)
    x = 0.9 * z + 0.25 * rng.normal(0.0, 1.0, size=n)
    y = 0.7 * z + 0.25 * rng.normal(0.0, 1.0, size=n)

    report = conditional_dependence_report(x, y, z)

    csv_path = OUT_DIR / 'a2_confounding_summary.csv'
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['metric', 'value'])
        for key in ['dcor_raw', 'dcor_partial_residual', 'partial_distance_correlation']:
            writer.writerow([key, float(report[key])])

    plt.figure(figsize=(11, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(x, y, s=14, alpha=0.6)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Raw relationship (confounded by Z)')

    # residual view
    design = np.column_stack([np.ones(n), z])
    bx, *_ = np.linalg.lstsq(design, x, rcond=None)
    by, *_ = np.linalg.lstsq(design, y, rcond=None)
    rx = x - design @ bx
    ry = y - design @ by

    plt.subplot(1, 2, 2)
    plt.scatter(rx, ry, s=14, alpha=0.6)
    plt.xlabel('Residual X | Z')
    plt.ylabel('Residual Y | Z')
    plt.title('After residualization (X indep Y | Z)')

    text = (
        f"dCor raw = {report['dcor_raw']:.3f}\n"
        f"dCor residual = {report['dcor_partial_residual']:.3f}\n"
        f"Partial dCor = {report['partial_distance_correlation']:.3f}"
    )
    plt.gcf().text(0.5, -0.02, text, ha='center', fontsize=10)
    plt.tight_layout()
    fig_path = IMG_DIR / 'a2_confounding_demo.png'
    plt.savefig(fig_path, dpi=170, bbox_inches='tight')
    plt.close()

    return report


def main():
    a1_rows = _simulate_a1()
    a2_report = _simulate_a2()
    print('A1 rows:', a1_rows)
    print('A2 report:', a2_report)


if __name__ == '__main__':
    main()