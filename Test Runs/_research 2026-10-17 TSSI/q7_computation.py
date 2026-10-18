# COMPUTATION, NOT A CLEARANCE. TSSI owner cash and the Q7 range (USD millions).
# Inputs transcribed from the filed statements (10-K FY2025 acc 0001654954-26-002342 for 2023-2025;
# XBRL first-filed 10-K values for 2021-2022 cross-checked by tools/run.py; 10-Q/A acc 0001654954-26-007668 for 2026-06-30).
import sys
sys.stdout.reconfigure(encoding="utf-8")
yrs   = [2021, 2022, 2023, 2024, 2025]
ocf   = [-10.452, 14.712, -8.269, 15.296, 34.863]
sbc   = [0.469, 0.530, 0.581, 1.235, 3.956]
capex = [0.064, 0.536, 0.257, 8.483, 32.743]
da    = [0.536, 0.383, 0.320, 0.608, 3.765]
sales = [27.410, 30.637, 54.399, 148.144, 245.719]
# operating pre-tax for the statutory-tax line (op. income incl. factoring fees, plus other income); losses taxed at zero
optax_base = [-1.232, -0.017, -0.221, 5.572, 6.527]
int_inc  = [0.0, 0.0, 0.355, 0.562, 1.657]    # 2021-22: no interest-income line tagged; taken as zero (flagged)
bank_int = [0.0, 0.0, 0.0, 0.0, 0.423]        # cash interest on bank debt, net of capitalized
T = 0.21                                      # federal statutory rate (CONVENTION of Q7, Whose tax)
r = 0.0543                                    # US Treasury 30-yr par yield, 2026-10-16
FLOOR = 0.10
shares = 28.219070                            # cover of 10-Q/A, as of 2026-08-07
price = 7.07                                  # close 2026-10-16, aggregator (flagged)
cash = 67.679; debt = 4.161 + 11.919          # 2026-06-30, restricted cash 1.811 excluded (collateral for a letter of credit)
net_debt = debt - cash
nol = 54.0                                    # NOL at 2025-12-31 per 10-K tax note

def adj(i, capital):
    fed = T * max(0.0, optax_base[i])
    allequity = -(1 - T) * int_inc[i] + (1 - T) * bank_int[i]
    return ocf[i] - sbc[i] - capital[i] - fed + allequity
allsp = [adj(i, capex) for i in range(5)]
maint = [adj(i, da) for i in range(5)]
eqonly_maint = [maint[i] + (1-T)*int_inc[i] - (1-T)*bank_int[i] for i in range(5)]
mean = lambda x: sum(x)/len(x)
print("year  allspending  maintenance  sales  maint/sales")
for i in range(5):
    print(yrs[i], f"{allsp[i]:9.2f} {maint[i]:11.2f} {sales[i]:8.1f} {100*maint[i]/sales[i]:7.1f}%")
A, M, E = mean(allsp), mean(maint), mean(eqonly_maint)
print(f"5-yr mean: all-spending {A:.2f}, maintenance {M:.2f}, maintenance equity-only {E:.2f}")
h1, h2 = mean(maint[:2]), mean(maint[3:])
g_shown = (h2/h1)**(1/3) - 1
g_sales = (sales[4]/sales[0])**(1/4) - 1
print(f"growth by halves (maintenance): {h1:.2f} -> {h2:.2f}, {100*g_shown:.0f}%/yr; sales 2021-25 {100*g_sales:.0f}%/yr")
g = min(g_sales, r)   # (f): cut to sales growth, never above the discount rate
print(f"growth carried after cap (f): {100*g:.2f}%")
def pv(cf0, g, rate, years=10):
    v = 0; c = cf0
    for t in range(1, years+1):
        c *= (1+g); v += c/(1+rate)**t
    return v + (c/rate)/(1+rate)**years
def pv_nog(cf0, rate): return cf0/rate
# NOL shelter: 80% limitation on post-2017 NOLs ignored for simplicity? no: apply 80% of taxable base
def shelter_pv(base, rate):
    left = nol; v = 0; t = 0
    while left > 0 and t < 30:
        t += 1; use = min(left, 0.8*base); left -= use; v += T*use/(1+rate)**t
    return v, t
sh, yrs_used = shelter_pv(6.527, r)
print(f"NOL shelter PV at {r:.4f}: {sh:.2f} (used over {yrs_used} yrs); at 10%: {shelter_pv(6.527,0.10)[0]:.2f}")
lo, hi = pv_nog(M, r), pv(M, g, r)
print(f"RANGE (enterprise, maintenance central): no-growth {lo:.1f}  growth {hi:.1f}  width {hi/lo:.2f}x")
eq = lambda ev, s=sh: (ev - net_debt + s)/shares
print(f"per share all-equity basis: {eq(lo):.2f} to {eq(hi):.2f}  vs price {price}")
print(f"all-spending case beside: no-growth EV {pv_nog(A, r):.1f} -> per share {eq(pv_nog(A,r)):.2f}")
# literal window = same five years (no aberrational-cycle base adopted)
# equity-only beside
lo_e, hi_e = pv_nog(E, r), pv(E, g, r)
print(f"equity-only basis: {(lo_e+sh)/shares:.2f} to {(hi_e+sh)/shares:.2f}")
# fair price: each end at 10%, averaged
sh10 = shelter_pv(6.527, FLOOR)[0]
f_lo, f_hi = pv_nog(M, FLOOR), pv(M, g, FLOOR)
fair = eq((f_lo+f_hi)/2, sh10)
fair_e = ((pv_nog(E,FLOOR)+pv(E,g,FLOOR))/2 + sh10)/shares
print(f"FAIR PRICE all-equity: {fair:.2f}  (ends {eq(f_lo,sh10):.2f}, {eq(f_hi,sh10):.2f});  equity-only {fair_e:.2f}")
# floor test: return earned at the price on each case (IRR of the enterprise at market EV)
mcap = price*shares; ev_mkt = mcap + net_debt - sh
def irr(cf0, g):
    lo_, hi_ = 0.001, 1.0
    for _ in range(200):
        mid = (lo_+hi_)/2
        if pv(cf0, g, mid) > ev_mkt: lo_ = mid
        else: hi_ = mid
    return mid
print(f"market cap {mcap:.1f}; EV at price (less net cash, less shelter PV) {ev_mkt:.1f}")
print(f"return at price: maintenance no-growth {100*M/ev_mkt:.1f}%, maintenance growth {100*irr(M,g):.1f}%, all-spending {100*A/ev_mkt:.1f}%")
