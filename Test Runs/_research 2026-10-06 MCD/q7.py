"""Q7 arithmetic for MCD, run 2026-10-06. COMPUTATION, not a clearance.
CONVENTION of the framework (Q7, the range): five-year mean of owner cash after every real cost, carried for ten years at
the growth shown on the aggregate owner cash (capped by Q3), then zero nominal growth, discounted at the long government
rate; the ends are the no-growth case and the shown-growth case.
Floor CONVENTION: about 10% pre-tax; owner cash is after corporate tax, so the after-tax equivalent is taken at the
company's 2025 effective rate, 21.4% (10-K FY2025, Provision for income taxes) -> 7.86%.
All figures $M except per share."""
OC = {  # column A: OCF - SBC - capex, from the filed cash-flow statements (Step 0 table)
    2021: 9141.5 - 139.2 - 2040.0, 2022: 7386.7 - 166.7 - 1899.2, 2023: 9611.9 - 175.2 - 2357.4,
    2024: 9447 - 172 - 2775, 2025: 10551 - 165 - 3365}
OC_B = {2021: 6730.4, 2022: 4503.0, 2023: 6157.3, 2024: 5644.0, 2025: 6434.0}   # column B
OC_C = {2021: 7134.2, 2022: 5349.4, 2023: 7458.5, 2024: 7178.0, 2025: 8187.0}   # depreciation variant
SOV = 0.0566            # US Treasury 30-year par yield, 10/05/2026 (tools/sources.py)
SHARES = 707.641531     # cover, 10-Q accession 0000063908-26-000073
PRICE = 233.04          # aggregator close 2026-10-05, flagged
TAX = 0.214
FLOOR_AT = 0.10 * (1 - TAX)

def mean(d): return sum(d.values()) / len(d)
def cagr(d):
    ys = sorted(d); return (d[ys[-1]] / d[ys[0]]) ** (1 / (ys[-1] - ys[0])) - 1
def ols_growth(d):
    import math
    ys = sorted(d); xs = [y - ys[0] for y in ys]; ls = [math.log(d[y]) for y in ys]
    mx = sum(xs) / len(xs); ml = sum(ls) / len(ls)
    b = sum((x - mx) * (l - ml) for x, l in zip(xs, ls)) / sum((x - mx) ** 2 for x in xs)
    return math.exp(b) - 1
def pv(base, g, r, years=10):
    v = 0.0; cf = base
    for t in range(1, years + 1):
        cf *= (1 + g); v += cf / (1 + r) ** t
    return v + (cf / r) / (1 + r) ** years
def price_for_return(base, g, target):
    return pv(base, g, target) / SHARES
def irr(base, g, price_total):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(base, g, mid) > price_total: lo = mid
        else: hi = mid
    return mid

cap = PRICE * SHARES
for name, d in (('A (all capex)', OC), ('B (A less restaurant purchases net and Other investing)', OC_B),
                ('C (depreciation variant)', OC_C)):
    m = mean(d); g_end = cagr(d); g_ols = ols_growth(d)
    print(f'--- {name}: five-year mean {m:,.0f}; growth shown 2021->2025 endpoint {g_end:.2%}, log-trend {g_ols:.2%}')
    for label, g in (('no growth', 0.0), ('shown growth (endpoint)', g_end), ('shown growth (log-trend)', g_ols)):
        v = pv(m, g, SOV)
        print(f'   {label:26s} value {v:,.0f} = ${v / SHARES:,.2f}/sh; return at price {irr(m, g, cap):.2%} after tax; '
              f'price that earns the floor ({FLOOR_AT:.2%} after tax): ${price_for_return(m, g, FLOOR_AT):,.2f}')
print(f'market cap at ${PRICE}: {cap:,.0f}; owner-cash yield (A mean) {mean(OC) / cap:.2%}')
# sensitivity, not the convention: the ten-year record 2016->2025 of column A (refranchising years included)
g10 = (7021 / 4107) ** (1 / 9) - 1
v = pv(mean(OC), g10, SOV)
print(f'sensitivity only: 2016->2025 growth of column A {g10:.2%}: value ${v / SHARES:,.2f}/sh; return at price {irr(mean(OC), g10, cap):.2%}')
for g in (0.03, 0.05):
    print(f'sensitivity only: {g:.0%} for ten years then flat: ${pv(mean(OC), g, SOV) / SHARES:,.2f}/sh; return at price {irr(mean(OC), g, cap):.2%}')
