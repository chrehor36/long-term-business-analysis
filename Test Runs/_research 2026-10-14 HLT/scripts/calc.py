# HLT run 2026-10-14: arithmetic only. Every input is a filed figure (USD millions), source in comments.
Y = list(range(2017, 2026))
# Cash flow statements: FY2019 10-K 0001585689-20-000013 (2017-2019); FY2022 10-K 0001585689-23-000036 (2020-2022);
# FY2025 10-K 0001585689-26-000007 (2023-2025)
OCF  = dict(zip(Y, [849,1255,1384,708,109,1681,1946,2013,2129]))
SBC  = dict(zip(Y, [121,127,154,97,193,162,169,176,170]))
CAPX = dict(zip(Y, [58,72,81,46,35,39,151,96,101]))
SOFT = dict(zip(Y, [75,87,124,46,44,63,96,102,84]))
ACQ  = dict(zip(Y, [0,0,0,0,0,0,0,236,4]))
FLP  = dict(zip(Y, [None,None,42,26,40,42,40,38,41]))   # finance lease principal, XBRL FinanceLeasePrincipalPayments (financing section)
INTP = dict(zip(Y, [314,330,360,433,359,383,492,562,648]))  # cash interest paid (supplemental)
TAXP = dict(zip(Y, [526,288,363,79,181,389,478,492,523]))   # cash income taxes paid
KEY  = dict(zip(Y, [75,103,90,50,200,81,233,105,231]))      # contract acquisition costs, inside OCF
ADV  = dict(zip(Y, [334+29,-18+207,-17+191,215+610,-128-105,174+31,215+337,330+242,542-61]))  # change in deferred revenues + loyalty liability, inside OCF
# Segment revenues (FY2019 10-K note 18; FY2022 10-K note 17; FY2025 10-K note 18)
MF   = dict(zip(Y, [1927,2157,2315,1138,1809,2619,3055,3339,3575]))
TOTR = dict(zip(Y, [8131,8906,9452,4307,5788,8773,10235,11174,12039]))
REIM = dict(zip(Y, [2572+2155,2881+2357,3110+2576,1375+1332,1503+1841,2441+2596,5827,6428,7085]))
SALES = {y: TOTR[y]-REIM[y] for y in Y}
OPI  = dict(zip(Y, [1132,1432,1657,-418,1010,2094,2225,2370,2693]))
T = 0.21  # CONVENTION of this run: after-tax interest at the 21% U.S. federal statutory rate
print("year   OCF  SBC capex soft acq  FLP  ownerCash(eq) ownerCash+aftertaxInt  sales  oc/sales  advances key")
OC, OCU = {}, {}
for y in Y:
    flp = FLP[y] or 0
    OC[y] = OCF[y]-SBC[y]-CAPX[y]-SOFT[y]-ACQ[y]-flp
    OCU[y] = OC[y] + INTP[y]*(1-T)
    print(f"{y} {OCF[y]:5} {SBC[y]:4} {CAPX[y]:4} {SOFT[y]:4} {ACQ[y]:4} {str(FLP[y]):>4} {OC[y]:10} {OCU[y]:12.0f} {SALES[y]:8} {OC[y]/SALES[y]:7.1%} {ADV[y]:6} {KEY[y]:4}")
avg = lambda d, ys: sum(d[y] for y in ys)/len(ys)
cyc = range(2019, 2026); win = range(2021, 2026)
for name, ys in (("cycle 2019-2025", cyc), ("literal window 2021-2025", win)):
    print(f"{name}: owner cash eq {avg(OC,ys):.0f}; all-equity {avg(OCU,ys):.0f}; before acquisitions eq {avg({y:OC[y]+ACQ[y] for y in Y},ys):.0f}; key money avg {avg(KEY,ys):.0f}; advances avg {avg(ADV,ys):.0f}")
h1, h2 = avg(OCU, range(2019,2022)), avg(OCU, range(2023,2026))
print(f"halves (all-equity): 2019-21 {h1:.0f}, 2023-25 {h2:.0f}; growth over 4 yrs {(h2/h1)**0.25-1:.1%}")
print(f"peak-to-peak owner cash 2019->2025 (eq) {(OC[2025]/OC[2019])**(1/6)-1:.1%}; all-equity {(OCU[2025]/OCU[2019])**(1/6)-1:.1%}")
print(f"sales (before reimbursements) 2019->2025 {(SALES[2025]/SALES[2019])**(1/6)-1:.1%}; M&F fees 2019->2025 {(MF[2025]/MF[2019])**(1/6)-1:.1%}")
print(f"highest owner cash / sales in years read: {max(OC[y]/SALES[y] for y in Y):.1%} ({max(Y, key=lambda y: OC[y]/SALES[y])})")
# a 9.9% rate carried ten years against sales at 4.7%
g_oc = (OC[2025]/OC[2019])**(1/6)-1; g_s=(SALES[2025]/SALES[2019])**(1/6)-1
print(f"test (f): 2025 share {OC[2025]/SALES[2025]:.1%} carried ten years at {g_oc:.1%} vs sales at {g_s:.1%} -> {OC[2025]*(1+g_oc)**10/(SALES[2025]*(1+g_s)**10):.1%}")

def value(C, g, r, n=10):
    pv = sum(C*(1+g)**t/(1+r)**t for t in range(1, n+1))
    term = C*(1+g)**n/r/(1+r)**n
    return pv+term
def irr(C, g, ev):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        m=(lo+hi)/2
        if value(C,g,m) > ev: lo=m
        else: hi=m
    return m
RF = 0.0556; SH = 225.064910; PRICE = 329.59
# Net debt at 2026-06-30 (10-Q 0001585689-26-000043): debt and finance leases at face 13,444 less cash 1,009 (restricted 55 left out)
ND = 13444 - 1009
EV = PRICE*SH + ND
print(f"\nprice {PRICE} x {SH}M = cap {PRICE*SH:,.0f}; net debt {ND:,}; EV {EV:,.0f}")
CU = avg(OCU, cyc); CE = avg(OC, cyc)
CUm = CU + avg(KEY, cyc)   # maintenance variant: all contract acquisition costs treated as growth (upper bound)
sh2 = (avg(SALES,range(2023,2026))/avg(SALES,range(2019,2022)))**0.25-1
print(f"sales growth between the same halves (carries the 2020-21 trough): {sh2:.1%}")
cases = [("no growth", 0.0), ("shown growth, cut to M&F fee growth 7.5%", (MF[2025]/MF[2019])**(1/6)-1), ("sales growth 4.7%", g_s), ("EXTREME: sales growth between halves", sh2), ("EXTREME: uncut halves growth 28.4%", (h2/h1)**0.25-1)]
for lab, C, base in (("ALL-EQUITY (central)", CU, "EV"), ("ALL-EQUITY, key money as growth", CUm, "EV"), ("EQUITY-ONLY", CE, "cap")):
    print(f"\n{lab}: base {C:.0f}")
    for cl, g in cases:
        v = value(C, g, RF); v10 = value(C, g, 0.10)
        if base == "EV":
            ps, ps10 = (v-ND)/SH, (v10-ND)/SH; ret = irr(C, g, EV)
        else:
            ps, ps10 = v/SH, v10/SH; ret = irr(C, g, PRICE*SH)
        print(f"  {cl:45} value@{RF:.2%} {v:9,.0f} -> ${ps:8.2f}/sh ; @10% ${ps10:8.2f}/sh ; expected return at price {ret:.2%}")
# literal window beside
CUw = avg(OCU, win); CEw = avg(OC, win)
gw = (OCU[2025]/OCU[2021])**0.25-1
print(f"\nliteral window 2021-2025 all-equity base {CUw:.0f}; end-to-end growth {gw:.1%} (from a negative-to-low 2021, meaningless; cut by (f))")
for cl, g in cases:
    print(f"  {cl:45} @rf ${(value(CUw,g,RF)-ND)/SH:8.2f}/sh ; @10% ${(value(CUw,g,0.10)-ND)/SH:8.2f}/sh ; return at price {irr(CUw,g,EV):.2%}")
# 2025 alone, as a sensitivity only
C25 = OCU[2025]
print(f"\n2025 alone (sensitivity, not the convention) all-equity {C25:.0f}: return at price, 7.5% growth {irr(C25,cases[1][1],EV):.2%}")
# fair price: each end valued at 10%, averaged
lo = (value(CU,0.0,0.10)-ND)/SH; hi=(value(CU,cases[1][1],0.10)-ND)/SH
loE = value(CE,0.0,0.10)/SH; hiE = value(CE,cases[1][1],0.10)/SH
print(f"\nFAIR PRICE all-equity: ends ${lo:.2f} and ${hi:.2f} -> ${(lo+hi)/2:.2f}; equity-only ends ${loE:.2f}, ${hiE:.2f} -> ${(loE+hiE)/2:.2f}")
loM = (value(CUm,0.0,0.10)-ND)/SH; hiM=(value(CUm,cases[1][1],0.10)-ND)/SH
print(f"fair price, key-money-as-growth variant: ${(loM+hiM)/2:.2f}")
# buybacks: prices paid
print("\nbuyback prices paid: 2025 $3,182M incl excise / 12.5M sh ~= $", round(3182/12.5,2), "; Q4 2025 $272.40; H1 2026 $314.62; Q2 2026 $326.99")
