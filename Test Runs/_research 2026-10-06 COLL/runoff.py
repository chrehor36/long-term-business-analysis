# COLL product run-off computation. COMPUTATION, NOT A CLEARANCE (the run closed at Q1).
# Every input is from the filings named in the run file, or is a CONVENTION of the run, labelled there.
# Pre-tax, unlevered (enterprise) cash: revenue x contribution margin, less ~2 capex; no replacement purchases.
# Valuation date 2026-10-05; Q4 2026 counted at 0.125 yr, each later calendar year at mid-year.

SOV = 0.0566          # US Treasury 30-yr par yield, 2026-10-05 (tools/run.py)
FLOOR = 0.10          # Q7 CONVENTION, about ten percent pre-tax
SHARES = 32.555613    # cover count, 10-Q 2026-06-30, as of 2026-07-31 (pre-ASR)
PRICE = 21.87         # close 2026-10-05, aggregator, flagged
NET_DEBT = 1147.2     # 2026-06-30 balance sheet, see run file Step 0 (pre-ASR, pairs with SHARES)

def erode(base, growth, loe_year, start=2027, end=2045, first=0.5, after=0.35):
    """revenue path: grows at `growth` until loe_year, then -first in loe year, -after each year after"""
    out = {}
    r = base
    for y in range(start, end + 1):
        if y < loe_year:
            r = r * (1 + growth) if y > start else r
        elif y == loe_year:
            r = r * (1 - first)
        else:
            r = r * (1 - after)
        out[y] = r
    return out

CASES = {
 # product: (2027 base revenue $M, growth pre-LOE, first year of generic entry)
 'low': dict(margin=0.45, prods={
    'Nucynta':  (67.0, 0.00, 2028),   # already generic in 2026; 2027 = half of ~135
    'Belbuca':  (165.0, 0.00, 2028),  # entry mid-2027 (2027 base already cut by a quarter), full -50% 2028
    'Xtampza':  (171.0, -0.10, 2030), # -10%/yr, entry 2030 (Teva acceleration / earliest patent date)
    'Jornay':   (200.0, 0.03, 2032),
    'Azstarys': (115.0, 0.00, 2034),
    'Symproic': (14.0, -0.05, 2031)}),
 'central': dict(margin=0.50, prods={
    'Nucynta':  (67.0, 0.00, 2028),
    'Belbuca':  (220.0, 0.00, 2028),  # Alvogen 30-month stay ends ~Jan 2028; trial April 2027
    'Xtampza':  (180.0, -0.05, 2034), # Teva licence from 2033-09-02
    'Jornay':   (210.0, 0.08, 2032),
    'Azstarys': (125.0, 0.08, 2038),  # most patents to Dec 2037
    'Symproic': (14.0, -0.05, 2031)}),
 'high': dict(margin=0.55, prods={
    'Nucynta':  (75.0, 0.00, 2028),
    'Belbuca':  (225.0, 0.00, 2033),  # '539 patent upheld to Dec 2032
    'Xtampza':  (190.0, 0.00, 2034),
    'Jornay':   (215.0, 0.12, 2033),
    'Azstarys': (130.0, 0.12, 2038),
    'Symproic': (15.0, 0.00, 2031)}),
}
Q4_2026_EBIT = 0.25 * 445.0 * 0.95   # a quarter of the low end of 2026 adjusted-EBITDA guidance, less SBC (~5%), pre-tax

def streams(case):
    c = CASES[case]
    rev = {}
    for p, (b, g, loe) in c['prods'].items():
        for y, v in erode(b, g, loe).items():
            rev[y] = rev.get(y, 0) + v
    cash = {y: v * c['margin'] - 2.0 for y, v in rev.items()}
    return rev, cash

def pv(cash, r):
    tot = Q4_2026_EBIT / (1 + r) ** 0.125
    for y, v in cash.items():
        tot += v / (1 + r) ** (y - 2026 - 0.5 + 0.25)
    return tot

def irr_on_ev(cash, ev):
    lo, hi = -0.5, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(cash, mid) > ev: lo = mid
        else: hi = mid
    return mid

ev_now = PRICE * SHARES + NET_DEBT
print(f"market cap {PRICE*SHARES:,.1f}  net debt {NET_DEBT:,.1f}  EV {ev_now:,.1f}")
for case in ('low', 'central', 'high'):
    rev, cash = streams(case)
    ev_s = pv(cash, SOV); ev_f = pv(cash, FLOOR)
    print(f"\n{case.upper()}: margin {CASES[case]['margin']:.0%}")
    print('  revenue  ' + ' '.join(f"{y}:{rev[y]:.0f}" for y in range(2027, 2040)))
    print('  cash     ' + ' '.join(f"{y}:{cash[y]:.0f}" for y in range(2027, 2040)))
    print(f"  sum of pre-tax cash 2026Q4-2045: {Q4_2026_EBIT + sum(cash.values()):,.0f}")
    print(f"  EV at sovereign {SOV:.2%}: {ev_s:,.0f}  -> equity/share {(ev_s-NET_DEBT)/SHARES:,.2f}")
    print(f"  EV at floor 10%: {ev_f:,.0f}  -> equity/share {(ev_f-NET_DEBT)/SHARES:,.2f}")
    print(f"  pre-tax IRR on today's EV: {irr_on_ev(cash, ev_now):.1%}")

# The Q7 convention as written, for comparison (5-yr mean owner cash, D&A basis, tools/run.py: 54.4)
oe = 54.4
conv_nogrowth = sum(oe / (1 + SOV) ** t for t in range(1, 11)) + (oe / SOV) / (1 + SOV) ** 10
print(f"\nQ7 convention, no-growth end, OE (D&A basis) 54.4: EV {conv_nogrowth:,.0f} -> equity/share {(conv_nogrowth-NET_DEBT)/SHARES:,.2f}")

# Sensitivity: costs part fixed (CONVENTION of the run, a test of the uniform-margin simplification):
# costs = 120 fixed + 35% of revenue, which reproduces the central 50% margin at 2027 revenue of ~816.
print("\nSENSITIVITY, central revenue with 120 fixed + 35% variable costs:")
rev, _ = streams('central')
cash = {y: max(v * 0.65 - 120.0, 0.0) - 2.0 if v > 0 else 0 for y, v in rev.items()}
ev_s = pv(cash, SOV); ev_f = pv(cash, FLOOR)
print('  cash     ' + ' '.join(f"{y}:{cash[y]:.0f}" for y in range(2027, 2040)))
print(f"  EV at sovereign: {ev_s:,.0f} -> {(ev_s-NET_DEBT)/SHARES:,.2f}/share; at 10%: {ev_f:,.0f} -> {(ev_f-NET_DEBT)/SHARES:,.2f}/share; IRR on today's EV {irr_on_ev(cash, ev_now):.1%}")
