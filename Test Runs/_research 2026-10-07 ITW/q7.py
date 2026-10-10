# Q7 arithmetic for the ITW run (COMPUTATION; the judgments are in the run file). USD millions except per share.
# Construction (framework Q7 CONVENTIONS): owner cash base, carried 10 years at the growth shown (capped), then zero
# nominal growth, discounted at the 30-year Treasury par yield; ends = no-growth and shown-growth cases.
RATE = 0.0564          # US Treasury 30-year par yield, 10/06/2026 (tools/sources.py)
NET_DEBT = 8855.0      # 2026-06-30 10-Q: 3,145 + 6,549 - 839
SHARES = 284.8         # 10-Q cover, 2026-06-30
PRICE = 261.94         # aggregator quote 2026-10-07
FLOOR = 0.10           # CONVENTION: about ten percent

def pv(base, g, r, years=10):
    v, cf = 0.0, base
    for t in range(1, years + 1):
        cf *= (1 + g)
        v += cf / (1 + r) ** t
    return v + (cf / r) / (1 + r) ** years

def irr(base, g, price_total):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(base, g, mid) > price_total: lo = mid
        else: hi = mid
    return mid

# all-equity owner cash, acquisitions net of sales deducted (run file Q4 table)
AE = {2018: 2603, 2019: 2912, 2020: 2687, 2021: 1631, 2022: 2303, 2023: 3224, 2024: 3278, 2025: 2742}
EO = {2018: 2408, 2019: 2744, 2020: 2530, 2021: 1477, 2022: 2149, 2023: 3022, 2024: 3063, 2025: 2520}
AE_noacq = {2021: 2362, 2022: 2027, 2023: 3217, 2024: 2998, 2025: 2860}   # acquisitions left out (organic pair)
avg = lambda d, ys: sum(d[y] for y in ys) / len(ys)
W = range(2021, 2026); C = range(2018, 2026)
cases = {
  "central: cycle base 2018-2025, all-equity, acq deducted": (avg(AE, C), 0.0162),
  "literal window 2021-2025, all-equity, acq deducted":     (avg(AE, W), 0.0162),
  "organic pair: window, acquisitions left out, organic 2.0%": (avg(AE_noacq, W), 0.020),
}
ev_price = PRICE * SHARES + NET_DEBT
print(f"EV at price {ev_price:,.0f}  market cap {PRICE*SHARES:,.0f}")
for name, (b, g) in cases.items():
    lo, hi = pv(b, 0.0, RATE), pv(b, g, RATE)
    ps = lambda ev: (ev - NET_DEBT) / SHARES
    gm = g / 2
    fair_ev = pv(b, gm, FLOOR)
    print(f"\n{name}\n  base {b:,.0f}  growth {g:.2%}")
    print(f"  EV range {lo:,.0f} .. {hi:,.0f}   per share {ps(lo):.2f} .. {ps(hi):.2f}   width {hi/lo:.2f}x (EV) {ps(hi)/ps(lo):.2f}x (per share)")
    print(f"  fair price (midpoint growth {gm:.2%} at 10%): EV {fair_ev:,.0f} -> {ps(fair_ev):.2f} a share")
    print(f"  expected return at the price: no growth {b/ev_price:.2%}; shown growth IRR {irr(b, g, ev_price):.2%}")
# equity-only beside
for ys, lab in ((C, "cycle 2018-2025"), (W, "window 2021-2025")):
    b = avg(EO, ys); g = 0.0162
    lo, hi = pv(b, 0, RATE) / SHARES, pv(b, g, RATE) / SHARES
    fair = pv(b, g / 2, FLOOR) / SHARES
    print(f"\nequity-only {lab}: base {b:,.0f}  range {lo:.2f} .. {hi:.2f}  fair {fair:.2f}  yield at price {b/(PRICE*SHARES):.2%}")
# growth evidence
eo_1620 = (1537 + 2066 + 2408 + 2744 + 2530) / 5
eo_2125 = avg(EO, W)
print(f"\ngrowth between five-year averages (equity-only, acq deducted): 2016-20 {eo_1620:,.0f} -> 2021-25 {eo_2125:,.0f}: {(eo_2125/eo_1620)**0.2-1:.2%}/yr")
print(f"literal end years 2021->2025 all-equity acq-deducted: {(AE[2025]/AE[2021])**0.25-1:.2%}/yr (2021 is the MTS year)")
# price needed for the shown-growth case to yield the floor, and the growth the price implies at the sovereign
lo_, hi_ = 0.0, 0.2
b = avg(AE, C)
for _ in range(200):
    m = (lo_ + hi_) / 2
    if pv(b, m, RATE) < ev_price: lo_ = m
    else: hi_ = m
print(f"growth for ten years the price implies at {RATE:.2%} (then flat): {m:.2%}")
