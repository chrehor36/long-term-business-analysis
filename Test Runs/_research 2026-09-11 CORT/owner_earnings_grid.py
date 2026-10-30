#!/usr/bin/env python3
"""Owner-earnings grid for CORT: every window x both (c) ends x both SBC measures.
Every input is from a filed Consolidated Statement of Cash Flows (10-K vintages FY2009-FY2025)
or, for the [E3-70] grant-date measure, the filed option/restricted-stock activity tables.
$M. Arithmetic only; the judgment is in the run file."""
import sys, statistics
sys.stdout.reconfigure(encoding="utf-8")

# year: (OCF, SBC charge, D&A, capex)   -- filed cash-flow statements
CF = {
 2009: (-17.97, 1.80, 0.01, 0.00), 2010: (-22.29, 2.12, 0.01, 0.00), 2011: (-27.40, 3.44, 0.00, 0.03),
 2012: (-36.02, 5.31, 0.03, 0.15), 2013: (-37.06, 5.20, 0.07, 0.13), 2014: (-27.38, 5.20, 0.14, 0.17),
 2015: (3.13, 6.01, 0.15, 0.02),  2016: (18.39, 7.06, 0.09, 0.19),  2017: (60.94, 13.36, 0.11, 0.42),
 2018: (115.67, 23.75, 0.24, 0.30), 2019: (136.12, 29.31, 0.70, 1.09), 2020: (151.97, 33.54, 0.53, 1.24),
 2021: (167.89, 42.93, 1.07, 0.47), 2022: (120.32, 42.44, 0.78, 0.41), 2023: (126.68, 48.94, 1.04, 0.14),
 2024: (198.30, 61.35, 0.80, 2.17), 2025: (142.00, 84.50, 1.15, 0.21),
}
# [E3-70] measure: grant-date fair value of the YEAR'S grants (options x WAGDFV + restricted x WAGDFV),
# from each vintage's equity note. 2020-2021 are options only (restricted grants not tabulated in
# those vintages), so those two are floors.
GRANT = {2020: 5.225*7.55, 2021: 5.460*15.06,
         2022: 2.958*11.27 + 0.534*23.37, 2023: 3.178*13.65 + 0.659*24.04,
         2024: 3.813*14.65 + 0.916*31.35, 2025: 2.866*36.08 + 1.192*68.07}

def oe(y, sbc_measure, c_end):
    ocf, sbc, da, cap = CF[y]
    s = sbc if sbc_measure == "charge" else GRANT.get(y, sbc)
    c = max(da, cap) if c_end == "conservative" else min(da, cap)
    return ocf - s - c

CAP = 12422.7
print("GRANT-DATE VALUE OF THE YEAR'S GRANTS [E3-70] vs the accounting charge ($M):")
for y in sorted(GRANT):
    print(f"  {y}: grants {GRANT[y]:6.1f}   charge {CF[y][1]:6.1f}   ratio {GRANT[y]/CF[y][1]:.2f}x")

print("\nOWNER EARNINGS BY YEAR ($M)  [OCF - SBC - (c)], (c) at the conservative end (larger of D&A, capex):")
print(f"  {'year':>6}{'OCF':>9}{'SBC chg':>9}{'D&A':>7}{'capex':>7}{'OE(charge)':>12}{'OE(grant)':>11}")
for y in sorted(CF):
    ocf, sbc, da, cap = CF[y]
    g = f"{oe(y,'grant','conservative'):11.1f}" if y in GRANT else f"{'':>11}"
    print(f"  {y:>6}{ocf:9.1f}{sbc:9.1f}{da:7.2f}{cap:7.2f}{oe(y,'charge','conservative'):12.1f}{g}")

print("\nWINDOW GRID: mean owner earnings ($M) and yield on $12,422.7M cap")
print(f"  {'window':<14}{'years':<10}{'charge/cons':>12}{'charge/gen':>12}{'grant/cons':>12}{'yield chg':>11}{'yield grant':>13}")
windows = [("3-yr", range(2023, 2026)), ("4-yr", range(2022, 2026)), ("5-yr", range(2021, 2026)),
           ("6-yr", range(2020, 2026)), ("7-yr", range(2019, 2026)), ("8-yr", range(2018, 2026)),
           ("9-yr", range(2017, 2026)), ("10-yr", range(2016, 2026)), ("12-yr", range(2014, 2026)),
           ("15-yr", range(2011, 2026)), ("17-yr", range(2009, 2026)),
           ("ex-2025 4-yr", range(2021, 2025)), ("2024-25", range(2024, 2026))]
rows = []
for name, yrs in windows:
    yrs = list(yrs)
    a = statistics.fmean(oe(y, "charge", "conservative") for y in yrs)
    b = statistics.fmean(oe(y, "charge", "generous") for y in yrs)
    gy = [y for y in yrs if y in GRANT]
    g = statistics.fmean(oe(y, "grant", "conservative") for y in gy) if gy and len(gy) == len(yrs) else None
    gs = f"{g:12.1f}" if g is not None else f"{'n/a':>12}"
    gyld = f"{g/CAP*100:12.2f}%" if g is not None else f"{'':>13}"
    print(f"  {name:<14}{yrs[0]}-{str(yrs[-1])[2:]:<5}{a:12.1f}{b:12.1f}{gs}{a/CAP*100:10.2f}%{gyld}")
    rows.append((name, a, b, g))
vals = [r[1] for r in rows if r[0] not in ("ex-2025 4-yr", "2024-25")]
print(f"\n  charge-basis, conservative (c), all eleven windows: min {min(vals):.1f}  max {max(vals):.1f}  width {max(vals)/min(vals) if min(vals)>0 else float('nan'):.2f}x")
gv = [r[3] for r in rows if r[3] is not None]
print(f"  grant-basis windows available (2020-25 only): min {min(gv):.1f}  max {max(gv):.1f}")
print("\nH1 2026 (10-Q): OCF 16.77, SBC 52.46, D&A 1.46, capex 2.73 -> OE(charge) %.1f for six months" % (16.77-52.46-2.73))
print("TTM to 2026-06-30 (charge basis, conservative c): FY2025 + H1'26 - H1'25 where H1'25: OCF 49.07, SBC 40.85, D&A 0.93, capex 0.16")
ttm = (142.00-84.50-1.15) + (16.77-52.46-2.73) - (49.07-40.85-0.93)
print(f"  TTM OE(charge) = {ttm:.1f}")
