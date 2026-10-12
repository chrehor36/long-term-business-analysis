"""SBUX Q7, specific (a) cycle variant (COMPUTATION). FY2016-FY2025 from the filed cash flow statements
(FY2016-FY2018 from the FY2018 10-K, FY2019-FY2020 from the FY2020 10-K, FY2021-FY2025 as in q7.py; XBRL series
checked to those statements). USD millions. Imports the valuation helpers of q7.py."""
import importlib.util, os
spec = importlib.util.spec_from_file_location("q7", os.path.join(os.path.dirname(os.path.abspath(__file__)), "q7.py"))
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
FY     = list(range(2016, 2026))
OCF    = [4575.1, 4174.3, 11937.8, 5047.0, 1597.8, 5989.1, 4397.3, 6008.7, 6095.6, 4747.5]
NESTLE = [0, 0, 7000.0, 0, 0, 0, 0, 0, 0, 0]          # "an upfront payment of approximately $7 billion" (10-K FY2018 Note 2)
SBC    = [218.1, 176.0, 250.3, 308.0, 248.6, 319.1, 271.5, 302.7, 308.3, 318.3]
CAPEX  = [1440.3, 1519.4, 1976.4, 1806.6, 1483.6, 1470.0, 1841.3, 2333.6, 2777.5, 2305.5]
ACQ    = [0, 0, 1311.3, 0, 0, 0, 0, 0, 0, 177.1]
DIVEST = [69.6, 85.4, 608.2, 684.3, 0, 1175.0, 59.3, 110.0, 0, 0]
INTP   = [74.7, 96.6, 137.1, 299.5, 396.9, 501.1, 474.7, 524.3, 570.7, 588.3]
INTI   = [0, 0, 0, 0, 0, 90.1, 97.0, 81.2, 122.8, 113.3]   # interest income netted only where q7.py has it
TAX    = [1379.7, 1432.6, 1262.0, 871.6, 239.7, 1156.6, 948.5, 1277.2, 1207.3, 650.6]
PRE    = [4198.6, 4317.5, 5780.0, 4466.2, 1164.4, 5356.9, 4231.9, 5401.9, 4969.6, 2507.3]
REV    = [21315.9, 22386.8, 24719.5, 26508.6, 23518.0, 29060.6, 32250.3, 35975.6, 36176.2, 37184.4]
def series(nestle_out=True, levered=False):
    out = []
    for i in range(10):
        v = OCF[i] - (NESTLE[i] if nestle_out else 0) - SBC[i] - CAPEX[i] - ACQ[i] + DIVEST[i]
        if not levered: v += (INTP[i] - INTI[i]) * (1 - TAX[i] / PRE[i])
        out.append(v)
    return out
for nestle_out in (True, False):
    u = series(nestle_out); l = series(nestle_out, True)
    c1, c2 = sum(u[:5]) / 5, sum(u[5:]) / 5
    g = (c2 / c1) ** (1 / 5) - 1
    l1, l2 = sum(l[:5]) / 5, sum(l[5:]) / 5; gl = (l2 / l1) ** (1 / 5) - 1
    base = c2
    top = q.per_share(q.pv(base, 0.0, q.SOV)); bot = q.per_share(q.pv(base, g, q.SOV))
    if bot > top: top, bot = bot, top
    fair = q.per_share((q.pv(base, 0.0, q.FLOOR) + q.pv(base, g, q.FLOOR)) / 2)
    fair_eq = q.per_share((q.pv(l2, 0.0, q.FLOOR) + q.pv(l2, gl, q.FLOOR)) / 2, all_equity=False)
    print(f"\n== CYCLE VARIANT, Nestle prepayment {'removed' if nestle_out else 'kept as proceeds of a business sold'}")
    print("  unlevered by FY:", [round(x) for x in u])
    print(f"  cycle FY2016-20 avg {c1:.0f}; cycle FY2021-25 avg {c2:.0f}; growth between cycles {g:.1%}/yr")
    te = q.per_share(q.pv(l2, 0.0, q.SOV), False); be = q.per_share(q.pv(l2, gl, q.SOV), False)
    if be > te: te, be = be, te
    print(f"  ALL-EQUITY range ${bot:.2f} to ${top:.2f} (width {top/bot:.2f}x); fair ${fair:.2f}; EQUITY-ONLY range ${be:.2f} to ${te:.2f}, fair ${fair_eq:.2f}; levered cycle growth {gl:.1%}")
    print("  owner cash / revenue by FY:", [f"{x/r:.1%}" for x, r in zip(u, REV)])
# the most generous case any reading supports: highest five-year unlevered average, growth at revenue growth FY2016-25
best = max(sum(series()[i:i+5]) / 5 for i in range(6))
grev = (REV[-1] / REV[0]) ** (1 / 9) - 1
print(f"\nGENEROUS BOUND: best five-year unlevered average {best:.0f}, carried at revenue growth {grev:.1%} for ten years:"
      f" ${q.per_share(q.pv(best, grev, q.SOV)):.2f} a share at the sovereign; at ten percent ${q.per_share(q.pv(best, grev, q.FLOOR)):.2f}")
