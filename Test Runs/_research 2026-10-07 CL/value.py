# Q4 owner cash and the Q7 range under the framework's CONVENTION construction; arithmetic only, every input from the filings
years = [2021, 2022, 2023, 2024, 2025]
ocf   = [3325, 2556, 3745, 4107, 4198]   # cash-flow statements (FY2022 and FY2025 10-Ks)
sbc   = [135, 125, 122, 135, 155]        # stock-based compensation expense, same
capex = [567, 696, 705, 561, 564]        # capital expenditures, same
nci   = [166, 135, 170, 168, 157]        # dividends to noncontrolling interests, statements of changes in equity
acq   = [0, 809, 0, 0, 293]              # payment for acquisitions, net of cash acquired
netint= [103, 153, 232, 225, 192]        # interest expense less interest income (income statements; 2021 from the FY2022 10-K)
TAX = 0.23                               # the company's own non-GAAP effective rate 2024-2025 (22.7%, 23.1%), MD&A
R = 0.0564                               # US Treasury 30-year par yield, 2026-10-06
FLOOR = 0.10                             # Q7 CONVENTION, about ten percent
SH = 797.172829                          # millions of shares, 10-Q cover, 2026-06-30
NETDEBT = 6404                           # 2026-06-30: 34 + 7,823 - 1,370 - 83
PRICE = 87.25
MCAP = SH * PRICE
def avg(x): return sum(x) / len(x)
eq      = [o - s - c - n for o, s, c, n in zip(ocf, sbc, capex, nci)]          # owner cash after interest (equity-only)
unlev   = [e + i * (1 - TAX) for e, i in zip(eq, netint)]                     # before interest, after the company's tax
eq_a    = [e - a for e, a in zip(eq, acq)]
unlev_a = [u - a for u, a in zip(unlev, acq)]
def cagr(a, b, n): return (b / a) ** (1 / n) - 1
def stream(base, g, n=10):
    # years 1..10 at g, then zero nominal growth forever (CONVENTION: no real growth computed as zero nominal)
    cf = [base * (1 + g) ** t for t in range(1, n + 1)]
    return cf, cf[-1]
def pv(base, g, r):
    cf, last = stream(base, g)
    return sum(c / (1 + r) ** t for t, c in enumerate(cf, 1)) + last / r / (1 + r) ** len(cf)
def irr(base, g, price):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        (lo, hi) = (mid, hi) if pv(base, g, mid) > price else (lo, mid)
    return mid
def show(label, series, basis_netdebt, cap_vs):
    base, g = avg(series), cagr(series[0], series[-1], 4)
    lo_v, hi_v = pv(base, 0, R), pv(base, g, R)
    lo_v, hi_v = min(lo_v, hi_v), max(lo_v, hi_v)
    mid = (lo_v + hi_v) / 2
    fair = (pv(base, 0, FLOOR) + pv(base, g, FLOOR)) / 2   # the midpoint stream (average of the two end streams) at the floor
    ps = lambda v: (v - basis_netdebt) / SH
    print(f"\n{label}")
    print("  series:", [round(x) for x in series], f" five-year average {base:,.0f}; growth between end years {100*g:.2f}%")
    print(f"  range (whole): {lo_v:,.0f} to {hi_v:,.0f}  width {hi_v/lo_v:.2f} to one; midpoint {mid:,.0f}")
    print(f"  per share: ${ps(lo_v):.2f} to ${ps(hi_v):.2f}, midpoint ${ps(mid):.2f}; fair price ${ps(fair):.2f}; price ${PRICE}")
    print(f"  expected return at the price ({cap_vs:,.0f}): no-growth {100*irr(base,0,cap_vs):.2f}%, shown growth {100*irr(base,g,cap_vs):.2f}%")
    return base, g
print("owner cash after interest (equity-only):", [round(x) for x in eq], "avg", round(avg(eq)))
print("owner cash before interest (all-equity):", [round(x) for x in unlev], "avg", round(avg(unlev)))
print(f"market cap {MCAP:,.0f}; plus net debt {MCAP+NETDEBT:,.0f}")
show("ALL-EQUITY, acquisitions deducted, total growth credited (central, default pair)", unlev_a, NETDEBT, MCAP + NETDEBT)
show("EQUITY-ONLY, acquisitions deducted, total growth credited", eq_a, 0, MCAP)
# organic pair: acquisitions left out, only organic growth as the filer reports it credited (4.5, 7.0, 8.5, 7.4, 1.4)
org = (1.045 * 1.07 * 1.085 * 1.074 * 1.014) ** (1 / 5) - 1
for label, series, nd, cap in [("ALL-EQUITY, organic pair", unlev, NETDEBT, MCAP + NETDEBT), ("EQUITY-ONLY, organic pair", eq, 0, MCAP)]:
    base = avg(series)
    lo_v, hi_v = pv(base, 0, R), pv(base, org, R)
    fair = (pv(base, 0, FLOOR) + pv(base, org, FLOOR)) / 2
    print(f"\n{label}: base {base:,.0f}, organic growth {100*org:.2f}%: ${(lo_v-nd)/SH:.2f} to ${(hi_v-nd)/SH:.2f} a share; fair ${(fair-nd)/SH:.2f}; "
          f"return at price {100*irr(base,0,cap):.2f}% to {100*irr(base,org,cap):.2f}%")

# beside the central case, not deciding: (e) maintenance-only spending at the stated guess of $525M a year (the midpoint of
# $500M-$550M), growth spending left out and the same shown growth credited; and the longer record of growth
MAINT = 525
unlev_m = [u - a + (c - MAINT) for u, a, c in zip(unlev, acq, capex)]
show("ALL-EQUITY, maintenance-only spending (guess $525M), acquisitions deducted, shown growth", unlev_m, NETDEBT, MCAP + NETDEBT)
# longer record: OCF - SBC - capex - acquisitions, three-year averages 2014-2016 against 2023-2025 (no minority or interest adjustment)
early = avg([3298-131-757-87, 2949-125-691-13, 3141-123-593-5]); late = avg([3745-122-705-0, 4107-135-561-0, 4198-155-564-293])
g_long = (late / early) ** (1 / 9) - 1
base = avg(unlev_a)
print(f"\nlonger record, 2014-16 to 2023-25 averages: {early:,.0f} to {late:,.0f}, {100*g_long:.2f}% a year")
print(f"  central base at that growth: top ${(pv(base, g_long, R)-NETDEBT)/SH:.2f} a share; return at price {100*irr(base, g_long, MCAP+NETDEBT):.2f}%")
