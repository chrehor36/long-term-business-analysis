"""IBM 2026-10-06 run: owner cash and the Q7-convention arithmetic. COMPUTATION - NOT A CLEARANCE.
Inputs are the filed cash-flow statements: FY2023-FY2025 from the FY2025 10-K (0000051143-26-000010),
FY2021-FY2022 from the FY2023 10-K (0000051143-24-000012). USD millions.
"""
years = [2021, 2022, 2023, 2024, 2025]
ocf  = {2021: 12796, 2022: 10435, 2023: 13931, 2024: 13445, 2025: 13193}
sbc  = {2021: 982,   2022: 987,   2023: 1133,  2024: 1311,  2025: 1715}
capex= {2021: 2062,  2022: 1346,  2023: 1245,  2024: 1048,  2025: 1091}
soft = {2021: 706,   2022: 626,   2023: 565,   2024: 637,   2025: 647}
acq  = {2021: 3293,  2022: 2348,  2023: 5082,  2024: 3289,  2025: 8294}
rev  = {2021: 57350, 2022: 60530, 2023: 61860, 2024: 62753, 2025: 67535}

shares = 942.134390   # cover of 10-Q filed 2026-07-23, accession 0000051143-26-000078
price = 221.58        # aggregator quote 2026-10-05 via tools/run.py (flagged)
r = 0.0566            # US Treasury 30-year par yield, 2026-10-05 (tools/sources.py)
floor = 0.10          # CONVENTION, Q7 floor

oc = {y: ocf[y] - sbc[y] - capex[y] - soft[y] for y in years}
oca = {y: oc[y] - acq[y] for y in years}
print("FY   OCF    SBC  capex  soft   owner cash  /rev   acquisitions  after acq")
for y in years:
    print(y, ocf[y], sbc[y], capex[y], soft[y], oc[y], f"{oc[y]/rev[y]:.1%}", acq[y], oca[y])
avg = sum(oc.values()) / 5
avga = sum(oca.values()) / 5
g = (oc[2025] / oc[2021]) ** 0.25 - 1
print(f"5-yr avg owner cash {avg:.1f}; after acquisitions {avga:.1f}; growth shown (aggregate, FY2021->FY2025) {g:.2%}")

def pv(c, g, rate, years=10):
    v, cf = 0.0, c
    for t in range(1, years + 1):
        cf *= (1 + g)
        v += cf / (1 + rate) ** t
    v += cf / rate / (1 + rate) ** years   # zero nominal growth after year ten
    return v

lo = avg / r
hi = pv(avg, g, r)
print(f"no-growth end  {lo:,.0f}  = ${lo/shares:.2f}/sh")
print(f"shown-growth end {hi:,.0f} = ${hi/shares:.2f}/sh ; width {hi/lo:.2f} to one")
print(f"market cap at price {price*shares:,.0f}; owner-cash yield {avg/(price*shares):.2%}")
fair = pv(avg, g, floor) / shares
cheap = avg / floor / shares
print(f"fair (central = shown growth, at 10%) ${fair:.2f}; cheap (no growth at 10%) ${cheap:.2f}")
print(f"sensitivity: after-acquisition owner cash, no growth, at sovereign ${avga/r/shares:.2f}; at 10% ${avga/floor/shares:.2f}")
# implied return at the price on the central case: solve rate where pv = market cap
mc = price * shares
lo_r, hi_r = 0.001, 0.5
for _ in range(200):
    mid = (lo_r + hi_r) / 2
    if pv(avg, g, mid) > mc: lo_r = mid
    else: hi_r = mid
print(f"expected return at price, central case: {mid:.2%}")
