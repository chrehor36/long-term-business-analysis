# ENIC run 2026-10-23: the arithmetic behind the run file. Arithmetic only; no judgment is made here.
# Every input is transcribed from the filed statements named beside it (accession numbers in the run file).
# CLP years (2016-2022) are translated at the Banco Central de Chile annual average dolar observado
# (flows) and the year-end rate printed in the 20-F (stocks); 2023-2025 are the company's own US$ figures
# (2025 20-F, which restated 2023 and 2024 into US$ under IAS 21 at average rates).

AVG = {2016: 676.83, 2017: 649.33, 2018: 640.29, 2019: 702.63, 2020: 792.22, 2021: 759.27, 2022: 872.33}  # BCCh, fetched 2026-10-23
YE = {2016: 669.47, 2017: 614.75, 2018: 694.77, 2019: 748.74, 2020: 710.95, 2021: 844.69, 2022: 855.86}  # 20-F tables

# Cash flow lines. CLP years in Ch$ billions, USD years in US$ millions.
# ocf, ppe, intang, lease (payments on borrowings and lease liabilities), int_paid, int_rec, nci_div (declared, equity statement),
# da (depreciation and amortization, excl. impairment), rev (revenues and other operating income), ebit (operating income as filed)
CLP = {
    2019: dict(ocf=743.712, ppe=300.346, intang=20.732, lease=4.498, int_paid=134.430, int_rec=6.034, nci_div=16.578, da=236.627, rev=2770.834, ebit=526.055),
    2020: dict(ocf=755.866, ppe=514.807, intang=39.507, lease=4.941, int_paid=139.251, int_rec=5.671, nci_div=18.163, da=229.957, rev=2585.402, ebit=-34.255),
    2021: dict(ocf=412.893, ppe=748.013, intang=38.059, lease=6.061, int_paid=142.891, int_rec=3.297, nci_div=21.783, da=210.928, rev=2855.230, ebit=259.594),
    2022: dict(ocf=744.779, ppe=915.693, intang=21.869, lease=6.613, int_paid=186.962, int_rec=20.152, nci_div=23.365, da=238.273, rev=4956.432, ebit=912.357),
}
USD = {
    2023: dict(ocf=840.165, ppe=758.168, intang=30.517, lease=21.929, int_paid=229.992, int_rec=41.179, nci_div=24.988, da=301.699, rev=5215.138, ebit=914.098),
    2024: dict(ocf=1622.170, ppe=724.780, intang=40.637, lease=18.956, int_paid=217.723, int_rec=22.013, nci_div=36.639, da=313.083, rev=4224.825, ebit=395.299),
    2025: dict(ocf=1319.678, ppe=462.284, intang=36.824, lease=36.535, int_paid=174.336, int_rec=12.322, nci_div=43.284, da=387.430, rev=4662.730, ebit=1011.339),
}
# Income tax paid on divestiture gains, inside operating cash, added back because the proceeds are left out
# (2025 20-F, Item 5.B: US$280M in 2023 on the Enel Transmision gain; US$74M in 2024 on the Arcadia gain).
DIVEST_TAX = {2023: 280.0, 2024: 74.0}

rows = {}
for y, d in CLP.items():
    rows[y] = {k: v * 1000 / AVG[y] for k, v in d.items()}  # Ch$ bn -> US$ M
for y, d in USD.items():
    rows[y] = dict(d)

def oc(y, maint=False, equity_only=False):
    r = rows[y]
    capex = r['da'] if maint else (r['ppe'] + r['intang'])
    x = r['ocf'] - capex - r['lease'] - r['nci_div'] + DIVEST_TAX.get(y, 0.0)
    if equity_only:
        x -= (r['int_paid'] - r['int_rec'])
    return x

print("year  OCF   capex   D&A  allspend_AE  maint_AE  allspend_EO  maint_EO  revenue  EBIT")
for y in sorted(rows):
    r = rows[y]
    print(f"{y} {r['ocf']:7.1f} {r['ppe']+r['intang']:7.1f} {r['da']:6.1f} {oc(y):10.1f} {oc(y,True):9.1f} {oc(y,False,True):10.1f} {oc(y,True,True):9.1f} {r['rev']:8.1f} {r['ebit']:7.1f}")

def avg(ys, **k):
    return sum(oc(y, **k) for y in ys) / len(ys)

W = [2021, 2022, 2023, 2024, 2025]      # literal five-year window
C = [2019, 2020, 2021, 2022, 2023, 2024]  # cycle, peak (2019) to peak (2024), CONVENTION of the run
print()
for name, ys in (("window 2021-25", W), ("cycle 2019-24", C)):
    print(f"{name}: all-spend AE {avg(ys):.1f}  maint AE {avg(ys, maint=True):.1f}  all-spend EO {avg(ys, equity_only=True):.1f}  maint EO {avg(ys, maint=True, equity_only=True):.1f}")

# Growth: maintenance-only owner cash, first to last year of the cycle, then the cap of specific (f)
g_shown = (oc(2024, True) / oc(2019, True)) ** (1 / 5) - 1
share_max = max(oc(y, True) / rows[y]['rev'] for y in rows)
g_sales = (rows[2024]['rev'] / rows[2019]['rev']) ** (1 / 5) - 1
base = avg(C, maint=True)
print(f"\nshown growth 2019->2024 (maint AE): {g_shown:.2%}; owner cash in yr10 at that rate {base*(1+g_shown)**10:.0f} vs sales ~{rows[2025]['rev']:.0f}; highest share of sales earned {share_max:.1%}")
print(f"sales growth 2019->2024: {g_sales:.2%}")

def pv(c0, g, r, n=10):
    v, c = 0.0, c0
    for t in range(1, n + 1):
        c *= (1 + g)
        v += c / (1 + r) ** t
    return v + (c / r) / (1 + r) ** n  # zero nominal growth after year ten

RF = 0.0529     # US Treasury 30-year par yield, 2026-10-22
FLOOR = 0.10
SHARES = 69_166_557_219
ADS = 50
PRICE_ADS = 4.34
ND = 3785.0 - 276.0   # gross financial debt (incl. leases) less cash, 2026-06-30, Q2 2026 6-K
mcap = SHARES / ADS * PRICE_ADS / 1e6
print(f"\nmarket cap US$M {mcap:.1f}; net debt {ND:.1f}; EV {mcap+ND:.1f}")

def per(eq_m):
    s = eq_m * 1e6 / SHARES
    return s, s * ADS

for label, b in (("cycle maint AE (central)", avg(C, maint=True)), ("window maint AE", avg(W, maint=True)),
                 ("cycle all-spend AE", avg(C)), ("window all-spend AE", avg(W))):
    lo = pv(b, 0.0, RF); hi = pv(b, g_sales, RF)
    flo = pv(b, 0.0, FLOOR); fhi = pv(b, g_sales, FLOOR)
    fair = (flo + fhi) / 2
    print(f"{label}: base {b:.1f}; EV range {lo:.0f}-{hi:.0f}; equity {lo-ND:.0f}-{hi-ND:.0f}; per ADS {per(lo-ND)[1]:.2f}-{per(hi-ND)[1]:.2f}; "
          f"fair EV {fair:.0f}; fair equity {fair-ND:.0f}; fair per share {per(fair-ND)[0]:.5f} per ADS {per(fair-ND)[1]:.2f}")

# Equity-only beside: owner cash after net interest, against the market value of the shares
for label, b in (("cycle maint EO", avg(C, maint=True, equity_only=True)), ("cycle all-spend EO", avg(C, equity_only=True))):
    lo = pv(b, 0.0, RF); hi = pv(b, g_sales, RF)
    fair = (pv(b, 0.0, FLOOR) + pv(b, g_sales, FLOOR)) / 2
    print(f"{label}: base {b:.1f}; equity range {lo:.0f}-{hi:.0f}; per ADS {per(lo)[1]:.2f}-{per(hi)[1]:.2f}; fair equity {fair:.0f}; per share {per(fair)[0]:.5f}; per ADS {per(fair)[1]:.2f}")

# Expected return at the price (all-equity, central base): solve r with pv(base, g, r) = EV
def irr(b, g, target):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        m = (lo + hi) / 2
        if pv(b, g, m) > target: lo = m
        else: hi = m
    return m
b = avg(C, maint=True)
print(f"\nexpected return at the price, central base: no growth {irr(b,0.0,mcap+ND):.2%}; growth case {irr(b,g_sales,mcap+ND):.2%}")
bw = avg(W, maint=True)
print(f"expected return at the price, window maint base: no growth {irr(bw,0.0,mcap+ND):.2%}; growth case {irr(bw,g_sales,mcap+ND):.2%}")

# Returns on capital employed, after a 27% statutory Chilean rate on operating income (CONVENTION of the run)
CE = {  # total equity + net debt (borrowings, leases, Enel Finance International loans, less cash), US$M
    2019: (3747.284 + 208.815 + 1692.604 + 5.842 + 47.566 + 784.373 - 235.685) * 1000 / YE[2019],
    2020: (3594.274 + 157.499 + 1483.589 + 7.008 + 44.858 + 1164.044 - 332.036) * 1000 / YE[2020],
    2021: (3346.493 + 88.340 + 1941.874 + 11.105 + 148.557 + 1300.059 - 309.975) * 1000 / YE[2021],
    2022: (4388.939 + 68.520 + 2183.803 + 19.021 + 216.665 + 1147.097 - 875.214) * 1000 / YE[2022],
    2023: 5427.862 + 701.175 + 2171.325 + 27.520 + 278.097 + 1179.760 - 642.206 - 77.226,
    2024: 5345.302 + 84.003 + 2382.396 + 26.982 + 268.670 + 1019.514 + 167.097 - 384.761 - 19.588,
    2025: 5549.507 + 322.082 + 2170.328 + 41.518 + 368.679 + 861.531 + 167.101 - 461.924 - 0.982,
}
UNDERLYING = {2020: 713.0 * 1000 / AVG[2020], 2024: 657.0}  # Bocamina II impairment (Ch$ bn, D&A+impairment less D&A); 2024 hedge-discontinuation loss
print("\nyear  CE  EBIT  EBIT-after-27%/CE  underlying")
for y in sorted(CE):
    e = rows[y]['ebit']; u = e + UNDERLYING.get(y, 0.0)
    print(f"{y} {CE[y]:7.0f} {e:7.0f} {e*0.73/CE[y]:7.1%} {u*0.73/CE[y]:7.1%}")

# Specific (e): the growth case charges the growth spending (capital spending above the maintenance guess, cycle average)
# against the growth it buys, for the ten years of growth; it stops when growth stops.
gs = sum(rows[y]['ppe'] + rows[y]['intang'] - rows[y]['da'] for y in C) / len(C)
def annuity(r, n=10): return (1 - (1 + r) ** -n) / r
print(f"\ngrowth spending, cycle average (capex less D&A): {gs:.1f}")
for label, b, nd in (("AE central", avg(C, maint=True), ND), ("EO beside", avg(C, maint=True, equity_only=True), 0.0)):
    top_rf = pv(b, 0.0, RF); gro_rf = pv(b, g_sales, RF) - gs * annuity(RF)
    top_f = pv(b, 0.0, FLOOR); gro_f = pv(b, g_sales, FLOOR) - gs * annuity(FLOOR)
    fair = (top_f + gro_f) / 2
    print(f"{label}: growth worth {pv(b,g_sales,RF)-top_rf:.0f} vs its cost {gs*annuity(RF):.0f} at the sovereign; "
          f"range (inverted) bottom {gro_rf:.0f} top {top_rf:.0f} -> equity {gro_rf-nd:.0f} to {top_rf-nd:.0f}; per share {per(gro_rf-nd)[0]:.4f}-{per(top_rf-nd)[0]:.4f}; per ADS {per(gro_rf-nd)[1]:.2f}-{per(top_rf-nd)[1]:.2f}; "
          f"width {(top_rf-nd)/(gro_rf-nd):.2f}x; at 10%: top {top_f:.0f} growth {gro_f:.0f}; fair {fair:.0f} -> equity {fair-nd:.0f}; per share {per(fair-nd)[0]:.5f}; per ADS {per(fair-nd)[1]:.2f}")
    print(f"   expected return at the price: top case {irr(b,0.0,mcap+nd if nd else mcap):.2%}")

# Beside: the literal window 2021-2025 on the same (e) construction, and the cycle drawn from 2018 (sensitivity)
gsW = sum(rows[y]['ppe'] + rows[y]['intang'] - rows[y]['da'] for y in W) / len(W)
b = avg(W, maint=True)
top_rf = pv(b, 0.0, RF); gro_rf = pv(b, g_sales, RF) - gsW * annuity(RF)
fair = (pv(b, 0.0, FLOOR) + pv(b, g_sales, FLOOR) - gsW * annuity(FLOOR)) / 2
print(f"\nwindow 2021-25 (e): growth spending {gsW:.1f}; range equity {gro_rf-ND:.0f} to {top_rf-ND:.0f}; per ADS {per(gro_rf-ND)[1]:.2f}-{per(top_rf-ND)[1]:.2f}; fair per share {per(fair-ND)[0]:.5f}; per ADS {per(fair-ND)[1]:.2f}")
r18 = dict(ocf=735.526, ppe=300.539, intang=0.0, lease=1.890, nci_div=19.603, da=215.187)
oc18_all = (r18['ocf'] - r18['ppe'] - r18['intang'] - r18['lease'] - r18['nci_div']) * 1000 / 640.29
oc18_m = (r18['ocf'] - r18['da'] - r18['lease'] - r18['nci_div']) * 1000 / 640.29
print(f"2018 owner cash: all-spend {oc18_all:.1f}; maint {oc18_m:.1f}; cycle 2018-24 maint avg {(oc18_m + sum(oc(y,True) for y in C))/7:.1f}; all-spend avg {(oc18_all + sum(oc(y) for y in C))/7:.1f}")
