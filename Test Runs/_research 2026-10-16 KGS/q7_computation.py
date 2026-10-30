# COMPUTATION, NOT A CLEARANCE. KGS run 2026-10-16. Q7 range convention applied after the Q2 STOP.
# All figures USD millions from the filed cash-flow statements (Kodiak FY2023 10-K 0001767042-24-000011 for
# 2021-2023, FY2025 10-K 0001767042-26-000012 for 2023-2025) and CSI Compressco LP's 10-K XBRL facts
# (FY2023 10-K 0001449488-24-000013) for 2021-2023, combined because the CSI deal (2024-04-01) was paid in
# shares and units (a merger under Q7 (c)). CSI's Q1 2024 is not filed separately and is left out (said so).
r = 0.0543      # US Treasury 30-year par, 2026-10-15
T = 0.21        # CONVENTION of this run: interest added back net of the 21% federal statutory rate
yrs = [2021, 2022, 2023, 2024, 2025]
K = dict(ocf=[250.0, 219.8, 266.3, 328.0, 599.7], sbc=[1.2, 1.0, 5.9, 17.7, 24.5],
         capex=[201.9, 259.3, 219.8, 337.0, 315.5], proc=[0.0, 8.1, 1.4, 35.0, 30.2],
         intp=[119.9, 143.4, 216.6, 147.1, 168.7], dep=[150.5, 165.0, 173.4, 245.8, 259.2],
         rev=[606.4, 707.9, 850.4, 1159.3, 1308.1])
C = dict(ocf=[27.2, 35.5, 62.2, 0, 0], sbc=[2.0, 1.6, 1.5, 0, 0], capex=[43.4, 52.1, 57.9, 0, 0],
         proc=[1.3, 8.1, 6.4, 0, 0], intp=[49.2, 47.3, 53.4, 0, 0], dep=[74.9, 75.1, 74.4, 0, 0],
         rev=[304.2, 353.4, 386.1, 0, 0])
S = {k: [a + b for a, b in zip(K[k], C[k])] for k in K}
n = len(yrs)
A_eq = [S['ocf'][i] - S['sbc'][i] - S['capex'][i] + S['proc'][i] for i in range(n)]   # all spending, after interest
B_eq = [S['ocf'][i] - S['sbc'][i] - S['dep'][i] for i in range(n)]                    # maintenance guess = depreciation
A_ae = [A_eq[i] + S['intp'][i] * (1 - T) for i in range(n)]                            # all-equity (before interest)
B_ae = [B_eq[i] + S['intp'][i] * (1 - T) for i in range(n)]
mean = lambda x: sum(x) / len(x)
print('year   OCF   SBC  capex  proc  int   dep  | A_eq   B_eq   A_ae   B_ae   rev   A_ae/rev')
for i, y in enumerate(yrs):
    print(f"{y} {S['ocf'][i]:6.1f} {S['sbc'][i]:5.1f} {S['capex'][i]:6.1f} {S['proc'][i]:5.1f} {S['intp'][i]:5.1f} {S['dep'][i]:5.1f} |"
          f" {A_eq[i]:6.1f} {B_eq[i]:6.1f} {A_ae[i]:6.1f} {B_ae[i]:6.1f} {S['rev'][i]:7.1f} {A_ae[i]/S['rev'][i]*100:5.1f}%")
for k, v in [('A_eq', A_eq), ('B_eq', B_eq), ('A_ae', A_ae), ('B_ae', B_ae)]:
    print(f'mean {k}: {mean(v):.1f}')
# growth shown, aggregate (Q7 PG specific); series A_ae all positive: end years, and halves
g_end = (A_ae[-1] / A_ae[0]) ** (1 / 4) - 1
h1, h2 = mean(A_ae[:2]), mean(A_ae[3:])
g_half = (h2 / h1) ** (1 / 3) - 1
g_sales = (S['rev'][-1] / S['rev'][0]) ** (1 / 4) - 1
print(f'growth shown A_ae: end-years {g_end*100:.1f}%  halves {g_half*100:.1f}%;  sales growth combined {g_sales*100:.1f}%')
# cap (f): would the shown rate carried ten years need owner cash above the highest share of sales?
best_share = max(A_ae[i] / S['rev'][i] for i in range(n))
need = mean(A_ae) * (1 + g_half) ** 10
sales10 = S['rev'][-1] * (1 + g_sales) ** 10
print(f'cap test: year-10 owner cash at shown rate {need:.0f}; at best share {best_share*100:.1f}% needs sales {need/best_share:.0f}; sales at own growth {sales10:.0f}')
g = min(g_sales, r)   # the cut: own sales growth, never above the discount rate
print(f'growth carried after the cut: {g*100:.2f}%')
def pv(c, g, rate, years=10):
    v, cf = 0.0, c
    for t in range(1, years + 1):
        cf *= (1 + g); v += cf / (1 + rate) ** t
    return v + cf / rate / (1 + rate) ** years
# DPS, closed 2026-04-01 after the window: own filed record FY2025 (8-K/A 0001193125-26-221869, Ex. 99.1)
dps_ocf, dps_capex, dps_int, dps_opinc = 37.2, 21.2 + 6.4, 7.4, 25.4
dps_ae = dps_ocf - dps_capex + dps_int - dps_opinc * T      # LLC: corporate tax added at 21% on operating income
dps_eq = dps_ocf - dps_capex - (dps_opinc - dps_int) * T
print(f'DPS owner cash all-equity {dps_ae:.1f}, equity-only {dps_eq:.1f}')
netdebt = 2720.989 + 45.625 - 137.553 + 32.8   # 10-Q 2026-06-30 debt + finance leases - cash + subsequent buyout
shares, price = 101.104031, 47.81
print(f'net debt {netdebt:.1f}; EV at price {price*shares+netdebt:.1f}')
# ALL-EQUITY range: central maintenance-only no-growth vs all-spending growth case (Q7 (e))
lo_ae = pv(mean(B_ae), 0, r) + pv(dps_ae, 0, r)
hi_ae = pv(mean(A_ae), g, r) + pv(dps_ae, 0, r)
ends = sorted([lo_ae, hi_ae])
print(f'ALL-EQUITY whole-business: no-growth(maint) {lo_ae:.0f}  growth(all-spend) {hi_ae:.0f}')
per = lambda v: (v - netdebt) / shares
print(f'  per share: {per(ends[0]):.2f} to {per(ends[1]):.2f}  width {ends[1]/ends[0]:.2f}:1 (whole business)')
print(f'  beside: all-spending no-growth {per(pv(mean(A_ae),0,r)+pv(dps_ae,0,r)):.2f}; maintenance growth {per(pv(mean(B_ae),g,r)+pv(dps_ae,0,r)):.2f}')
f_lo = pv(mean(B_ae), 0, 0.10) + pv(dps_ae, 0, 0.10)
f_hi = pv(mean(A_ae), g, 0.10) + pv(dps_ae, 0, 0.10)
print(f'  at ten percent: {f_lo:.0f} and {f_hi:.0f}; FAIR PRICE all-equity {per((f_lo+f_hi)/2):.2f}')
print(f'  floor test: best case at ten percent {max(f_lo,f_hi):.0f} vs EV {price*shares+netdebt:.0f}')
# EQUITY-ONLY: A_eq changes sign -> halves (b): first half mean negative -> meaningless -> no-growth alone
print(f'EQUITY-ONLY: A_eq halves {mean(A_eq[:2]):.1f} and {mean(A_eq[3:]):.1f} (sign change: no-growth case alone)')
eo_c = pv(mean(B_eq), 0, r) + pv(dps_eq, 0, r); eo_a = pv(mean(A_eq), 0, r) + pv(dps_eq, 0, r)
print(f'  no-growth maintenance {eo_c/shares:.2f}/sh; all-spending beside {eo_a/shares:.2f}/sh')
eo_f = pv(mean(B_eq), 0, 0.10) + pv(dps_eq, 0, 0.10)
print(f'  FAIR PRICE equity-only {eo_f/shares:.2f}/sh (all-spending at ten percent beside: {(pv(mean(A_eq),0,0.10)+pv(dps_eq,0,0.10))/shares:.2f})')
# literal window beside: tools/run.py three-year Kodiak-only equity-only means 91.2 (capex) / 142.2 (D&A)
print(f'literal 3-yr window (run.py, Kodiak only, after interest): {91.2/r/shares:.2f} and {142.2/r/shares:.2f} per share at no growth')
# filer-definition maintenance (maintenance + other capex) beside, 2024-2025 only: 66.2+58.8, 76.0+62.8
fm = [328.0 - 17.7 - 125.0 + 147.1 * (1 - T), 599.7 - 24.5 - 138.8 + 168.7 * (1 - T)]
print(f"filer-definition maintenance, all-equity, 2024-25: {fm[0]:.1f}, {fm[1]:.1f}; no-growth per share on their mean {per(pv(mean(fm),0,r)+pv(dps_ae,0,r)):.2f}")
