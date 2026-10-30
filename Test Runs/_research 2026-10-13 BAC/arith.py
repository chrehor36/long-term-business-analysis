# BAC run 2026-10-13: arithmetic only. Every input is a filed figure (source in the comment); the
# construction is Q7's range convention as the run file states it. COMPUTATION, NOT A CLEARANCE.
# Dollars in millions unless noted.

# Net income applicable to common shareholders (after preferred dividends), as filed.
# 2019-2025: XBRL NetIncomeLossAvailableToCommonStockholdersBasic, latest 10-K carrying each year
# (0000070858-26-000157 for 2023-2025; FY2021 10-K 0000070858-22-000062 for 2019-2021; FY2022 10-K 0000070858-23-000092).
ni_common = {2019: 25998, 2020: 16473, 2021: 30557, 2022: 26015, 2023: 24656, 2024: 25344, 2025: 29055}

# Standardized-approach RWA (USD bn) and CET1 ratio at year end, Corporation, from each 10-K's capital table:
# 2018-2019 FY2019 10-K (0000070858-20-000011); 2020-2021 FY2021 10-K; 2022 FY2022 10-K; 2023 FY2023 10-K
# (0000070858-24-000122); 2024-2025 FY2025 10-K (0000070858-26-000157).
rwa = {2018: 1437, 2019: 1493, 2020: 1480, 2021: 1618, 2022: 1605, 2023: 1651, 2024: 1696, 2025: 1773}
cet1 = {2018: .116, 2019: .112, 2020: .119, 2021: .106, 2022: .112, 2023: .118, 2024: .119, 2025: .114}

# Revenue, net of interest expense (XBRL Revenues, FY2025 10-K), for the cap test.
rev = {2019: 91244, 2020: 85528, 2021: 89113, 2022: 94950, 2023: 102769, 2024: 105856, 2025: 113097}

# Cash returned to common owners (dividends declared + repurchases), from the equity statements of the
# FY2022 and FY2025 10-Ks; a cross-check on owner cash, not an input.
returned = {2021: 6575 + 25126, 2022: 6963 + 5073, 2023: 7374 + 4576, 2024: 7822 + 13104, 2025: 8083 + 21433}

price = 54.58                 # close 2026-10-12, Yahoo chart (aggregator, live quote only, flagged)
shares = 6_992_748_365 / 1e6  # 10-Q cover, filed 2026-07-31, accession 0000070858-26-000394 (millions)
r_sov = 0.0560                # US Treasury 30-year par yield, 2026-10-09 (tools/sources.py)
r_floor = 0.10                # Q7 floor CONVENTION, about ten percent

# Owner cash, the CONVENTION of this run: maintenance-only = net income to common (depreciation taken as the
# maintenance spend, stock pay already expensed); after growth spending = less the CET1 capital retained to hold
# the start-of-year CET1 ratio against the year's RWA growth.
def after_growth(y):
    return ni_common[y] - cet1[y - 1] * (rwa[y] - rwa[y - 1]) * 1000

oc = {y: after_growth(y) for y in ni_common}

def avg(d, ys):
    return sum(d[y] for y in ys) / len(ys)

def pv(base, g, r, years=10):
    """base grows at g for `years`, then flat (zero nominal growth) forever; discounted at r."""
    v, cf = 0.0, base
    for t in range(1, years + 1):
        cf *= (1 + g)
        v += cf / (1 + r) ** t
    return v + (cf / r) / (1 + r) ** years

def irr(base, g, value, years=10):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(base, g, mid, years) > value:
            lo = mid
        else:
            hi = mid
    return mid

cap = price * shares
print(f"market value of common at ${price}: {cap:,.0f}m on {shares:,.1f}m shares")
print("year  NIcommon  RWAgrowth(bn)  capital retained  ownercash(after growth)  returned  share of revenue")
for y in sorted(ni_common):
    print(f"{y}  {ni_common[y]:8,.0f}  {rwa[y]-rwa[y-1]:6.0f}  {ni_common[y]-oc[y]:9,.0f}  {oc[y]:9,.0f}  "
          f"{returned.get(y, float('nan')):9,.0f}  {oc[y]/rev[y]*100:5.1f}%")

win = [2021, 2022, 2023, 2024, 2025]
cyc = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
cases = {}
for label, ys in (("literal window 2021-2025", win), ("cycle base 2019-2025", cyc)):
    m_base = avg(ni_common, ys)          # maintenance-only owner cash
    g_base = avg(oc, ys)                 # owner cash after the capital that growth needs
    half = len(ys) // 2
    first, second = ys[:half], ys[-half:]
    span = (sum(second) / len(second)) - (sum(first) / len(first))
    g_halves = (avg(oc, second) / avg(oc, first)) ** (1 / span) - 1
    g_ends = (oc[ys[-1]] / oc[ys[0]]) ** (1 / (ys[-1] - ys[0])) - 1
    g_rev = (rev[ys[-1]] / rev[ys[0]]) ** (1 / (ys[-1] - ys[0])) - 1
    print(f"\n== {label}")
    print(f"  maintenance-only owner cash (avg NI to common): {m_base:,.0f}")
    print(f"  owner cash after growth capital (avg): {g_base:,.0f}   returned avg: "
          f"{avg(returned, [y for y in ys if y in returned]):,.0f}")
    print(f"  growth: end-to-end {g_ends*100:.1f}%  between halves {g_halves*100:.1f}%  revenue {g_rev*100:.1f}%")
    ng = m_base / r_sov
    gr = pv(g_base, g_halves, r_sov)
    print(f"  no-growth case (maintenance-only, flat): {ng:,.0f}m = ${ng/shares:.2f}/sh")
    print(f"  growth case (after growth capital, {g_halves*100:.1f}% ten years, flat after): {gr:,.0f}m = ${gr/shares:.2f}/sh")
    lo, hi = sorted([ng, gr])
    print(f"  range ${lo/shares:.2f} to ${hi/shares:.2f}; width {hi/lo:.2f} to one")
    ng10 = m_base / r_floor
    gr10 = pv(g_base, g_halves, r_floor)
    print(f"  at ten percent: no-growth ${ng10/shares:.2f}/sh, growth ${gr10/shares:.2f}/sh; "
          f"fair price (average) ${(ng10+gr10)/2/shares:.2f}/sh")
    print(f"  return at the price: no-growth yield {m_base/cap*100:.2f}%; growth case IRR {irr(g_base, g_halves, cap)*100:.2f}%")
    # cap test (f): owner cash carried ten years against the highest share of revenue in the filings read
    top_share = max(oc[y] / rev[y] for y in ys)
    oc10 = g_base * (1 + g_halves) ** 10
    rev10 = avg(rev, ys) * (1 + g_rev) ** 10
    print(f"  cap test: owner cash year ten {oc10:,.0f} = {oc10/rev10*100:.1f}% of revenue grown at its own rate; "
          f"highest share in window {top_share*100:.1f}%")
    cases[label] = (ng, gr)

# Beside, not central: the long cycle that holds the bank's own credit losses, 2007-2019 peak to peak, on net
# income to common as filed (FY2010 10-K five-year summary 0000950123-11-018743 for 2006-2010; XBRL for the rest).
long_ni = {2007: 14800, 2008: 2556, 2009: -2204, 2010: -3595, 2011: 85, 2012: 2760, 2013: 10082, 2014: 4476,
           2015: 14427, 2016: 16140, 2017: 16618, 2018: 26696, 2019: 25998}
lavg = sum(long_ni.values()) / len(long_ni)
print(f"\n== beside: 2007-2019 average NI to common {lavg:,.0f}m; no-growth at the sovereign ${lavg/r_sov/shares:.2f}/sh, "
      f"at ten percent ${lavg/r_floor/shares:.2f}/sh")

# Added after the first print: the cycle base's end years (2019, 2025) are both ordinary years, so its
# end-to-end rate is meaningful and is the shown growth by specific (b); the halves rate is shown beside.
print("\n== cycle base 2019-2025, shown growth end-to-end (central)")
m_base, g_base = avg(ni_common, cyc), avg(oc, cyc)
g_e = (oc[2025] / oc[2019]) ** (1 / 6) - 1
ng, gr = m_base / r_sov, pv(g_base, g_e, r_sov)
lo, hi = sorted([ng, gr])
print(f"  growth {g_e*100:.2f}%: no-growth ${ng/shares:.2f}, growth case ${gr/shares:.2f}; range ${lo/shares:.2f} to ${hi/shares:.2f}, width {hi/lo:.2f}")
ng10, gr10 = m_base / r_floor, pv(g_base, g_e, r_floor)
print(f"  at ten percent: ${ng10/shares:.2f} and ${gr10/shares:.2f}; fair price ${(ng10+gr10)/2/shares:.2f}")
print(f"  return at the price: no-growth {m_base/cap*100:.2f}%, growth case IRR {irr(g_base, g_e, cap)*100:.2f}%")
print(f"  bottom of range per share ${lo/shares:.2f}; buyback average prices 2021-2025: "
      + ", ".join(f"{y} ${v:.2f}" for y, v in {2021: 25126/615.3, 2022: 5073/125.9, 2023: 4576/146.7,
                                               2024: 13104/331.5, 2025: 21433/451.9}.items()))
