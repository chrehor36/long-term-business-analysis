"""GRMN Q7 arithmetic, 2026-10-07. COMPUTATION, NOT A CLEARANCE (the file closed at Q1).
Inputs are filed figures (USD millions) from the cash-flow statements of the 10-Ks FY2022 (0000950170-23-003566)
and FY2025 (0001193125-26-056028), and the 10-Q for 2026-06-27 (0001193125-26-322114)."""
R = 0.0564           # 30-year Treasury par yield, 2026-10-06
FLOOR = 0.10         # the floor CONVENTION, about ten percent
SH = 192.852536      # cover count, 10-Q, 2026-07-24
PRICE = 276.05
NET_CASH = 2334.235 + 331.955 + 1703.680   # cash + current + noncurrent marketable securities, 2026-06-27; no borrowings
TAX = 350.6 / (1663.9 + 350.6)             # FY2025 effective rate, used to take interest income out after tax (run CONVENTION)
yrs = [2021, 2022, 2023, 2024, 2025]
ocf = [1012.427, 788.259, 1376.265, 1432.471, 1633.359]
sbc = [92.522, 76.801, 101.422, 137.162, 166.003]
capex = [307.645, 244.286, 193.524, 193.571, 270.446]
acq = [20.175, 13.455, 150.853, 16.444, 175.655]
intang = [1.942, 1.907, 0.0, 0.0, 0.0]       # purchase of intangible assets, shown separately in FY2021-22 only
dep = [103.498, 118.743, 132.347, 140.494, 152.611]
intinc = [28.573, 40.826, 77.302, 113.520, 128.874]

def stream(base, g, n=10):
    return [base * (1 + g) ** t for t in range(1, n + 1)]
def pv(cfs, r):
    v = sum(c / (1 + r) ** (t + 1) for t, c in enumerate(cfs))
    return v + cfs[-1] / r / (1 + r) ** len(cfs)       # zero nominal growth after year ten
def cagr(a, b, n): return (b / a) ** (1 / n) - 1

def case(label, oc):
    base = sum(oc) / len(oc); g = cagr(oc[0], oc[-1], 4)
    lo, hi = pv(stream(base, 0), R), pv(stream(base, g), R)
    mid_stream = [(a + b) / 2 for a, b in zip(stream(base, 0), stream(base, g))]
    fair = pv(mid_stream, FLOOR)
    print(f"\n{label}\n  by year: " + ", ".join(f"{y} {v:,.1f}" for y, v in zip(yrs, oc)))
    print(f"  five-year average {base:,.1f}; growth shown (2021 to 2025, aggregate) {g:.1%}")
    print(f"  value at {R:.2%}: no-growth {lo:,.0f}  shown-growth {hi:,.0f}  width {hi/lo:.2f} to 1")
    print(f"  fair value of the midpoint stream at {FLOOR:.0%}: {fair:,.0f}")
    return lo, hi, fair

eq = [o - s - c - a - i for o, s, c, a, i in zip(ocf, sbc, capex, acq, intang)]
bi = [e - x * (1 - TAX) for e, x in zip(eq, intinc)]
print(f"tax rate for interest {TAX:.1%}; net cash {NET_CASH:,.1f}; shares {SH:.3f}M; price {PRICE}")
lo, hi, fair = case("ALL-EQUITY BASIS (central): owner cash before interest, all capital spending and acquisitions deducted", bi)
print(f"  PER SHARE (range plus net cash): ${(lo+NET_CASH)/SH:,.2f} to ${(hi+NET_CASH)/SH:,.2f}; fair price ${(fair+NET_CASH)/SH:,.2f}")
lo2, hi2, fair2 = case("EQUITY-ONLY (beside): owner cash after interest income, against the market value", eq)
print(f"  PER SHARE: ${lo2/SH:,.2f} to ${hi2/SH:,.2f}; fair price ${fair2/SH:,.2f}")
dv = [o - s - d - a - i - x * (1 - TAX) for o, s, d, a, i, x in zip(ocf, sbc, dep, acq, intang, intinc)]
lo3, hi3, fair3 = case("DEPRECIATION VARIANT (beside; depreciation in place of capital spending), all-equity", dv)
print(f"  PER SHARE: ${(lo3+NET_CASH)/SH:,.2f} to ${(hi3+NET_CASH)/SH:,.2f}; fair price ${(fair3+NET_CASH)/SH:,.2f}")
# what the price implies: the expected return on the central mid stream at today's enterprise value
ev = PRICE * SH - NET_CASH
mid = [(a + b) / 2 for a, b in zip(stream(sum(bi)/5, 0), stream(sum(bi)/5, cagr(bi[0], bi[-1], 4)))]
lo_r, hi_r = 0.0001, 0.5
for _ in range(100):
    m = (lo_r + hi_r) / 2
    if pv(mid, m) > ev: lo_r = m
    else: hi_r = m
print(f"\nmarket cap {PRICE*SH:,.0f}; enterprise value {ev:,.0f}; return the midpoint stream earns at the price {m:.2%}")
