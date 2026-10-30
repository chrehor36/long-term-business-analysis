"""AXP owner cash and the Q7 CONVENTION range. Inputs are the filed figures transcribed in xbrl_axp.txt (10-K accessions
listed there), USD millions. Arithmetic only; the run file carries the judgment."""
NI  = {2020: 3135, 2021: 8060, 2022: 7514, 2023: 8374, 2024: 10129, 2025: 10833}
EQ  = {2020: 22984, 2021: 22177, 2022: 24711, 2023: 28057, 2024: 30264, 2025: 33474}
BUY = {2021: 7652, 2022: 3502, 2023: 3650, 2024: 6020, 2025: 5814}
DIV = {2021: 1448, 2022: 1565, 2023: 1780, 2024: 1999, 2025: 2271}
ISS = {2021: 64, 2022: 56, 2023: 28, 2024: 100, 2025: 57}
CAPEX = {2021: 1550, 2022: 1855, 2023: 1563, 2024: 1911, 2025: 2425}
SHARES = 675.309833   # millions, 10-Q cover 2026-07-14
PRICE = 304.02
R = 0.0566            # US Treasury 30-year par yield, 2026-10-05
FLOOR = 0.10          # CONVENTION, Q7

years = range(2021, 2026)
print("year   NI    dEquity  OC=NI-dE   distributions(div+buyback-issuance)")
oc = {}
for y in years:
    oc[y] = NI[y] - (EQ[y] - EQ[y-1])
    dist = DIV[y] + BUY[y] - ISS[y]
    print(y, NI[y], EQ[y]-EQ[y-1], oc[y], dist)
mean5 = sum(oc.values()) / 5
mean4 = sum(oc[y] for y in range(2022, 2026)) / 4
print(f"five-year mean owner cash {mean5:,.0f}; 2022-2025 mean {mean4:,.0f}")
g_oc = (oc[2025] / oc[2021]) ** 0.25 - 1
g_ni = (NI[2025] / NI[2021]) ** 0.25 - 1
g_oc22 = (oc[2025] / oc[2022]) ** (1/3) - 1
print(f"growth: owner cash 2021-25 {g_oc:.2%}; net income 2021-25 {g_ni:.2%}; owner cash 2022-25 {g_oc22:.2%}")

def value(base, g, r, years=10):
    v, c = 0.0, base
    for t in range(1, years + 1):
        c *= (1 + g); v += c / (1 + r) ** t
    return v + (c / r) / (1 + r) ** years   # zero nominal growth after year ten

def irr(base, g, price_total):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(base, g, mid) > price_total: lo = mid
        else: hi = mid
    return mid

mcap = SHARES * PRICE
print(f"market cap {mcap:,.0f}")
for label, base, g in [("no growth", mean5, 0.0), ("shown growth (NI 2021-25)", mean5, g_ni),
                       ("uncapped (OC 2022-25)", mean5, g_oc22), ("no growth, 2022-25 base", mean4, 0.0),
                       ("NI growth, 2022-25 base", mean4, g_ni)]:
    v = value(base, g, R); v10 = value(base, g, FLOOR)
    print(f"{label:28s} g={g:6.2%} value@5.66% {v:>10,.0f} = ${v/SHARES:7.2f}/sh | value@10% {v10:>9,.0f} = ${v10/SHARES:7.2f}/sh | IRR at price {irr(base, g, mcap):.2%}")
need = None
lo, hi = 0.0, 0.6
for _ in range(200):
    mid = (lo + hi) / 2
    if value(mean5, mid, FLOOR) < mcap: lo = mid
    else: hi = mid
print(f"ten-year growth needed for 10% at the price: {mid:.2%}")
# Q3 cap check: shown growth carried ten years
print(f"owner cash in year 10 at NI growth: {mean5*(1+g_ni)**10:,.0f}; at OC 2022-25 growth: {mean5*(1+g_oc22)**10:,.0f}")
# buybacks: average price per share paid (10-K Note on share repurchases: shares and cost)
for y, cost, sh in [(2023, 3500, 22), (2024, 5900, 24), (2025, 5300, 17)]:
    print(y, f"avg cost per share about ${cost/sh:,.0f}")
# capex beyond depreciation
DA = {2023: 1651, 2024: 1676, 2025: 1777}
for y in DA: print(y, "capex - D&A", CAPEX[y] - DA[y])
