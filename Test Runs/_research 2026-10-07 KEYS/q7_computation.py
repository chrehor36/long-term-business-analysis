# COMPUTATION, NOT A CLEARANCE. KEYS run 2026-10-07. Q7 construction of THE FRAMEWORK v5 (range convention, six specifics,
# all-equity basis, fair price at the ~10% floor). USD millions. Sources: 10-K FY2021-FY2025 cash-flow statements via XBRL
# companyfacts (OCF, SBC expense, capex, acquisitions, interest paid, interest income), cross-checked FY2025 OCF 1,409 to the
# filed statement (acc 0001601046-25-000127); net debt at 2026-07-31 from 10-Q acc 0001601046-26-000036.
yrs   = [2021, 2022, 2023, 2024, 2025]
ocf   = [1322, 1144, 1408, 1052, 1409]
sbc   = [104, 126, 136, 145, 176]          # AllocatedShareBasedCompensationExpense (segment reconciliation figure)
capex = [174, 185, 197, 154, 128]
dep   = [117, 117, 120, 126, 131]          # depreciation only (variant)
intpaid = [75, 75, 75, 75, 77]
intinc  = [3, 16, 102, 81, 102]
# acquisitions net of divestitures: cash paid for businesses (investing) + 2024 ESI minority buyout (financing, 458)
# + 2024 repayment of ESI debt assumed (24) - 2025 divestiture proceeds to Viavi (399)
acq   = [178, 33, 85, 681 + 458 + 24, 2022 - 399]
T = 0.21                                  # statutory US rate used only to put interest after tax (effective rate ~20%)
r = 0.0564                                # US Treasury 30-year par yield, 2026-10-06
FLOOR = 0.10
shares = 170.244745                       # cover of 10-Q, acc 0001601046-26-000036
price = 379.50                            # aggregator quote 2026-10-07 (tools/run.py), flagged
debt, cash = 2517, 2605                   # 2026-07-31 carrying value of senior notes; cash and equivalents
netdebt = debt - cash                     # long-term equity investments (188) left out; operating leases left out

lev   = [o - s - c for o, s, c in zip(ocf, sbc, capex)]
unlev = [l + (ip - ii) * (1 - T) for l, ip, ii in zip(lev, intpaid, intinc)]
levdep = [o - s - d for o, s, d in zip(ocf, sbc, dep)]
avg = lambda x: sum(x) / len(x)

def pv(c0, g, rate):
    v = 0.0; c = c0
    for t in range(1, 11):
        c *= (1 + g); v += c / (1 + rate) ** t
    return v + c / rate / (1 + rate) ** 10   # no nominal growth after year 10

def cagr(a, b, n): return (b / a) ** (1 / n) - 1

def case(label, base, g, nd):
    lo_g, hi_g = (g, 0.0) if g < 0 else (0.0, g)   # negative growth makes the bottom (specific b)
    v_lo, v_hi = pv(base, lo_g, r), pv(base, hi_g, r)
    ps = lambda v: (v - nd) / shares
    mid10 = (pv(base, lo_g, FLOOR) + pv(base, hi_g, FLOOR)) / 2
    print(f"{label}: base {base:,.0f}  growth {g*100:.2f}%  EV {v_lo:,.0f}-{v_hi:,.0f}  per share ${ps(v_lo):.2f}-${ps(v_hi):.2f}"
          f"  width {v_hi/v_lo if v_lo>0 else float('nan'):.2f}:1  fair price ${ps(mid10):.2f}  vs price ${price}")

print("unlevered owner cash by year", [round(x) for x in unlev], "avg", round(avg(unlev)))
print("levered owner cash by year  ", lev, "avg", round(avg(lev)))
print("depreciation variant (lev)  ", levdep, "avg", round(avg(levdep)))
print("acquisitions net            ", acq, "avg", round(avg(acq)))
g_total_u = cagr(unlev[0], unlev[-1], 4); g_total_l = cagr(lev[0], lev[-1], 4)
# organic revenue growth as the filer reports it: FY22 +10%, FY23 +1% (no acquisition impact stated), FY24 -9% with
# acquisitions +3 pts (organic -12%), FY25 +8% (acquisitions immaterial)
g_org = (1.10 * 1.01 * 0.88 * 1.08) ** 0.25 - 1
print(f"total growth (unlevered, end years) {g_total_u*100:.2f}%; levered {g_total_l*100:.2f}%; organic revenue {g_org*100:.2f}%")
print(f"net debt {netdebt}; market cap {price*shares:,.0f}; EV {price*shares+netdebt:,.0f}")
print("ALL-EQUITY BASIS (central)")
case(" default pair: acquisitions deducted, total growth", avg(unlev) - avg(acq), g_total_u, netdebt)
case(" organic pair: acquisitions left out, organic growth", avg(unlev), g_org, netdebt)
print("EQUITY-ONLY (beside, never decides)")
case(" default pair", avg(lev) - avg(acq), g_total_l, 0)
case(" organic pair", avg(lev), g_org, 0)
print("price-implied: owner cash yield on EV (unlevered, before acquisitions)", f"{avg(unlev)/(price*shares+netdebt)*100:.2f}%")
