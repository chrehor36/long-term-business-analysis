#!/usr/bin/env python3
"""Q4 arithmetic: owner earnings by window, TTM, the [E2-60] distribution test."""
from compute import OCF, CAPEX, DA, SBC, BUYBK, SALES, YRS

# 10-Q for the six months ended 2026-06-30, accession 0000898173-26-000045
H1_26 = dict(ocf=2039412, capex=552050, sbc=17512, buyback=2433023, da=273643)
H1_25 = dict(ocf=1511966, capex=587685, sbc=18812, buyback=1176640, da=247159)

CAP = 808960792 * 86.86 / 1000            # $k
SOV = 0.0527
FLOOR = 0.10

print("=" * 78)
print("A. OWNER EARNINGS BY YEAR  [E2-23]  OCF - SBC - (c)")
print("=" * 78)
print(f"{'FY':>6}{'OCF':>11}{'SBC':>8}{'capex':>10}{'D&A':>9}"
      f"{'OE@capex':>11}{'OE@D&A':>11}{'yoy@capex':>10}")
prev = None
for y in YRS:
    a = OCF[y] - SBC[y] - CAPEX[y]
    b = OCF[y] - SBC[y] - DA[y]
    yoy = "" if prev is None else f"{(a/prev-1)*100:+8.1f}%"
    print(f"{y:>6}{OCF[y]:>11,}{SBC[y]:>8,}{CAPEX[y]:>10,}{DA[y]:>9,}"
          f"{a:>11,}{b:>11,}{yoy:>10}")
    prev = a

oe25 = OCF[2025] - SBC[2025] - CAPEX[2025]
oe21 = OCF[2021] - SBC[2021] - CAPEX[2021]
print(f"\n  2021 peak {oe21:,} -> 2025 {oe25:,} = {(oe25/oe21-1)*100:+.1f}% "
      f"over FOUR CONSECUTIVE DECLINES, while revenue rose "
      f"{(SALES[2025]/SALES[2021]-1)*100:+.1f}%")

ttm_ocf = OCF[2025] - H1_25["ocf"] + H1_26["ocf"]
ttm_cap = CAPEX[2025] - H1_25["capex"] + H1_26["capex"]
ttm_sbc = SBC[2025] - H1_25["sbc"] + H1_26["sbc"]
ttm_da = DA[2025] - H1_25["da"] + H1_26["da"]
print(f"\n  TTM to 2026-06-30: OCF {ttm_ocf:,}  capex {ttm_cap:,}  SBC {ttm_sbc:,}  D&A {ttm_da:,}")
print(f"  TTM OE @capex = {ttm_ocf-ttm_sbc-ttm_cap:,}   @D&A = {ttm_ocf-ttm_sbc-ttm_da:,}")
print(f"  H1-2026 OE {H1_26['ocf']-H1_26['sbc']-H1_26['capex']:,} vs "
      f"H1-2025 {H1_25['ocf']-H1_25['sbc']-H1_25['capex']:,}")
print("  CAUTION: H1-26 OCF rose $527M while net income rose only $112M; the")
print("  condensed statement shows 'Other' +455,557 (vs -227,014) and income taxes")
print("  payable -33,836 (vs +314,779) -- a large working-capital/timing component.")

print("\n" + "=" * 78)
print("B. WINDOWS  [E4-25, E2-42, E4-38]  -- every window published, none preferred")
print("=" * 78)
W = {"5y default 2021-2025 [E2-42]": list(range(2021, 2026)),
     "4y ex-2021 stimulus [E4-41]": [2022, 2023, 2024, 2025],
     "3y 2023-2025": [2023, 2024, 2025],
     "10y 2016-2025": YRS,
     "8y ex-2020/21 [E4-41]": [2016, 2017, 2018, 2019, 2022, 2023, 2024, 2025]}
rows = {}
for lbl, ys in W.items():
    a = sum(OCF[y] - SBC[y] - CAPEX[y] for y in ys) / len(ys)
    b = sum(OCF[y] - SBC[y] - DA[y] for y in ys) / len(ys)
    rows[lbl] = (a, b)
    print(f"  {lbl:<32} @capex {a:>10,.0f}   @D&A {b:>10,.0f}")
print(f"  {'TTM to 2026-06-30':<32} @capex {ttm_ocf-ttm_sbc-ttm_cap:>10,.0f}"
      f"   @D&A {ttm_ocf-ttm_sbc-ttm_da:>10,.0f}")
print(f"  {'FY2025 alone (most recent audited)':<32} @capex {oe25:>10,.0f}"
      f"   @D&A {OCF[2025]-SBC[2025]-DA[2025]:>10,.0f}")

allv = [v for r in rows.values() for v in r] + [ttm_ocf-ttm_sbc-ttm_cap,
        ttm_ocf-ttm_sbc-ttm_da, oe25, OCF[2025]-SBC[2025]-DA[2025]]
lo, hi = min(allv), max(allv)
print(f"\n  FULL RANGE {lo:,.0f} .. {hi:,.0f}   WIDTH {(hi/lo-1)*100:.1f}%")

print("\n" + "=" * 78)
print("C. [E2-60] -- WERE DISTRIBUTIONS FUNDED BY DEBT?")
print("=" * 78)
DEBT = {2021: 3826978, 2022: 4371653, 2023: 5570125, 2024: 5520932, 2025: 6016904}
print(f"{'FY':>6}{'OE@capex':>12}{'buybacks':>12}{'gap':>12}{'total debt':>12}{'d debt':>11}")
cum_gap = cum_debt = 0
for y in [2022, 2023, 2024, 2025]:
    a = OCF[y] - SBC[y] - CAPEX[y]
    gap = BUYBK[y] - a
    dd = DEBT[y] - DEBT[y - 1]
    cum_gap += gap; cum_debt += dd
    print(f"{y:>6}{a:>12,}{BUYBK[y]:>12,}{gap:>12,}{DEBT[y]:>12,}{dd:>11,}")
h1 = H1_26["ocf"] - H1_26["sbc"] - H1_26["capex"]
gap = H1_26["buyback"] - h1
dd = 7014543 - DEBT[2025]
cum_gap += gap; cum_debt += dd
print(f"{'H1-26':>6}{h1:>12,}{H1_26['buyback']:>12,}{gap:>12,}{7014543:>12,}{dd:>11,}")
print(f"\n  CUMULATIVE 2022 -> 2026-06-30: buybacks exceeded owner earnings by "
      f"{cum_gap:,}k;\n  total debt rose {cum_debt:,}k. Ratio {cum_debt/cum_gap:.2f}x.")

print("\n" + "=" * 78)
print("D. VALUATION GRID -- COMPUTATION, NOT A CLEARANCE (operator rule 3)")
print("=" * 78)
print(f"  market cap {CAP:,.0f}k = ${CAP/1e6:.2f}bn at $86.86 x 808,960,792 sh")
print(f"\n{'owner earnings':>16}{'yield':>9}{'zero-g value @5.27%':>22}{'$/share':>10}"
      f"{'@10% floor':>13}{'$/sh':>9}{'g for 10%':>11}")
for lbl, v in [("low  " + f"{lo:,.0f}", lo), ("TTM  " + f"{ttm_ocf-ttm_sbc-ttm_cap:,.0f}",
                ttm_ocf-ttm_sbc-ttm_cap), ("high " + f"{hi:,.0f}", hi)]:
    y = v / CAP
    print(f"{lbl:>16}{y*100:>8.2f}%{v/SOV/1e6:>20,.1f}bn{v/SOV/808960792*1000:>10.2f}"
          f"{v/FLOOR/1e6:>11,.1f}bn{v/FLOOR/808960792*1000:>9.2f}{(FLOOR-y)*100:>10.2f}%")
print(f"\n  growth needed just to reach the {SOV*100:.2f}% sovereign:")
for lbl, v in [("low", lo), ("TTM", ttm_ocf-ttm_sbc-ttm_cap), ("high", hi)]:
    print(f"    {lbl:>4}: {(SOV - v/CAP)*100:+.2f}%   perpetual")
