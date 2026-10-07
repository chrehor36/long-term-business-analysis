"""TFC - the Q3 primary test [E2-01] and the bank (c) CONVENTION, both constructions.

CCB (2026-09-19) adopted, as a labelled CONVENTION:
    (c) = delta(total assets) x the Tier 1 leverage ratio
    "owner earnings" for a bank = net income - (c)
ACNB (2026-09-19) ruled that delta(assets) must be SPLIT into organic and acquired whenever the
filer has bought anything inside the window, or (c) reports a stock issuance as a loss of
earning power.

Truist forces a third refinement and this script computes it beside the other two, so the run
can say which it uses and why:
  (i)   CCB RAW:      delta(total assets) x Tier 1 leverage ratio
  (ii)  ACNB SPLIT:   organic delta(assets) only - perimeter effects removed by name
  (iii) RWA/CET1:     delta(risk-weighted assets) x the CET1 ratio
The third exists because Truist's total assets move by $20bn on a securities repositioning and
by $7.7bn when a discontinued segment leaves the balance sheet, neither of which is growth the
business had to fund; risk-weighted assets and the CET1 ratio are the binding constraint the
company itself cites ("Creates $945MM or 22 bps of CET1 capital", 8-K of 2026-09-15).
"""

M = 1e6  # figures below are in $ millions already

# Filed balance-sheet totals, $M (companyfacts, latest vintage; cross-checked to the 10-K
# balance sheets: 547,538 / 531,176 / 535,349 / 555,255 / 541,241 / 509,228 / 473,078).
ASSETS = {2019: 473078, 2020: 509228, 2021: 541241, 2022: 555255,
          2023: 535349, 2024: 531176, 2025: 547538, 2026.5: 556023}
# Risk-weighted assets, $M, from each 10-K's holding-company capital table.  2019 is NOT filed
# in the documents pulled for this run; the 2020 row is therefore EXCLUDED from every RWA total
# and the 2019 entry below is a placeholder that no reported figure depends on.
RWA = {2019: 366000, 2020: 379153, 2021: 390886, 2022: 434413, 2023: 423705, 2024: 418337,
       2025: 443257, 2026.5: 434799}
# Holding-company Tier 1 LEVERAGE ratio, %, from the same tables.
LEV = {2020: 9.6, 2021: 8.7, 2022: 8.5, 2023: 9.3, 2024: 10.5, 2025: 10.0, 2026.5: 10.1}
# Holding-company CET1 ratio, %.
CET1 = {2020: 10.0, 2021: 9.6, 2022: 9.0, 2023: 10.1, 2024: 11.5, 2025: 10.8, 2026.5: 10.9}

# Net income and net income available to COMMON, $M, as filed (total company, i.e. including
# discontinued operations, because that is what the shareholder actually earned in the year).
NI = {2020: 4581, 2021: 6406, 2022: 6267, 2023: -1047, 2024: 4840, 2025: 5307, 2026.5: 3030}
NIC = {2020: 4184, 2021: 6033, 2022: 5927, 2023: -1452, 2024: 4469, 2025: 4974, 2026.5: 2900}

# Common equity = total equity - preferred, $M.
EQ = {2019: 66558 - 5102, 2020: 70912 - 8048, 2021: 69271 - 6673, 2022: 60537 - 6673,
      2023: 59253 - 6673, 2024: 63679 - 5907, 2025: 65189 - 4916, 2026.5: 64095 - 5411}
GW = {2019: 24154, 2020: 24447, 2021: 26098, 2022: 23233, 2023: 17156, 2024: 17125,
      2025: 17125, 2026.5: 17125}
INT = {2019: 3142, 2020: 2984, 2021: 3408, 2022: 3672, 2023: 1909, 2024: 1550,
       2025: 1256, 2026.5: 1130}

# Named perimeter effects on total assets, $M, to be REMOVED to get organic growth (ACNB rule).
# 2021: Service Finance acquired 2021-12-06 for $2.0bn cash - loans and intangibles acquired.
# 2023: TIH reclassified to discontinued operations; the student loan portfolio was sold.
# 2024: TIH sold 2024-05-06 - $7,655M of "assets of discontinued operations" left the balance
#       sheet (FY2024 10-K balance sheet, 2023-12-31 column).
PERIM = {2020: 0, 2021: 3300, 2022: 0, 2023: -3400, 2024: -7655, 2025: 0, 2026.5: 0}

YEARS = [2020, 2021, 2022, 2023, 2024, 2025, 2026.5]


def prev(y):
    return {2020: 2019, 2021: 2020, 2022: 2021, 2023: 2022, 2024: 2023,
            2025: 2024, 2026.5: 2025}[y]


def tce(y):
    return EQ[y] - GW[y] - INT[y]


print("=" * 108)
print("THE PRIMARY TEST [E2-01] - earnings rate on equity capital employed, recomputed")
print("%-7s %10s %10s %10s %8s %8s %10s %8s" % (
    "year", "NI common", "avg common", "ROE %", "avg TCE", "ROTCE %", "avg assets", "ROA %"))
for y in YEARS:
    p = prev(y)
    ace = (EQ[p] + EQ[y]) / 2.0
    atce = (tce(p) + tce(y)) / 2.0
    aa = (ASSETS[p] + ASSETS[y]) / 2.0
    n = NIC[y] * (2 if y == 2026.5 else 1)   # H1 2026 annualised
    print("%-7s %10s %10s %10.2f %8s %8.2f %10s %8.3f" % (
        ("H1-26 ann." if y == 2026.5 else y), f"{n:,.0f}", f"{ace:,.0f}",
        100 * n / ace, f"{atce:,.0f}", 100 * n / atce, f"{aa:,.0f}", 100 * n / aa))

print()
print("=" * 108)
print("THE (c) EQUIVALENT - three constructions, $M")
print("%-7s %11s %9s %11s %11s %11s %11s %11s" % (
    "year", "d assets", "lev %", "(i) CCB", "organic d", "(ii) ACNB", "d RWA x CET1", "NI"))
tot = {"i": 0.0, "ii": 0.0, "iii": 0.0, "ni": 0.0}
for y in YEARS:
    p = prev(y)
    da = ASSETS[y] - ASSETS[p]
    ci = da * LEV[y] / 100.0
    org = da - PERIM[y]
    cii = org * LEV[y] / 100.0
    drwa = RWA[y] - RWA[p] if p in RWA else None
    ciii = drwa * CET1[y] / 100.0 if drwa is not None else None
    n = NI[y] * (2 if y == 2026.5 else 1)
    if y != 2026.5:
        tot["i"] += ci
        tot["ii"] += cii
        if ciii is not None:
            tot["iii"] += ciii
        tot["ni"] += n
    print("%-7s %11s %9.1f %11s %11s %11s %11s %11s" % (
        ("H1-26 ann." if y == 2026.5 else y), f"{da:,.0f}", LEV[y], f"{ci:,.0f}",
        f"{org:,.0f}", f"{cii:,.0f}",
        f"{ciii:,.0f}" if ciii is not None else "n/a", f"{n:,.0f}"))
print("-" * 108)
print("2021-2025 totals:  (i) CCB %s   (ii) ACNB %s   (iii) RWA/CET1 %s   net income %s" % (
    f"{tot['i'] - (ASSETS[2020]-ASSETS[2019])*LEV[2020]/100:,.0f}",
    f"{tot['ii'] - (ASSETS[2020]-ASSETS[2019]-PERIM.get(2020,0))*LEV[2020]/100:,.0f}",
    f"{tot['iii'] - (RWA[2020]-RWA.get(2019, RWA[2020]))*CET1[2020]/100:,.0f}",
    f"{tot['ni'] - NI[2020]:,.0f}"))

print()
print("OWNER EARNINGS ON THE BANK CONVENTION = net income - (c), by construction, $M")
print("%-7s %11s %11s %11s %11s" % ("year", "NI", "(i) CCB", "(ii) ACNB", "(iii) RWA"))
s = {"i": 0.0, "ii": 0.0, "iii": 0.0, "n": 0}
for y in [2021, 2022, 2023, 2024, 2025]:
    p = prev(y)
    da = ASSETS[y] - ASSETS[p]
    ci = da * LEV[y] / 100.0
    cii = (da - PERIM[y]) * LEV[y] / 100.0
    ciii = (RWA[y] - RWA[p]) * CET1[y] / 100.0
    n = NI[y]
    s["i"] += n - ci
    s["ii"] += n - cii
    s["iii"] += n - ciii
    s["n"] += 1
    print("%-7s %11s %11s %11s %11s" % (
        y, f"{n:,.0f}", f"{n-ci:,.0f}", f"{n-cii:,.0f}", f"{n-ciii:,.0f}"))
print("5-yr mean %s %11s %11s %11s" % (
    " " * 1, f"{s['i']/5:,.0f}", f"{s['ii']/5:,.0f}", f"{s['iii']/5:,.0f}"))
print("3-yr mean (2023-25), (iii) basis: %s" % f"{(NI[2023]-(RWA[2023]-RWA[2022])*CET1[2023]/100 + NI[2024]-(RWA[2024]-RWA[2023])*CET1[2024]/100 + NI[2025]-(RWA[2025]-RWA[2024])*CET1[2025]/100)/3:,.0f}")
print("2025 alone, (iii) basis: %s" % f"{NI[2025]-(RWA[2025]-RWA[2024])*CET1[2025]/100:,.0f}")

print()
print("=" * 108)
print("EQUITY RECONCILIATION - where the common equity came from, 2020-12-31 to 2025-12-31")
d_eq = EQ[2025] - EQ[2020]
cum_ni = sum(NIC[y] for y in (2021, 2022, 2023, 2024, 2025))
print("  common equity  %s -> %s   change %s" % (
    f"{EQ[2020]:,.0f}", f"{EQ[2025]:,.0f}", f"{d_eq:,.0f}"))
print("  cumulative net income available to common 2021-2025: %s" % f"{cum_ni:,.0f}")
print("  cumulative common dividends 2021-2025 (2.5+2.7+2.8+2.8+2.7): %s" % f"{13500:,.0f}")
print("  cumulative buybacks 2021-2025 (1.6+0.25+0+1.0+2.5): %s" % f"{5350:,.0f}")
print("  implied AOCI + other: %s" % f"{d_eq - cum_ni + 13500 + 5350:,.0f}")
print()
print("TANGIBLE BOOK VALUE PER SHARE, filed: 26.78 (2020) 25.47 (2021) 18.04 (2022)"
      " 24.05* (2023) 30.01 (2024) 33.48 (2025) 33.40 (2026-06-30)")
print("  *2023 TBVPS is computed here from filed TCE and shares and is flagged in the run.")
sh = {2020: 1348000, 2021: 1332000, 2022: 1330000, 2023: 1334000, 2024: 1315936,
      2025: 1262470, 2026.5: 1221626}
for y in YEARS:
    print("   %-7s TCE %10s  shares %10s  TBVPS %7.2f  BVPS %7.2f" % (
        ("2026-06-30" if y == 2026.5 else y), f"{tce(y):,.0f}", f"{sh[y]:,.0f}",
        tce(y) * 1000.0 / sh[y], EQ[y] * 1000.0 / sh[y]))
