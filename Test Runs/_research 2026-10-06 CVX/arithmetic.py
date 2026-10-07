"""Every computed number in `Test Runs/2026-10-06 Run - CVX Chevron.md`. Inputs are transcribed from the filed
statements named beside each series (accessions in the run file). USD millions unless stated. Run: python -I arithmetic.py
"""

YEARS = list(range(2016, 2026))
DAYS = {y: (366 if y in (2016, 2020, 2024) else 365) for y in YEARS}

# ---------------- Chevron, upstream segment earnings (after tax) and net production incl. affiliates (MBOE/d)
# Earnings: 10-K FY2018 (2016-2018 via FY2019 table), 10-K FY2019, 10-K FY2022, 10-K FY2025 "Total Upstream".
CVX_UP = {2016: -2537, 2017: 8150, 2018: 13316, 2019: 2576, 2020: -2433, 2021: 15818, 2022: 30284,
          2023: 17438, 2024: 18602, 2025: 12822}
# Production: 10-K FY2018 selected operating data (2016-2018), FY2019 (2019), FY2022 (2020-2022), FY2025 (2023-2025).
CVX_PROD = {2016: 2594, 2017: 2728, 2018: 2930, 2019: 3058, 2020: 3083, 2021: 3099, 2022: 2999,
            2023: 3120, 2024: 3338, 2025: 3723}

# ---------------- ExxonMobil, Upstream earnings (U.S. GAAP) and oil-equivalent production (koebd)
# 10-K FY2019 0000034088-20-000016 (2017-2019); FY2022 0000034088-23-000020 (2020-2022); FY2025 0000034088-26-000045.
XOM_UP = {2017: 13355, 2018: 14079, 2019: 14442, 2020: -20030, 2021: 15775, 2022: 36479,
          2023: 21308, 2024: 25390, 2025: 21354}
XOM_PROD = {2017: 3985, 2018: 3833, 2019: 3952, 2020: 3761, 2021: 3712, 2022: 3737,
            2023: 3738, 2024: 4333, 2025: 4736}

# ---------------- ConocoPhillips, segment net income total (net income less Corporate and Other) and total production
# 10-K FY2019 0001193125-20-039954; FY2022 0001163165-23-000006; FY2025 0001163165-26-000009.
COP_UP = {2017: -855 + 2136, 2018: 6257 + 1667, 2019: 7189 - 38, 2020: -2701 + 1880, 2021: 8079 + 210,
          2022: 18680 + 330, 2023: 11791, 2024: 10126, 2025: 9126}
COP_PROD = {2017: 1377, 2018: 1283, 2019: 1348, 2020: 1127, 2021: 1567, 2022: 1738,
            2023: 1826, 2024: 1987, 2025: 2375}


def per_boe(up, prod):
    return {y: up[y] / (prod[y] * DAYS[y] / 1000.0) for y in up}


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs)


print("UPSTREAM AFTER-TAX EARNINGS PER BOE PRODUCED ($/BOE)")
c, x, p = per_boe(CVX_UP, CVX_PROD), per_boe(XOM_UP, XOM_PROD), per_boe(COP_UP, COP_PROD)
for y in YEARS:
    print(f"  {y}  CVX {c[y]:7.2f}   XOM {x.get(y, float('nan')):7.2f}   COP {p.get(y, float('nan')):7.2f}")
span = range(2017, 2026)
print(f"  mean 2017-2025  CVX {mean(c[y] for y in span):.2f}  XOM {mean(x[y] for y in span):.2f}  COP {mean(p[y] for y in span):.2f}")
# volume-weighted (total earnings / total barrels) 2017-2025
def wtd(up, prod):
    return sum(up[y] for y in span) / sum(prod[y] * DAYS[y] / 1000.0 for y in span)
print(f"  weighted 2017-2025  CVX {wtd(CVX_UP, CVX_PROD):.2f}  XOM {wtd(XOM_UP, XOM_PROD):.2f}  COP {wtd(COP_UP, COP_PROD):.2f}")
print(f"  CVX years ahead of XOM: {[y for y in span if c[y] > x[y]]}")
print(f"  CVX years ahead of COP: {[y for y in span if c[y] > p[y]]}")
print(f"  CVX 2016: {c[2016]:.2f}")

# ---------------- Average production (lifting) cost per BOE, consolidated operations, Table IV / supplementary data
CVX_LIFT = {2016: 13.15, 2017: 11.41, 2018: 10.78, 2019: 10.62, 2020: 10.07, 2021: 9.90, 2022: 10.16,
            2023: 10.23, 2024: 9.23, 2025: 9.71}
XOM_LIFT = {2020: 11.57, 2021: 12.15, 2022: 13.09, 2023: 12.05, 2024: 11.70, 2025: 11.29}
COP_LIFT = {2020: 10.99, 2021: 9.99, 2022: 11.27, 2023: 11.87, 2024: 12.26, 2025: 12.01}
print("\nLIFTING COST PER BOE, consolidated ($/BOE)")
for y in range(2020, 2026):
    print(f"  {y}  CVX {CVX_LIFT[y]:6.2f}  XOM {XOM_LIFT[y]:6.2f}  COP {COP_LIFT[y]:6.2f}")
print(f"  mean 2020-2025  CVX {mean(CVX_LIFT[y] for y in range(2020, 2026)):.2f}  XOM {mean(XOM_LIFT.values()):.2f}  COP {mean(COP_LIFT.values()):.2f}")

# ---------------- Chevron owner cash: OCF - stock pay - capex - net loans to equity affiliates (cash-flow statements)
OCF = {2016: 12690, 2017: 20338, 2018: 30618, 2019: 27314, 2020: 10577, 2021: 29187, 2022: 49602,
       2023: 35609, 2024: 31492, 2025: 33939}
CAPEX = {2016: 18109, 2017: 13404, 2018: 13792, 2019: 14116, 2020: 8922, 2021: 8056, 2022: 11974,
         2023: 15829, 2024: 16448, 2025: 17347}
AFF_LOANS = {2016: -2034, 2017: -16, 2018: 111, 2019: -1245, 2020: -1419, 2021: 401, 2022: -24,
             2023: -302, 2024: -233, 2025: 778}   # net repayment (borrowing) of loans by equity affiliates
# stock pay: compensation expense for options plus SARs, restricted stock, performance shares, RSUs (notes); a negative
# year (2023, -15) is taken as zero.
SBC = {2016: 271 + 371, 2017: 137 + 231, 2018: 105 + 60, 2019: 81 + 313, 2020: 94 + 96, 2021: 60 + 701,
       2022: 60 + 1013, 2023: max(0, 85 - 100), 2024: 90 + 510, 2025: 73 + 399}
DDA = {2023: 17326, 2024: 17282, 2025: 20132, 2022: 16319, 2021: 17925, 2020: 19508}
OC = {y: OCF[y] - SBC[y] - CAPEX[y] + AFF_LOANS[y] for y in YEARS}
print("\nCHEVRON OWNER CASH (USD M)")
for y in YEARS:
    print(f"  {y}  OCF {OCF[y]:7,}  SBC {SBC[y]:6,}  capex {CAPEX[y]:7,}  aff.loans {AFF_LOANS[y]:7,}  owner cash {OC[y]:8,}")
m5 = mean(OC[y] for y in range(2021, 2026))
m10 = mean(OC.values())
print(f"  five-year mean 2021-2025: {m5:,.0f}")
print(f"  ten-year mean 2016-2025:  {m10:,.0f}")
print(f"  five-year mean 2016-2020: {mean(OC[y] for y in range(2016, 2021)):,.0f}")
# depreciation variant (OCF - SBC - D&A + affiliate loans), the convention's side figure
for y in range(2021, 2026):
    pass
dvar = {y: OCF[y] - SBC[y] - DDA[y] + AFF_LOANS[y] for y in range(2021, 2026)}
print(f"  D&A variant 2021-2025: {dvar}, mean {mean(dvar.values()):,.0f}")

# ---------------- reserve life and return on capital employed (10-K FY2025 reserves table; ROCE as filed each year)
print(f"\nreserve life: 10,591 MMBOE / (3,723 MBOED x 365) = {10591 / (3723 * 365 / 1000):.1f} years")
ROCE = {2016: -0.1, 2017: 5.0, 2018: 8.2, 2019: 2.0, 2020: -2.8, 2021: 9.4, 2022: 20.3, 2023: 11.9, 2024: 10.1, 2025: 6.6}
print(f"ROCE mean 2016-2025: {mean(ROCE.values()):.2f}%  years below the 5.66% sovereign: "
      f"{[y for y in ROCE if ROCE[y] < 5.66]}")

# ---------------- Q7 (COMPUTATION - NOT A CLEARANCE): the convention's range
PRICE, SHARES = 206.47, 1975.771274   # USD; millions of shares (10-Q Q2 2026 cover)
CAP = PRICE * SHARES
R = 0.0566
print(f"\nmarket cap {CAP:,.0f} M")
def pv(base, g, r=R, n=10):
    v, cf = 0.0, base
    for t in range(1, n + 1):
        cf *= (1 + g)
        v += cf / (1 + r) ** t
    term = cf / r / (1 + r) ** n          # zero nominal growth after year ten
    return v + term
# growth shown on aggregate owner cash: compound rate between the first and last years of the window
g5 = (OC[2025] / OC[2021]) ** (1 / 4) - 1
print(f"  growth shown 2021->2025 on aggregate owner cash: {g5:.2%}")
for label, base in (("five-year mean", m5), ("ten-year mean", m10)):
    lo = pv(base, 0.0)
    print(f"  {label} {base:,.0f}: no-growth value {lo:,.0f} M = ${lo / SHARES:,.2f}/sh;  yield at price {base / CAP:.2%}")
# net debt and noncontrolling interests (balance sheet 2025-12-31 / 10-Q 2026-06-30) noted in the run, not netted here
gv = pv(m5, g5)
print(f"  shown-growth case ({g5:.2%} for ten years, then flat): {gv:,.0f} M = ${gv / SHARES:,.2f}/sh")
print(f"  width top/bottom: {pv(m5, 0.0) / gv:.2f}")
# the floor: about ten percent pre-tax (CONVENTION). Gross-up at the mean of the filed effective tax rates 2024-2025.
ETR = (0.355 + 0.368) / 2
for label, base in (("five-year mean", m5), ("ten-year mean", m10)):
    pre = base / (1 - ETR)
    print(f"  {label}: pre-tax owner cash {pre:,.0f} M; pre-tax yield at price {pre / CAP:.2%}; "
          f"price at which no-growth clears 10% pre-tax ${pre / 0.10 / SHARES:,.2f}/sh")

# ---------------- Q6 facts (not reached): average prices paid under the 2023 Program (10-Q Q2 2026 MD&A)
print(f"\n2023 Program to 2026-06-30: $44.0B / 281M shares = ${44.0e3 / 281:,.2f}/sh;  "
      f"Q2 2026: $3.0B / 16.2M = ${3.0e3 / 16.2:,.2f}/sh")
