# Q7 range for MPTI by the framework's range convention. USD thousands.
price = 66.41; shares = 4346.476  # thousands of shares, cover 2026-07-31
mcap = price*shares
cash = 96245 + 687 + 68   # cash, short-term investments, equity securities at 2026-06-30 (10-Q 0001437749-26-027371)
debt = 0                   # no borrowings; operating leases left out
netdebt = debt - cash
ev = mcap + netdebt
sov = 0.0543
def pv(base, g, r, years=10):
    v = 0.0; c = base
    for t in range(1, years+1):
        c = c*(1+g); v += c/(1+r)**t
    term = c/r/(1+r)**years   # zero nominal growth after year ten
    return v + term
def irr(base, g, target):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        mid = (lo+hi)/2
        if pv(base, g, mid) > target: lo = mid
        else: hi = mid
    return mid
print(f"market cap {mcap:,.0f}  net debt {netdebt:,.0f}  EV {ev:,.0f}")
cases = {
 "maint, all-equity (central)": 3076,
 "all-spend, all-equity": 2358,
 "maint, as-filed tax (beside)": 3705 - (416+190+6-8-9)/5,  # as-filed oc_m less avg after-tax interest
 "2025 alone maint all-equity (not the convention; shown for the floor test)": 6596,
}
growths = {"no growth": 0.0, "cut to discount rate 5.43%": 0.0543, "sales growth 19.49%": 0.1949}
for name, base in cases.items():
    print("\n==", name, f"base {base:,.0f}")
    for gname, g in growths.items():
        v = pv(base, g, sov); ps = (v - netdebt)/shares
        r = irr(base, g, ev)
        v10 = pv(base, g, 0.10); ps10 = (v10 - netdebt)/shares
        print(f"  {gname:28s} value EV {v:9,.0f}  per share {ps:7.2f}  | expected return at price {r:6.2%} | at 10%: per share {ps10:7.2f}")
# fair price: each end of the central range valued at 10%, averaged
for name, base in [("maint central", 3076), ("all-spend", 2358)]:
    for top_g in (0.0543, 0.1949):
        lo = (pv(base, 0.0, 0.10) - netdebt)/shares
        hi = (pv(base, top_g, 0.10) - netdebt)/shares
        print(f"fair price all-equity [{name}, top growth {top_g:.2%}]: ends {lo:.2f} / {hi:.2f} -> {(lo+hi)/2:.2f}")
# equity-only: owner cash after interest (window average, interest income included), against market value, no cash added
for name, base in [("maint equity-only", 3076 + (416+190+6-8-9)/5), ("all-spend equity-only", 2358 + (416+190+6-8-9)/5)]:
    for top_g in (0.0543, 0.1949):
        lo = pv(base, 0.0, 0.10)/shares; hi = pv(base, top_g, 0.10)/shares
        print(f"fair price equity-only [{name}, top {top_g:.2%}]: {lo:.2f} / {hi:.2f} -> {(lo+hi)/2:.2f}; expected return at mcap: no-growth {irr(base,0.0,mcap):.2%}, top {irr(base,top_g,mcap):.2%}")
