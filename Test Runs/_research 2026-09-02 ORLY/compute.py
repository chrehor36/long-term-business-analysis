#!/usr/bin/env python3
"""ORLY run — arithmetic only. Operator rule 8: computes, never concludes."""
import json, os, sys
from datetime import date

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- CPI (BLS, annual avg)
CPI = {2013:232.957, 2014:236.736, 2015:237.017, 2016:240.007, 2017:245.120,
       2018:251.107, 2019:255.657, 2020:258.811, 2021:270.970, 2022:292.655,
       2023:304.702, 2024:313.689, 2025:321.943}
SETC = {2013:146.422, 2014:144.823, 2015:144.236, 2016:143.555, 2017:143.041,
        2018:143.662, 2019:146.437, 2020:148.051, 2021:155.100, 2022:175.752,
        2023:180.806, 2024:180.842, 2025:184.705}

# --------------------------------------- ORLY 10-K FY2025 ten-year Selected Financial Data
# accession 0000898173-26-000009, filed 2026-02-27. Read off the filed table.
YRS = list(range(2016, 2026))
SPS   = {2016:1826, 2017:1807, 2018:1842, 2019:1881, 2020:2057,
         2021:2298, 2022:2415, 2023:2578, 2024:2642, 2025:2728}   # $k per wtd-avg store
SPSF  = {2016:251, 2017:248, 2018:251, 2019:255, 2020:277,
         2021:307, 2022:322, 2023:340, 2024:342, 2025:346}        # $ per wtd-avg sq ft
COMP  = {2016:4.8, 2017:1.4, 2018:3.8, 2019:4.0, 2020:10.9,
         2021:13.3, 2022:6.4, 2023:7.9, 2024:2.9, 2025:4.7}       # %
STORES= {2016:4829, 2017:5019, 2018:5219, 2019:5460, 2020:5616,
         2021:5784, 2022:5971, 2023:6157, 2024:6378, 2025:6585}
SQFT  = {2016:35123, 2017:36685, 2018:38455, 2019:40227, 2020:41668,
         2021:43185, 2022:44604, 2023:46681, 2024:48809, 2025:51515}  # k sq ft, domestic
SALES = {2016:8593096, 2017:8977726, 2018:9536428, 2019:10149985, 2020:11604493,
         2021:13327563, 2022:14409860, 2023:15812250, 2024:16708479, 2025:17781992}
OPINC = {2016:1699206, 2017:1725400, 2018:1815184, 2019:1920726, 2020:2419336,
         2021:2917168, 2022:2954491, 2023:3186376, 2024:3251157, 2025:3460612}
OCF   = {2016:1510713, 2017:1403687, 2018:1727555, 2019:1708479, 2020:2836603,
         2021:3207310, 2022:3148250, 2023:3034084, 2024:3049576, 2025:2761993}
CAPEX = {2016:476344, 2017:465940, 2018:504268, 2019:628057, 2020:465579,
         2021:442853, 2022:563342, 2023:1006264, 2024:1023387, 2025:1168815}
DA    = {2016:217866, 2017:233845, 2018:258937, 2019:270875, 2020:314635,
         2021:328217, 2022:357933, 2023:409061, 2024:461892, 2025:511230}
SBC   = {2016:18859, 2017:19401, 2018:20176, 2019:21921, 2020:22747,
         2021:24656, 2022:26458, 2023:27511, 2024:28931, 2025:35115}
BUYBK = {2016:1505437, 2017:2172530, 2018:1714013, 2019:1432791, 2020:2087194,
         2021:2476048, 2022:3282265, 2023:3151155, 2024:2076529, 2025:2096962}
# split-adjusted (15-for-1, 2025-06-10) year-end shares outstanding
SHARES_RAW = {2016:92851815, 2017:84302187, 2018:79043919, 2019:75618659,
              2020:71123109, 2021:67029042, 2022:62353221, 2023:59072792,
              2024:862232760, 2025:841909238}
SHARES = {y: (v*15 if y <= 2023 else v) for y, v in SHARES_RAW.items()}


def hdr(t):
    print("\n" + "=" * 78); print(t); print("=" * 78)


def deflate(series, base, defl, label):
    print(f"\n-- {label} — nominal, and deflated to {base} dollars --")
    print(f"{'yr':>5} {'nominal':>10} {'real':>10} {'yoy real':>9}")
    prev = None
    dec = 0
    for y in sorted(series):
        real = series[y] * defl[base] / defl[y]
        yoy = "" if prev is None else f"{(real/prev-1)*100:+7.2f}%"
        if prev is not None and real < prev:
            dec += 1
        print(f"{y:>5} {series[y]:>10,.0f} {real:>10,.1f} {yoy:>9}")
        prev = real
    first, last = min(series), max(series)
    r0 = series[first]
    r1 = series[last] * defl[base] / defl[last]
    n = last - first
    print(f"   nominal {first}->{last}: {(series[last]/series[first]-1)*100:+.1f}%"
          f"   REAL: {(r1/r0-1)*100:+.1f}%   ({(( r1/r0)**(1/n)-1)*100:+.2f}%/yr)"
          f"   real declines: {dec} of {n}")
    return r1 / r0 - 1


if __name__ == "__main__":
    hdr("1. THE DEFLATED PHYSICAL SERIES  (the DG instrument)")
    print("CPI-U all items, BLS annual averages, base 2016=240.007 -> 2025=321.943")
    deflate(SPSF, 2016, CPI, "Sales per weighted-average SQUARE FOOT ($)")
    deflate(SPS, 2016, CPI, "Sales per weighted-average STORE ($ thousands)")
    print("\nSame two series deflated by CPI motor-vehicle PARTS & EQUIPMENT (SETC)")
    print("  -- this is the category price index, so it is the closer proxy to a UNITS series")
    deflate(SPSF, 2016, SETC, "Sales per wtd-avg SQUARE FOOT, parts-deflated")
    deflate(SPS, 2016, SETC, "Sales per wtd-avg STORE, parts-deflated")

    hdr("2. DIY vs DIFM  (10-K revenue disaggregation note, FY2025 accession -26-000009)")
    diy  = {2023:8248213, 2024:8473041, 2025:8765647}
    prof = {2023:7245747, 2024:7836283, 2025:8651746}
    oth  = {2023:318290,  2024:399155,  2025:364599}
    for y in (2023, 2024, 2025):
        tot = diy[y] + prof[y] + oth[y]
        print(f"{y}: DIY {diy[y]:>10,} ({diy[y]/tot*100:5.1f}%)  "
              f"PROF {prof[y]:>10,} ({prof[y]/tot*100:5.1f}%)  other {oth[y]:>8,}  tot {tot:>11,}")
    print(f"\n2y nominal: DIY {(diy[2025]/diy[2023]-1)*100:+.2f}%   "
          f"PROF {(prof[2025]/prof[2023]-1)*100:+.2f}%")
    d = CPI[2023] / CPI[2025]
    print(f"2y REAL (CPI-U {CPI[2023]}->{CPI[2025]}, deflator {d:.5f}): "
          f"DIY {(diy[2025]*d/diy[2023]-1)*100:+.2f}%   PROF {(prof[2025]*d/prof[2023]-1)*100:+.2f}%")
    d2 = SETC[2023] / SETC[2025]
    print(f"2y REAL (parts CPI SETC, deflator {d2:.5f}): "
          f"DIY {(diy[2025]*d2/diy[2023]-1)*100:+.2f}%   PROF {(prof[2025]*d2/prof[2023]-1)*100:+.2f}%")

    hdr("3. MARGIN, CAPEX/D&A, AND THE OCF SERIES")
    print(f"{'yr':>5} {'sales':>11} {'opinc':>10} {'margin':>7} {'OCF':>10} "
          f"{'capex':>9} {'D&A':>8} {'cx/D&A':>7} {'OCF/sales':>9}")
    for y in YRS:
        print(f"{y:>5} {SALES[y]:>11,} {OPINC[y]:>10,} {OPINC[y]/SALES[y]*100:>6.2f}% "
              f"{OCF[y]:>10,} {CAPEX[y]:>9,} {DA[y]:>8,} {CAPEX[y]/DA[y]:>7.2f} "
              f"{OCF[y]/SALES[y]*100:>8.2f}%")

    hdr("4. THE BUYBACK RECORD  [E5-08] condition 2")
    tot_sh_start = SHARES[2016]
    cum = 0
    print(f"{'yr':>5} {'$ spent':>12} {'sh o/s (adj)':>15} {'sh retired':>12} {'avg $/sh':>9}")
    prev_sh = SHARES[2016]
    for y in YRS:
        cum += BUYBK[y]
        ret = prev_sh - SHARES[y]
        avg = BUYBK[y] * 1000 / ret if ret > 0 else float('nan')
        print(f"{y:>5} {BUYBK[y]:>12,} {SHARES[y]:>15,} {ret:>12,} {avg:>9,.2f}")
        prev_sh = SHARES[y]
    print(f"\n2016-2025 cumulative repurchases: ${cum:,}k = ${cum/1e6:.2f}bn")
    print(f"shares 2016 {SHARES[2016]:,} -> 2025 {SHARES[2025]:,} = "
          f"{(SHARES[2025]/SHARES[2016]-1)*100:+.1f}%")
    print(f"blended average price paid 2016-2025 = "
          f"${cum*1000/(SHARES[2016]-SHARES[2025]):,.2f}/share (split-adjusted)")
    # full history from XBRL, 2011 first buyback year
    ALL = {2011:976632, 2012:1445287, 2013:933028, 2014:866484, 2015:1136213}
    ALL.update(BUYBK)
    tot_all = sum(ALL.values())
    sh2010 = 141025544 * 15
    print(f"\n2011-2025 cumulative: ${tot_all/1e6:.2f}bn; shares "
          f"{sh2010:,} (2010) -> {SHARES[2025]:,} = {(SHARES[2025]/sh2010-1)*100:+.1f}%")
    print(f"blended average price paid 2011-2025 = "
          f"${tot_all*1000/(sh2010-SHARES[2025]):,.2f}/share (split-adjusted)")

    hdr("5. CASH TAXES AS A SHARE OF PRETAX INCOME  [E4-30]")
    PRETAX = {2019:1790329, 2020:2266405, 2021:2781914, 2022:2798655,
              2023:3004750, 2024:3045064, 2025:3240171}
    CASHTAX = {2023:315060, 2024:640426, 2025:1067524}
    for y in sorted(CASHTAX):
        print(f"{y}: cash taxes {CASHTAX[y]:>10,} / pretax {PRETAX[y]:>10,} = "
              f"{CASHTAX[y]/PRETAX[y]*100:5.2f}%")

    hdr("6. OWNER EARNINGS  [E2-23]  — OCF - SBC - (c)")
    def oe(years, cfun, label):
        vals = [OCF[y] - SBC[y] - cfun(y) for y in years]
        m = sum(vals) / len(vals)
        print(f"  {label:<34} n={len(years)}  mean {m:>10,.0f}   "
              f"[{min(vals):,.0f} .. {max(vals):,.0f}]")
        return m
    print("\n(c) = TOTAL CAPEX  (the conservative end where capex > D&A)")
    r = {}
    for w, ys in (("5y 2021-2025", list(range(2021,2026))),
                  ("10y 2016-2025", YRS),
                  ("3y 2023-2025", [2023,2024,2025]),
                  ("7y ex-2020/21", [2016,2017,2018,2019,2022,2023,2024,2025])):
        r[("capex", w)] = oe(ys, lambda y: CAPEX[y], w)
    print("\n(c) = D&A  (the [E3-44] default proxy)")
    for w, ys in (("5y 2021-2025", list(range(2021,2026))),
                  ("10y 2016-2025", YRS),
                  ("3y 2023-2025", [2023,2024,2025]),
                  ("7y ex-2020/21", [2016,2017,2018,2019,2022,2023,2024,2025])):
        r[("da", w)] = oe(ys, lambda y: DA[y], w)
    lo = min(r.values()); hi = max(r.values())
    print(f"\n  COMBINED RANGE  {lo:,.0f} .. {hi:,.0f}   width {(hi/lo-1)*100:.1f}%")
    cap = 808960792 * 86.86 / 1000   # $k
    print(f"\n  market cap = 808,960,792 x $86.86 = ${cap:,.0f}k = ${cap/1e6:.2f}bn")
    print(f"  yield on range: {lo/cap*100:.2f}% .. {hi/cap*100:.2f}%   sovereign 5.27%")
    print(f"  growth needed for 10% floor [E4-28], bottom boundary: "
          f"{(0.10 - lo/cap)*100:.2f}%")
    print(f"  growth needed for 10% floor, top of range:            "
          f"{(0.10 - hi/cap)*100:.2f}%")
    print(f"  growth needed to reach the 5.27% sovereign, bottom:   "
          f"{(0.0527 - lo/cap)*100:.2f}%")
