"""SITE owner cash and Q7 COMPUTATION, NOT A CLEARANCE. Inputs transcribed from the filed cash-flow statements
(FY2023-FY2025 from 10-K 0001650729-26-000005; earlier years from XBRL first-filed vintages, spot-checked against
the filed statements of 10-Ks 0001650729-23-000003 and 0001650729-21-000006). USD millions."""
Y = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
OCF   = [72.9, 16.3, 78.1, 130.8, 229.4, 210.8, 217.2, 297.5, 283.4, 300.5]
SBC   = [4.7, 5.9, 7.9, 11.7, 10.6, 14.3, 18.3, 25.7, 25.0, 27.0]
CAPEX = [8.8, 14.5, 14.9, 19.5, 18.6, 32.5, 27.1, 32.1, 40.5, 53.7]
INTG  = [0.0, 1.5, 5.0, 1.9, 7.2, 4.5, 14.6, 3.9, 4.3, 1.4]      # purchases of intangible assets (software)
PROC  = [0.3, 0.3, 3.5, 1.0, 1.0, 2.2, 2.2, 2.7, 5.9, 9.6]      # proceeds from sale of property and equipment
# fleet acquired on finance leases: ROU assets obtained (2019 on); before 2019 the capital-lease principal paid (proxy, labelled)
FLROU = [4.2, 5.1, 6.2, 15.0, 27.4, 14.2, 26.0, 51.4, 61.3, 38.1]
FLPRN = [4.2, 5.1, 6.2, 6.5, 8.5, 10.4, 12.6, 18.5, 26.7, 32.5]  # finance-lease principal paid
INTP  = [16.5, 23.9, 26.2, 30.3, 27.3, 15.6, 15.5, 26.8, 29.8, 34.7]  # cash interest paid
TAX   = [21.3, 18.0, 1.3, 13.8, 27.5, 56.1, 67.7, 49.8, 36.0, 45.7]
NI    = [30.6, 54.6, 73.9, 77.7, 121.3, 238.4, 245.4, 173.4, 124.4, 157.4]  # 2024-25 incl. NCI (filed Net income)
ACQ   = [66.4, 82.9, 147.7, 71.5, 159.4, 147.2, 244.9, 192.7, 138.2, 37.9]
CONT  = [0.0, 0.0, 4.0, 3.0, 4.8, 8.6, 10.0, 8.0, 5.6, 3.8]       # contingent consideration paid (financing); 2016-17 not read
SALES = [1648.2, 1861.7, 2112.3, 2357.5, 2704.5, 3475.7, 4014.5, 4301.2, 4540.6, 4704.8]
DEPR  = [None]*7 + [64.1, 75.3, 80.7]   # depreciation incl. finance-lease ROU amortization (filed CF line)
SWAM  = [None]*7 + [1.0, 2.7, 4.5]      # software amortization = 'software and intangible' line less AmortizationOfIntangibleAssets
rows = []
for i, y in enumerate(Y):
    t = TAX[i] / (NI[i] + TAX[i])
    eq_only = OCF[i] - SBC[i] - CAPEX[i] - INTG[i] + PROC[i] - FLPRN[i]
    all_eq = OCF[i] + INTP[i] * (1 - t) - SBC[i] - CAPEX[i] - INTG[i] + PROC[i] - FLROU[i]
    rows.append((y, t, eq_only, all_eq, ACQ[i] + CONT[i]))
    dep = '' if DEPR[i] is None else f"  D&A-basis eq-only {OCF[i]-SBC[i]-DEPR[i]-SWAM[i]:6.1f}"
    print(f"{y}  t={t:5.1%}  owner cash equity-only {eq_only:6.1f}  all-equity {all_eq:6.1f}  purchases {ACQ[i]+CONT[i]:6.1f}  OC/sales {all_eq/SALES[i]:5.1%}{dep}")
W = [r for r in rows if 2021 <= r[0] <= 2025]
avg = lambda xs: sum(xs) / len(xs)
B_all = avg([r[3] for r in W]); B_eq = avg([r[2] for r in W])
purch = sum(r[4] for r in W); before = sum(r[3] for r in W)
print(f"\nwindow FY2021-FY2025: avg all-equity {B_all:.1f}  avg equity-only {B_eq:.1f}")
print(f"net purchases {purch:.1f} vs owner cash before purchases {before:.1f}: ratio {purch/before:.2f} (serial acquirer if > 0.5)")
# growth
org = [0.11, 0.00, -0.01, 0.01]  # filer's Organic Daily Sales growth FY2022..FY2025
g_org = 1.0
for x in org: g_org *= (1 + x)
g_org = g_org ** 0.25 - 1
g_tot_all = (W[-1][3] / W[0][3]) ** 0.25 - 1
g_sales = (SALES[-1] / SALES[5]) ** 0.25 - 1
print(f"organic growth (filer ODS, FY2022-25) {g_org:.2%}; total growth of all-equity owner cash 2021->2025 {g_tot_all:.2%}; sales growth {g_sales:.2%}")
def value(B, g, r, yrs=10):
    v = sum(B * (1 + g) ** t / (1 + r) ** t for t in range(1, yrs + 1))
    v += B * (1 + g) ** yrs / r / (1 + r) ** yrs
    return v
def irr(B, g, price):
    lo, hi = 0.001, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(B, g, mid) > price: lo = mid
        else: hi = mid
    return mid
SOV = 0.056; FLOOR = 0.10
SH = 43.655390; PX = 87.99
ND = 505.7 + 137.3 - 87.4 + 10.0   # June 28 2026 debt + finance leases - cash, plus the July buyback the 10-Q states
MCAP = SH * PX; EV = MCAP + ND
print(f"\nshares {SH}M price {PX} mcap {MCAP:.1f} net debt {ND:.1f} EV {EV:.1f}")
def case(label, B, glo, ghi, base_cost, nd):
    lo, hi = value(B, glo, SOV), value(B, ghi, SOV)
    plo, phi = (lo - nd) / SH, (hi - nd) / SH
    r_lo, r_hi = irr(B, glo, base_cost), irr(B, ghi, base_cost)
    f_lo, f_hi = value(B, glo, FLOOR), value(B, ghi, FLOOR)
    fair = ((f_lo + f_hi) / 2 - nd) / SH
    print(f"{label}: B {B:.1f} g {glo:.2%}/{ghi:.2%}  value {lo:.0f}..{hi:.0f}  per share {plo:.2f}..{phi:.2f} (width {phi/plo if plo>0 else float('nan'):.2f}x)  "
          f"expected return at price {r_lo:.2%}/{r_hi:.2%}  fair {fair:.2f}")
    return plo, phi, fair
print("\nCENTRAL (all-equity, organic pair: purchases left out, filer's organic growth):")
c = case("all-equity organic", B_all, 0.0, g_org, EV, ND)
print("BESIDE (equity-only, organic pair):")
case("equity-only organic", B_eq, 0.0, g_org, MCAP, 0.0)
# default pair: acquisitions deducted, total growth credited (capped at sales growth per (f) if absurd)
B_def = avg([r[3] - r[4] for r in W])
print(f"BESIDE (all-equity, default pair: purchases deducted, avg {B_def:.1f}, total growth {g_tot_all:.2%}):")
case("all-equity default", B_def, 0.0, g_tot_all, EV, ND)
print("BESIDE (literal window = same five years; FY2025 single year for scale):")
case("all-equity organic on FY2025 alone", W[-1][3], 0.0, g_org, EV, ND)
nd_dec = 381.5 + 3.9 + 134.8 - 190.6
print(f"BESIDE (net debt at the Dec 28 2025 year-end, {nd_dec:.1f}, the seasonal low):")
case("all-equity organic, Dec net debt", B_all, 0.0, g_org, MCAP + nd_dec, nd_dec)
