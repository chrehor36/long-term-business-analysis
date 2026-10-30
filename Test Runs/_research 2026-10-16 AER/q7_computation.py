# COMPUTATION, NOT A CLEARANCE. AER owner cash and the Q7 range under the v5 conventions.
# All figures USD millions, from the filed cash-flow statements (20-F FY2025 0001628280-26-007513,
# FY2023 0001378789-24-000010, FY2021 0001378789-22-000006) and income statements / balance sheets.
# Russia insurance recoveries (investing) are left out of every year: one-off, aberrational.
Y = [2021, 2022, 2023, 2024, 2025]
OCF  = {2021:3694, 2022:5171, 2023:5261, 2024:5437, 2025:5393}
SBC  = {2021:96,   2022:103,  2023:97,   2024:111,  2025:166}
DT   = {2021:-6,   2022:-10,  2023:280,  2024:251,  2025:501}   # deferred tax expense added back in OCF
MREC = {2021:449,  2022:780,  2023:817,  2024:921,  2025:970}   # maintenance payments received (financing)
MRET = {2021:209,  2022:245,  2023:201,  2024:248,  2025:249}   # maintenance payments returned
DA   = {2021:1738, 2022:2390, 2023:2481, 2024:2580, 2025:2647}
GAIN = {2021:89,   2022:229,  2023:490,  2024:651,  2025:819}   # net gain on sale (in investing proceeds)
MRW  = {2021:139,  2022:390,  2023:328,  2024:343,  2025:158}   # maintenance rights write-off (non-cash add-back)
IMP  = {2021:128,  2022:97,   2023:87,   2024:50,   2025:101}
FLC  = {2021:124,  2022:630,  2023:407,  2024:367,  2025:322}   # collections of finance leases (principal, in OCF)
PUR  = {2021:1703, 2022:3480, 2023:4663, 2024:5063, 2025:3654}
PRE  = {2021:86,   2022:391,  2023:1570, 2024:1554, 2025:2420}
PRO  = {2021:797,  2022:1636, 2023:2122, 2024:2675, 2025:2872}
ACQ  = {2021:22493}                                               # GECAS, net of cash acquired
INTP = {2021:1110, 2022:1565, 2023:1650, 2024:1806, 2025:1911}   # interest paid, net of capitalized
LEASEREV = {2021:4412, 2022:6531, 2023:6860, 2024:7004, 2025:7369}
BASE = {2021:69090, 2022:64041, 2023:64948, 2024:65841, 2025:66657}  # lease-asset base, year-end
TAX = 0.15   # CONVENTION of the run: Pillar Two minimum rate for the interest add-back

def pre(y):  # owner cash before capital spending, book tax charged
    return OCF[y] - SBC[y] - DT[y] + MREC[y] - MRET[y]
caseM = {y: pre(y) - (DA[y] - GAIN[y] + MRW[y] + IMP[y] + FLC[y]) for y in Y}       # maintenance-only (central)
caseA = {y: pre(y) - (PUR[y] + PRE[y] - PRO[y]) for y in Y}                          # all spending, GECAS left out
caseD = {y: caseA[y] - ACQ.get(y, 0) for y in Y}                                     # default pair, GECAS deducted
caseB = {y: pre(y) - ((PUR[y] + PRE[y] - PRO[y]) - (BASE[y] - BASE[y-1])) for y in Y if y >= 2023}  # asset-base check
aeadd = {y: INTP[y] * (1 - TAX) for y in Y}

def avg(d, ys): return sum(d[y] for y in ys) / len(ys)
def value(B, g, r, n=10):
    v = 0.0; c = B
    for t in range(1, n + 1):
        c *= (1 + g); v += c / (1 + r) ** t
    return v + (c / r) / (1 + r) ** n
def irr(B, g, P):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        if value(B, g, m) > P: lo = m
        else: hi = m
    return m

R, FLOOR = 0.0543, 0.10
ND, SH, PX = 41087.1, 157.184065, 147.33
MCAP = SH * PX; EV = MCAP + ND
print(f"market cap {MCAP:,.0f}  net debt {ND:,.0f}  EV {EV:,.0f}")
for name, d in [('M maintenance (central)', caseM), ('A all-spending organic', caseA), ('D default, GECAS deducted', caseD)]:
    print(name, {y: round(d[y]) for y in Y})
print('B asset-base check', {y: round(caseB[y]) for y in caseB})
print('owner cash M / lease revenue', {y: round(caseM[y] / LEASEREV[y] * 100, 1) for y in Y})
g_shown = (caseM[2025] / caseM[2022]) ** (1 / 3) - 1
g_sales = (LEASEREV[2025] / LEASEREV[2022]) ** (1 / 3) - 1
print(f"shown growth M 2022-2025 {g_shown*100:.1f}%  lease revenue growth 2022-2025 {g_sales*100:.1f}%")
print(f"cap test: M base x (1+g)^10 = {avg(caseM,[2022,2023,2024,2025])*(1+g_shown)**10:,.0f} vs lease revenue at own growth "
      f"{LEASEREV[2025]*(1+g_sales)**10:,.0f} -> share {avg(caseM,[2022,2023,2024,2025])*(1+g_shown)**10/(LEASEREV[2025]*(1+g_sales)**10)*100:.0f}% vs highest filed {max(caseM[y]/LEASEREV[y] for y in Y)*100:.1f}%")

def report(label, Beq, Bae, g):
    out = {}
    for basis, B, sub in [('all-equity', Bae, ND), ('equity-only', Beq, 0.0)]:
        lo = (value(B, 0, R) - sub) / SH; hi = (value(B, g, R) - sub) / SH
        f0 = (value(B, 0, FLOOR) - sub) / SH; fg = (value(B, g, FLOOR) - sub) / SH
        price_basis = EV if basis == 'all-equity' else MCAP
        r0 = irr(B, 0, price_basis); rg = irr(B, g, price_basis)
        print(f"  {label:34s} {basis:11s} B={B:7,.0f} g={g*100:4.1f}%  range ${lo:7.2f} to ${hi:7.2f}  "
              f"fair ${ (f0+fg)/2:7.2f} (ends {f0:.2f}/{fg:.2f})  return at price {r0*100:5.2f}% / {rg*100:5.2f}%")
        out[basis] = (lo, hi, (f0 + fg) / 2)
    return out

yrs4 = [2022, 2023, 2024, 2025]; yrs5 = Y
print("\nRANGES at the sovereign 5.43%, fair price at 10%, per share; return at price = discount rate equating value to price")
c = report('M central, base 2022-2025', avg(caseM, yrs4), avg(caseM, yrs4) + avg(aeadd, yrs4), g_sales)
report('M literal window 2021-2025', avg(caseM, yrs5), avg(caseM, yrs5) + avg(aeadd, yrs5), g_sales)
report('A all-spending, base 2022-2025', avg(caseA, yrs4), avg(caseA, yrs4) + avg(aeadd, yrs4), g_sales)
report('B asset-base check, 2023-2025', avg(caseB, [2023,2024,2025]), avg(caseB, [2023,2024,2025]) + avg(aeadd, [2023,2024,2025]), g_sales)
print(f"\nD default pair literal window: average {avg(caseD, yrs5):,.0f} (negative: no positive value; range not computable)")
print(f"bases: M 2022-25 eq {avg(caseM,yrs4):,.0f} ae-add {avg(aeadd,yrs4):,.0f}; M 2021-25 eq {avg(caseM,yrs5):,.0f} ae-add {avg(aeadd,yrs5):,.0f}; A 2022-25 {avg(caseA,yrs4):,.0f}")

# CENTRAL CONSTRUCTION (specific (e)): no-growth end = maintenance-only owner cash M at zero growth;
# growth end = M less the growth spending actually made (that is, the all-spending series A), carried at the
# business's own lease-revenue growth 2022-2025 (4.1%), because M's own shown growth (9.2%) fails cap (f).
print("\nCENTRAL: ends M@0 and A@g (growth spending charged against the growth it buys)")
for basis, Bm, Ba, sub, pb in [('all-equity', avg(caseM,yrs4)+avg(aeadd,yrs4), avg(caseA,yrs4)+avg(aeadd,yrs4), ND, EV),
                               ('equity-only', avg(caseM,yrs4), avg(caseA,yrs4), 0.0, MCAP)]:
    lo = (value(Bm,0,R)-sub)/SH; hi = (value(Ba,g_sales,R)-sub)/SH
    f0 = (value(Bm,0,FLOOR)-sub)/SH; fg = (value(Ba,g_sales,FLOOR)-sub)/SH
    print(f"  {basis:11s} range ${min(lo,hi):.2f} to ${max(lo,hi):.2f} (no-growth end {lo:.2f}, growth end {hi:.2f}); width {max(lo,hi)/min(lo,hi):.2f}x; "
          f"fair ${(f0+fg)/2:.2f} (ends at 10%: {f0:.2f} / {fg:.2f}); return at price {irr(Bm,0,pb)*100:.2f}% / {irr(Ba,g_sales,pb)*100:.2f}%")

# BESIDE, specific (b): the all-spending series A measured between halves of the base years (2022-23 vs 2024-25).
gA = (avg(caseA,[2024,2025]) / avg(caseA,[2022,2023])) ** (1/2) - 1
for basis, Ba, sub, pb in [('all-equity', avg(caseA,yrs4)+avg(aeadd,yrs4), ND, EV), ('equity-only', avg(caseA,yrs4), 0.0, MCAP)]:
    v = (value(Ba,gA,R)-sub)/SH; f = (value(Ba,gA,FLOOR)-sub)/SH
    print(f"BESIDE A at its own halves growth {gA*100:.1f}%: {basis:11s} value at 5.43% ${v:.2f}; at 10% ${f:.2f}; return at price {irr(Ba,gA,pb)*100:.2f}%")
