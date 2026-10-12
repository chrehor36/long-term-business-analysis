# Q7 final arithmetic for the TXN run (COMPUTATION feeds the STOP). USD millions.
import importlib.util, sys
spec = importlib.util.spec_from_file_location("v", "scripts/value.py")
src = open("scripts/value.py").read().split("avg = lambda")[0]   # reuse the series and owner-cash definitions only
ns = {}; exec(src.replace('print(', 'pass; (lambda *a, **k: None)('), ns)
OC_m, OC_c, OC_m_eq, REV = ns["OC_m"], ns["OC_c"], ns["OC_m_eq"], ns["REV"]
avg = lambda d, ys: sum(d[y] for y in ys) / len(ys)
R = 0.056; SH = 913.248; P = 283.74
DEBT = 14052; CASH = 3660 + 3341; RECV = 2163; ND = DEBT - CASH - RECV
SLAB_EV = 7500
EMB = 0.108   # Embedded Processing share of 2021-2025 operating profit: carried at no growth (parts convention)
def pv(oc0, g, r, n=10, emb=0.0):
    v = 0; a = oc0 * (1 - emb); b = oc0 * emb
    for t in range(1, n + 1):
        a *= (1 + g); v += (a + b) / (1 + r) ** t
    return v + ((a + b) / r) / (1 + r) ** n
def irr(f, target):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(m) > target else (lo, m)
    return m
mc = SH * P; EV = mc + ND
print(f"market cap {mc:,.0f}; net debt {DEBT-CASH:,.0f} less CHIPS receivables {RECV:,} = {ND:,.0f}; EV {EV:,.0f}")
prev, last = [2014, 2015, 2016, 2017, 2018, 2019], [2020, 2021, 2022, 2023]
print("owner cash (maintenance, all-equity):", {y: round(OC_m[y]) for y in OC_m})
b_prev, b_last = avg(OC_m, prev), avg(OC_m, last)
g_oc = (b_last / b_prev) ** (1 / 5) - 1
r_prev, r_last = avg(REV, prev), avg(REV, last); g_rev = (r_last / r_prev) ** (1 / 5) - 1
hi_share = max(OC_m[y] / REV[y] for y in OC_m)
oc10 = b_last * (1 + g_oc) ** 10; rev10 = r_last * (1 + g_rev) ** 10
print(f"cycle base (2020-2023) {b_last:.0f}; previous cycle (2014-2019) {b_prev:.0f}; shown OC growth {g_oc:.2%}; revenue growth between cycles {g_rev:.2%}")
print(f"cap test: OC year 10 {oc10:.0f} vs revenue {rev10:.0f} = {oc10/rev10:.1%} share; highest share on file {hi_share:.1%} -> cap {'APPLIES' if oc10/rev10 > hi_share else 'does not apply'}")
g = g_rev if oc10 / rev10 > hi_share else g_oc
def case(label, oc0, gg, emb=EMB, eq=False):
    v = pv(oc0, gg, R, emb=emb); v10 = pv(oc0, gg, 0.10, emb=emb)
    if eq:
        ps, ps10 = v / SH, v10 / SH; i = irr(lambda r: pv(oc0, gg, r, emb=emb), mc)
    else:
        ps, ps10 = (v - ND) / SH, (v10 - ND) / SH; i = irr(lambda r: pv(oc0, gg, r, emb=emb), EV)
    print(f"  {label:62s} value {v:9,.0f}  ${ps:7.2f}/sh @5.6%  ${ps10:7.2f}/sh @10%  return at price {i:5.2%}")
    return ps, ps10, i
print("CENTRAL (all-equity, maintenance-only owner cash, cycle base, Embedded at no growth)")
lo = case("bottom: no growth", b_last, 0.0)
hi = case(f"top: growth {g:.2%} ten years (cap applied), then zero", b_last, g)
print(f"  RANGE ${lo[0]:.2f} to ${hi[0]:.2f}  (width {hi[0]/lo[0]:.2f} to 1)   FAIR ${(lo[1]+hi[1])/2:.2f}")
case(f"beside: shown owner-cash growth {g_oc:.2%} uncapped", b_last, g_oc)
case(f"beside: shown growth {g_oc:.2%} uncapped, Embedded growing too", b_last, g_oc, emb=0.0)
print("EQUITY-ONLY (owner cash after interest, against market value)")
bq, pq = avg(OC_m_eq, last), avg(OC_m_eq, prev); gq = (bq / pq) ** 0.2 - 1
elo = case("bottom", bq, 0.0, eq=True); ehi = case(f"top {g:.2%}", bq, g, eq=True)
print(f"  RANGE ${elo[0]:.2f} to ${ehi[0]:.2f}   FAIR ${(elo[1]+ehi[1])/2:.2f}   (shown eq growth {gq:.2%})")
print("ALL-SPENDING case beside (all capital spending, CHIPS netted)")
ca, cp = avg(OC_c, last), avg(OC_c, prev); gc = (ca / cp) ** 0.2 - 1
case("bottom", ca, 0.0); case(f"top shown {gc:.2%}", ca, gc)
print("LITERAL WINDOW 2021-2025 beside")
w = avg(OC_m, [2021, 2022, 2023, 2024, 2025]); gl = (OC_m[2025] / OC_m[2021]) ** 0.25 - 1
print(f"  window average {w:.0f}; literal growth {gl:.2%} (negative: rule (b), it is the bottom; no growth the top)")
case("literal bottom (negative growth)", w, gl, emb=0.0); case("literal top (no growth)", w, 0.0, emb=0.0)
print("SILICON LABS AS IF CLOSED (beside, not central): EV added to net debt, target owner cash credited at nothing (negative on file)")
d = SLAB_EV / SH
print(f"  every per-share figure falls by ${d:.2f}: range ${lo[0]-d:.2f} to ${hi[0]-d:.2f}; fair ${(lo[1]+hi[1])/2-d:.2f}")
