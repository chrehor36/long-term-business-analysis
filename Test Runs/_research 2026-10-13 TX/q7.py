# COMPUTATION, NOT A CLEARANCE (TX run 2026-10-13). Filed figures in $ million; see run file for sources.
yrs  = list(range(2015, 2026))
cfo  = [1323,1100, 384,1739,1648,1761,2677,2753,2501,1906,2314]   # net cash from operating activities
capx = [ 467, 435, 409, 520,1052, 560, 524, 581,1461,1865,2501]   # capital expenditures (cash line)
lease= [   0,   0,   4,   8,  39,  42,  46,  49,  59,  61,  65]   # lease payments (financing)
da   = [ 434, 407, 474, 589, 661, 631, 592, 616, 658, 743, 788]   # depreciation and amortization
ipaid= [  84,  77,  95, 144, 101,  56,  36,  43, 134, 195, 222]
irec = [   8,  14,  19,  21,  29,  49,  63,  32, 202, 263, 213]   # 2015-2019: filed interest income (no cash line tagged)
acq  = [   0,   0,1891,   0,5.8,  17, 0.8, 4.2,118.7,  0,   0]   # businesses and minority stakes bought for cash (2023: consideration paid only)
sales= [7877,7224,9700,11455,10193,8735,16091,16414,17610,17649,15609]
Y = {y:i for i,y in enumerate(yrs)}
def series(maint, before_interest):
    out=[]
    for i in range(len(yrs)):
        spend = da[i] if maint else capx[i] + lease[i]
        oc = cfo[i] - spend - acq[i]
        if before_interest: oc += ipaid[i] - irec[i]
        out.append(oc)
    return out
def avg(s, a, b): return sum(s[Y[a]:Y[b]+1]) / (b - a + 1)
r, floor = 0.056, 0.10
def pv(c, g, d, n=10):
    v = sum(c*(1+g)**t/(1+d)**t for t in range(1, n+1))
    return v + c*(1+g)**n/d/(1+d)**n
shares = 1963.076776            # million shares outstanding (issued 2,004,743,442 less 41,666,666 treasury)
netdebt = 2843.752 + 206.896 - 1430.687 - 1300.918   # 30 Jun 2026: borrowings + leases - cash - other investments
csn = 599.1                     # CSN litigation provision, 30 Jun 2026 (shown beside, not in net debt)
parent_book = 12299.555/16739.014          # owners' share of total equity, 30 Jun 2026
parent_profit = 1 - (542+325+310+227-122)/(4367+2093+986+174+303)   # 2021-2025 cumulative profit split
price_ads = 58.99
print('maintenance-only owner cash (CFO - D&A - acquisitions), equity-only:')
for y, v in zip(yrs, series(True, False)): print(' ', y, round(v), ' all-spending', round(series(False, False)[Y[y]]))
for label, maint in (('MAINTENANCE-ONLY (central, specific e)', True), ('ALL-SPENDING (beside)', False)):
    for basis, bi in (('all-equity', True), ('equity-only', False)):
        s = series(maint, bi)
        c1, c2 = avg(s, 2015, 2019), avg(s, 2019, 2025)
        lit = avg(s, 2021, 2025)
        g_shown = (c2/c1)**(1/5) - 1 if c1 > 0 else float('nan')
        sg = (avg(sales, 2019, 2025)/avg(sales, 2015, 2019))**(1/5) - 1
        g_lit = (s[Y[2025]]/s[Y[2021]])**(1/4) - 1 if s[Y[2021]] > 0 and s[Y[2025]] > 0 else float('nan')
        print(f'\n{label}, {basis}: cycle 2015-19 avg {c1:.0f}, cycle 2019-25 avg {c2:.0f}, shown growth {g_shown*100:.1f}%/yr; sales growth same cycles {sg*100:.1f}%/yr; literal 2021-25 avg {lit:.0f}, literal end-to-end growth {g_lit*100 if g_lit==g_lit else float("nan"):.1f}%')
        g = min(g_shown, sg) if g_shown == g_shown else 0.0
        for nm, base in (('cycle base', c2), ('literal window', lit)):
            lo, hi = pv(base, 0, r), pv(base, g, r)
            lo10, hi10 = pv(base, 0, floor), pv(base, g, floor)
            for share_nm, ps in (('book share', parent_book), ('profit share', parent_profit)):
                if basis == 'all-equity':
                    f = lambda v: (v - netdebt) * ps / shares
                    fc = lambda v: (v - netdebt - csn) * ps / shares
                else:
                    f = lambda v: v * ps / shares
                    fc = lambda v: (v - csn) * ps / shares
                print(f'  {nm:15s} {share_nm:12s} range ${f(lo):.2f}-${f(hi):.2f}/sh (${f(lo)*10:.2f}-${f(hi)*10:.2f}/ADS), width {hi/lo if lo>0 else float("nan"):.2f}x; '
                      f'fair (avg of ends at 10%) ${(f(lo10)+f(hi10))/2:.2f}/sh ${(f(lo10)+f(hi10))*5:.2f}/ADS; growth end at 10% ${f(hi10)*10:.2f}/ADS; with CSN provision fair ${(fc(lo10)+fc(hi10))*5:.2f}/ADS')
print(f'\nprice ${price_ads}/ADS = ${price_ads/10:.3f}/share; market value ${price_ads/10*shares:,.0f}M; net debt 30 Jun 2026 ${netdebt:.0f}M; parent book share {parent_book:.3f}; parent profit share {parent_profit:.3f}')
