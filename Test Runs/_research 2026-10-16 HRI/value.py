"""HRI owner cash and the Q7 COMPUTATION (arithmetic only; every input transcribed from the filed cash-flow
statements: FY2022 10-K 0001364479-23-000006 for 2021-2022, FY2025 10-K 0001364479-26-000050 for 2023-2025;
balance sheet and debt table from the 10-Q for 2026-06-30, 0001364479-26-000109)."""
YRS = [2021, 2022, 2023, 2024, 2025]
OCF   = [744.0, 916.7, 1086, 1225, 1085]
SBC   = [23.3, 27.1, 18, 17, 34]
RCAP  = [593.8, 1168.5, 1320, 1048, 1097]   # rental equipment expenditures
RPRO  = [106.9, 121.1, 325, 288, 448]       # proceeds from disposal of rental equipment
NCAP  = [48.0, 103.7, 156, 161, 157]        # non-rental capital expenditures
NPRO  = [4.6, 7.5, 15, 10, 20]              # proceeds from disposal of property and equipment
FLP   = [12.9, 14.9, 16, 19, 22]            # principal payments under finance lease and financing obligations
RDEP  = [420.7, 535.9, 643, 679, 856]       # depreciation of rental equipment
PDEP  = [55.6, 63.5, 71, 82, 109]           # depreciation of property and equipment
GAIN  = [19.8, 36.9, 94, 87, 91]            # gain on sale of rental equipment (removed from OCF)
INT   = [82.7, 114.1, 221, 258, 419]        # cash paid for interest
ACQ   = [431.0, 515.2, 430, 600, 4257]      # acquisitions, net of cash acquired
DIV   = [0, 0, 0, 0, 99]                    # proceeds from disposal of business (2025)
T = 0.21   # CONVENTION of this run: interest added back at the federal statutory rate (the larger add-back)
SH = 33.431444; PRICE = 121.28; SOV = 0.0543
NETDEBT = 7912 + 93 + 5 - 43   # total debt incl. finance leases (carrying) + financing obligations (long-term 93, current 5) - cash
EV = SH * PRICE + NETDEBT

def avg(x): return sum(x) / len(x)
A_eq = [o - s - rc + rp - nc + np_ - f for o, s, rc, rp, nc, np_, f in zip(OCF, SBC, RCAP, RPRO, NCAP, NPRO, FLP)]
M_eq = [o - s - rd - pd + g - f for o, s, rd, pd, g, f in zip(OCF, SBC, RDEP, PDEP, GAIN, FLP)]
ia = [i * (1 - T) for i in INT]
A_ae = [a + i for a, i in zip(A_eq, ia)]; M_ae = [m + i for m, i in zip(M_eq, ia)]
print("year  A_eq   M_eq   A_allequity  M_allequity  acquisitions")
for y, a, m, aa, ma, q in zip(YRS, A_eq, M_eq, A_ae, M_ae, ACQ):
    print(f"{y} {a:7.1f} {m:7.1f} {aa:10.1f} {ma:11.1f} {q:10.1f}")
print(f"avg  {avg(A_eq):7.1f} {avg(M_eq):7.1f} {avg(A_ae):10.1f} {avg(M_ae):11.1f} {avg(ACQ):10.1f}")
netbuy = sum(ACQ) - sum(DIV)
print(f"net purchases over window {netbuy:.0f}; half of all-equity owner cash before purchases {sum(A_ae)/2:.0f} -> serial acquirer: {netbuy > sum(A_ae)/2}")
print(f"market cap {SH*PRICE:.1f}  net debt {NETDEBT:.1f}  EV {EV:.1f}")

def pv(base, g, r, years=10):
    """cash grows at g for ten years, then zero nominal growth for ever; discounted at r"""
    tot, c = 0.0, base
    for t in range(1, years + 1):
        c *= (1 + g); tot += c / (1 + r) ** t
    return tot + (c / r) / (1 + r) ** years

def halves(x):
    a, b = avg(x[:2]), avg(x[-2:]); return (b / a) ** (1 / 3) - 1 if a > 0 and b > 0 else None
print("growth between halves (first two vs last two years, three years apart):",
      {k: (round(v * 100, 1) if v is not None else None) for k, v in
       [("A_ae", halves(A_ae)), ("M_ae", halves(M_ae)), ("A_eq", halves(A_eq)), ("M_eq", halves(M_eq))]})
sales = [2073.1, 2738.8, 3282, 3568, 4376]
print(f"sales growth 2021-2025 {((sales[-1]/sales[0])**0.25-1)*100:.1f}% (includes acquisitions)")
G_ORG = -0.06   # the filer's one organic figure: pro forma equipment rental revenue, 2025, -6% (FY2025 10-K, MD&A)

def per_share(ev_value, basis="ae"):
    return (ev_value - NETDEBT) / SH if basis == "ae" else ev_value / SH

print("\nVALUE RANGE (COMPUTATION), discounted at the sovereign", SOV)
cases = {
 "central: organic pair, maintenance-only (M), all-equity": (avg(M_ae), "ae"),
 "beside: organic pair, all spending (A), all-equity": (avg(A_ae), "ae"),
 "beside: organic pair, maintenance-only (M), equity-only": (avg(M_eq), "eq"),
 "beside: organic pair, all spending (A), equity-only": (avg(A_eq), "eq"),
}
for name, (base, b) in cases.items():
    top = pv(base, 0.0, SOV); bot = pv(base, G_ORG, SOV)
    print(f"{name}: base {base:.1f}; no growth {per_share(top,b):8.2f}; -6% {per_share(bot,b):8.2f} a share")
dflt = avg(A_ae) - (netbuy / 5)
print(f"default pair (acquisitions deducted, total growth credited): owner cash after purchases {dflt:.1f} a year, negative, no positive value on any growth")
print("\nFLOOR TEST at the price: owner cash / what is paid")
for name, (base, b) in cases.items():
    paid = EV if b == "ae" else SH * PRICE
    print(f"{name}: {base/paid*100:.2f}% on {paid:.0f}")
# growth needed for the central case to earn 10% at the price: solve pv(base,g,0.10)=EV
lo, hi = -0.5, 1.0
for _ in range(100):
    mid = (lo + hi) / 2
    if pv(avg(M_ae), mid, 0.10) < EV: lo = mid
    else: hi = mid
print(f"growth for ten years (then flat) the central base would need to earn 10% at the price: {mid*100:.1f}% a year")
print("\nFAIR PRICE (Part VII: each end case valued at 10%, the two averaged)")
for name, (base, b) in cases.items():
    top = pv(base, 0.0, 0.10); bot = pv(base, G_ORG, 0.10)
    print(f"{name}: top {per_share(top,b):8.2f} bottom {per_share(bot,b):8.2f} fair {per_share((top+bot)/2,b):8.2f}")
