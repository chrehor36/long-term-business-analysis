"""Q7 range and fair price arithmetic for MARUY (JPY bn; per share in JPY). Inputs from ownercash.py output and the filings."""
r_gov = 0.04136      # 30-year JGB, MOF jgbcme.csv, 2026-10-08
shares = 1621.224186  # million: issued 1,660,758,361 less treasury 33,979,475 (2026-06-30) less 5,554,700 bought 2026-08-04..09-30
price = 4702.0        # TSE close 2026-10-09 (aggregator, flagged)
net_debt = 2050.5 + 27.7  # bonds and borrowings less cash and time deposits at 2026-06-30 (Q1 tanshin), plus buyback cash paid Aug-Sep 2026
nci = 150.3           # non-controlling interests at 2026-06-30, treated as a prior claim (CONVENTION of this run)

def value(base, g, r, years=10):
    pv, c = 0.0, base
    for t in range(1, years + 1):
        c = c * (1 + g)
        pv += c / (1 + r) ** t
    pv += (c / r) / (1 + r) ** years   # zero nominal growth after year ten
    return pv

def case(label, base, g, claims):
    lo = base / r_gov; hi = value(base, g, r_gov)
    lo10 = base / 0.10; hi10 = value(base, g, 0.10)
    a = sorted([lo, hi])
    ps = lambda v: (v - claims) / shares * 1000
    fair = (ps(lo10) + ps(hi10)) / 2
    print(f"{label}: base {base:.1f} g {g*100:.2f}%  range {a[0]:,.0f}-{a[1]:,.0f}bn -> JPY {ps(a[0]):,.0f}-{ps(a[1]):,.0f}/sh"
          f"  width {a[1]/a[0]:.2f}x  fair (10%) JPY {fair:,.0f}  [ends at 10%: {ps(lo10):,.0f} / {ps(hi10):,.0f}]")
    return ps(a[0]), ps(a[1]), fair

mcap = price * shares / 1000
print(f"market cap {mcap:,.0f}bn; all-equity EV {mcap+net_debt+nci:,.0f}bn")
def g(a, b, n=5): return (b / a) ** (1 / n) - 1
claims_ae = net_debt + nci
print("--- central: all-equity basis, cycle base FY2016-25, growth between FY2016-20 and FY2021-25 averages")
case("all-equity, acquisitions deducted", 275.5, g(248.3, 302.8), claims_ae)
case("all-equity, organic pair (beside)", 289.0, g(241.0, 336.9), claims_ae)
print("--- literal window FY2021-25 average, beside")
case("all-equity, literal 5-yr avg, cycle growth", 302.8, g(248.3, 302.8), claims_ae)
print("--- equity-only beside (owner cash after interest; NCI still deducted)")
case("equity-only, acquisitions deducted", 252.2, g(230.2, 274.2), nci)
# expected return at the price: the rate at which the growth case equals EV
def irr(base, gr, target):
    lo, hi = 0.0001, 0.5
    for _ in range(100):
        m = (lo + hi) / 2
        if value(base, gr, m) > target: lo = m
        else: hi = m
    return m
ev = mcap + claims_ae
for lab, b, gg in (("central growth case", 275.5, g(248.3, 302.8)), ("organic growth case", 289.0, g(241.0, 336.9)), ("no-growth", 275.5, 0.0)):
    print(f"expected return at the price, {lab}: {irr(b, gg, ev)*100:.2f}%")
print(f"ADS price check: JPY {price} / USDJPY 158.06 (2026-10-08) = ${price/158.06:.2f} vs MARUY $29.74")
