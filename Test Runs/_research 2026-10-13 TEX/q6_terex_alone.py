# Terex alone before the REV merger: was the stock issued at $58.99 below this run's computed range? (COMPUTATION)
exec(open('q7_computation.py').read().split('out = []')[0])
a, p, m = series(tex)
nd = 2584 - 772        # 10-K FY2025 balance sheet: total debt less cash at 2025-12-31
sh = 64.9              # shares outstanding 2025-12-31 (statement of changes in equity)
g = (4335 / 3870.6) ** 0.25 - 1
for lab, c in (("all-spending", avg(p)), ("maintenance-only", avg(m))):
    for gl, gg in (("no growth", 0), ("organic", g)):
        print("%-17s %-10s per share at 5.6%%: %6.2f   at 10%%: %6.2f" % (lab, gl, (pv(c, gg, R) - nd) / sh, (pv(c, gg, FLOOR) - nd) / sh))
