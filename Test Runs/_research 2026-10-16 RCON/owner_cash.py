"""Owner cash after every real cost, RMB, transcribed from the filed cash-flow statements (20-F FY2020, FY2023, FY2026
and XBRL for FY2016-FY2017). owner cash = CFO - PP&E - construction in progress - land use rights - investments in
unconsolidated entities - share pay (CFO adds share pay back; it is a real cost). Loans to third parties are a financial
asset, not capital spending, and are shown separately. Arithmetic only; COMPUTATION, NOT A CLEARANCE."""
# year: (CFO, PPE, CIP, land, unconsol_inv, SBC, interest_paid_guess, loans_net_out)
Y = {
2016: (-285_674, 181_075, 0, 0, 0, 2_096_162, 0, 0),
2017: (-7_381_551, 638_119, 0, 0, 0, 2_039_446, 0, 0),
2018: (-19_569_820, 1_503_410-32_000, 9_157_103, 1_361_969, 4_037_736, 14_621_838+3_050_896, 0, 1_960_000-435_250),
2019: (-32_212_172, 1_735_956, 4_606_823, 0, 4_205_080, 21_288_204+845_781, 0, 4_000_000-1_000_000),
2020: (-5_230_676, 85_974-900, 3_782_912, 0, 0, 7_944_835+33_927, 0, 9_480_000-11_239_623),
2021: (-34_050_468, 522_416, 0, 0, 0, 6_140_037, 0, 51_638_458-5_150_377),
2022: (-26_247_237, 692_206, 0, 0, 0, 39_263_485+8_935_919, 0, 171_071_510-171_435_032),
2023: (-51_688_331, 940_673-31_950, 0, 0, 0, 26_191_707+5_805_840, 0, 103_146_761-40_113_311),
2024: (-43_747_933, 282_184-20_000, 219_132, 15_000_251, 0, 22_427_682+1_070_143, 332_881+648_581+34_375, 196_437_504-117_522_129),
2025: (-33_771_174, 1_010_812-2_000, 8_924_101, 0, 0, 10_279_881, 343_159+349_792+380_208, 140_490_800-100_478_982),
2026: (-58_801_965, 307_295-3_580, 52_653_099, 0, 700_000, 12_687_016, 312_841+731_042, 166_200_000-96_417_165),
}
FX = 6.7851  # RMB per USD, the filer's convenience rate at 2026-06-30 (20-F FY2026, Note 2)
r_sov = 0.0207  # MoF China government bond yield curve, 30-year, 2026-10-15
oc, ocm = {}, {}
print("FY   CFO      capex(all)  SBC     owner cash  maint-only*  loans out (net)   [RMB m]")
for y, (cfo, ppe, cip, land, inv, sbc, intr, loans) in Y.items():
    capall = ppe + cip + land + inv
    oc[y] = cfo - capall - sbc
    ocm[y] = cfo - ppe - sbc            # *maintenance-only: growth spending (plant, land, investees) left out
    print(f"{y} {cfo/1e6:8.2f} {capall/1e6:9.2f} {sbc/1e6:8.2f} {oc[y]/1e6:10.2f} {ocm[y]/1e6:11.2f} {loans/1e6:12.2f}")
w = range(2022, 2027)
avg = sum(oc[y] for y in w) / 5; avgm = sum(ocm[y] for y in w) / 5
intr_avg = sum(Y[y][6] for y in (2024, 2025, 2026)) / 3
print(f"5-yr avg owner cash FY2022-26 (equity-only, after interest): {avg/1e6:.2f}m; maintenance-only: {avgm/1e6:.2f}m")
print(f"all-equity: add back interest paid (avg FY2024-26 {intr_avg/1e6:.2f}m; company pays ~no tax): {(avg+intr_avg)/1e6:.2f}m")
print(f"Sign: every year FY2016-FY2026 negative: {all(v < 0 for v in oc.values())}; maintenance-only negative every year: {all(v < 0 for v in ocm.values())}")
# Net debt at 2026-06-30 (borrowings less cash and securities), plus the ATM proceeds the 20-F states as a subsequent event
cash, rcash, sti = 29_745_574, 104, 9_005_007
debt = 11_306_258 + 20_033_917
atm = 8_732_665 * FX
net_cash = cash + rcash + sti - debt + atm
sh = 2_195_938 + 20_000_000 / 3600   # Class A at the 20-F date + Class B at 1/3,600 of a Class A
price = 1.05
mcap = sh * price
print(f"net cash incl. ATM gross: {net_cash/1e6:.2f}m RMB = ${net_cash/FX/1e6:.2f}m; shares (A-equivalent) {sh:,.0f}; mcap ${mcap/1e6:.3f}m")
for basis, cash_flow in (("all-equity", avg + intr_avg), ("maintenance-only all-equity", avgm + intr_avg), ("equity-only", avg), ("maintenance-only equity-only", avgm)):
    v_sov = cash_flow / r_sov            # no growth after year ten and none before: a flat perpetuity at the sovereign
    v_10 = cash_flow / 0.10
    adj = net_cash if "equity-only" not in basis else (cash + rcash + sti + atm)  # equity-only: market value against owner cash after interest; debt already charged via interest
    if "equity-only" in basis: adj = net_cash  # the equity's claim still nets the borrowings; shown on the same net-cash line
    ps_sov = (v_sov + adj) / sh / FX; ps_10 = (v_10 + adj) / sh / FX
    print(f"{basis:28s} value at 2.07%: {v_sov/1e6:9.1f}m RMB -> ${ps_sov:9.2f}/share | at 10% (fair-price leg): {v_10/1e6:8.1f}m -> ${ps_10:8.2f}/share")
# Floor test: expected return at the price, owner cash yield on enterprise value
ev_usd = mcap - net_cash / FX
print(f"EV at price: ${ev_usd/1e6:.2f}m (negative = market cap below net cash); owner-cash yield on price: {(avg+intr_avg)/FX/mcap*100:.0f}% (negative)")
print(f"loans to third parties 2026-06-30: 330.0m RMB = ${330_043_282/FX/1e6:.1f}m = ${330_043_282/FX/sh:.2f}/share (not counted: not cash or securities)")
