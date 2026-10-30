# COMPUTATION, NOT A CLEARANCE: the Q7 range and fair price for CDNL, figures in USD millions from the filings named in the run file
import sys; sys.stdout.reconfigure(encoding="utf-8")
T = 0.23          # CONVENTION of this run: statutory rate, 21% federal plus North Carolina 2.25% net of the federal benefit, rounded
R = 0.0543        # 30-year Treasury par yield, 2026-10-16
F = 0.10          # the floor convention
# Cardinal, 10-K FY2025 (0001193125-26-120014) cash-flow statement and MD&A
yrs = [2023, 2024, 2025]
ocf   = [30.883, 42.629, 37.901]
intp  = [3.987, 4.568, 6.543]      # cash paid for interest
taxp  = [0.0, 1.353, 1.691]        # cash paid for taxes (NC pass-through entity tax)
sbc   = [0.0, 0.0, 5.869]
capex = [12.268, 20.755, 43.815]
sale  = [0.804, 0.297, 0.454]
fleq  = [9.028, 4.163, 1.442]      # equipment financed with finance leases (non-cash capital spending)
dep   = [13.181 - 0.003, 18.664 - 0.086, 32.375 - 7.128]   # D&A less amortization of intangibles
ebit  = [29.530, 35.934, 40.404]
acq   = [10.895, 0.0, 59.398]
rev   = [247.924, 315.188, 456.045]
def oc(i, maint):
    spend = dep[i] if maint else (capex[i] - sale[i] + fleq[i])
    return ocf[i] + intp[i] + taxp[i] - sbc[i] - spend - T * ebit[i]
m = [oc(i, True) for i in range(3)]; a = [oc(i, False) for i in range(3)]
for i, y in enumerate(yrs):
    print(f"{y}: owner cash before interest after statutory tax, maintenance-only {m[i]:7.2f}; all-spending {a[i]:7.2f}; acquisitions {acq[i]:6.2f}; sales {rev[i]:7.1f}")
avg_m, avg_a = sum(m)/3, sum(a)/3
print(f"three-year averages: maintenance-only {avg_m:.2f}; all-spending {avg_a:.2f}; all-spending less acquisitions {(sum(a)-sum(acq))/3:.2f}")
print(f"serial acquirer test: purchases {sum(acq):.1f} against owner cash before purchases {sum(a):.1f} (all-spending) / {sum(m):.1f} (maintenance)")
g_m = (m[2]/m[0])**0.5 - 1
print(f"growth shown, maintenance-only owner cash 2023 to 2025: {100*g_m:.1f}% a year; sales {100*((rev[2]/rev[0])**0.5-1):.1f}% a year")
# ALGC, 8-K/A 0001193125-26-209128 Ex.99.1, two filed years; carried flat (CONVENTION of this run)
algc_ocf=[24.001, 41.599]; algc_int=[0.340, 0.245]; algc_tax=[1.201, 1.384]; algc_dep=[6.360, 7.268]; algc_cap=[2.577-0.374, 3.502-0.348]; algc_ebit=[27.077, 34.518]
algc_m = sum(algc_ocf[i]+algc_int[i]+algc_tax[i]-algc_dep[i]-T*algc_ebit[i] for i in range(2))/2
algc_a = sum(algc_ocf[i]+algc_int[i]+algc_tax[i]-algc_cap[i]-T*algc_ebit[i] for i in range(2))/2
print(f"ALGC two-year average owner cash: maintenance (depreciation) {algc_m:.2f}; capex as filed {algc_a:.2f}")
# net debt, 10-Q 2026-06-30 (0001193125-26-345109), plus Allied cash paid 2026-10-01 (8-K 0001193125-26-410735), plus contingent and deferred consideration
debt = 10.970 + 186.070 + 3.433 + 4.072; cash = 339.092
netdebt = debt - cash + 88.9 + 12.3 + 1.2
shares = 20.428610 + 27.044449 + 1.006796
price = 14.62
print(f"net debt {netdebt:.1f} (negative = net cash); shares {shares:.3f}M; market value {price*shares:.1f}; enterprise value {price*shares+netdebt:.1f}")
def pv(base, g, r, n=10):
    v = sum(base*(1+g)**t/(1+r)**t for t in range(1, n+1))
    return v + base*(1+g)**n/r/(1+r)**n
def case(base_c, g, base_algc, r):
    return pv(base_c, g, r) + base_algc/r
for label, bc, ba in (("CENTRAL maintenance-only", avg_m, algc_m), ("all-spending, beside", avg_a, algc_a)):
    top = case(bc, 0.0, ba, R); bot = case(bc, g_m, ba, R)
    ps = lambda v: (v - netdebt)/shares
    print(f"{label}: range ${ps(bot):.2f} to ${ps(top):.2f} a share (bottom = shown decline {100*g_m:.0f}%, top = no growth), width {top/bot:.2f} to 1 on value")
    yld_top = (bc+ba)/(price*shares+netdebt)
    print(f"   cash yield of the top case at the price on enterprise value: {100*yld_top:.2f}% (floor about 10%)")
    fair = ((case(bc,0.0,ba,F)+case(bc,g_m,ba,F))/2 - netdebt)/shares
    # equity-only: owner cash after interest (3-yr average cash interest after tax at T) against market value
    ia = (sum(intp)/3)*(1-T)
    fair_eq = ((case(bc-ia,0.0,ba,F)+case(bc-ia,g_m,ba,F))/2)/shares
    print(f"   fair price all-equity ${fair:.2f}; equity-only ${fair_eq:.2f}")
# literal window beside: Cardinal alone, no ALGC, maintenance-only
top = pv(avg_m,0,R); bot = pv(avg_m,g_m,R)
print(f"literal window, Cardinal's own three years only (no deal after the window): ${(bot-netdebt)/shares:.2f} to ${(top-netdebt)/shares:.2f}")
