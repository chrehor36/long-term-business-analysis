# COMPUTATION, NOT A CLEARANCE: the literal 2021-2025 window shown beside the cycle base (specific (a)); its end-to-end
# change is negative, so by specific (b) the decline is the bottom and no growth the top.
exec(open('q7.py').read().split("print('maintenance-only")[0])
for maint, nm in ((True, 'maintenance-only'), (False, 'all-spending')):
    s = series(maint, True)
    lit = avg(s, 2021, 2025)
    if s[Y[2021]] > 0 and s[Y[2025]] > 0:
        g = (s[Y[2025]]/s[Y[2021]])**(1/4) - 1
    else:   # sign change: first half against second half of the window
        g = (avg(s, 2024, 2025)/avg(s, 2021, 2022))**(1/2.5) - 1 if avg(s, 2024, 2025) > 0 else None
    f = lambda v: (v - netdebt) * parent_book / shares * 10
    if g is None:
        print(nm, 'literal avg', round(lit), 'halves meaningless; no-growth only', round(f(pv(lit, 0, r)), 2), '/ADS; at 10%:', round(f(pv(lit, 0, floor)), 2))
        continue
    lo, hi = pv(lit, g, r), pv(lit, 0, r)
    lo10, hi10 = pv(lit, g, floor), pv(lit, 0, floor)
    print(f'{nm}: literal avg {lit:.0f}, end-to-end growth {g*100:.1f}%/yr; range ${f(lo):.2f}-${f(hi):.2f}/ADS; fair ${(f(lo10)+f(hi10))/2:.2f}/ADS')
