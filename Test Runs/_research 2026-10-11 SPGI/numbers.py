"""SPGI run 2026-10-11: owner cash on the price-date perimeter and the Q7 arithmetic.
Every input is typed from a filing named beside it (USD millions). Estimates are marked EST and are the run's
CONVENTION (see the run file, Q4 and Q7). Run: python numbers.py
"""
# ---- consolidated cash flow, SPGI 10-Ks (FY2025 0000064040-26-000013; FY2022 0000064040-23-000058) ----
OCF   = {2021: 3598, 2022: 2603, 2023: 3710, 2024: 5689, 2025: 5651}
CAPEX = {2021: 35,   2022: 89,   2023: 143,  2024: 124,  2025: 195}   # incl. additions to technology projects
SBC   = {2021: 122,  2022: 214,  2023: 171,  2024: 247,  2025: 236}
NCI   = {2021: 227,  2022: 270,  2023: 280,  2024: 287,  2025: 321}   # distributions to CME (27% of S&P DJI)
INTP  = {2021: 130,  2022: 240,  2023: 369,  2024: 391,  2025: 390}   # interest paid
ACQ   = {2021: 99,   2022: -210, 2023: 296,  2024: 305,  2025: 2023}  # acquisitions net of cash acquired
DISP  = {2021: 16,   2022: 3509, 2023: 1014, 2024: 168,  2025: 1549}  # proceeds from dispositions
TAXR  = {2021: 0.22, 2022: 0.22, 2023: 778/3671, 2024: 1141/5308, 2025: 1407/6227}  # provision / pre-tax (pro forma 8-K/A for 2023-25)

# ---- IHS Markit FY2021 (year to 2021-11-30), 10-K 0001598014-22-000011 ----
IHS = dict(ocf=1486.2, capex=294.3, sbc=226.9, intp=212.4, acq=46.9,
           ebitda_transport=645.0, ebitda_segments=962.0 + 645.0 + 339.5)
ihs_oc = IHS['ocf'] - IHS['capex'] - IHS['sbc']
ihs_transport_share = IHS['ebitda_transport'] / IHS['ebitda_segments']          # EST: Mobility share by adj. EBITDA
ihs_oc_ex = ihs_oc * (1 - ihs_transport_share)

# ---- Mobility removed (8-K/A 0001104659-26-080571, Ex. 99.2 pro forma; FY2022 10-K Note 12 for 2022) ----
# EST: Mobility cash = OP + depreciation + amortization - its pro forma tax - capex share (PP&E 19/261) - SBC share (revenue share)
MOB = {
    2022: dict(op=213, dep=6,  amort=248, tax=0.21 * 213, rev=1142, totrev=11181),
    2023: dict(op=317, dep=9,  amort=302, tax=63, rev=1484, totrev=12497),
    2024: dict(op=374, dep=13, amort=302, tax=92, rev=1609, totrev=14208),
    2025: dict(op=373, dep=14, amort=303, tax=69, rev=1747, totrev=15336),
}
PPE_SHARE = 19 / 261
def mob_cash(y):
    if y not in MOB: return 0.0
    m = MOB[y]
    return m['op'] + m['dep'] + m['amort'] - m['tax'] - PPE_SHARE * CAPEX[y] - SBC[y] * m['rev'] / m['totrev']
def mob_pre_da(y):  # Mobility cash before D&A is removed from the D&A variant below
    if y not in MOB: return 0.0
    m = MOB[y]
    return m['op'] + m['dep'] + m['amort'] - m['tax'] - SBC[y] * m['rev'] / m['totrev']

# continuing-operations depreciation + amortization (pro forma), for the depreciation variant
DA_CONT = {2023: 92 + 740, 2024: 83 + 775, 2025: 96 + 766}

oc_eq, oc_ae = {}, {}
for y in range(2021, 2026):
    v = OCF[y] - CAPEX[y] - SBC[y] - NCI[y] - mob_cash(y)
    ip = INTP[y]
    if y == 2021:
        v += ihs_oc_ex; ip += IHS['intp']
    if y == 2022:  # EST: IHS Markit Jan-Feb 2022 not filed; 2/12 of FY2021 ex-Transportation
        v += ihs_oc_ex * 2 / 12; ip += IHS['intp'] * 2 / 12
    oc_eq[y] = v
    oc_ae[y] = v + ip * (1 - TAXR[y])

print("OWNER CASH, price-date perimeter (Mobility out), USD M")
print("year  OCF-capex-SBC-NCI  Mobility-EST  IHS-EST   equity-basis  all-equity")
for y in range(2021, 2026):
    base = OCF[y] - CAPEX[y] - SBC[y] - NCI[y]
    ihs = ihs_oc_ex if y == 2021 else (ihs_oc_ex * 2 / 12 if y == 2022 else 0)
    print(f"{y}  {base:8.0f}  {mob_cash(y):8.0f}  {ihs:8.0f}  {oc_eq[y]:10.0f}  {oc_ae[y]:10.0f}")
print(f"IHS FY2021 owner cash {ihs_oc:.0f}, Transportation share {ihs_transport_share:.3f}, ex-Transportation {ihs_oc_ex:.0f}")

lit_eq = sum(oc_eq.values()) / 5; lit_ae = sum(oc_ae.values()) / 5
cen_eq = sum(oc_eq[y] for y in (2023, 2024, 2025)) / 3
cen_ae = sum(oc_ae[y] for y in (2023, 2024, 2025)) / 3
print(f"\nliteral window 2021-2025 average: equity {lit_eq:.0f}  all-equity {lit_ae:.0f}")
print(f"central base 2023-2025 (filer's own pro forma perimeter): equity {cen_eq:.0f}  all-equity {cen_ae:.0f}")

# acquisitions net of dispositions (convention (c)), central years
net_acq = {y: ACQ[y] - DISP[y] for y in OCF}
print("acquisitions net of dispositions:", net_acq, " central-years average", round(sum(net_acq[y] for y in (2023,2024,2025))/3))

# depreciation variant (all D&A of continuing operations charged instead of capex), equity basis
print("\nDEPRECIATION VARIANT (equity basis): OCF - SBC - NCI - Mobility(pre-capex) - continuing D&A")
dv = {}
for y in (2023, 2024, 2025):
    dv[y] = OCF[y] - SBC[y] - NCI[y] - mob_pre_da(y) - DA_CONT[y]
    print(y, round(dv[y]))
print("average", round(sum(dv.values()) / 3))

# ---- sales, pro forma continuing (8-K/A) and the cap test ----
REV = {2023: 11013, 2024: 12599, 2025: 13589}
g_sales = (REV[2025] / REV[2023]) ** 0.5 - 1
g_oc_end = (oc_ae[2025] / oc_ae[2023]) ** 0.5 - 1
g_lit_end = (oc_ae[2025] / oc_ae[2021]) ** 0.25 - 1
h1 = (oc_ae[2021] + oc_ae[2022]) / 2; h2 = (oc_ae[2024] + oc_ae[2025]) / 2
g_lit_halves = (h2 / h1) ** (1 / 3) - 1
print(f"\ngrowth shown: central end-years 2023->2025 {g_oc_end:.3%}; sales 2023->2025 {g_sales:.3%}")
print(f"literal: end-years 2021->2025 {g_lit_end:.3%}; halves {g_lit_halves:.3%}")
share_2025 = oc_ae[2025] / REV[2025]
legacy2020 = (3567 - 76 - 90 - 194 + 159 * 0.79) / 7442    # SPGI FY2020 (FY2022 10-K / companyfacts): highest share found
print(f"owner cash / sales 2025 {share_2025:.3f}; highest share in filings read (SPGI 2020, all-equity) {legacy2020:.3f}")
for g in (g_oc_end, g_lit_halves):
    s10 = oc_ae[2025] * (1 + g) ** 10 / (REV[2025] * (1 + g_sales) ** 10)
    print(f"  carried at {g:.3%} ten years: share of sales at sales growth {s10:.3f}")

# ---- market, net debt ----
SHARES = 294.8; PRICE = 407.82; RATE = 0.056
mcap = SHARES * PRICE
debt = 2572 + 12598 - 1986          # 10-Q 2026-06-30 less Mobility Global notes (carrying; became Mobility's)
cash = 4134 - 121 - (1986 - 1974)   # EST: less Mobility's operating cash (121 at 3/31 pro forma) and notes proceeds kept
net_debt = debt - cash
ev = mcap + net_debt
print(f"\nmarket cap {mcap:.0f}; debt {debt:.0f}; cash {cash:.0f}; net debt {net_debt:.0f}; EV {ev:.0f}")

def value(base, g, r):
    pv, cf = 0.0, base
    for t in range(1, 11):
        cf *= (1 + g); pv += cf / (1 + r) ** t
    pv += cf / r / (1 + r) ** 10   # zero nominal growth after year ten
    return pv
def irr(base, g, price):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(base, g, mid) > price: lo = mid
        else: hi = mid
    return mid

def report(label, base_ae, base_eq, g):
    lo_ae = base_ae / RATE; hi_ae = value(base_ae, g, RATE)
    lo_ps = (lo_ae - net_debt) / SHARES; hi_ps = (hi_ae - net_debt) / SHARES
    lo_eq = base_eq / RATE / SHARES; hi_eq = value(base_eq, g, RATE) / SHARES
    f_ae = ((base_ae / 0.10 + value(base_ae, g, 0.10)) / 2 - net_debt) / SHARES
    f_eq = (base_eq / 0.10 + value(base_eq, g, 0.10)) / 2 / SHARES
    print(f"\n{label}: base all-equity {base_ae:.0f}, equity {base_eq:.0f}, growth {g:.3%} ten years then zero, rate {RATE:.2%}")
    print(f"  all-equity range per share ${lo_ps:.2f} to ${hi_ps:.2f}  (ratio {hi_ps/lo_ps:.2f}); equity-only ${lo_eq:.2f} to ${hi_eq:.2f}")
    print(f"  expected return at the price (all-equity, EV {ev:.0f}): no-growth {irr(base_ae,0,ev):.3%}; growth case {irr(base_ae,g,ev):.3%}")
    print(f"  expected return at the price (equity-only, mcap {mcap:.0f}): no-growth {irr(base_eq,0,mcap):.3%}; growth case {irr(base_eq,g,mcap):.3%}")
    print(f"  FAIR PRICE (each end at 10%, averaged): all-equity ${f_ae:.2f}; equity-only ${f_eq:.2f}")
    return lo_ps, hi_ps

report("CENTRAL (2023-2025 perimeter base; growth = sales growth 2023-2025 after the cap)", cen_ae, cen_eq, g_sales)
report("LITERAL WINDOW (2021-2025 average; growth = halves, cut to sales growth 2023-2025)", lit_ae, lit_eq, g_sales)
report("LITERAL WINDOW, end-year growth 2021->2025 (no cut needed)", lit_ae, lit_eq, g_lit_end)
report("DEPRECIATION VARIANT (central years, all-equity approximated by adding the same after-tax interest)",
       sum(dv.values())/3 + (cen_ae - cen_eq), sum(dv.values())/3, g_sales)
# sensitivity: growth needed for the top case to earn 10% at the price
for g in (0.12, 0.15, 0.18):
    print(f"growth {g:.0%}: expected return at price (all-equity) {irr(cen_ae, g, ev):.3%}")

# ---- Q6 STOP test: was SPGI's stock below its own Q7 range when it paid for IHS Markit wholly in stock? ----
print("\nQ6 DEAL TEST (point in time: the merger's price date 2022-02-25, Treasury 30-year par 2.29%; signing 2020-11-30, 1.58%)")
S = {2017: (2016, 123, 99, 111, 139), 2018: (2064, 113, 94, 154, 151), 2019: (2776, 115, 78, 143, 162),
     2020: (3567, 76, 90, 194, 159), 2021: (3598, 35, 122, 227, 130)}   # OCF, capex, SBC, NCI, interest paid (10-Ks)
spgi_ae = {y: o - c - s - n + i * 0.79 for y, (o, c, s, n, i) in S.items()}
avg_spgi = sum(spgi_ae.values()) / 5
net_cash_2021 = 6497 - 4114       # FY2021 balance sheet: cash less long-term debt (no current debt)
sh_pre = 241.1; px_close = 380.89
for r in (0.0229, 0.0158, 0.03):
    bottom = (avg_spgi / r + net_cash_2021) / sh_pre
    print(f"  SPGI all-equity owner cash 2017-2021 avg {avg_spgi:.0f}; no-growth bottom at {r:.2%}: ${bottom:.2f}/share vs $380.89 given")
I = {2019: (1251.3, 278.1, 223.8, 244.4), 2020: (1138.8, 274.8, 265.7, 225.1), 2021: (1486.2, 294.3, 226.9, 212.4)}
ihs_ae = {y: o - c - s + i * 0.79 for y, (o, c, s, i) in I.items()}
avg_ihs = sum(ihs_ae.values()) / 3
paid_ev = 43536 + 968 + 4191 - 310
print(f"  IHS Markit all-equity owner cash FY2019-21 avg {avg_ihs:.0f}; enterprise value paid {paid_ev:.0f}; no-growth value at 2.29% {avg_ihs/0.0229:.0f} (paid / no-growth = {paid_ev/(avg_ihs/0.0229):.2f})")
mc_pre = sh_pre * px_close
print(f"  SPGI market cap at $380.89: {mc_pre:.0f}; price / no-growth value at 2.29% = {(mc_pre - net_cash_2021)/(avg_spgi/0.0229):.2f}")
share_given = 113.8 / (sh_pre + 113.8)
ihs_eq21 = 1486.2 - 294.3 - 226.9; spgi_eq21 = 3598 - 35 - 122 - 227
print(f"  shares given: {share_given:.1%} of the combined; IHS share of combined FY2021 owner cash: equity basis {ihs_eq21/(ihs_eq21+spgi_eq21):.1%}, all-equity {ihs_ae[2021]/(ihs_ae[2021]+spgi_ae[2021]):.1%}")
