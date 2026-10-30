# TBTC run 2026-10-25: arithmetic only (Q7 COMPUTATION). Inputs typed from the filings named beside each line.
# Units: USD thousands unless noted. No conclusion is drawn here.
T = 0.25  # company tax on interest income removed for the all-equity basis (run CONVENTION; 2022-2025 effective rates 25.4%, 19.8%, 25.3%, 22.2%)
R = 0.0533  # 30-year Treasury par yield, 10/23/2026 (US Treasury daily par yield curve, via tools/sources.py)
F = 0.10    # floor (Part VII fair-price definition)
SH = 4642.887  # thousand shares, 10-Q cover 0001437749-26-027186 (issued 4,756,734 less treasury 113,847)
PRICE = 5.37   # close 2026-10-23, aggregator (tools/run.py), live quote only
CASH = 8152.589  # cash and equivalents 2026-06-30, 10-Q 0001437749-26-027186; no borrowings; line of credit undrawn
SUBSEQ_DIV = 0.02 * SH  # dividend declared 2026-08-07, stated as a subsequent event in the same 10-Q
NETCASH = CASH - SUBSEQ_DIV

# Per year: NI, non-cash items from the cash-flow statement (stock pay NOT added back; D&A treated as the maintenance guess
# and so netted against maintenance spending), PPP forgiveness removed, interest income removed after tax.
years = [2021, 2022, 2023, 2024, 2025]
NI = {2021: 1710.651, 2022: 1624.453, 2023: 1613.005, 2024: 1576.428, 2025: 1626.620}
INT = {2021: 83.304, 2022: 145.891, 2023: 330.005, 2024: 388.716, 2025: 477.951}
DEFTAX = {2021: -260.0, 2022: 340.0, 2023: 10.0, 2024: 113.0, 2025: 207.0}
PROV = {2021: 0.0, 2022: 87.627 + 1.274, 2023: 46.934, 2024: 5.108, 2025: -0.827}   # credit-loss provision (+ 2022 inventory reserve)
LEASE_NONCASH = {2021: 0.0, 2022: 0.0, 2023: 0.0, 2024: 44.755, 2025: 29.013}
GAIN = {2021: 0.0, 2022: 0.0, 2023: 0.0, 2024: -18.0, 2025: -0.35}
PPP = {2021: -473.4, 2022: 0, 2023: 0, 2024: 0, 2025: 0}
DA = {2021: 22.964, 2022: 7.879, 2023: 1.065, 2024: 21.099, 2025: 41.370}
SBC = {2021: 123.214, 2022: 218.993, 2023: 139.226, 2024: 122.441, 2025: 105.183}
STOCK_SVC = {2021: 0, 2022: 0, 2023: 7.621, 2024: 2.700, 2025: 0}
ACCR_INT = {2021: 0, 2022: 0, 2023: -2.805, 2024: -124.939, 2025: 0}
LOSS_INV = {2021: 57.0, 2022: 0, 2023: 0, 2024: 0, 2025: 0}
OCF = {2021: 2797.644, 2022: -63.878, 2023: 394.940, 2024: 2018.053, 2025: 1806.481}
CAPEX = {2021: 0.0, 2022: 0.0, 2023: 39.422 + 16.691, 2024: 129.075, 2025: 31.114 + 61.989}  # PPE + capitalized software

ocm, allsp, wc, gs = {}, {}, {}, {}
for y in years:
    # owner cash after maintenance only (maintenance spending = D&A), before working-capital change, before interest
    ocm[y] = NI[y] + PPP[y] - INT[y] * (1 - T) + DEFTAX[y] + PROV[y] + LEASE_NONCASH[y] + GAIN[y]
    pre_wc = NI[y] + DA[y] + DEFTAX[y] + PROV[y] + LEASE_NONCASH[y] + GAIN[y] + PPP[y] + SBC[y] + STOCK_SVC[y] + ACCR_INT[y] + LOSS_INV[y]
    wc[y] = OCF[y] - pre_wc                     # cash effect of working capital (negative = absorbed)
    gs[y] = (CAPEX[y] - DA[y]) - wc[y]           # growth spending: capex above D&A plus working capital absorbed
    allsp[y] = ocm[y] - gs[y]
    print(f"{y}: maint-only {ocm[y]:8.1f}  wc {wc[y]:8.1f}  growth spend {gs[y]:8.1f}  all-spending {allsp[y]:8.1f}")
B = sum(ocm.values()) / 5
G = sum(gs.values()) / 5
A = sum(allsp.values()) / 5
print(f"5-yr avg: maintenance-only {B:.1f}; growth spending {G:.1f}; all-spending {A:.1f}")
lit = (ocm[2025] / ocm[2021]) ** 0.25 - 1
h1 = (ocm[2021] + ocm[2022]) / 2; h2 = (ocm[2024] + ocm[2025]) / 2
halves = (h2 / h1) ** (1 / 3) - 1
print(f"growth: literal 2021->2025 {lit:.4f}; halves (21-22 vs 24-25, 3 yrs apart) {halves:.4f}")
a1 = (allsp[2021] + allsp[2022]) / 2; a2 = (allsp[2024] + allsp[2025]) / 2
print(f"all-spending halves {((a2/a1)**(1/3)-1):.4f}")
rev = {2021: 6966.683, 2025: 11048.237}
print(f"sales growth 2021->2025 {(rev[2025]/rev[2021])**0.25-1:.4f}")

def nogrowth(base, r):
    return base / r

def growth(base, gspend, g, r):
    v = 0.0
    for t in range(1, 11):
        v += (base - gspend) * (1 + g) ** t / (1 + r) ** t
    v += base * (1 + g) ** 10 / r / (1 + r) ** 10   # zero growth after year ten, growth spending stops
    return v

def ps(v, net=NETCASH):
    return (v + net) / SH

for label, g in [("CENTRAL (halves)", halves), ("LITERAL window", lit)]:
    ng = nogrowth(B, R); gr = growth(B, G, g, R)
    lo, hi = min(ng, gr), max(ng, gr)
    ng10 = nogrowth(B, F); gr10 = growth(B, G, g, F)
    fair = (ps(ng10) + ps(gr10)) / 2
    print(f"\n{label}: g={g:.4f}")
    print(f"  range (all-equity, at {R}): whole {lo:,.0f} to {hi:,.0f}; per share {ps(lo):.2f} to {ps(hi):.2f}; width {hi/lo:.2f} (whole), {ps(hi)/ps(lo):.2f} (per share)")
    print(f"  at 10%: no-growth {ps(ng10):.2f}; growth {ps(gr10):.2f}; FAIR {fair:.2f}  vs price {PRICE}")
    print(f"  growth spending charged: year 1 {G*(1+g):.1f}, year 10 {G*(1+g)**10:.1f}")
    # equity-only: owner cash after interest (interest income after tax added, held flat), against market value, no cash credit
    ie = sum(INT.values()) / 5 * (1 - T)
    ng10e = (nogrowth(B, F) + ie / F) / SH; gr10e = (growth(B, G, g, F) + ie / F) / SH
    ngRe = (nogrowth(B, R) + ie / R) / SH; grRe = (growth(B, G, g, R) + ie / R) / SH
    print(f"  equity-only: range {min(ngRe,grRe):.2f} to {max(ngRe,grRe):.2f}; at 10% {ng10e:.2f} / {gr10e:.2f}; FAIR {(ng10e+gr10e)/2:.2f} (interest after tax {ie:.1f}/yr held flat)")

# all-spending case beside (no maintenance split), halves growth on the all-spending series
print(f"\nall-spending beside: no-growth {ps(A/R):.2f} at long rate, {ps(A/F):.2f} at 10%")
ev = PRICE * SH - NETCASH
print(f"market value {PRICE*SH:,.0f}; net cash {NETCASH:,.0f}; enterprise value {ev:,.0f}; maint-only yield {B/ev:.4f}; all-spending yield {A/ev:.4f}")
