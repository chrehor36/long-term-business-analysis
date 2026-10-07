"""PLPC owner earnings — the six-window rebuild the brief demanded.

All figures $ thousands, taken from the FILED Statements of Consolidated Cash Flows:
  2018-2020  FY2020 10-K, accession 0001564590-21-011273
  2020-2022  FY2022 10-K, accession 0000950170-23-006020
  2023-2025  FY2025 10-K, accession 0000080035-26-000007
  2016-2017  SEC companyfacts XBRL ONLY - flagged, and excluded from every headline window.
"""
import statistics, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

#      yr : (OCF,      SBC,   D&A,    capex,   acq)
D = {
    2016: (25966,  1372, 12001, 24731,     0),   # XBRL only
    2017: (33827,  3062, 12789, 11230,     0),   # XBRL only
    2018: (22976,  4236, 12444,  9528,     0),
    2019: (27217,  4396, 13748, 29467, 18894),
    2020: (41642,  4089, 13838, 24569,     0),
    2021: (33598,  4163, 15564, 18384,     0),
    2022: (26153,  4596, 16430, 40598, 16235),
    2023: (107642, 4948, 18914, 35332, 12089),
    2024: (67480,  3412, 20830, 14651,     0),
    2025: (73467,  4955, 23030, 40132,  4746),
}
FILED_FROM = 2018

rows = []
for y, (ocf, sbc, da, cap, acq) in sorted(D.items()):
    rows.append(dict(y=y, ocf=ocf, sbc=sbc, da=da, cap=cap, acq=acq,
                     oe_cap=ocf - sbc - cap,     # (c) = total capex   -> conservative end
                     oe_da=ocf - sbc - da))      # (c) = D&A [E3-44]   -> optimistic end
by = {r["y"]: r for r in rows}

print("PLPC OWNER EARNINGS BY YEAR  ($M)   OE = OCF - SBC - (c)")
print(f"{'yr':>5} {'OCF':>8} {'SBC':>7} {'OCF-SBC':>9} {'D&A':>7} {'capex':>8} {'cap/D&A':>8} |"
      f" {'OE@capex':>9} {'OE@D&A':>8} | {'acq':>7} {'src':>6}")
for r in rows:
    src = "FILED" if r["y"] >= FILED_FROM else "xbrl"
    print(f"{r['y']:>5} {r['ocf']/1e3:8.1f} {r['sbc']/1e3:7.1f} {(r['ocf']-r['sbc'])/1e3:9.1f} "
          f"{r['da']/1e3:7.1f} {r['cap']/1e3:8.1f} {r['cap']/r['da']:8.2f} | "
          f"{r['oe_cap']/1e3:9.1f} {r['oe_da']/1e3:8.1f} | {r['acq']/1e3:7.1f} {src:>6}")

def mean(ys, k):
    return statistics.mean([by[y][k] for y in ys if y in by]) / 1e3

WINDOWS = [
    ("3yr 2023-25", range(2023, 2026)),
    ("4yr 2022-25", range(2022, 2026)),
    ("5yr 2021-25", range(2021, 2026)),      # the corpus default window [E2-42]
    ("6yr 2020-25", range(2020, 2026)),
    ("7yr 2019-25", range(2019, 2026)),
    ("8yr 2018-25", range(2018, 2026)),
    ("5yr 2019-23", range(2019, 2024)),      # alternative TERMINAL date [E4-38]
    ("5yr 2018-22", range(2018, 2023)),      # alternative terminal date [E4-38]
]

print("\nSIX-PLUS WINDOWS x TWO (c) ENDS  — the rebuild [E4-25, E4-38]")
print(f"{'window':>14} {'OE@capex':>10} {'OE@D&A':>10}   {'yield@capex':>12} {'yield@D&A':>10}")
CAP = 1947.9      # 4,888,701 shares x $398.45  (2026-09-04)
vals = []
for nm, ys in WINDOWS:
    ys = set(ys)
    a, b = mean(ys, "oe_cap"), mean(ys, "oe_da")
    vals += [a, b]
    print(f"{nm:>14} {a:10.1f} {b:10.1f}   {a/CAP*100:11.2f}% {b/CAP*100:9.2f}%")

lo, hi = min(vals), max(vals)
print(f"\nTRUE RANGE across 8 windows x 2 (c) ends: {lo:.1f} to {hi:.1f}")
print(f"  width = {hi/lo:.2f}x  = {(hi/lo-1)*100:.0f}%   [published screen row said 9.6%]")
print(f"  yields on cap ${CAP:.0f}M: {lo/CAP*100:.2f}% to {hi/CAP*100:.2f}%   sovereign 5.24%")
print(f"  published screen row: oe 27 to 58 -> {58/27:.2f}x; yield_bottom 1.44%")

print("\nDROP-THE-BEST-YEAR TEST  (best_year_dep 0.154; 2023 OCF is the outlier)")
for nm, ys in WINDOWS:
    ys = set(ys)
    if 2023 not in ys:
        continue
    a, b = mean(ys, "oe_cap"), mean(ys, "oe_da")
    ys2 = ys - {2023}
    a2, b2 = mean(ys2, "oe_cap"), mean(ys2, "oe_da")
    print(f"{nm:>14}  with 2023: {a:6.1f}/{b:6.1f}   without 2023: {a2:6.1f}/{b2:6.1f}"
          f"   shift {(a2-a):+6.1f}/{(b2-b):+6.1f}")

print("\nLEVEL-SHIFT TEST  (screen row said 2.68 STEP UP - normalize down [E4-41])")
early = [2018, 2019, 2020, 2021]
late = [2022, 2023, 2024, 2025]
for k, lab in (("ocf", "OCF"), ("oe_cap", "OE@capex"), ("oe_da", "OE@D&A")):
    e, l = mean(set(early), k), mean(set(late), k)
    print(f"  {lab:>9}: 2018-21 mean {e:7.1f}   2022-25 mean {l:7.1f}   ratio {l/e:5.2f}x")
print("  NET INCOME, $M: 2018 26.6 2019 23.3 2020 29.8 2021 35.7 2022 54.4"
      " 2023 63.3 2024 37.1 2025 35.3   <- peaked 2023, down 44% since")

print("\nWORKING-CAPITAL DECOMPOSITION of the 2023 spike (filed detail lines, $k)")
print("  2022  AR (28,049)  Inv (36,979)  AP +6,707   -> WC drag  (58,321)")
print("  2023  AR +16,969   Inv (4,952)   AP +2,302   -> WC release +14,319")
print("  swing 2022->2023 = +72.6M of pure working capital. OCF rose 26.2 -> 107.6 = +81.5M.")

print("\nCUMULATIVE CAPEX vs D&A")
for a, b, lab in ((2018, 2025, "8yr 2018-25"), (2021, 2025, "5yr 2021-25")):
    ys = [y for y in D if a <= y <= b]
    c = sum(by[y]["cap"] for y in ys) / 1e3
    d = sum(by[y]["da"] for y in ys) / 1e3
    print(f"  {lab}: capex {c:6.1f}  D&A {d:6.1f}  ratio {c/d:.2f}x  excess {c-d:+.1f}")
