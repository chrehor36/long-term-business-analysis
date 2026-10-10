# COMPUTATION, NOT A CLEARANCE. AMAT run 2026-10-07. Arithmetic only; every input is a filed line (USD millions).
# Sources: XBRL company facts (facts.json) checked against the 10-K cash-flow statements; interest income from the
# FY2023 10-K note (2021-2023) and XBRL InvestmentIncomeInterest (2023-2025).
yrs = list(range(2014, 2026))
OCF = dict(zip(yrs, [1800,1163,2566,3789,3787,3247,3804,5442,5399,8700,8677,7958]))
SBC = dict(zip(yrs, [177,187,201,220,258,263,307,346,413,490,577,668]))
CAPEX = dict(zip(yrs, [241,215,253,345,622,441,422,668,787,1106,1190,2260]))
# D&A: 2014-2018 = depreciation + amortization of intangibles (XBRL); 2019-2022 DepreciationDepletionAndAmortization;
# 2023-2025 segment-note totals (10-K FY2025): 515, 392, 435
DA = dict(zip(yrs, [191+184,185+186,200+189,214+193,258+199,363,376,394,444,515,392,435]))
ACQ = dict(zip(yrs, [12,4,16,68,6,28,107,12,441,25,0,29]))
FLP = {2023:7, 2024:102}          # finance-lease principal (financing section), counted as capital spending
INT_EXP = {2021:236,2022:228,2023:238,2024:247,2025:269}
INT_INC = {2021:26,2022:44,2023:262,2024:486,2025:406}
T = 0.21   # CONVENTION of this run: after-tax interest at the US statutory rate (the filer's reconciliation starts at 21%)

def oc_all(y):   # all spending: OCF - SBC - capex - acquisitions - finance-lease principal
    return OCF[y]-SBC[y]-CAPEX[y]-ACQ[y]-FLP.get(y,0)
def oc_maint(y): # maintenance only, depreciation as the maintenance guess (M1998-127), acquisitions deducted
    return OCF[y]-SBC[y]-DA[y]-ACQ[y]-FLP.get(y,0)
def unlev(y, f): # all-equity: add back after-tax interest expense, remove after-tax interest income on the cash
    return f(y) + (INT_EXP[y]-INT_INC[y])*(1-T)

print("year   OCF   SBC capex  D&A  acq | OC all  OC maint")
for y in yrs:
    print(y, f"{OCF[y]:5} {SBC[y]:5} {CAPEX[y]:5} {DA[y]:4} {ACQ[y]:4} | {oc_all(y):6} {oc_maint(y):7}")

W = range(2021, 2026)
def mean(f, ys): return sum(f(y) for y in ys)/len(ys)
def cagr(a, b, n): return (b/a)**(1/n)-1
r = 0.0564
def value(C, g, rate=r, n=10):
    v = 0; c = C
    for t in range(1, n+1):
        c *= (1+g); v += c/(1+rate)**t
    return v + c/rate/(1+rate)**n          # after year ten: zero nominal growth (the PG specific)

SH = 793.597; PRICE = 530.27
CASH_SEC = 14501; DEBT = 1299+5245          # 10-Q July 26, 2026: cash+ST+LT investments; short-term + long-term debt
NET_DEBT = DEBT - CASH_SEC                  # negative = net cash
MCAP = SH*PRICE
print(f"\nmarket cap {MCAP:,.0f}  net debt {NET_DEBT:,}  EV {MCAP+NET_DEBT:,.0f}")

def solve_g(C, target, rate=r):
    lo, hi = -0.5, 0.5
    for _ in range(200):
        m = (lo+hi)/2
        if value(C, m, rate) < target: lo = m
        else: hi = m
    return m

def report(label, f_eq, ys, g_override=None, base_override=None):
    out = {}
    for basis, f in (("equity-only", f_eq), ("all-equity", lambda y: unlev(y, f_eq))):
        C = base_override[basis] if base_override else mean(f, ys)
        g = g_override[basis] if g_override else cagr(f(ys[0]), f(ys[-1]), len(ys)-1)
        g_cap = g    # specific (f): inside the ten years the shown rate is the cap; nothing above the discount rate after
                     # year ten (the value function carries zero nominal growth after year ten)
        v0 = value(C, 0.0); vg = value(C, g_cap)
        lo, hi = min(v0, vg), max(v0, vg)
        if basis == "all-equity":
            lo_s, hi_s = (lo-NET_DEBT)/SH, (hi-NET_DEBT)/SH
        else:
            lo_s, hi_s = lo/SH, hi/SH
        mid = (lo+hi)/2
        gm = solve_g(C, mid)
        fair_total = value(C, gm, 0.10)
        fair = (fair_total-NET_DEBT)/SH if basis == "all-equity" else fair_total/SH
        out[basis] = (C, g, g_cap, lo_s, hi_s, hi/lo, fair, gm)
        print(f"{label:38} {basis:11} base {C:7,.0f} g shown {g*100:5.1f}% used {g_cap*100:5.1f}%  "
              f"range ${lo_s:6.0f} - ${hi_s:6.0f} /sh (width {hi/lo:4.2f}x)  fair ${fair:6.0f}  (mid-case g {gm*100:4.1f}%)")
    return out

print()
report("LITERAL WINDOW FY2021-25, maint-only", oc_maint, list(W))
report("LITERAL WINDOW FY2021-25, all spending", oc_all, list(W))
# whole-cycle variant (CONVENTION of this run): no second trough since FY2019, so the base is the FY2019-FY2025 average
# (trough to latest) and the growth is measured between the FY2014-FY2018 average and the FY2019-FY2025 average
A = list(range(2014, 2019)); B = list(range(2019, 2026))
def cyc(f):
    gA = mean(f, A); gB = mean(f, B)
    span = (sum(B)/len(B)) - (sum(A)/len(A))
    return gB, cagr(gA, gB, span)
for nm, f in (("maint-only", oc_maint), ("all spending", oc_all)):
    # unlevered adjustment only available 2021-2025; the cycle variant is shown on the equity basis, with the
    # all-equity base taken as the equity base plus the FY2021-25 mean interest adjustment
    adj = sum((INT_EXP[y]-INT_INC[y])*(1-T) for y in W)/5
    bE, gE = cyc(f)
    report(f"WHOLE CYCLE FY2019-25 base, {nm}", f, list(B),
           g_override={"equity-only": gE, "all-equity": gE},
           base_override={"equity-only": bE, "all-equity": bE+adj})

# the price's implied growth, all-equity, maint-only base
C = mean(lambda y: unlev(y, oc_maint), list(W))
print(f"\nall-equity maint-only base {C:,.0f}; EV at price {MCAP+NET_DEBT:,.0f}; growth for ten years the price needs at 5.64%: "
      f"{solve_g(C, MCAP+NET_DEBT)*100:.1f}%; at 10%: {solve_g(C, MCAP+NET_DEBT, 0.10)*100:.1f}%")
C2 = mean(oc_maint, list(W))
print(f"owner-cash yield at price, equity-only maint-only: {C2/MCAP*100:.2f}%; all spending: {mean(oc_all, list(W))/MCAP*100:.2f}%")
# tax sensitivity: cash taxes paid / pre-tax income FY2021-25 against 21% statutory
tp = [851,1869,1006,957,1504]; pti = [6771,7599,7716,8152,9271]
print(f"cash tax rate FY2021-25 {sum(tp)/sum(pti)*100:.1f}%; extra tax at 21% statutory per year {(0.21*sum(pti)-sum(tp))/5:,.0f}")
