# DPMAY run 2026-10-12: owner cash and the Q7 range, every input from the filed statements (GBP m).
# Sources: the consolidated cash flow statements of the Annual Reports FY2016 to FY2025 (each year's own report,
# current-year column), statement of changes in equity for share-based payments. Run: python calc.py
FY = list(range(2016, 2026))
ncfo   = dict(zip(FY, [58.4, 59.6, 65.3, 70.3, 85.4, 116.1, 125.0, 189.2, 198.1, 267.6]))  # net cash from operating activities (after interest and tax paid)
ppe    = dict(zip(FY, [3.5, 3.1, 5.3, 9.7, 8.4, 4.9, 14.3, 21.6, 18.9, 13.4]))
intang = dict(zip(FY, [0.2, 0.2, 1.3, 1.2, 1.0, 1.3, 1.1, 1.5, 0.8, 1.0]))
ppe_in = dict(zip(FY, [2.4, 0.1, 0.0, 0.0, 5.8, 4.8, 9.9, 1.5, 5.7, 1.3]))
lease  = dict(zip(FY, [0, 0, 0, 0, 7.6, 9.5, 10.9, 13.9, 16.0, 14.6]))  # IFRS 16 from FY2020; before, rentals sat inside ncfo
sbc    = dict(zip(FY, [0.4, 0.8, 1.0, 0.8, 0.8, 1.8, 2.8, 4.1, 7.1, 6.2]))  # share-based payments, SOCE
intp   = dict(zip(FY, [0.6, 0.4, 0.0, 0.1, 1.5, 5.6, 15.0, 26.7, 23.2, 26.3]))  # interest paid, net
acq    = dict(zip(FY, [30.1, 19.5, 18.1, 77.2, 13.8, 451.4, 173.0, 258.5, 270.5, 53.8]))  # businesses, net of cash acquired
defer  = dict(zip(FY, [0.7, 0.6, 0.3, 1.1, 1.1, 6.6, 7.1, 12.3, 10.3, 4.7]))
mino   = dict(zip(FY, [0, 0, 2.0, 0, 0, 0, 0.3, 0, 0, 0.8]))
disp   = dict(zip(FY, [2.2, 0.0, 4.0, 0.0, 0.8, 11.0, 13.7, 21.5, 0.0, 40.3]))
rev    = dict(zip(FY, [382.6, 451.9, 485.1, 544.7, 538.4, 787.4, 1012.8, 1200.3, 1363.4, 1524.5]))
TAX = 0.25  # UK statutory rate, AR2025 note 7 (CONVENTION of this run: interest added back after tax at this rate)

oc, ocu, a = {}, {}, {}
print('FY   ncfo  capex  lease  sbc | OC(eq)  OC(unlev)  acq(net)  OC/sales')
for y in FY:
    oc[y] = ncfo[y] - ppe[y] - intang[y] + ppe_in[y] - lease[y] - sbc[y]
    ocu[y] = oc[y] + intp[y] * (1 - TAX)
    a[y] = acq[y] + defer[y] + mino[y] - disp[y]
    print(y, f'{ncfo[y]:6.1f} {ppe[y]+intang[y]-ppe_in[y]:6.1f} {lease[y]:5.1f} {sbc[y]:4.1f} | {oc[y]:6.1f} {ocu[y]:8.1f} {a[y]:8.1f}   {100*ocu[y]/rev[y]:5.1f}%')

W = range(2021, 2026)
avg = lambda d: sum(d[y] for y in W) / 5
B, Beq, A = avg(ocu), avg(oc), avg(a)
g_shown = (ocu[2025] / ocu[2021]) ** 0.25 - 1
g_sales = (rev[2025] / rev[2021]) ** 0.25 - 1
print(f'\nwindow FY2021-25: OC unlevered avg {B:.1f}; equity-only avg {Beq:.1f}; acquisitions avg {A:.1f}')
print(f'shown growth of unlevered OC {100*g_shown:.1f}%/yr; sales growth {100*g_sales:.1f}%/yr; FY2016-25 OC growth {100*((ocu[2025]/ocu[2016])**(1/9)-1):.1f}%')
maxshare = max(ocu[y] / rev[y] for y in FY)
share10 = (ocu[2025] / rev[2025]) * ((1 + g_shown) / (1 + g_sales)) ** 10
print(f'highest OC/sales in filings read {100*maxshare:.1f}%; at shown OC growth vs sales growth the share in year 10 = {100*share10:.1f}% -> cut applies' )

R = 0.0605          # BoE GLC nominal 30-year spot, 2026-10-08
SH = 134.236030     # m shares: 134,317,398 TVR 30 Nov 2025 less 81,368 EBT shares at 30 Sep 2025
ND_FILED = 343.9    # net debt 31 Mar 2026 (HY26), borrowings less cash, leases excluded
ND = ND_FILED + 45 + 125  # + post-period acquisitions c.45 (HY26 note 15) + CDM c.125 closed by July 2026 (Q3 transcript)
PRICE = 77.85       # GBP, LSE close 2026-10-09, aggregator

def case(base, acq, g, r, years=10):
    """years 1-10: (base - acq) growing at g; after year 10: base*(1+g)^10, no growth, no purchases."""
    pv = sum((base - acq) * (1 + g) ** t / (1 + r) ** t for t in range(1, years + 1))
    term = base * (1 + g) ** years / r / (1 + r) ** years
    return pv + term

def report(label, base, acqv, g, nd):
    v = case(base, acqv, g, R) - nd
    return v, v / SH

g_cap = min(g_sales, R)   # the (f) cut: sales growth, never above the discount rate
print(f'\ngrowth carried after the cut: min(sales {100*g_sales:.1f}%, rate {100*R:.2f}%) = {100*g_cap:.2f}%')
rows = [
    ('no-growth (no purchases), all-equity', B, 0, 0.0, ND),
    ('growth, acquisitions deducted, cut rate, all-equity', B, A, g_cap, ND),
    ('no-growth, equity-only', Beq, 0, 0.0, 0),
    ('growth, acquisitions deducted, equity-only', Beq, A, g_cap, 0),
]
res = {}
for lab, b, ac, g, nd in rows:
    v, ps = report(lab, b, ac, g, nd)
    res[lab] = ps
    print(f'{lab:55s} value {v:8.0f}m  {ps:6.2f}/share')

# organic pair (acquisitions left out, organic growth as the filer reports it FY22-FY25: 15, 8, 6, 11 %)
g_org = (1.15 * 1.08 * 1.06 * 1.11) ** 0.25 - 1
for lab, b, nd in [('organic pair top, all-equity', B, ND), ('organic pair top, equity-only', Beq, 0)]:
    v = case(b, 0, g_org, R) - nd
    print(f'{lab:55s} g={100*g_org:.1f}% value {v:8.0f}m  {v/SH:6.2f}/share')

# fair price: each end case valued at 10%, averaged
def at10(base, acqv, g, nd):
    return (case(base, acqv, g, 0.10) - nd) / SH
f_ng, f_gr = at10(B, 0, 0.0, ND), at10(B, A, g_cap, ND)
e_ng, e_gr = at10(Beq, 0, 0.0, 0), at10(Beq, A, g_cap, 0)
print(f'\nFAIR all-equity: no-growth {f_ng:.2f}, growth {f_gr:.2f}, average {(f_ng+f_gr)/2:.2f}')
print(f'FAIR equity-only: no-growth {e_ng:.2f}, growth {e_gr:.2f}, average {(e_ng+e_gr)/2:.2f}')
f_o = at10(B, 0, g_org, ND)
print(f'FAIR organic pair (all-equity): no-growth {f_ng:.2f}, organic {f_o:.2f}, average {(f_ng+f_o)/2:.2f}')

# floor test at the price: return at which the best defensible case equals the price
EV = PRICE * SH + ND
print(f'\nmarket cap {PRICE*SH:.0f}m, EV {EV:.0f}m; OC yield on EV {100*B/EV:.2f}%')
def irr(base, acqv, g):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if case(base, acqv, g, mid) > EV: lo = mid
        else: hi = mid
    return mid
for lab, b, ac, g in [('no-growth', B, 0, 0.0), ('growth cut', B, A, g_cap), ('organic pair', B, 0, g_org),
                      ('shown 23.9% uncut, acq deducted (not allowed, shown only)', B, A, g_shown)]:
    print(f'expected return at the price, {lab}: {100*irr(b, ac, g):.2f}%')

# sensitivities
print('\nnet debt at the filed date with stated subsequent completions only (343.9+45):',
      f'no-growth {(case(B,0,0,R)-(ND_FILED+45))/SH:.2f}/share')
dep_var = B - 2.0
print(f'depreciation variant (capex replaced by depreciation, about 2m lower): no-growth {(case(dep_var,0,0,R)-ND)/SH:.2f}/share')
for oc_alt in (2 * B,):
    print(f'if owner cash doubled to {oc_alt:.0f}: no-growth {(case(oc_alt,0,0,R)-ND)/SH:.2f}/share')

# variants shown beside the central figures (none decides the box)
A_ex21 = sum(a[y] for y in range(2022, 2026)) / 4
print(f'\nVARIANTS (all-equity, per share at the 6.05% rate; expected return at the price)')
for lab, b, ac, g in [('sales growth 18.0% uncapped, acq deducted', B, A, g_sales),
                      ('shown 23.9% uncut, acq deducted', B, A, g_shown),
                      (f'cut rate, acq avg FY22-25 only ({A_ex21:.1f})', B, A_ex21, g_cap),
                      ('organic 9.9%, no acq', B, 0, g_org)]:
    v = (case(b, ac, g, R) - ND) / SH
    print(f'{lab:45s} {v:7.2f}/share   return at price {100*irr(b, ac, g):.2f}%')
print(f'top/bottom width of central range: {res["no-growth (no purchases), all-equity"]/res["growth, acquisitions deducted, cut rate, all-equity"]:.2f} to 1')
