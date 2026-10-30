"""Q7 arithmetic for the KMTUY run, COMPUTATION, NOT A CLEARANCE (sums only; the run file states every input).
Range convention: five-year average owner cash, grown at the shown aggregate rate for ten years,
then zero nominal growth, discounted at the JGB 30-year (MOF jgbcme.csv, 2026-10-09).
Fair price (Part VII): each end case valued at 10%, the two averaged, less net debt (all-equity basis)."""
R = 0.04085            # JGB 30Y, MOF, 2026-10-09
SH = 891_510_104       # shares outstanding 2026-06-30 (930,340,620 issued less 38,830,516 treasury)
ND = 1_071_743         # JPY mn: debt 808,709 + 142,273 + 692,630 less cash 571,869 at 2026-06-30
PRICE = 7416.0         # Tokyo, 2026-10-13 (aggregator, flagged)
FX = 158.144           # JPY per USD, 2026-10-13 (aggregator, flagged)

def value(base, g, r, years=10):
    pv, cf = 0.0, base
    for t in range(1, years + 1):
        cf *= (1 + g)
        pv += cf / (1 + r) ** t
    return pv + (cf / r) / (1 + r) ** years

def irr(base, g, ev):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        (lo, hi) = (mid, hi) if value(base, g, mid) > ev else (lo, mid)
    return mid

def per_share(eq_mn): return eq_mn * 1e6 / SH

mcap = PRICE * SH / 1e6
ev = mcap + ND
print(f"market cap JPY {mcap:,.0f} mn; EV (all-equity) JPY {ev:,.0f} mn")
cases = {
  "central, all-equity, literal window FY2021-FY2025": (188_640, 0.155, ND, ev),
  "beside, cycle base trough-to-trough (FY2022-25 avg, growth between cycle averages)": (201_250, 0.146, ND, ev),
  "beside, depreciation variant, all-equity": (209_000, None, ND, ev),
  "equity-only (after interest), against market cap": (171_280, 0.140, 0, mcap),
}
for name, (base, g, nd, against) in cases.items():
    if g is None:
        print(f"\n{name}: base {base:,} no-growth only (growth not measured on this series)")
        lo = value(base, 0.0, R); print(f"  no-growth value {per_share(lo - nd):,.0f}/share; return at price {base/against:.2%}")
        continue
    lo, hi = value(base, 0.0, R), value(base, g, R)
    lo_ps, hi_ps = per_share(lo - nd), per_share(hi - nd)
    f_lo, f_hi = value(base, 0.0, 0.10), value(base, g, 0.10)
    fair = per_share((f_lo + f_hi) / 2 - nd)
    print(f"\n{name}: base {base:,} mn, growth {g:.1%}")
    print(f"  range JPY {lo_ps:,.0f} to {hi_ps:,.0f} a share (width {hi_ps/lo_ps:.2f} to 1) against {PRICE:,.0f}")
    print(f"  expected return at the price: no-growth {irr(base,0.0,against):.2%}, shown-growth {irr(base,g,against):.2%}")
    print(f"  ends at 10%: {per_share(f_lo-nd):,.0f} and {per_share(f_hi-nd):,.0f}; FAIR PRICE JPY {fair:,.0f} a share = USD {fair/FX:,.2f} per ADS")
    print(f"  range per ADS USD {lo_ps/FX:,.2f} to {hi_ps/FX:,.2f}; price per ADS at FX USD {PRICE/FX:,.2f}")
