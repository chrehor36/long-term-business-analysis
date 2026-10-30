"""Q7 arithmetic for KO under the framework's CONVENTION (Part IV, Q7): five-year average owner cash after every real
cost, carried ten years at the growth shown (aggregate, never above it, capped by Q3), then zero nominal growth,
discounted throughout at the long government rate; the ends are the no-growth and shown-growth cases. The floor
(CONVENTION): about ten percent pre-tax expected return on the price paid. USD millions unless stated.
Inputs from owner_cash_output.txt (FY2021-FY2025), the 10-Q for the quarter ended 2026-07-03 (0001628280-26-050503)
for net debt, the 10-Q cover for shares, tools/sources.py for the rate, tools/run.py for the price (aggregator).
"""
R = 0.0566                     # US Treasury 30-year par yield, 2026-10-05
PRICE = 86.51                  # 2026-10-05 close, aggregator, flagged
SHARES = 4302.549243           # millions, 10-Q cover
MCAP = PRICE * SHARES
DEBT = 48 + 6494 + 37001       # loans and notes, current maturities, long-term debt, 2026-07-03
CASH = 12907 + 622 + 2842      # cash, short-term investments, marketable securities, 2026-07-03
NET_DEBT = DEBT - CASH
EV = MCAP + NET_DEBT

OC_RECAST = [10921, 9178, 9660, 10455, 11086]          # capex basis, recast (fairlife, IRS deposit added back)
OC_RECAST_DA = [10836, 9402, 10384, 11444, 12148]      # D&A basis, recast
OC_FILED = [10921, 9178, 9493, 4455, 5017]             # capex basis, as filed
UNLEV = [11504.0, 9847.9, 10777.9, 11773.5, 12448.0]   # recast capex basis + interest paid x (1-0.21)
PRETAX = [13827, 12429, 13655, 15386, 15683]           # recast capex basis + interest paid + income taxes paid


def mean(x):
    return sum(x) / len(x)


def shown_growth(series):
    return (series[-1] / series[0]) ** (1 / (len(series) - 1)) - 1


def value(c0, g, r=R, years=10):
    """PV of c0*(1+g)^t for t=1..years, then the year-10 cash flat forever (zero nominal growth)."""
    pv = 0.0
    c = c0
    for t in range(1, years + 1):
        c = c * (1 + g)
        pv += c / (1 + r) ** t
    pv += (c / r) / (1 + r) ** years
    return pv


def irr(price, c0, g, years=10):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(c0, g, mid, years) > price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def price_for(target, c0, g, years=10):
    return value(c0, g, target, years)


print(f"price ${PRICE}  shares {SHARES:,.1f}M  market cap {MCAP:,.0f}  net debt {NET_DEBT:,.0f} (debt {DEBT:,} less cash {CASH:,})  EV {EV:,.0f}")
print(f"rate {R*100:.2f}%\n")

c_lev = mean(OC_RECAST)
g_lev = shown_growth(OC_RECAST)
c_da = mean(OC_RECAST_DA)
g_da = shown_growth(OC_RECAST_DA)
c_un = mean(UNLEV)
g_un = shown_growth(UNLEV)
c_pt = mean(PRETAX)
g_pt = shown_growth(PRETAX)
print(f"five-year means: recast capex basis {c_lev:,.1f} (shown growth {g_lev*100:.2f}%/yr);"
      f" recast D&A basis {c_da:,.1f} ({g_da*100:.2f}%); as filed {mean(OC_FILED):,.1f};"
      f" unlevered {c_un:,.1f} ({g_un*100:.2f}%); pre-tax unlevered {c_pt:,.1f} ({g_pt*100:.2f}%)\n")

print("THE RANGE at the long government rate (equity = PV of levered owner cash; unlevered rows less net debt):")
rows = [
    ("no growth, recast capex basis (bottom)", value(c_lev, 0.0)),
    (f"shown growth {g_lev*100:.2f}%, recast capex basis (top)", value(c_lev, g_lev)),
    ("no growth, recast D&A basis", value(c_da, 0.0)),
    (f"shown growth {g_da*100:.2f}%, recast D&A basis", value(c_da, g_da)),
    ("no growth, as filed capex basis", value(mean(OC_FILED), 0.0)),
    ("no growth, unlevered, less net debt", value(c_un, 0.0) - NET_DEBT),
    (f"shown growth {g_un*100:.2f}%, unlevered, less net debt", value(c_un, g_un) - NET_DEBT),
]
for name, eq in rows:
    print(f"  {name:<52} equity {eq:>10,.0f}   per share ${eq/SHARES:7.2f}")

print("\nSTRESS AND GENEROUS VARIANTS (shown, not chosen):")
gen = [0.02, 0.04, 0.055]
for g in gen:
    eq = value(c_lev, g)
    print(f"  generous: {g*100:.1f}% for ten years (above the growth shown)       equity {eq:>10,.0f}   per share ${eq/SHARES:7.2f}")
# tax dispute lost: deposit+interest not refunded (already paid, so no further cash), plus 14bn for 2010-2025, plus
# 3.5 points on the tax rate on pre-tax income of about the pre-tax mean less interest
pretax_income_proxy = c_pt - mean([738, 848, 1415, 1669, 1724])
tax_drag = 0.035 * pretax_income_proxy
eq_tax = value(c_lev - tax_drag, 0.0) - 14000
print(f"  tax case lost (company's own figures): -$14,000M now, -3.5 points x {pretax_income_proxy:,.0f} = -{tax_drag:,.0f} a year;"
      f" no growth: equity {eq_tax:,.0f}, per share ${eq_tax/SHARES:.2f}")

print("\nTHE FLOOR (about 10% pre-tax on the price paid; all-equity basis, price paid = market cap + net debt):")
for name, g in [("no growth", 0.0), (f"shown growth {g_pt*100:.2f}% (pre-tax series)", g_pt),
                (f"shown growth {g_lev*100:.2f}% (owner-cash series)", g_lev), ("generous 5.5%", 0.055)]:
    print(f"  {name:<40} expected pre-tax return at ${PRICE}: {irr(EV, c_pt, g)*100:5.2f}%")
print(f"  after-tax, levered, on market cap (no growth): {c_lev/MCAP*100:.2f}%")

print("\nCOMPUTATION, NOT A CLEARANCE: the prices at which the floor is met")
for name, g in [("cheap (no growth clears 10% pre-tax)", 0.0), (f"fair (central case, shown growth {g_lev*100:.2f}%, clears 10%)", g_lev)]:
    ev_at = price_for(0.10, c_pt, g)
    eq_at = ev_at - NET_DEBT
    print(f"  {name:<58} EV {ev_at:,.0f}  equity {eq_at:,.0f}  per share ${eq_at/SHARES:.2f}")
ev_v = price_for(0.10, c_pt, g_pt)
label = f"fair, variant (pre-tax series shown growth {g_pt*100:.2f}%)"
print(f"  {label:<58} EV {ev_v:,.0f}  equity {ev_v-NET_DEBT:,.0f}  per share ${(ev_v-NET_DEBT)/SHARES:.2f}")
top = value(c_lev, g_lev)
print(f"\nprice against the top of the range: {PRICE/(top/SHARES):.2f} times; width of the range (top/bottom): {top/value(c_lev, 0.0):.3f}")
