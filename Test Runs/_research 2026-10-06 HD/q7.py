"""Q7 range under the v5 CONVENTION (framework Q7): five-year mean owner cash after every real cost, carried ten years at
the growth shown (aggregate, never above it), then zero nominal growth, discounted at the 30-year Treasury.
Inputs: owner cash table in the run file STEP 0 (filed XBRL, OCF - SBC - capex); shares from the 10-Q cover
(0001628280-26-058715); sovereign 5.66% (US Treasury, 10/05/2026); price $281.15 (aggregator, flagged)."""
import math

oc = {2021: 13606, 2022: 11130, 2023: 17566, 2024: 15883, 2025: 12124}       # all capex
ocd = {2021: 13310, 2022: 11274, 2023: 17545, 2024: 16032, 2025: 12289}      # depreciation variant
shares, price, r = 997.689626, 281.15, 0.0566
mcap = shares * price

def mean(d):
    return sum(d.values()) / len(d)

def endpoint(d):
    return (d[2025] / d[2021]) ** (1 / 4) - 1

def fit(d):  # least-squares slope of ln(owner cash) on year
    xs, ys = list(d), [math.log(v) for v in d.values()]
    xb, yb = sum(xs) / len(xs), sum(ys) / len(ys)
    b = sum((x - xb) * (y - yb) for x, y in zip(xs, ys)) / sum((x - xb) ** 2 for x in xs)
    return math.exp(b) - 1

def value(base, g, rate, years=10):
    v, cf = 0.0, base
    for t in range(1, years + 1):
        cf *= (1 + g)
        v += cf / (1 + rate) ** t
    v += (cf / rate) / (1 + rate) ** years
    return v

def irr(base, g, target):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(base, g, mid) > target:
            lo = mid
        else:
            hi = mid
    return mid

def price_at(base, g, rate):
    return value(base, g, rate) / shares

for label, d in (("all capex", oc), ("depreciation variant", ocd)):
    b, ge, gf = mean(d), endpoint(d), fit(d)
    print(f"== {label}: five-year mean {b:,.0f}; growth endpoint FY2021->FY2025 {100*ge:.2f}%/yr; log-fit {100*gf:.2f}%/yr")
    for name, g in (("no growth", 0.0), ("shown growth, endpoint", ge), ("shown growth, log-fit", gf)):
        v = value(b, g, r)
        print(f"   {name:24s} g={100*g:6.2f}%  value ${v:,.0f}M  per share ${v/shares:,.2f}  "
              f"expected return at ${price} {100*irr(b, g, mcap):.2f}%  price clearing 10% ${price_at(b, g, 0.10):,.2f}")
b = mean(oc)
print(f"owner-cash yield at the price (all capex) {100*b/mcap:.2f}% against the sovereign {100*r:.2f}%")
print(f"market cap ${mcap:,.0f}M; growth the price needs (10y then flat) to return 5.66%: ", end="")
lo, hi = -0.1, 0.3
for _ in range(200):
    mid = (lo + hi) / 2
    if value(b, mid, r) < mcap:
        lo = mid
    else:
        hi = mid
print(f"{100*mid:.2f}%/yr; to return 10%: ", end="")
lo, hi = -0.1, 0.5
for _ in range(200):
    mid = (lo + hi) / 2
    if value(b, mid, 0.10) < mcap:
        lo = mid
    else:
        hi = mid
print(f"{100*mid:.2f}%/yr")
