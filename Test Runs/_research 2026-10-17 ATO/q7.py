# Q7 range, fair price and floor test for ATO (USD millions). Inputs from owner_cash.py and the filings.
SH = 168.988553            # shares, 10-Q cover 2026-07-31
PRICE = 167.34             # close 2026-10-16, aggregator
NETDEBT = (9748.716 + 502.542 + 63.751 + 8.858) - 520.953   # 10-Q 2026-06-30: borrowings incl. finance leases, securitized; less cash
MCAP = SH * PRICE; EV = MCAP + NETDEBT
B_AE, B_EQ = 767.9, 659.5  # 5-yr avg owner cash, maintenance = D&A, book tax, Uri lines out
B_AE25, B_EQ25 = 1151.2, 1015.6  # FY2025 alone, beside
B_CASH25 = 1419.8  # FY2025, cash-tax variant (deferred taxes kept), beside
S = 2139.2                 # 5-yr avg growth spending (capex - D&A)
RHO_AE, RHO_EQ = 0.094, 0.086  # window's incremental cash return on growth spending (owner_cash.py)
SOV, FLOOR = 0.0543, 0.10
G_CAP = 0.0543             # (f): sales growth 8.4% cut to the discount rate

def pv(cfs, term, r):
    v = sum(cf / (1 + r) ** (t + 1) for t, cf in enumerate(cfs))
    return v + term / r / (1 + r) ** len(cfs)

def no_growth(B, r):
    return B / r

def growth_spend_all(B, rho, r):
    # B1: average growth spending continued 10 years, each year's spend earning rho from the next year; stops after year 10
    cfs = [B + rho * S * t - S for t in range(10)]
    return pv(cfs, B + rho * S * 10, r)

def growth_capped(B, rho, r, g=G_CAP):
    # B2: owner cash grows at the capped rate; only the spending that buys that growth is charged (at rho)
    cf = [B * (1 + g) ** t for t in range(1, 12)]   # cash before growth spend, years 1..11
    spend = [(cf[t + 1] - cf[t]) / rho for t in range(10)]   # spend in year t buys next year's increment
    net = [cf[t] - spend[t] for t in range(10)]
    return pv(net, cf[9], r)   # after year 10: no growth, no spend; terminal on year-10 cash

def irr(f, target, lo=-0.5, hi=0.5):
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > target: lo = mid
        else: hi = mid
    return mid

print(f"market cap {MCAP:,.1f}  net debt {NETDEBT:,.1f}  EV {EV:,.1f}")
for lab, B, rho, base, sub in [("ALL-EQUITY, 5-yr avg", B_AE, RHO_AE, EV, NETDEBT), ("EQUITY-ONLY, 5-yr avg", B_EQ, RHO_EQ, MCAP, 0.0),
                               ("ALL-EQUITY, FY2025 alone (beside)", B_AE25, RHO_AE, EV, NETDEBT), ("EQUITY-ONLY, FY2025 alone (beside)", B_EQ25, RHO_EQ, MCAP, 0.0)]:
    print("\n==", lab)
    for name, fn in [("no growth", lambda r: no_growth(B, r)), ("growth B1 (avg spend, rho credited)", lambda r: growth_spend_all(B, rho, r)),
                     ("growth B2 (capped 5.43%, spend that buys it)", lambda r: growth_capped(B, rho, r))]:
        v_s, v_f = fn(SOV), fn(FLOOR)
        ret = irr(lambda r: fn(r) if r > 0.0001 else 1e12, base, 0.0001, 0.5)
        print(f"  {name:46s} value@5.43% {v_s:10,.0f} -> ${(v_s - sub) / SH:8.2f}/sh | value@10% {v_f:9,.0f} -> ${(v_f - sub) / SH:8.2f}/sh | return at price {ret*100:5.2f}%")
# beside: all spending charged; maintenance at the 87% safety share
for lab, cf in [("all spending, AE 5-yr avg", -1371.3), ("maint = 87% of capex (FY2025), AE", 2049.5 - 268.6 - 30.5 - 0.87 * 3561.4 + 171.7 * 0.79)]:
    print(f"\nbeside: {lab}: owner cash {cf:,.1f}/yr -> no value on any rate")
# forwards beside: +6.128939M shares, +936.8 cash
SH2 = SH + 6.128939; ND2 = NETDEBT - 936.841
print(f"\nforwards settled (beside): shares {SH2:.3f}M, net debt {ND2:,.1f}")
for name, v in [("no growth AE @5.43%", no_growth(B_AE, SOV)), ("B1 AE @5.43%", growth_spend_all(B_AE, RHO_AE, SOV)), ("no growth AE @10%", no_growth(B_AE, FLOOR)), ("B1 AE @10%", growth_spend_all(B_AE, RHO_AE, FLOOR))]:
    print(f"  {name}: ${(v - ND2) / SH2:.2f}/sh")
print(f"\nowner cash needed to earn 10% at the price with no growth: AE {EV*0.10:,.0f}  equity-only {MCAP*0.10:,.0f}")
print("\ncash-tax variant, FY2025 alone, all-equity (beside):")
for name, fn in [("no growth", lambda r: no_growth(B_CASH25, r)), ("growth B1", lambda r: growth_spend_all(B_CASH25, RHO_AE, r))]:
    ret = irr(lambda r: fn(r), EV, 0.0001, 0.5)
    print(f"  {name}: value@10% {fn(FLOOR):,.0f} -> ${(fn(FLOOR)-NETDEBT)/SH:.2f}/sh; return at price {ret*100:.2f}%")
