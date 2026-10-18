# COMPUTATION, NOT A CLEARANCE: Q7 range and fair price for UHS, USD millions.
import sys; sys.stdout.reconfigure(encoding='utf-8')
Y = [2021, 2022, 2023, 2024, 2025]
OCF = {2021: 884.0, 2022: 996.0, 2023: 1267.797, 2024: 2067.101, 2025: 1864.397}
SBC = {2021: 74.0, 2022: 85.0, 2023: 87.720, 2024: 99.349, 2025: 95.688}
CAPEX = {2021: 855.659, 2022: 734.001, 2023: 743.055, 2024: 943.810, 2025: 1015.152}
DA = {2021: 533.0, 2022: 582.0, 2023: 568.041, 2024: 584.831, 2025: 618.743}
NCI = {2021: 7.0, 2022: 5.0, 2023: 7.0, 2024: 7.0, 2025: 12.0}          # dividends to minority partners
FLP = {2021: 0.0, 2022: 0.0, 2023: 4.0, 2024: 4.0, 2025: 2.0}            # finance-lease principal (2021-22 not found)
ERP = {2021: 0.0, 2022: 0.0, 2023: 0.0, 2024: 0.0, 2025: 24.695}         # ERP application spending, investing section
CARES = {2021: 695.0 + 84.0, 2022: 94.0, 2023: 0, 2024: 0, 2025: 0}      # repayments of 2020 advances and deferred payroll tax
ACQ = {2021: 105.415 - 25.425, 2022: 20.309 - 12.001, 2023: 3.728 - 24.187, 2024: 18.998 - 38.563, 2025: 47.804 - 15.863}
INTPAID = {2021: 76.0, 2022: 120.0, 2023: 200.0, 2024: 168.0, 2025: 156.0}
TAXR = {2021: 306/1293, 2022: 209/866, 2023: 221/940, 2024: 335/1498, 2025: 461/1972}
SH = 58.936515; PRICE = 178.90; R = 0.056; FLOOR = 0.10
ND0 = 771.910 + 4079.937 - 138.800          # 2026-06-30 debt (current + long-term) less cash
TALK = 835.0 - 37.0; IRE = 188.0            # subsequent events stated: Talkspace financing less its cash; Ireland
ND = ND0 + TALK + IRE
ADD_INT_AT = (TALK + IRE) * 0.0575 * (1 - 0.234)   # after-tax interest on the added debt, equity-only basis
def oc(y, cares=True, da=False):
    spend = DA[y] if da else CAPEX[y] + ERP[y]
    return OCF[y] - SBC[y] - spend - NCI[y] - FLP[y] + (CARES[y] if cares else 0)
def value(b, g, r):
    v = 0; c = b
    for t in range(1, 11):
        c *= (1 + g); v += c / (1 + r) ** t
    return v + c / r / (1 + r) ** 10
def growth(a, z):
    return (z / a) ** (1 / 4) - 1 if a > 0 and z > 0 else None
def show(label, series, nd, shares=SH, extra=''):
    b = sum(series[y] for y in Y) / 5
    g = growth(series[2021], series[2025])
    gl = g if g is not None else 0.0
    ng = value(b, 0.0, R); gg = value(b, gl, R)
    lo, hi = sorted([ng, gg])
    ps = lambda v: (v - nd) / shares
    fair = ((value(b, 0.0, FLOOR) + value(b, gl, FLOOR)) / 2 - nd) / shares
    ev = PRICE * shares + nd
    # expected return at the price on each end: solve r such that value(b,g,r) = ev
    def irr(gx):
        a, z = 0.0001, 0.5
        for _ in range(100):
            m = (a + z) / 2
            if value(b, gx, m) > ev: a = m
            else: z = m
        return m
    print(f"{label}: base {b:,.0f}  growth {('%.2f%%' % (g*100)) if g is not None else 'n/a'}  "
          f"range ${ps(lo):,.2f} to ${ps(hi):,.2f} a share (whole business {lo:,.0f} to {hi:,.0f}; net debt {nd:,.0f})  "
          f"width {hi/lo if lo>0 else float('nan'):.2f}x  fair ${fair:,.2f}  return at price: no-growth {irr(0)*100:.2f}%, growth {irr(gl)*100:.2f}% {extra}")
    return b, gl
unlev = {y: oc(y) + INTPAID[y] * (1 - TAXR[y]) - ACQ[y] for y in Y}
lev = {y: oc(y) - ACQ[y] for y in Y}
print('owner cash after interest, CARES-corrected, before acquisitions:', {y: round(oc(y)) for y in Y})
print('literal (no CARES correction):', {y: round(oc(y, cares=False)) for y in Y})
print('unlevered, after acquisitions:', {y: round(unlev[y]) for y in Y})
print('levered, after acquisitions:', {y: round(lev[y]) for y in Y})
print(f'net debt: 2026-06-30 {ND0:,.1f}; plus Talkspace {TALK:,.0f} and Ireland {IRE:,.0f} = {ND:,.1f}; market cap {PRICE*SH:,.0f}')
print('--- CENTRAL: all-equity basis, all spending, acquisitions deducted, total growth (default pair)')
show('central all-equity', unlev, ND)
lev2 = {y: lev[y] - ADD_INT_AT for y in Y}
print('--- beside: equity-only (after interest; after-tax interest on the added debt %.0f deducted each year)' % ADD_INT_AT)
show('equity-only', lev2, 0.0)
print('--- beside: literal window, no CARES correction (all-equity)')
show('literal all-equity', {y: oc(y, cares=False) + INTPAID[y]*(1-TAXR[y]) - ACQ[y] for y in Y}, ND)
print('--- beside: depreciation variant (D&A in place of capital spending), all-equity')
show('D&A variant', {y: oc(y, da=True) + INTPAID[y]*(1-TAXR[y]) - ACQ[y] for y in Y}, ND)
print('--- beside: organic pair (acquisitions left out; filer reports same-facility revenue growth, not organic owner cash)')
show('organic (no acq deducted, same growth)', {y: oc(y) + INTPAID[y]*(1-TAXR[y]) for y in Y}, ND)
# sensitivity: company's own estimate of the OBBBA cut, ~$500M pretax by 2032, phased 2028-2032, after tax at 23.4%
def value_cut(b, g, r, cut=500*(1-0.234)):
    v = 0; c = b
    for t in range(1, 11):
        c *= (1 + g); yr = 2026 + t
        k = 0 if yr < 2028 else min(1, (yr - 2027) / 5)
        v += (c - cut * k) / (1 + r) ** t
    return v + (c - cut) / r / (1 + r) ** 10
b = sum(unlev[y] for y in Y) / 5; g = growth(unlev[2021], unlev[2025])
lo, hi = value_cut(b, 0, R), value_cut(b, g, R)
print(f"--- beside (sensitivity, the company's own OBBBA estimate deducted): range ${(lo-ND)/SH:,.2f} to ${(hi-ND)/SH:,.2f}; fair ${((value_cut(b,0,FLOOR)+value_cut(b,g,FLOOR))/2-ND)/SH:,.2f}")
