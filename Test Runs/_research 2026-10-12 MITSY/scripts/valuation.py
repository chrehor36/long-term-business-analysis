"""Q7 arithmetic for Mitsui & Co. (Mn JPY -> bn). COMPUTATION; the framework's rules are in the run file.
Cases follow Q7's range convention: five-year average (FY2022-26) owner cash after the company's tax; ten years at the
growth shown (capped), then zero nominal growth; discounted at the 30-year JGB (range) and at 10% (floor test, fair price)."""
from owner_cash import rows
R = rows(); W = [2022, 2023, 2024, 2025, 2026]; C = list(range(2017, 2027))
avg = lambda k, ys: sum(R[y][k] for y in ys) / len(ys) / 1000
SOV = 0.0414; FLOOR = 0.10
SHARES = 2839.906064  # mn
MCAP = SHARES * 4775 / 1000  # bn
NET_DEBT = 4416.7 + 42.1
REV = {2022: 11757.6, 2026: 13995.2}
def pv(base, g, r, n=10):
    s = sum(base * (1 + g) ** t / (1 + r) ** t for t in range(1, n + 1))
    return s + base * (1 + g) ** n / r / (1 + r) ** n
def per_share(ev, nd=NET_DEBT): return (ev - nd) * 1000 / SHARES
maint_u = avg('oc_maint_u', W); maint_e = avg('oc_maint', W); all_u = avg('oc_all_u', W); all_e = avg('oc_all', W)
g_shown = (R[2026]['oc_maint_u'] / R[2022]['oc_maint_u']) ** 0.25 - 1
g_halves = (avg('oc_maint_u', W) / avg('oc_maint_u', range(2017, 2022))) ** 0.2 - 1
g_sales = (REV[2026] / REV[2022]) ** 0.25 - 1
growth_spend_u = maint_u - all_u
charge = growth_spend_u * g_sales / g_shown  # spending charged for the capped growth (run CONVENTION: proportional)
print(f'market cap {MCAP:.1f}  net debt {NET_DEBT:.1f}  EV {MCAP+NET_DEBT:.1f}')
print(f'5yr avg: maint-only all-equity {maint_u:.1f}, equity-only {maint_e:.1f}; all-spending all-equity {all_u:.1f}, equity-only {all_e:.1f}')
print(f'growth: shown FY22->26 (maint, all-equity) {g_shown:.2%}; decade halves {g_halves:.2%}; sales FY22->26 {g_sales:.2%}')
peak_share = max(R[y]['oc_maint_u'] / 1000 / s for y, s in ((2023, 14306.4), (2025, 14662.6), (2026, 13995.2), (2024, 13324.9), (2022, 11757.6)))
print(f'cap test: maint OC carried 10y at shown rate = {maint_u*(1+g_shown)**10:.0f} bn = {maint_u*(1+g_shown)**10/REV[2026]:.1%} of FY26 sales; highest share in window {peak_share:.1%} -> cut to sales growth')
print(f'growth spending (maint - all), all-equity avg {growth_spend_u:.1f}; charged for capped growth {charge:.1f}')
cases = {
 'no-growth, maintenance-only (bottom)': (maint_u, maint_e, 0.0),
 'growth at sales rate, growth spending charged (top)': (maint_u - charge, maint_e - charge, g_sales),
 'beside: all spending, growth at sales rate': (all_u, all_e, g_sales),
 'beside: maint-only, shown growth 12.6%, NO growth spending (breaks (e) and (f))': (maint_u, maint_e, g_shown),
 'beside: maint-only, decade-halves growth, NO growth spending (breaks (e) and (f))': (maint_u, maint_e, g_halves),
}
EV = MCAP + NET_DEBT
for name, (bu, be, g) in cases.items():
    ev_s = pv(bu, g, SOV); ev_f = pv(bu, g, FLOOR); eq_s = pv(be, g, SOV); eq_f = pv(be, g, FLOOR)
    print(f'{name}: base {bu:.1f} g {g:.2%} | at JGB: EV {ev_s:.0f} -> {per_share(ev_s):,.0f}/sh (equity-only {eq_s*1000/SHARES:,.0f}) | at 10%: EV {ev_f:.0f} vs {EV:.0f} -> {per_share(ev_f):,.0f}/sh (equity-only {eq_f*1000/SHARES:,.0f}) | clears floor: {ev_f >= EV}')
b = cases['no-growth, maintenance-only (bottom)']; t = cases['growth at sales rate, growth spending charged (top)']
fair_ae = (per_share(pv(b[0], b[2], FLOOR)) + per_share(pv(t[0], t[2], FLOOR))) / 2
fair_eo = (pv(b[1], b[2], FLOOR) + pv(t[1], t[2], FLOOR)) / 2 * 1000 / SHARES
print(f'FAIR PRICE all-equity {fair_ae:,.0f}/sh (ADS x20 = {fair_ae*20:,.0f} yen = ${fair_ae*20/158.68:,.0f}); equity-only {fair_eo:,.0f} (ADS {fair_eo*20/158.68:,.0f} USD)')
lo, hi = per_share(pv(b[0], b[2], SOV)), per_share(pv(t[0], t[2], SOV))
print(f'RANGE all-equity {lo:,.0f} to {hi:,.0f} (width {hi/lo:.2f}x); ADS ${lo*20/158.68:,.0f} to ${hi*20/158.68:,.0f}; price 4,775 (ADS ${4775*20/158.68:,.0f})')
# cycle base: ten-year FY2017-26
cm_u = avg('oc_maint_u', C); cm_e = avg('oc_maint', C)
print(f'cycle base FY2017-26: maint all-equity {cm_u:.1f} -> no-growth at JGB {per_share(cm_u/SOV):,.0f}/sh; at 10% {per_share(cm_u/FLOOR):,.0f}/sh; equity-only at JGB {cm_e/SOV*1000/SHARES:,.0f}')
# literal window, all spending: the table's literal figure
print(f'literal window all-spending all-equity no growth at JGB: {per_share(all_u/SOV):,.0f}/sh')
# implied return at price for the most generous allowed case (top): solve r
import math
lo_r, hi_r = 0.0001, 0.5
for _ in range(100):
    m = (lo_r + hi_r) / 2
    if pv(t[0], t[2], m) > EV: lo_r = m
    else: hi_r = m
print(f'implied return at the price, top case, all-equity: {lo_r:.2%}')
lo_r, hi_r = 0.0001, 0.5
for _ in range(100):
    m = (lo_r + hi_r) / 2
    if pv(b[0], 0, m) > EV: lo_r = m
    else: hi_r = m
print(f'implied return at the price, bottom case: {lo_r:.2%}')
