# Q7 arithmetic for the OTIS run (owner cash from Q4; sovereign 5.60%; floor 10%; shares 380.669M)
R, FLOOR, SH = 0.056, 0.10, 380.669
NET_DEBT = 210 + 8226 - 813          # 2026-06-30: short-term borrowings + long-term debt incl. current, less cash ($M)
EQ  = [1374, 1260, 1340, 1270, 1295]  # owner cash after interest, 2021-2025
ALL = [1476, 1367, 1453, 1397, 1442]  # owner cash before interest (after-tax interest added back)
BOLT = (80 + 46 + 36 + 87 + 109 - 61) / 5   # bolt-on acquisitions net of disposals, yearly average
NCI = (1802 + 75 + 217) / 5                  # minority buyouts, yearly average (literal deduction variant)
avg = lambda xs: sum(xs) / len(xs)
def pv(base, g, r, years=10):
    v, cf = 0.0, base
    for t in range(1, years + 1):
        cf *= (1 + g); v += cf / (1 + r) ** t
    return v + cf / r / (1 + r) ** years   # zero nominal growth after year ten
def cagr(xs): return (xs[-1] / xs[0]) ** (1 / (len(xs) - 1)) - 1
def per_share(ev, debt): return (ev - debt) / SH
g_all, g_eq = cagr(ALL), cagr(EQ)
print(f"net debt {NET_DEBT:,.0f}; bolt-on avg {BOLT:.1f}; NCI avg {NCI:.1f}")
print(f"growth shown, all-equity {g_all*100:.2f}%  equity-only {g_eq*100:.2f}%")
cases = {}
base_all = avg(ALL) - BOLT; base_eq = avg(EQ) - BOLT
print(f"base all-equity {base_all:.1f}; base equity-only {base_eq:.1f}")
for name, g in [("no growth (top)", 0.0), ("shown growth (bottom)", g_all)]:
    ev = pv(base_all, g, R); cases[name] = per_share(ev, NET_DEBT)
    print(f"ALL-EQUITY {name:24s} EV {ev:9,.0f}  per share {cases[name]:7.2f}")
for name, g in [("no growth", 0.0), ("shown growth", g_eq)]:
    print(f"EQUITY-ONLY {name:23s} value {pv(base_eq, g, R):9,.0f}  per share {pv(base_eq, g, R)/SH:7.2f}")
# literal variant: minority buyouts deducted too
b2 = avg(ALL) - BOLT - NCI
print(f"LITERAL (buyouts deducted) base {b2:.1f}: no growth {per_share(pv(b2,0,R),NET_DEBT):.2f}, shown {per_share(pv(b2,g_all,R),NET_DEBT):.2f}")
# organic pair: acquisitions left out, organic sales growth as filed credited (2022 2.5, 2023 5.6, 2024 1, 2025 0)
g_org = (1.025 * 1.056 * 1.01 * 1.00) ** 0.25 - 1
b3 = avg(ALL)
print(f"ORGANIC PAIR base {b3:.1f} at {g_org*100:.2f}%: {per_share(pv(b3,g_org,R),NET_DEBT):.2f} (no growth {per_share(pv(b3,0,R),NET_DEBT):.2f})")
# maintenance-only variant: capex at depreciation (116,118,126,120,113) instead of capex (156,115,138,126,152)
add = avg([156-116, 115-118, 138-126, 126-120, 152-113])
print(f"MAINTENANCE-ONLY add-back {add:.1f}: no growth {per_share(pv(base_all+add,0,R),NET_DEBT):.2f}")
# fair price: midpoint case (growth halfway between ends) discounted at the floor
g_mid = (0.0 + g_all) / 2
fair_all = per_share(pv(base_all, g_mid, FLOOR), NET_DEBT)
fair_eq = pv(base_eq, (0.0 + g_eq) / 2, FLOOR) / SH
print(f"FAIR all-equity {fair_all:.2f}; equity-only {fair_eq:.2f}")
mid_val = (cases['no growth (top)'] + cases['shown growth (bottom)']) / 2
print(f"range mid {mid_val:.2f}; width top/bottom {cases['no growth (top)']/cases['shown growth (bottom)']:.2f}")
# expected return at the price: all-equity, central base, no growth: yield on EV
ev_price = 65.95 * SH + NET_DEBT
print(f"EV at price {ev_price:,.0f}; base/EV {base_all/ev_price*100:.2f}%; equity-only base/mcap {base_eq/(65.95*SH)*100:.2f}%")
# beside: the longer series 2018-2025 (pre-spin years carry little interest and the parent's cost allocation)
OLD = {2018: 1550-172-38-173 + 0.75*20, 2019: 1469-145-37-163 + 0.75*18, 2020: 1480-183-63-149 + 0.75*81}
g_long = (1442 / OLD[2018]) ** (1/7) - 1
print({k: round(v) for k, v in OLD.items()}, f"g 2018-2025 {g_long*100:.2f}%",
      f"value at that growth on the central base {per_share(pv(base_all, g_long, R), NET_DEBT):.2f}")
# price-implied: growth for ten years that makes the central base worth the price
lo, hi = -0.05, 0.30
for _ in range(80):
    m = (lo + hi) / 2
    if per_share(pv(base_all, m, R), NET_DEBT) < 65.95: lo = m
    else: hi = m
print(f"growth for ten years the price needs at 5.60% (then zero): {m*100:.2f}%")
