"""Owner earnings for Colgate from the FILED cash-flow statements (hand-transcribed, $M), every window, both (c) ends.
Arithmetic only. Sources: 10-K FY2017 (2015-2017), FY2020 (2018-2020), FY2023 (2021-2023), FY2025 (2023-2025), 10-Q Q2 2026 (H1).
Where two vintages print a year, both were read; they agree except where noted (2020 capex 410 in the FY2020 10-K; XBRL old tag 409).
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
Y = list(range(2015, 2026))
OCF  = dict(zip(Y, [2949, 3141, 3054, 3056, 3133, 3719, 3325, 2556, 3745, 4107, 4198]))
SBC  = dict(zip(Y, [125, 123, 127, 109, 100, 107, 135, 125, 122, 135, 155]))     # CFS add-back = equity statement = Note 8
DA   = dict(zip(Y, [449, 443, 475, 511, 519, 539, 556, 545, 567, 605, 630]))
AMORT = dict(zip(Y, [33, 33, 35, 59, 62, 88, 89, 80, 72, 75, 78]))               # Other (income) expense notes
CAPEX = dict(zip(Y, [691, 593, 553, 436, 335, 410, 567, 696, 705, 561, 564]))
ACQ  = dict(zip(Y, [13, 5, 0, 728, 1711, 353, 0, 809, 0, 0, 293]))              # payment for acquisitions, net of cash
ESOPDIV = dict(zip(Y, [38, 35, 32, 29, 25, 23, 20, 19, 17, 16, 15]))            # dividends paid on ESOP shares (Note 9), upper bound
REST = dict(zip(Y, [254, 228, 333, 152, 125, -16, 0, 95, 27, 85, 13]))          # restructuring program charges, pre-tax (Corporate tables)
SALES = dict(zip(Y, [16034, 15195, 15454, 15544, 15693, 16471, 17421, 17967, 19457, 20101, 20382]))
DEP = {y: DA[y] - AMORT[y] for y in Y}
# TTM to 2026-06-30 = FY2025 - H1 2025 + H1 2026
TTM = dict(OCF=4198 - 1484 + 1742, SBC=155 - 55 + 78, DA=630 - 299 + 311, CAPEX=564 - 232 + 266, ACQ=293 - 293 + 0)

rows = []
for y in Y:
    oc = OCF[y] - SBC[y] - CAPEX[y]
    od = OCF[y] - SBC[y] - DEP[y]
    oda = OCF[y] - SBC[y] - DA[y]
    rows.append((y, OCF[y], SBC[y], DA[y], DEP[y], CAPEX[y], oc, od, oda, ACQ[y], ESOPDIV[y], SALES[y]))

def mean(ys, idx):
    return sum(r[idx] for r in rows if r[0] in ys) / len(ys)

L = ["| year | OCF | SBC | D&A | depreciation (D&A − intangible amort.) | capex | OE, capex end | OE, depreciation end | OE, D&A end (INVALID if [E5-20] applies) | capex/depr. | acquisitions | ESOP dividends (upper bound) | SBC/OCF |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    y, ocf, sbc, da, dep, cx, oc, od, oda, acq, ed, s = r
    L.append(f"| {y} | {ocf:,} | {sbc} | {da} | {dep} | {cx} | {oc:,} | {od:,} | {oda:,} | {cx/dep:.2f} | {acq:,} | {ed} | {sbc/ocf:.1%} |")
t_oc = TTM["OCF"] - TTM["SBC"] - TTM["CAPEX"]
L.append(f"| TTM 2026-06-30 | {TTM['OCF']:,} | {TTM['SBC']} | {TTM['DA']} | n/a | {TTM['CAPEX']} | {t_oc:,} | | {TTM['OCF']-TTM['SBC']-TTM['DA']:,} | | 0 | | {TTM['SBC']/TTM['OCF']:.1%} |")

W = {
    "3-yr 2023-25": [2023, 2024, 2025],
    "5-yr 2021-25 (the [E2-42] default)": [2021, 2022, 2023, 2024, 2025],
    "5-yr 2020-24": [2020, 2021, 2022, 2023, 2024],
    "5-yr 2021-25 without 2022": [2021, 2023, 2024, 2025],
    "10-yr 2016-25 (post-Venezuela perimeter)": list(range(2016, 2026)),
    "11-yr 2015-25 (crosses the Venezuela perimeter change: shown, not used)": list(range(2015, 2026)),
    "5-yr 2016-20": [2016, 2017, 2018, 2019, 2020],
}
L += ["", "| window | OE capex end | OE depreciation end | OE D&A end | less ESOP-dividend upper bound (capex end) | mean acquisitions (display, not subtracted) | mean restructuring charges pre-tax (inside OCF as cash) |", "|---|---|---|---|---|---|---|"]
for name, ys in W.items():
    oc, od, oda = mean(ys, 6), mean(ys, 7), mean(ys, 8)
    ed = sum(ESOPDIV[y] for y in ys) / len(ys)
    acq = sum(ACQ[y] for y in ys) / len(ys)
    rs = sum(REST[y] for y in ys) / len(ys)
    L.append(f"| {name} | {oc:,.0f} | {od:,.0f} | {oda:,.0f} | {oc-ed:,.0f} | {acq:,.0f} | {rs:,.0f} |")
L.append(f"| TTM to 2026-06-30 (a single twelve months: not a mean) | {t_oc:,} | | {TTM['OCF']-TTM['SBC']-TTM['DA']:,} | | 0 | H1 2026 charges $305M |")

# per-share owner earnings (capex end), 10-yr, on weighted average diluted shares (10-K EPS notes)
DIL = dict(zip(Y, [909.7, 898.4, 887.8, 873.0, 861.1, 859.3, 848.3, 838.8, 829.2, 823.2, 811.1]))   # 10-K EPS notes FY2017, FY2020, FY2023, FY2025
L += ["", "| year | OE capex end per diluted share | growth |", "|---|---|---|"]
prev = None
for r in rows:
    y = r[0]
    if DIL.get(y):
        ps = r[6] / DIL[y]
        L.append(f"| {y} | ${ps:.2f} | {'' if prev is None else f'{ps/prev-1:+.1%}'} |")
        prev = ps
open(os.path.join(HERE, "oe_out.md"), "w", encoding="utf-8").write("\n".join(L))
print("\n".join(L))
tot_cx = sum(CAPEX[y] for y in range(2016, 2026)); tot_dep = sum(DEP[y] for y in range(2016, 2026)); tot_da = sum(DA[y] for y in range(2016, 2026))
print(f"\n2016-25 capex {tot_cx:,} vs depreciation {tot_dep:,} ({tot_cx/tot_dep:.2f}x) vs D&A {tot_da:,} ({tot_cx/tot_da:.2f}x); acquisitions {sum(ACQ[y] for y in range(2016,2026)):,}")
print("capex % sales", {y: f"{CAPEX[y]/SALES[y]:.1%}" for y in Y})
print("SBC/OCF cumulative 2016-25", f"{sum(SBC[y] for y in range(2016,2026))/sum(OCF[y] for y in range(2016,2026)):.1%}")

# WORKING-CAPITAL LINES INSIDE OCF (receivables + inventories + accounts payable and other accruals / working capital), as filed.
# Positive = cash released. Other non-current assets and liabilities excluded (not working capital).
WC = {2016: -17 - 4 + 100, 2017: -15 - 8 - 96, 2018: -79 - 58 + 18, 2019: 19 - 77 + 36, 2020: 138 - 251 + 520,
      2021: -84 - 72 + 14, 2022: -227 - 333 - 115, 2023: -37 + 194 + 309, 2024: -56 - 100 + 516, 2025: -16 + 109 + 251}
print("\nworking-capital release by year", WC)
for name, ys in W.items():
    if min(ys) < 2016:
        continue
    oc = mean(ys, 6); w = sum(WC[y] for y in ys) / len(ys)
    print(f"{name}: OE capex end {oc:,.0f}; mean working-capital release {w:+,.0f}; OE capex end ex working capital {oc - w:,.0f}")
# LatAm segment capex vs D&A (10-K segment notes FY2017-FY2025)
LA_CX = {2016: 94, 2017: 127, 2018: 131, 2019: 90, 2020: 104, 2021: 118, 2022: 121, 2023: 146, 2024: 126, 2025: 141}
LA_DA = {2016: 76, 2017: 82, 2018: 82, 2019: 84, 2020: 81, 2021: 88, 2022: 93, 2023: 98, 2024: 100, 2025: 106}
HI_CX = {2016: 38, 2017: 33, 2018: 35, 2019: 41, 2020: 56, 2021: 147, 2022: 297, 2023: 301, 2024: 143, 2025: 88}
HI_DA = {2019: 55, 2020: 58, 2021: 62, 2022: 65, 2023: 101, 2024: 132, 2025: 144}
print("LatAm capex/D&A 2016-25", sum(LA_CX.values()), sum(LA_DA.values()), round(sum(LA_CX.values()) / sum(LA_DA.values()), 2))
print("Hill's capex 2021-24", sum(HI_CX[y] for y in (2021, 2022, 2023, 2024)), "D&A 2021-24", sum(HI_DA[y] for y in (2021, 2022, 2023, 2024)))
