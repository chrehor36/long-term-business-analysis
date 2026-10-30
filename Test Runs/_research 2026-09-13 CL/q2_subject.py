"""Colgate's own filed volume / net selling price / foreign exchange decomposition, by segment, 2016-2025 and H1 2026,
transcribed from the MD&A sentences in each 10-K (verbatim sentences in vpfx_out.txt and the run file) and the Q2 2026 10-Q
six-month table. Arithmetic only: cumulative sums and compounding. Percent points."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
YRS = list(range(2016, 2026))
# (volume, net selling price, foreign exchange), each year as filed in the 10-K that first reports it
D = {
 "Total Company":  [(-3.0, 2.5, -4.5), (0.5, 0.5, 0.5), (1.0, 0.5, -1.0), (2.5, 2.0, -3.5), (5.5, 3.0, -3.5), (1.0, 3.5, 1.5), (-2.0, 9.5, -4.5), (-0.5, 10.0, -1.0), (3.1, 4.4, -4.1), (-0.4, 2.1, -0.3)],
 "North America":  [(2.5, -1.0, -0.5), (0.0, -2.0, 0.0), (6.5, 1.0, 0.0), (2.0, 0.5, -0.5), (8.0, 1.5, 0.0), (-4.0, 2.0, 1.0), (-2.0, 5.5, 0.0), (-4.5, 7.5, 0.0), (2.6, -1.9, -0.1), (-1.4, -0.2, -0.1)],
 "Latin America":  [(-14.0, 8.5, -10.0), (2.5, 3.0, 1.0), (-2.5, 1.5, -6.5), (3.0, 4.0, -7.0), (0.5, 8.5, -14.0), (1.0, 7.0, -1.0), (-5.0, 15.5, -2.0), (2.5, 13.0, 1.0), (3.9, 12.9, -13.7), (0.9, 2.9, -4.0)],
 "Europe":         [(2.5, -2.5, -3.0), (2.0, -1.0, 1.0), (2.5, -2.0, 4.0), (4.0, -0.5, -5.5), (11.0, -0.5, 1.5), (-0.5, 0.0, 4.0), (-4.0, 4.0, -10.5), (-4.5, 9.5, 2.5), (4.1, 2.5, 1.1), (1.1, 1.5, 4.4)],
 "Asia Pacific":   [(-1.0, 0.0, -4.0), (-0.5, 0.0, 0.0), (-1.5, 0.0, 0.0), (0.5, 1.0, -2.5), (-1.5, 2.0, -1.0), (3.0, 0.0, 3.0), (-0.5, 5.5, -6.5), (-3.5, 6.0, -4.0), (3.1, 1.0, -1.3), (-2.7, 1.7, -0.5)],
 "Africa/Eurasia": [(-4.0, 9.5, -9.5), (-4.5, 3.5, 3.5), (-1.0, 3.5, -4.0), (3.5, 4.0, -6.0), (5.0, 3.5, -8.5), (1.0, 6.0, -0.5), (-9.5, 21.5, -8.5), (4.5, 13.0, -17.5), (7.6, 5.7, -12.1), (0.5, 6.0, 0.5)],
 "Hill's":         [(0.0, 2.5, 0.0), (-1.0, 1.5, 0.5), (1.5, 2.0, 0.5), (3.5, 4.0, -1.5), (10.5, 4.0, -0.5), (8.0, 5.5, 1.5), (4.0, 11.5, -3.5), (5.0, 11.0, -0.5), (0.8, 4.1, -0.4), (-0.6, 3.0, 0.5)],
}
H1_2026 = {"Total Company": (1.0, 1.9, 3.8), "North America": (-3.6, 0.9, 0.2), "Latin America": (2.3, 3.1, 8.9),
           "Europe, Middle East & Africa (recast)": (2.7, 0.0, 4.9), "Asia Pacific (recast)": (4.3, 1.1, 1.5), "Hill's": (-0.5, 3.9, 1.7)}

def comp(xs):
    p = 1.0
    for x in xs:
        p *= 1 + x / 100
    return (p - 1) * 100

L = ["| segment | " + " | ".join(str(y) for y in YRS) + " | sum 2016-25 | compounded 2016-25 | sum 2021-25 | compounded 2021-25 |", "|---|" + "---|" * (len(YRS) + 4)]
for seg, rows in D.items():
    for k, lab in enumerate(("volume", "price", "FX")):
        xs = [r[k] for r in rows]
        L.append(f"| {seg} {lab} | " + " | ".join(f"{x:+.1f}" for x in xs) + f" | {sum(xs):+.1f} | {comp(xs):+.1f}% | {sum(xs[5:]):+.1f} | {comp(xs[5:]):+.1f}% |")
    pr = [r[1] for r in rows]; fx = [r[2] for r in rows]
    L.append(f"| {seg} price + FX (what pricing kept in USD) | " + " | ".join(f"{p+f:+.1f}" for p, f in zip(pr, fx)) + f" | {sum(pr)+sum(fx):+.1f} | {comp([p+f for p,f in zip(pr,fx)]):+.1f}% | {sum(pr[5:])+sum(fx[5:]):+.1f} | |")
L += ["", "| H1 2026 (10-Q six-month table) | volume | pricing | FX |", "|---|---|---|---|"]
for k, v in H1_2026.items():
    L.append(f"| {k} | {v[0]:+.1f} | {v[1]:+.1f} | {v[2]:+.1f} |")
# gross margin attribution (bps), MD&A
GM = {2016: (200, 20, -190, 0), 2018: (200, 40, -340, 0), 2019: (220, 70, -300, 0), 2020: (230, 130, -230, 0), 2021: (210, 120, -450, 0),
      2022: (220, 360, -810, 0), 2023: (270, 390, -480, -60), 2024: (280, 170, -230, 20), 2025: (260, 80, -420, 30)}
L += ["", "| gross margin attribution, bps (MD&A) | funding-the-growth savings | higher pricing | raw & packaging materials | mix |", "|---|---|---|---|---|"]
for y, g in GM.items():
    L.append(f"| {y} | +{g[0]} | +{g[1]} | {g[2]} | {g[3]:+d} |")
s = [sum(GM[y][i] for y in GM if y >= 2018) for i in range(4)]
L.append(f"| **sum 2018-2025** | **+{s[0]}** | **+{s[1]}** | **{s[2]}** | **{s[3]:+d}** |")
open(os.path.join(HERE, "q2_subject_out.md"), "w", encoding="utf-8").write("\n".join(L))
print("\n".join(L))
