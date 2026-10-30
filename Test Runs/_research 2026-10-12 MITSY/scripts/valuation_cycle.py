"""Q7 cycle base (specific (a)): FY2022, the first window year, is a commodity peak (profit then a record; the 104th report
calls FY2023 'record levels'), so the base is the average over the cycle FY2017-26 (the year after the FY2016 trough to
the latest year). Growth: only one cycle is in the filings read, so growth is measured between the halves of the cycle
(specific (b)), FY2017-21 against FY2022-26, then capped by the cap test (f) at sales growth FY2019-26 (revenue is not
comparable before FY2019, when IFRS 15 changed its basis). COMPUTATION."""
from valuation import pv, per_share, R, avg, SOV, FLOOR, SHARES, NET_DEBT, MCAP
C = list(range(2017, 2027)); H1 = range(2017, 2022); H2 = range(2022, 2027)
mu, me = avg('oc_maint_u', C), avg('oc_maint', C); au, ae = avg('oc_all_u', C), avg('oc_all', C)
g_halves = (avg('oc_maint_u', H2) / avg('oc_maint_u', H1)) ** 0.2 - 1
g_sales = (13995.2 / 8958.967) ** (1 / 7) - 1
cap_need = mu * (1 + g_halves) ** 10 / 13995.2
charge = (mu - au) * g_sales / g_halves
print(f'cycle avgs: maint all-equity {mu:.1f} equity-only {me:.1f}; all-spending all-equity {au:.1f} equity-only {ae:.1f}')
print(f'growth halves {g_halves:.2%}; carried 10y needs {cap_need:.1%} of FY26 sales (highest seen 5.4%) -> cut to sales growth FY2019-26 {g_sales:.2%}')
print(f'growth spending (maint-all) {mu-au:.1f}; charged for capped growth {charge:.1f}')
EV = MCAP + NET_DEBT
b = (mu, me, 0.0); t = (mu - charge, me - charge, g_sales)
for nm, c in (('bottom no-growth', b), ('top capped growth', t), ('beside all-spending capped growth', (au, ae, g_sales))):
    s, f = pv(c[0], c[2], SOV), pv(c[0], c[2], FLOOR)
    print(f'{nm}: JGB {per_share(s):,.0f}/sh (eq-only {pv(c[1],c[2],SOV)*1000/SHARES:,.0f}); 10%: EV {f:.0f} vs {EV:.0f} -> {per_share(f):,.0f}/sh (eq-only {pv(c[1],c[2],FLOOR)*1000/SHARES:,.0f}); clears {f>=EV}')
lo, hi = per_share(pv(b[0], 0, SOV)), per_share(pv(t[0], t[2], SOV))
fair = (per_share(pv(b[0], 0, FLOOR)) + per_share(pv(t[0], t[2], FLOOR))) / 2
fair_e = (pv(b[1], 0, FLOOR) + pv(t[1], t[2], FLOOR)) / 2 * 1000 / SHARES
print(f'RANGE {lo:,.0f} to {hi:,.0f} width {hi/lo:.2f}; ADS ${lo*20/158.68:,.0f}-${hi*20/158.68:,.0f}')
print(f'FAIR all-equity {fair:,.0f} (ADS ${fair*20/158.68:,.0f}); equity-only {fair_e:,.0f} (ADS ${fair_e*20/158.68:,.0f})')
for nm,c in (('bottom',b),('top',t)):
    lo_r, hi_r = 0.0001, 0.5
    for _ in range(100):
        m=(lo_r+hi_r)/2
        if pv(c[0],c[2],m) > EV: lo_r=m
        else: hi_r=m
    print(f'implied return at price, {nm}: {lo_r:.2%}')
