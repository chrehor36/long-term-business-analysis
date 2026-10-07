"""SPGI owner earnings, hand-built from the FILED cash-flow statements.
Never a net-income proxy. Every input is quoted in the run file with its 10-K.
Perimeters are kept separate and never blended inside one mean.
"""

# --- consolidated, as filed (10-K cash-flow statements FY2017-FY2025, $M) ---
OCF   = {2017:2016, 2018:2064, 2019:2776, 2020:3567, 2021:3598, 2022:2603, 2023:3710, 2024:5689, 2025:5651}
SBC   = {2017:  99, 2018:  94, 2019:  78, 2020:  90, 2021: 122, 2022: 214, 2023: 171, 2024: 247, 2025: 236}
CAPEX = {2017: 123, 2018: 113, 2019: 115, 2020:  76, 2021:  35, 2022:  89, 2023: 143, 2024: 124, 2025: 195}
DA    = {2017: 180, 2018: 206, 2019: 204, 2020: 206, 2021: 178, 2022:1013, 2023:1143, 2024:1173, 2025:1179}
NCID  = {2017: 111, 2018: 154, 2019: 143, 2020: 194, 2021: 227, 2022: 270, 2023: 280, 2024: 287, 2025: 321}
# working-capital movement inside OCF, summed from the filed detail lines
WC    = {2023:-460, 2024: 235, 2025:-432}

# --- Mobility, from the FILED Article 11 pro forma (8-K/A 0001104659-26-080571) ---
MOB_OP  = {2023:317, 2024:374, 2025:373}      # discontinued-operations column operating profit
MOB_DA  = {2023:311, 2024:315, 2025:317}      # depreciation 9/13/14 + amortization 302/302/303
MOB_TAX = {2023: 63, 2024: 92, 2025: 69}      # provision in the disc-ops column
MOB_CAPX= {2023: 22, 2024: 18, 2025: 28}      # 10-K Note 12 segment capital expenditures
# continuing-operations D&A, from the pro forma
CONT_DA = {2023: 92+740, 2024: 83+775, 2025: 96+766}


def oe(y, end="capex", perimeter="consolidated", strip_wc=False):
    ocf, capex, da = OCF[y], CAPEX[y], DA[y]
    if perimeter == "continuing":
        # remove Mobility's own cash generation. Mobility's SBC is left inside
        # continuing (see the run file): omitting it here overstates continuing OCF by
        # ~$26M and the full consolidated SBC deduction below over-deducts by the same,
        # so the two cancel.
        ocf = ocf - (MOB_OP[y] + MOB_DA[y] - MOB_TAX[y])
        capex = capex - MOB_CAPX[y]
        da = CONT_DA[y]
    c = capex if end == "capex" else da
    v = ocf - SBC[y] - c - NCID[y]
    if strip_wc:
        v = v - WC[y]
    return v


def mean(ys, **kw):
    return sum(oe(y, **kw) for y in ys) / len(ys)


if __name__ == "__main__":
    print("A. CONTINUING OPERATIONS ex-Mobility (the perimeter being priced), $M")
    print(f"{'yr':>6} {'contOCF':>8} {'SBC':>5} {'capex':>6} {'D&A':>6} {'NCIdist':>8} {'OE(capex)':>10} {'OE(D&A)':>8} {'OE ex-wc':>9}")
    for y in (2023, 2024, 2025):
        co = OCF[y] - (MOB_OP[y] + MOB_DA[y] - MOB_TAX[y])
        print(f"{y:>6} {co:>8} {SBC[y]:>5} {CAPEX[y]-MOB_CAPX[y]:>6} {CONT_DA[y]:>6} {NCID[y]:>8} "
              f"{oe(y,'capex','continuing'):>10} {oe(y,'da','continuing'):>8} "
              f"{oe(y,'capex','continuing',strip_wc=True):>9}")
    print(f"  3-yr mean 2023-25: capex end {mean([2023,2024,2025],end='capex',perimeter='continuing'):,.0f}"
          f" | D&A end {mean([2023,2024,2025],end='da',perimeter='continuing'):,.0f}"
          f" | capex end, wc movement stripped {mean([2023,2024,2025],end='capex',perimeter='continuing',strip_wc=True):,.0f}")
    print()
    print("B. CONSOLIDATED AS FILED, the [E2-42] five-year default 2021-2025, $M")
    print(f"{'yr':>6} {'OCF':>6} {'SBC':>5} {'capex':>6} {'D&A':>6} {'NCIdist':>8} {'OE(capex)':>10} {'OE(D&A)':>8}")
    for y in range(2021, 2026):
        print(f"{y:>6} {OCF[y]:>6} {SBC[y]:>5} {CAPEX[y]:>6} {DA[y]:>6} {NCID[y]:>8} "
              f"{oe(y):>10} {oe(y,'da'):>8}")
    print(f"  5-yr mean 2021-25: capex end {mean(range(2021,2026)):,.0f} | D&A end {mean(range(2021,2026),end='da'):,.0f}")
    print()
    print("C. PRE-MERGER LEGACY S&P GLOBAL, 2017-2021, $M")
    for y in range(2017, 2022):
        print(f"{y:>6} {OCF[y]:>6} {SBC[y]:>5} {CAPEX[y]:>6} {DA[y]:>6} {NCID[y]:>8} "
              f"{oe(y):>10} {oe(y,'da'):>8}")
    print(f"  5-yr mean 2017-21: capex end {mean(range(2017,2022)):,.0f} | D&A end {mean(range(2017,2022),end='da'):,.0f}")
    print()
    print("D. WITHOUT the NCI-distribution deduction (the bare CONVENTION), continuing 2023-25")
    for y in (2023, 2024, 2025):
        print(f"{y:>6} {oe(y,'capex','continuing')+NCID[y]:>8}")
    print(f"  mean {mean([2023,2024,2025],end='capex',perimeter='continuing')+sum(NCID[y] for y in (2023,2024,2025))/3:,.0f}")
    print()
    print("E. TTM to 2026-06-30, continuing (10-Q 0000064040-26-000045)")
    ocf_ttm = 5651 - 2398 + 2476
    capex_ttm = 195 - 104 + 65
    sbc_ttm = 236 - 92 + 95
    ncid_ttm = 321 - 168 + 162
    mob_op_ttm = 373 - 190 + 197
    mob_da_ttm = 317          # held at the FY2025 rate; the 10-Q gives no segment D&A
    mob_tax_ttm = round(mob_op_ttm * 0.23)
    cont_ocf = ocf_ttm - (mob_op_ttm + mob_da_ttm - mob_tax_ttm)
    cont_capex = capex_ttm - 28
    print(f"  consolidated OCF {ocf_ttm}, capex {capex_ttm}, SBC {sbc_ttm}, NCI dist {ncid_ttm}")
    print(f"  Mobility removed: op {mob_op_ttm} + D&A {mob_da_ttm} - tax {mob_tax_ttm} = {mob_op_ttm+mob_da_ttm-mob_tax_ttm}")
    print(f"  continuing OCF {cont_ocf}, continuing capex {cont_capex}")
    print(f"  OE (capex end) = {cont_ocf - sbc_ttm - cont_capex - ncid_ttm}")
    print()
    print("F. THE [E4-41] CYCLE NORMALIZATION, as a sensitivity and NOT baked in")
    for y, tr, bi in ((2023, 1425, 2539), (2024, 2326, 3911), (2025, 2470, 4327)):
        print(f"  {y}: Ratings transaction revenue {tr}, billed issuance ${bi}bn, {tr/bi/1000*1e4:.2f} bp")
    mid = (2539 + 3911 + 4327) / 3
    rate = sum(t / b for t, b in ((1425, 2539), (2326, 3911), (2470, 4327))) / 3
    print(f"  3-yr mean billed issuance ${mid:,.0f}bn at the 3-yr mean rate -> transaction revenue {mid*rate:,.0f}")
    print(f"  against FY2025 actual 2,470 -> a shortfall of {2470 - mid*rate:,.0f} pre-tax,"
          f" {(2470 - mid*rate)*0.77:,.0f} after tax at 23%")
