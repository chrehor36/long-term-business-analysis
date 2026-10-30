"""Owner cash (Q4 recast) and the Q7 range, AMETEK, window FY2021-FY2025. Arithmetic only; every input is a filed
figure (10-K cash-flow statements, FY2021-FY2025, accessions in tenk_accessions.txt; 10-Q Q2 2026 for net debt;
8-K 0001037868-26-000191 for the Indicor price). Writes valuation_out.txt.
Conventions applied are the framework's Q7 conventions (five-year average, shown growth capped, ten years then no
real growth at the sovereign; specifics (a) to (f); all-equity basis central, equity-only beside; floor ~10%).
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
SOV = 0.0560           # US Treasury 30-year par yield, 2026-10-09
FLOOR = 0.10           # Q7 floor CONVENTION, about ten percent
SHARES = 229.261244    # millions, 10-Q cover 2026-07-28
PRICE = 248.58         # aggregator close 2026-10-09
NET_DEBT_0630 = 1540.8 # 10-Q net debt table, 2026-06-30
INDICOR = 5000.0       # all-cash, closed 2026-08-26 (8-K); financing added, credited at nothing (no filed earnings)
NET_DEBT = NET_DEBT_0630 + INDICOR

Y = [2021, 2022, 2023, 2024, 2025]
OCF = {2021: 1160.457, 2022: 1149.373, 2023: 1735.296, 2024: 1828.848, 2025: 1801.763}
SBC = {2021: 46.103, 2022: 47.375, 2023: 46.199, 2024: 47.863, 2025: 47.767}
CAPEX = {2021: 110.671, 2022: 139.005, 2023: 136.249, 2024: 127.075, 2025: 130.248}
ACQ = {2021: 1959.218, 2022: 429.714, 2023: 2237.910, 2024: 117.514, 2025: 933.242}
DIVEST = {2021: 12.000, 2022: 3.734, 2023: 0.0, 2024: 0.0, 2025: 0.0}
INT_EXP = {2021: 80.4, 2022: 83.2, 2023: 81.8, 2024: 113.0, 2025: 81.3}
INT_INC = {2021: 1.4, 2022: 1.7, 2023: 11.1, 2024: 5.8, 2025: 5.5}
TAX = {2021: 233.1, 2022: 269.1, 2023: 293.2, 2024: 285.4, 2025: 318.2}
NI = {2021: 990.1, 2022: 1159.5, 2023: 1313.2, 2024: 1376.1, 2025: 1480.1}
WC = {2021: -125.387, 2022: -266.473, 2023: 142.786, 2024: 66.673, 2025: -60.615}  # the four change lines summed
ORGANIC = {2022: 0.11, 2023: 0.04, 2024: -0.02, 2025: 0.02}  # filer's company organic sales growth

out = ["COMPUTATION, NOT A CLEARANCE (computed during Q3 and Q4, before Q4 to Q6 closed; reported only at Q7)", ""]
def p(s=""):
    out.append(s)

etr = {y: TAX[y] / (NI[y] + TAX[y]) for y in Y}
oc_eq = {y: OCF[y] - SBC[y] - CAPEX[y] for y in Y}                      # equity basis, before acquisitions
oc_ae = {y: oc_eq[y] + (INT_EXP[y] - INT_INC[y]) * (1 - etr[y]) for y in Y}  # all-equity basis
netacq = {y: ACQ[y] - DIVEST[y] for y in Y}
p("OWNER CASH (USD millions)  = OCF - stock pay - all capital spending; all-equity adds back net interest after the company's tax")
p("year   OCF      SBC    capex   owner(eq)  ETR    net int a/t  owner(all-eq)  net acquisitions  WC change in OCF")
for y in Y:
    p(f"{y}  {OCF[y]:8.1f} {SBC[y]:6.1f} {CAPEX[y]:7.1f}  {oc_eq[y]:8.1f}  {etr[y]*100:4.1f}%  {oc_ae[y]-oc_eq[y]:8.1f}     {oc_ae[y]:8.1f}        {netacq[y]:8.1f}        {WC[y]:7.1f}")
avg = lambda d: sum(d[y] for y in Y) / len(Y)
p(f"five-year averages: owner(eq) {avg(oc_eq):.1f}; owner(all-eq) {avg(oc_ae):.1f}; net acquisitions {avg(netacq):.1f}; WC change {avg(WC):.1f}")
after_acq_ae = {y: oc_ae[y] - netacq[y] for y in Y}
after_acq_eq = {y: oc_eq[y] - netacq[y] for y in Y}
p(f"owner cash after net acquisitions: all-eq {[round(after_acq_ae[y],1) for y in Y]} avg {avg(after_acq_ae):.1f}; eq avg {avg(after_acq_eq):.1f}")

# growth shown, aggregate, end years 2021 -> 2025 (4 steps); and halves (b) where needed
def cagr(a, b, n):
    return (b / a) ** (1 / n) - 1
g_total_ae = cagr(oc_ae[2021], oc_ae[2025], 4)
g_total_eq = cagr(oc_eq[2021], oc_eq[2025], 4)
h1 = (oc_ae[2021] + oc_ae[2022]) / 2; h2 = (oc_ae[2024] + oc_ae[2025]) / 2
g_halves_ae = cagr(h1, h2, 2.5)
g_org = 1.0
for y in [2022, 2023, 2024, 2025]:
    g_org *= 1 + ORGANIC[y]
g_org = g_org ** (1 / 4) - 1
p(f"growth shown (aggregate owner cash before acquisitions, end years 2021->2025): all-eq {g_total_ae*100:.2f}%/yr, eq {g_total_eq*100:.2f}%/yr")
p(f"   first-half (2021-22) to second-half (2024-25) mean, 2.5 years apart: all-eq {g_halves_ae*100:.2f}%/yr")
p(f"organic growth shown (filer's organic sales growth 2022-2025 compounded): {g_org*100:.2f}%/yr")
p(f"WC intensity check (specific d): window average WC change {avg(WC):.1f}/yr against FY2019 (pre-event year) -45.0/yr: no adjustment made")

def value(base, g, r, years=10):
    """base = year-0 cash; years 1..10 grow at g; after year 10, flat (zero nominal growth); discounted at r."""
    pv = 0.0; cf = base
    for t in range(1, years + 1):
        cf = cf * (1 + g)
        pv += cf / (1 + r) ** t
    pv += (cf / r) / (1 + r) ** years
    return pv

def stream_value_mid(base_lo, g_lo, base_hi, g_hi, r, years=10):
    """value at rate r of the year-by-year average of the two end streams (the 'midpoint of the range')."""
    pv = 0.0; c1 = base_lo; c2 = base_hi
    for t in range(1, years + 1):
        c1 *= 1 + g_lo; c2 *= 1 + g_hi
        pv += (c1 + c2) / 2 / (1 + r) ** t
    pv += ((c1 + c2) / 2 / r) / (1 + r) ** years
    return pv

def report(label, base, g, net_debt, basis):
    lo, hi = value(base, 0.0, SOV), value(base, g, SOV)
    if g < 0:
        lo, hi = hi, lo
    eq_lo, eq_hi = lo - net_debt, hi - net_debt
    fair_whole = stream_value_mid(base, 0.0, base, g, FLOOR)
    fair = (fair_whole - net_debt) / SHARES
    mid = (eq_lo + eq_hi) / 2 / SHARES
    width = hi / lo if lo > 0 else float("nan")
    p(f"\n{label}  [{basis}]  base {base:,.1f}  growth {g*100:.2f}%")
    p(f"   whole-business value at {SOV*100:.2f}%: {lo:,.0f} to {hi:,.0f}   (width {width:.2f} to one)")
    p(f"   less net debt {net_debt:,.1f}: equity {eq_lo:,.0f} to {eq_hi:,.0f} = ${eq_lo/SHARES:,.2f} to ${eq_hi/SHARES:,.2f} a share (mid ${mid:,.2f}) vs price ${PRICE}")
    p(f"   FAIR PRICE (midpoint stream at {FLOOR*100:.0f}%, less net debt): ${fair:,.2f} a share")
    return eq_lo / SHARES, eq_hi / SHARES, fair

p(f"\nNET DEBT used: 2026-06-30 {NET_DEBT_0630} + Indicor {INDICOR} = {NET_DEBT}; market cap {PRICE*SHARES:,.0f}; EV {PRICE*SHARES+NET_DEBT:,.0f}")
p("\n==== DEFAULT PAIR (specific c): acquisitions deducted, total growth credited")
report("A1 central, all-equity", avg(after_acq_ae), g_total_ae, NET_DEBT, "all-equity, net debt deducted")
report("A1' SENSITIVITY ONLY, not the convention's growth (halves)", avg(after_acq_ae), g_halves_ae, NET_DEBT, "all-equity")
# Equity-only: owner cash after the window's interest, against the shares; no net-debt deduction (the debt is served
# in the cash), but Indicor's $5.0bn price is deducted because its financing is not in the window.
lo, hi = value(avg(after_acq_eq), 0, SOV), value(avg(after_acq_eq), g_total_eq, SOV)
fe = stream_value_mid(avg(after_acq_eq), 0, avg(after_acq_eq), g_total_eq, FLOOR)
p(f"\nA2 equity-only, default pair: base {avg(after_acq_eq):,.1f} growth {g_total_eq*100:.2f}%: ${(lo-INDICOR)/SHARES:,.2f} to ${(hi-INDICOR)/SHARES:,.2f} a share; fair ${(fe-INDICOR)/SHARES:,.2f}")
p("\n==== ORGANIC PAIR, beside: acquisitions left out, only organic growth credited")
report("B1 organic, all-equity", avg(oc_ae), g_org, NET_DEBT, "all-equity")
lo, hi = value(avg(oc_eq), 0, SOV), value(avg(oc_eq), g_org, SOV)
fe = stream_value_mid(avg(oc_eq), 0, avg(oc_eq), g_org, FLOOR)
p(f"\nB2 equity-only, organic pair: base {avg(oc_eq):,.1f} growth {g_org*100:.2f}%: ${(lo-INDICOR)/SHARES:,.2f} to ${(hi-INDICOR)/SHARES:,.2f} a share; fair ${(fe-INDICOR)/SHARES:,.2f}")
p("\n==== WITHOUT INDICOR (net debt at 2026-06-30 only), for the reader: the deal is valued at nothing by the convention")
report("A1 without Indicor", avg(after_acq_ae), g_total_ae, NET_DEBT_0630, "all-equity")
report("B1 without Indicor", avg(oc_ae), g_org, NET_DEBT_0630, "all-equity")

# expected return at the price, organic pair: IRR of buying EV at price for the organic stream
def irr(price_ev, base, g):
    lo, hi = 0.0, 0.5
    for _ in range(200):
        m = (lo + hi) / 2
        if value(base, g, m) > price_ev:
            lo = m
        else:
            hi = m
    return m
ev = PRICE * SHARES + NET_DEBT
p(f"\nEXPECTED RETURN at the price (EV {ev:,.0f}): organic pair top case {irr(ev, avg(oc_ae), g_org)*100:.2f}%; "
  f"default pair top case {irr(ev, avg(after_acq_ae), g_total_ae)*100:.2f}%; no-growth owner cash {avg(oc_ae)/ev*100:.2f}% yield")
# what growth for 10 years then flat would the price need at the floor and at the sovereign (organic base)
def need_g(price_ev, base, r):
    lo, hi = -0.5, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        if value(base, m, r) < price_ev:
            lo = m
        else:
            hi = m
    return m
p(f"growth for ten years (then flat) the price needs on the organic base: at the sovereign {need_g(ev, avg(oc_ae), SOV)*100:.2f}%/yr; at the floor {need_g(ev, avg(oc_ae), FLOOR)*100:.2f}%/yr")
open(os.path.join(HERE, "valuation_out.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
