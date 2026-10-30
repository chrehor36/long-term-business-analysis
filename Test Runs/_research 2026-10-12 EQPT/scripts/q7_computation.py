# COMPUTATION, NOT A CLEARANCE: the Q7 range and fair price by the framework's convention, for the reporting figures.
import sys; sys.stdout.reconfigure(encoding="utf-8")
r = 0.056      # 30-year Treasury par yield, 2026-10-09 (tools/sources.py)
floor = 0.10   # the floor CONVENTION
shares = 253.375963  # million, 10-Q cover (Class A 215,807,019 + Class B 37,568,944)
price = 15.085
# owner cash series ($M), scripts/owner_cash.py
ae_maint = [102.5, 138.3, 126.8, 109.9]     # all-equity, maintenance-only (OCF - D&A - SBC + cash interest x 0.79)
ae_all   = [-509.3, -170.4, 58.5, -478.1]   # all-equity, all spending
eq_maint = [13.9, -19.6, -55.1, -105.0]     # equity-only, maintenance-only
eq_all   = [-597.9, -328.3, -123.4, -693.0] # equity-only, all spending
pref_div = [0.0, 5.0, 9.0, 37.0]            # cash dividends on perpetual preferred (cash-flow statements)
avg = lambda x: sum(x)/len(x)
# net debt at 2026-06-30 (10-Q balance sheet) plus the subsequent event the 10-Q states (2034 notes; proceeds repaid ABL; $11M costs)
debt = 3635 + 2; fin_lease = 19 + 197; fin_oblig = 9 + 71; cash = 443; costs = 11
net_debt = debt + fin_lease + fin_oblig - cash + costs
pref = 370  # perpetual preferred, carrying amount at 2026-06-30
claims = net_debt + pref
print(f"net debt {net_debt}, perpetual preferred {pref}, claims ahead of common {claims}")
def g_pv(c0, g, r, years=10):
    # growth g for ten years, then zero nominal growth, discounted at r
    pv = 0; c = c0
    for t in range(1, years+1):
        c *= (1+g); pv += c/(1+r)**t
    return pv + (c/r)/(1+r)**years
g_m = (ae_maint[-1]/ae_maint[0])**(1/3) - 1
print(f"shown growth, all-equity maintenance-only series 2022->2025: {g_m:.4f}")
A_top = avg(ae_maint); A_bot = avg(ae_all)
E_top = avg(eq_maint) - avg(pref_div); E_bot = avg(eq_all) - avg(pref_div)
print(f"4-yr averages: AE maint {A_top:.1f}, AE all {A_bot:.1f}, EQ maint less pref div {E_top:.1f}, EQ all less pref div {E_bot:.1f}")
for lbl, rate in (("range at the sovereign", r), ("fair-price ends at the floor", floor)):
    top = A_top/rate; bot = A_bot/rate
    print(f"{lbl}: whole-business top {top:.0f} bottom {bot:.0f}; per share all-equity top {(top-claims)/shares:.2f} bottom {(bot-claims)/shares:.2f};"
          f" without the preferred: top {(top-net_debt)/shares:.2f}; equity-only top {E_top/rate/shares:.2f} bottom {E_bot/rate/shares:.2f}")
fair_ae = ((A_top/floor + A_bot/floor)/2 - claims)/shares
fair_eq = ((E_top/floor + E_bot/floor)/2)/shares
print(f"FAIR PRICE all-equity {fair_ae:.2f} (preferred deducted); equity-only {fair_eq:.2f}; price {price}")
print(f"maintenance-only growth case shown beside (not an end, by specific (e)): whole-business {g_pv(A_top, g_m, r):.0f}, per share {(g_pv(A_top, g_m, r)-claims)/shares:.2f}")
# sensitivity: start-up costs added back to the maintenance-only all-equity series (2023-2025 only; 2022 not filed)
startup = [124, 197, 252]
sens = avg([a+b for a, b in zip(ae_maint[1:], startup)])
print(f"SENSITIVITY (not a reporting figure): maintenance-only all-equity with start-up costs added back, 3-yr avg {sens:.1f}; value at sovereign {sens/r:.0f} vs claims {claims} + market cap {shares*price:.0f} = {claims+shares*price:.0f}")
