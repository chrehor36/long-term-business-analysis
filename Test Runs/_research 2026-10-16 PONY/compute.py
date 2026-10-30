# PONY owner cash and the Q7 COMPUTATION (USD millions). Inputs transcribed from the filed statements:
# FY2023-FY2025 20-F 0001104659-26-046406; FY2022 from FY2024 20-F 0001410578-25-000895; H1 2026 from 6-K 0001104659-26-098113.
yrs = [2022, 2023, 2024, 2025]
ocf   = {2022: -154.768, 2023: -115.421, 2024: -110.758, 2025: -164.955}
sbc   = {2022: 13.184, 2023: 3.254, 2024: 127.003, 2025: 30.798}   # cash-flow statement add-back
capex = {2022: 12.033, 2023: 5.091, 2024: 11.397, 2025: 43.875}
flp   = {2022: 0.853, 2023: 1.061, 2024: 1.015, 2025: 0.971}       # finance-lease principal
dnci  = {2022: 0.0, 2023: 0.0, 2024: 0.0, 2025: 6.435}             # dividends to a minority holder
invi  = {2022: 8.890, 2023: 19.389, 2024: 20.378, 2025: 42.985}    # investment income (P&L)
rlz   = {2022: -0.107, 2023: 2.993, 2024: 5.697, 2025: 20.313}     # realized gains, removed from OCF as non-cash
dep   = {2022: 16.770, 2023: 14.342, 2024: 8.361, 2025: 6.220}
rev   = {2022: 68.386, 2023: 71.899, 2024: 75.025, 2025: 90.001}
ipo_sbc_2024 = 98.8 + 21.9   # SBC recognized on vesting at the IPO, 20-F Item 5

eo, ae, eo_dep = {}, {}, {}
print("year   OCF     SBC    capex  FLprin  dNCI   EO(all spend)  interest   AE(before int)  EO(D&A basis)")
for y in yrs:
    eo[y] = ocf[y] - sbc[y] - capex[y] - flp[y] - dnci[y]
    intr = invi[y] - rlz[y]
    ae[y] = eo[y] - intr
    eo_dep[y] = ocf[y] - sbc[y] - dep[y] - flp[y] - dnci[y]
    print(f"{y} {ocf[y]:8.1f} {sbc[y]:7.1f} {capex[y]:7.1f} {flp[y]:6.1f} {dnci[y]:6.1f} {eo[y]:12.1f} {intr:10.1f} {ae[y]:14.1f} {eo_dep[y]:12.1f}")
m = lambda d: sum(d[y] for y in yrs) / len(yrs)
EO, AE, EOD = m(eo), m(ae), m(eo_dep)
print(f"4-yr mean: EO {EO:.1f}  AE {AE:.1f}  EO D&A basis {EOD:.1f}")
eo_x = dict(eo); eo_x[2024] += ipo_sbc_2024
ae_x = dict(ae); ae_x[2024] += ipo_sbc_2024
print(f"beside, 2024 without the IPO catch-up of {ipo_sbc_2024:.1f}: EO mean {m(eo_x):.1f}  AE mean {m(ae_x):.1f}")
h1 = (2022, 2023); h2 = (2024, 2025)
a1 = sum(ae[y] for y in h1)/2; a2 = sum(ae[y] for y in h2)/2
print(f"AE halves: {a1:.1f} -> {a2:.1f} (losses widening)")
salesg = (rev[2025]/rev[2022])**(1/3) - 1
print(f"sales growth 2022-2025 compound: {salesg*100:.1f}%")
# H1 2026 and TTM
print("H1 2026: OCF -118.215, capex -44.618, SBC 13.618 -> EO", round(-118.215-13.618-44.618,1),
      "; H1 2025: OCF -79.570, capex -14.464, SBC 16.217 -> EO", round(-79.570-16.217-14.464,1))
ttm = eo[2025] - (-79.570-16.217-14.464) + (-118.215-13.618-44.618)
print(f"TTM to 2026-06-30 EO (approx, FL and dNCI as FY2025): {ttm:.1f}")

shares = 354.095390 + 81.088770     # HKEX monthly return to 2026-09-30, 6-K 0001104659-26-114347
price = 4.93
cash_sec = 1390.5                   # cash, ST investments, restricted cash, LT debt instruments, 2026-06-30 (6-K 0001104659-26-098113)
debt = 0.0
netcash = cash_sec - debt
mcap = price * shares
print(f"shares {shares:.3f}M  mcap {mcap:.1f}  net cash {netcash:.1f}  EV {mcap-netcash:.1f}")

def pv(cf0, g, r, n=10):
    v = 0.0; c = cf0
    for t in range(1, n+1):
        c = c * (1+g); v += c / (1+r)**t
    term = c / r / (1+r)**n          # zero nominal growth after year ten
    return v + term
for label, r in (("CNY 30y sovereign 2.06%", 0.0206), ("USD 30y Treasury 5.43% (beside)", 0.0543), ("floor 10%", 0.10)):
    nog = pv(AE, 0.0, r); det = pv(AE, salesg, r)
    print(f"{label}: AE no-growth whole {nog:,.0f} -> per share {(nog+netcash)/shares:.2f};  deterioration at sales growth {det:,.0f} -> {(det+netcash)/shares:.2f}")
    nge = pv(EO, 0.0, r); dte = pv(EO, salesg, r)
    print(f"   equity-only EO: no-growth {nge/shares:.2f}  deterioration {dte/shares:.2f} per share")
# fair price (Part VII): each end case valued at 10%, averaged; all-equity less net debt; equity-only beside
ends_ae = [(pv(AE, 0.0, 0.10)+netcash)/shares, (pv(AE, salesg, 0.10)+netcash)/shares]
ends_eo = [pv(EO, 0.0, 0.10)/shares, pv(EO, salesg, 0.10)/shares]
print("fair price, no-growth case alone (range is the no-growth case alone by (b)): AE", round(ends_ae[0],2), " EO", round(ends_eo[0],2))
print("fair price if the deterioration end were admitted as the bottom: AE", round(sum(ends_ae)/2,2), " EO", round(sum(ends_eo)/2,2))
print(f"price {price} ; net cash per share {netcash/shares:.2f}")
