"""COMPUTATION, NOT A CLEARANCE. The Q7 construction of THE FRAMEWORK v5 (CONVENTION, confessed there),
run on Lam Research for the reporting figures the brief asks for after the file closed at Q1.
Inputs: series_LRCX.csv (SEC XBRL companyfacts, newest vintage, cross-checked to the FY2026 10-K,
accession 0000707549-26-000037), the FY2026 balance sheet, the cover share count, the Treasury 30-year rate.
Arithmetic only. Run: python value_range.py
"""
import csv, collections

R = 0.0560          # US Treasury daily par yield curve, 30-year, 2026-10-09 (tools/run.py, issuing authority)
FLOOR = 0.10        # Q7 floor CONVENTION, about ten percent, after the company's own tax
PRICE = 318.84      # close 2026-10-09, aggregator (tools/run.py), live quote only, flagged
SHARES = 1251.321   # millions, cover of the FY2026 10-K, as of 2026-08-04
DEBT = 3730.490 + 4.073   # long-term debt and finance leases + current portion, 2026-06-28, $M
CASH = 5579.171           # cash and cash equivalents, 2026-06-28, $M (no marketable securities on the face)
NET_DEBT = DEBT - CASH    # negative = net cash

d = collections.defaultdict(dict)
for r in csv.DictReader(open('series_LRCX.csv')):
    d[r['fiscal_end']][r['metric']] = float(r['value_millions'])
years = sorted(d)


def oc(e, basis, all_equity):
    x = d[e]
    spend = x['capex'] if basis == 'capex' else x['dna']
    v = x['ocf'] - x['sbc'] - spend - max(x.get('acq_paid', 0.0), 0.0)
    if all_equity:
        etr = x['tax'] / x['pretax'] if x['pretax'] > 0 else 0.0
        v += x['interest_exp'] * (1 - etr)
    return v


def pv(c0, g, r, n=10):
    """c0 = base-year cash; years 1..n grow at g, then zero nominal growth for ever; discount at r."""
    tot, c = 0.0, c0
    for t in range(1, n + 1):
        c *= (1 + g)
        tot += c / (1 + r) ** t
    tot += (c / r) / (1 + r) ** n
    return tot


def case(window, basis, all_equity, label):
    s = [oc(e, basis, all_equity) for e in window]
    avg = sum(s) / len(s)
    n = len(s) - 1
    g = (s[-1] / s[0]) ** (1 / n) - 1 if s[0] > 0 and s[-1] > 0 else None
    lo, hi = pv(avg, 0.0, R), pv(avg, g, R)
    lo_f, hi_f = pv(avg, 0.0, FLOOR), pv(avg, g, FLOOR)
    fair_total = (lo_f + hi_f) / 2          # PV at the floor of the midpoint stream (PV is linear)
    adj = -NET_DEBT if all_equity else 0.0  # all-equity: whole-business value less net debt
    ps = lambda v: (v + adj) / SHARES
    print(f"\n{label}  window {window[0][:4]}-{window[-1][:4]}  basis={basis}  "
          f"{'ALL-EQUITY (before interest)' if all_equity else 'EQUITY-ONLY (after interest)'}")
    print("  owner cash by year ($M):", ', '.join(f"{e[:4]} {v:,.0f}" for e, v in zip(window, s)))
    print(f"  average {avg:,.0f}  growth shown (aggregate, first to last) {g*100:.1f}%")
    print(f"  range (whole) ${lo/1e3:,.1f}B to ${hi/1e3:,.1f}B   width {hi/lo:.2f} to 1")
    print(f"  range per share ${ps(lo):,.2f} to ${ps(hi):,.2f}   price ${PRICE}")
    print(f"  FAIR PRICE (midpoint stream at the {FLOOR:.0%} floor) ${ps(fair_total):,.2f}"
          f"   [no-growth at floor ${ps(lo_f):,.2f}, growth at floor ${ps(hi_f):,.2f}]")
    print(f"  owner-cash yield at price: {avg/(PRICE*SHARES + (NET_DEBT if all_equity else 0))*100:.2f}%  vs sovereign {R*100:.2f}%")
    return lo, hi


print(f"net debt at 2026-06-28: ${NET_DEBT:,.1f}M (negative = net cash); market cap ${PRICE*SHARES/1e3:,.1f}B")
W = [y for y in years if y >= '2021-07']          # literal five-year window FY2022-FY2026
for basis in ('capex', 'dna'):
    case(W, basis, True, 'LITERAL WINDOW')
    case(W, basis, False, 'LITERAL WINDOW')
# Beside it: the last full trough-to-trough cycle (FY2019 trough to the year before the FY2024 trough).
C = [y for y in years if '2018-07' < y < '2023-07']
case(C, 'capex', True, 'CYCLE BASE (sensitivity, shown beside)')

# Specific (a) proper: growth between the averages of successive cycles (FY2013-FY2018 against FY2019-FY2023,
# midpoints FY2015.5 and FY2021, 5.5 years apart), applied to the FY2019-FY2023 average.
P = [y for y in years if '2012-07' < y < '2018-07']
a1 = sum(oc(e, 'capex', True) for e in P) / len(P)
a2 = sum(oc(e, 'capex', True) for e in C) / len(C)
gc = (a2 / a1) ** (1 / 5.5) - 1
lo, hi = pv(a2, 0.0, R), pv(a2, gc, R)
fair = (pv(a2, 0.0, FLOOR) + pv(a2, gc, FLOOR)) / 2
print(f"\nCYCLE BASE, specific (a): prior cycle FY2013-2018 avg {a1:,.0f}; last cycle FY2019-2023 avg {a2:,.0f}; "
      f"growth between cycle averages {gc*100:.1f}%/yr")
print(f"  range per share ${(lo-NET_DEBT)/SHARES:,.2f} to ${(hi-NET_DEBT)/SHARES:,.2f}  width {hi/lo:.2f} to 1;"
      f"  fair price ${(fair-NET_DEBT)/SHARES:,.2f}")

# THE CENTRAL PAIR under specific (e): the filer ties the FY2025-26 rise in capital spending to growth (US labs,
# manufacturing expansion), so the maintenance guess is depreciation [M1998-127]. Bottom = no growth on owner cash
# after maintenance only; top = the shown growth with ALL spending charged (the growth spending charged against
# the growth it buys). Literal window FY2022-FY2026; acquisitions deducted, total growth credited (default pair).
print("\nCENTRAL PAIR (specific e)")
for ae in (True, False):
    sb = [oc(e, 'dna', ae) for e in W]; st = [oc(e, 'capex', ae) for e in W]
    ab, at = sum(sb) / 5, sum(st) / 5
    gt = (st[-1] / st[0]) ** 0.25 - 1
    adj = -NET_DEBT if ae else 0.0
    lo, hi = pv(ab, 0.0, R), pv(at, gt, R)
    fair = (pv(ab, 0.0, FLOOR) + pv(at, gt, FLOOR)) / 2
    print(f"  {'ALL-EQUITY' if ae else 'EQUITY-ONLY'}: bottom ${(lo+adj)/SHARES:,.2f} (avg {ab:,.0f}, no growth) "
          f"top ${(hi+adj)/SHARES:,.2f} (avg {at:,.0f}, growth {gt*100:.1f}%)  width {hi/lo:.2f} to 1  "
          f"FAIR ${(fair+adj)/SHARES:,.2f}  price ${PRICE}")
