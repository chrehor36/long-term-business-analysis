"""Arithmetic for the PLTR run of 2026-10-26. Every input is a filed figure (USD thousands unless noted),
transcribed from the filings named beside it. No judgment is made here.
Usage: python -I calc.py
"""

# ---- filed inputs -------------------------------------------------------------------------
# accessions: FY2021 0001193125-22-050913, FY2022 0001321655-23-000011, FY2023 0001321655-24-000022,
# FY2024 0001321655-25-000022, FY2025 0001321655-26-000011, Q2 2026 10-Q 0001321655-26-000041
OCF = {2020: -296608, 2021: 333851, 2022: 223737, 2023: 712183, 2024: 1153865, 2025: 2134473}
SBC = {2020: 1270702, 2021: 778215, 2022: 564798, 2023: 475903, 2024: 691638, 2025: 684033}
CAPEX = {2020: 12236, 2021: 12627, 2022: 40027, 2023: 15114, 2024: 12634, 2025: 33882}
DA = {2020: 13871, 2021: 14897, 2022: 22522, 2023: 33354, 2024: 31587, 2025: 26145}
INT = {2020: 4680, 2021: 1607, 2022: 20309, 2023: 132572, 2024: 196792, 2025: 229181}
REV = {2018: 595409, 2019: 742555, 2020: 1092673, 2021: 1541889, 2022: 1905871, 2023: 2225012,
       2024: 2865507, 2025: 4475446}
OPINC = {2020: -1173679, 2021: -411046, 2022: -161201, 2023: 119966, 2024: 310403, 2025: 1414015}
NSS_TAX = {2024: 218280, 2025: 81117}          # taxes paid on net share settlement (financing)
# six months to June 30 (10-Q 0001321655-26-000041)
H1 = {2026: dict(ocf=2115332, sbc=466801, capex=21955, interest=143899, rev=3568047, opinc=1666002),
      2025: dict(ocf=849514, sbc=315310, capex=13818, interest=106696, rev=1887552, opinc=445365)}
CASH_0630 = 2030047
SECS_0630 = 7379052          # marketable securities (includes small public equity stakes)
DEBT_0630 = 0                # no borrowings; $500M undrawn revolver (FY2025 10-K)
# shares (cover of 10-Q, as of July 27, 2026)
SH_A, SH_B, SH_F = 2300713329, 101340151, 1005000
# awards outstanding June 30, 2026 (10-Q note): options, SARs, RSUs, P-RSUs (thousands of shares)
OPT_N, OPT_K = 149677, 10.06
SAR_N, SAR_K = 13671, 131.61
RSU_N, PRSU_N = 33249, 121
PRICE = 196.75               # close 2026-10-23, aggregator (live quote only), via tools/run.py
RF = 0.0533                  # US Treasury 30-year par yield, 10/23/2026 (tools/sources.py)
FLOOR = 0.10                 # CONVENTION of the framework (Q7): about ten percent


def pv_case(c0, g, r, years=10):
    """Owner cash c0 (year-0 level) grown at g for `years`, then zero nominal growth forever, at rate r."""
    pv, c = 0.0, c0
    for t in range(1, years + 1):
        c *= (1 + g)
        pv += c / (1 + r) ** t
    pv += (c / r) / (1 + r) ** years
    return pv


def main():
    print("STEP 0")
    shares = SH_A + SH_B + SH_F
    print(f"  cover shares {shares:,}  market cap ${shares*PRICE/1e9:,.2f}B")
    opt_net = OPT_N - OPT_N * OPT_K / PRICE
    sar_net = SAR_N * max(0.0, PRICE - SAR_K) / PRICE
    dil_k = opt_net + sar_net + RSU_N + PRSU_N
    dil = shares + dil_k * 1000
    print(f"  treasury-method dilution: options {opt_net:,.0f}k  SARs {sar_net:,.0f}k  RSU {RSU_N + PRSU_N:,}k"
          f"  total {dil_k:,.0f}k  diluted count {dil/1e6:,.1f}M  ({dil_k*1000/shares:.1%} of cover)")
    print(f"  diluted market value ${dil*PRICE/1e9:,.2f}B")
    netcash = CASH_0630 + SECS_0630 - DEBT_0630
    print(f"  net cash 2026-06-30 ${netcash/1e6:,.3f}B")
    ev = dil * PRICE / 1000 - netcash
    print(f"  enterprise value (diluted mkt value less net cash) ${ev/1e6:,.2f}B")

    print("\nOWNER CASH (OCF - SBC - capex), all-equity variant also less interest income, $M")
    oc, oce = {}, {}
    for y in range(2020, 2026):
        oc[y] = (OCF[y] - SBC[y] - CAPEX[y]) / 1000
        oce[y] = oc[y] - INT[y] / 1000
        da_var = (OCF[y] - SBC[y] - DA[y]) / 1000
        print(f"  {y}: OCF {OCF[y]/1000:8.1f} SBC {SBC[y]/1000:7.1f} capex {CAPEX[y]/1000:5.1f} D&A {DA[y]/1000:5.1f}"
              f" | owner cash {oc[y]:8.1f} (D&A variant {da_var:8.1f}) | less interest {oce[y]:8.1f}"
              f" | rev {REV[y]/1000:7.1f} margin {oc[y]*1000/REV[y]:6.1%}")
    win = range(2021, 2026)
    avg = sum(oc[y] for y in win) / 5
    avge = sum(oce[y] for y in win) / 5
    print(f"  five-year average 2021-2025: equity-only basis {avg:,.1f}  all-equity basis {avge:,.1f}")
    first = (oce[2021] + oce[2022]) / 2
    second = (oce[2024] + oce[2025]) / 2
    print(f"  (b) halves of the window, all-equity: first (2021-22) {first:,.1f}  second (2024-25) {second:,.1f}"
          f"  -> sign changes, growth meaningless")
    # TTM to June 30, 2026
    t = {k: None for k in ("ocf", "sbc", "capex", "interest", "rev", "opinc")}
    ttm_ocf = OCF[2025] + H1[2026]["ocf"] - H1[2025]["ocf"]
    ttm_sbc = SBC[2025] + H1[2026]["sbc"] - H1[2025]["sbc"]
    ttm_capex = CAPEX[2025] + H1[2026]["capex"] - H1[2025]["capex"]
    ttm_int = INT[2025] + H1[2026]["interest"] - H1[2025]["interest"]
    ttm_rev = REV[2025] + H1[2026]["rev"] - H1[2025]["rev"]
    ttm_oc = (ttm_ocf - ttm_sbc - ttm_capex) / 1000
    ttm_oce = ttm_oc - ttm_int / 1000
    print(f"  TTM to 2026-06-30: OCF {ttm_ocf/1000:,.1f} SBC {ttm_sbc/1000:,.1f} capex {ttm_capex/1000:,.1f}"
          f" interest {ttm_int/1000:,.1f} revenue {ttm_rev/1000:,.1f} -> owner cash {ttm_oc:,.1f},"
          f" all-equity {ttm_oce:,.1f} ({ttm_oce*1000/ttm_rev:.1%} of revenue)")
    best_margin = max(oc[y] * 1000 / REV[y] for y in range(2020, 2026))
    print(f"  highest owner-cash share of sales in the filed years: {best_margin:.1%}; TTM {ttm_oc*1000/ttm_rev:.1%}")
    g_sales_5 = (REV[2025] / REV[2020]) ** (1 / 5) - 1
    g_sales_4 = (REV[2025] / REV[2021]) ** (1 / 4) - 1
    print(f"  sales growth 2020-2025 CAGR {g_sales_5:.1%}; 2021-2025 {g_sales_4:.1%}")

    print("\nQ7 COMPUTATION, NOT A CLEARANCE")
    dil_m = dil / 1e6
    nc_m = netcash / 1000
    v_ng = avge / RF
    print(f"  range (b): no-growth case alone, all-equity: {v_ng:,.0f}M + net cash {nc_m:,.0f}M ="
          f" {v_ng+nc_m:,.0f}M = ${(v_ng+nc_m)/dil_m:,.2f}/share diluted"
          f" (${(v_ng+nc_m)/(shares/1e6):,.2f} on cover count)")
    v_ng_eq = avg / RF
    print(f"  equity-only beside: {v_ng_eq:,.0f}M = ${v_ng_eq/dil_m:,.2f}/share")
    fair = (avge / FLOOR + nc_m) / dil_m
    fair_eq = (avg / FLOOR) / dil_m
    print(f"  fair price (each end at 10%, averaged; one end): all-equity ${fair:,.2f}; equity-only ${fair_eq:,.2f}")
    print(f"  expected return at the price on the no-growth case: all-equity {avge/(ev/1000):.3%};"
          f" equity-only {avg/(dil*PRICE/1e6):.3%}")

    print("\n  SENSITIVITY (not the convention's range; to test whether ANY case earns the floor at the price)")
    ev_m = ev / 1000
    for label, c0 in (("TTM all-equity", ttm_oce), ("FY2025 all-equity", oce[2025])):
        for g in (0.0, g_sales_4, g_sales_5, 0.40, 0.50):
            v10 = pv_case(c0, g, FLOOR)
            vrf = pv_case(c0, g, RF)
            print(f"   {label:18s} c0 {c0:8.1f} g {g:5.1%}: value at 10% {v10/1000:8.1f}B ({v10/ev_m:5.1%} of EV);"
                  f" at {RF:.2%} {vrf/1000:8.1f}B ({vrf/ev_m:6.1%} of EV)")
    # growth the price requires at 10% on TTM
    lo, hi = 0.0, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if pv_case(ttm_oce, mid, FLOOR) < ev_m:
            lo = mid
        else:
            hi = mid
    print(f"   growth of TTM all-equity owner cash for ten years that the price requires to earn 10%: {lo:.1%}")
    yr10 = ttm_oce * (1 + lo) ** 10
    print(f"   -> year-ten owner cash {yr10/1000:,.1f}B; at the TTM owner-cash share of revenue"
          f" ({ttm_oce*1000/ttm_rev:.1%}) that is revenue of {yr10/(ttm_oce*1000/ttm_rev)/1000:,.0f}B")
    lo, hi = 0.0, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if pv_case(ttm_oce, mid, RF) < ev_m:
            lo = mid
        else:
            hi = mid
    print(f"   same at the sovereign {RF:.2%}: {lo:.1%}")
    # statutory tax beside (21% federal on the pre-tax owner cash proxy) for TTM
    print(f"   statutory-tax variant: TTM all-equity owner cash at 21% federal tax charged in full ="
          f" {ttm_oce*(1-0.21):,.1f}M (the company paid {21686/1000:.1f}M cash tax in FY2025)")
    # dilution history
    print("\nSHARE COUNT (weighted diluted, filed): 2021 1,923.6M; 2025 2,565.2M; Q2 2026 2,568.7M")
    print(f"  diluted growth 2021->2025: {(2565197/1923617)**(1/4)-1:.1%} a year; basic 2021->2025:"
          f" {(2369612/1923617)**(1/4)-1:.1%} a year")


main()
