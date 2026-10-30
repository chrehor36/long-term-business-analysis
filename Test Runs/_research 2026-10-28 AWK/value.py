"""AWK Q7 arithmetic (USD millions). Every input is from the filed statements named in the run file.
Usage: python -I value.py"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

Y = [2021, 2022, 2023, 2024, 2025]
# Consolidated statements of cash flows: FY2023 10-K (0001410636-24-000050) for 2021-2022, FY2025 10-K (0001410636-26-000034) for 2023-2025
OCF   = [1441, 1108, 1874, 2045, 2059]
SBC   = [17, 28, 25, 36, 32]            # stock-based compensation (XBRL AllocatedShareBasedCompensationExpense, same 10-Ks)
DA    = [636, 649, 704, 788, 894]       # depreciation and amortization
CAPEX = [1764, 2297, 2575, 2856, 3126]  # capital expenditures
REMOV = [109, 123, 159, 152, 175]       # removal costs from PP&E retirements, net (investing)
ACQ   = [135, 315, 81, 417, 71]         # acquisitions, net of cash acquired
SALES_PROCEEDS = [472, 608, 0, 0, 0]    # proceeds from sale of assets (HOS 2021, New York 2022)
DIVEST_TAX_2022 = 280                   # FY2023 10-K MD&A: estimated tax payments for taxable gains on the HOS and NY sales, first half 2022
INTPAID = [389, 414, 445, 483, 568]     # cash paid for interest, net of capitalized
REV   = [3930, 3792, 4234, 4684, 5140]  # operating revenues (statements of operations)
TAXRATE = [None, None, 252/1196, 308/1359, 311/1422]

# long-term debt incl. current maturities, excl. preferred: end 2020 (FY2021 10-K) and end 2025 (FY2025 10-K)
LTD_2020 = 9329 + 329
LTD_2025 = 12777 + 1479
# latest filed date 2026-06-30 (10-Q 0001410636-26-000120)
LTD_Q2 = 14043 + 446
PREF_Q2 = 3
EQ_Q2 = 11665
ST_Q2 = 1499
CASH_Q2 = 191
SHARES = 198.728989   # cover, 2026-07-20
PRICE = 141.10        # close 2026-10-27, aggregator, live quote only
R = 0.0530            # US Treasury 30-year par yield, 2026-10-27
FLOOR = 0.10

oc_m_lit = [o - s - d for o, s, d in zip(OCF, SBC, DA)]
oc_m = oc_m_lit[:]; oc_m[1] += DIVEST_TAX_2022
oc_all = [o - s - c - rm for o, s, c, rm in zip(OCF, SBC, CAPEX, REMOV)]
gs = [c + rm - d for c, rm, d in zip(CAPEX, REMOV, DA)]   # growth spending above the maintenance guess
avg = lambda v: sum(v) / len(v)
print("owner cash after maintenance (OCF-SBC-D&A), literal:", oc_m_lit, "avg", round(avg(oc_m_lit), 1))
print("owner cash after maintenance, 2022 divestiture tax added back:", oc_m, "avg", round(avg(oc_m), 1))
print("owner cash after ALL spending (OCF-SBC-capex-removal):", oc_all, "avg", round(avg(oc_all), 1))
print("  ... and after acquisitions:", [a - q for a, q in zip(oc_all, ACQ)], "avg", round(avg(oc_all) - avg(ACQ), 1))
print("growth spending (capex+removal-D&A):", gs, "avg", round(avg(gs), 1), "; acquisitions avg", round(avg(ACQ), 1))
print("owner cash / revenue (maintenance basis):", [round(a / r * 100, 1) for a, r in zip(oc_m, REV)])
C0 = avg(oc_m); GS0 = avg(gs) + avg(ACQ)
g_shown = (oc_m[-1] / oc_m[0]) ** (1 / 4) - 1
g_sales = (REV[-1] / REV[0]) ** (1 / 4) - 1
h1 = avg(oc_m[:2]); h2 = avg(oc_m[3:]); g_half = (h2 / h1) ** (1 / 3) - 1
print(f"C0 {C0:.1f}  GS0 (growth capex + acq) {GS0:.1f}")
print(f"shown growth 2021-2025 end years {g_shown*100:.2f}%  halves {g_half*100:.2f}%  sales growth {g_sales*100:.2f}%")
# cap (f): owner cash share of sales after ten years at shown growth vs sales growth
share10 = oc_m[-1] / REV[-1] * ((1 + g_shown) / (1 + g_sales)) ** 10
print(f"cap test: owner cash/sales in year 10 at shown growth {share10*100:.1f}% vs highest in statements read {max(a/r for a,r in zip(oc_m,REV))*100:.1f}%")

D0 = (LTD_2025 - LTD_2020) / 5
cap_share = LTD_Q2 / (LTD_Q2 + PREF_Q2 + EQ_Q2)
credit0 = min(D0, cap_share * GS0)
print(f"LT debt increase per year {D0:.1f}; own LT debt share of LT capital {cap_share*100:.1f}%; cap {cap_share*GS0:.1f}; credit {credit0:.1f}")

def pv_growth(c0, net_gs0, g, r, years=10):
    pv = 0.0
    for t in range(1, years + 1):
        pv += (c0 - net_gs0) * (1 + g) ** t / (1 + r) ** t
    c10 = c0 * (1 + g) ** years
    pv += c10 / r / (1 + r) ** years
    return pv

def report(label, c0, net_gs0, g, r, less=0.0, shares=SHARES):
    ng = c0 / r - less
    gr = pv_growth(c0, net_gs0, g, r) - less
    return ng / shares, gr / shares

for g, lab in ((g_sales, "growth = sales growth (cap (f) cut)"), (g_shown, "growth = shown rate")):
    ng, gr = report(lab, C0, GS0 - credit0, g, R)
    ngf, grf = report(lab, C0, GS0 - credit0, g, FLOOR)
    print(f"EQUITY-ONLY central, {lab}: no-growth ${ng:.2f}  growth ${gr:.2f}  | at 10%: ${ngf:.2f} / ${grf:.2f}  fair ${(ngf+grf)/2:.2f}")
    # literal window beside
    C0l = avg(oc_m_lit)
    ngl, grl = report(lab, C0l, GS0 - credit0, g, R)
    print(f"   literal window (no 2022 add-back): ${ngl:.2f} / ${grl:.2f}")
    # all spending charged, no maintenance split (all-spending case beside), with debt credit
    ngA = (avg(oc_all) - avg(ACQ) + credit0) / R / SHARES
    print(f"   all-spending case with the debt credit, no growth credited: ${ngA:.2f}")

# implied return at the price (equity-only, no-growth): owner cash / market cap
mcap = PRICE * SHARES
print(f"market cap {mcap:,.0f}; owner cash after maintenance / market cap {C0/mcap*100:.2f}%")
# IRR of growth case at the price
def irr(g):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv_growth(C0, GS0 - credit0, g, mid) > mcap: lo = mid
        else: hi = mid
    return mid
print(f"expected return at the price, growth case (sales g): {irr(g_sales)*100:.2f}%; (shown g): {irr(g_shown)*100:.2f}%; no-growth {C0/mcap*100:.2f}%")

# ALL-EQUITY beside: owner cash before interest, after company tax; all spending; less net debt
tax = avg([t for t in TAXRATE if t])
oc_m_unlev = [a + i * (1 - tax) for a, i in zip(oc_m, INTPAID)]
C0u = avg(oc_m_unlev)
netdebt = ST_Q2 + LTD_Q2 + PREF_Q2 - CASH_Q2
print(f"all-equity: effective tax {tax*100:.1f}%; unlevered owner cash after maintenance avg {C0u:.1f}; net debt 2026-06-30 {netdebt:,}")
for g, lab in ((g_sales, "sales g"), (g_shown, "shown g")):
    ng = (C0u / R - netdebt) / SHARES
    gr = (pv_growth(C0u, GS0, g, R) - netdebt) / SHARES
    ngf = (C0u / FLOOR - netdebt) / SHARES
    grf = (pv_growth(C0u, GS0, g, FLOOR) - netdebt) / SHARES
    print(f"ALL-EQUITY beside ({lab}): no-growth ${ng:.2f} growth ${gr:.2f} | at 10%: ${ngf:.2f} / ${grf:.2f} fair ${(ngf+grf)/2:.2f}")

# MERGER beside (signed, unclosed): Essential FY2021-2025, 10-Ks 0001562762-24-000047 and 0000078128-26-000050
W_OCF = [645, 600, 934, 770, 1010]; W_SBC = [10, 12, 11, 10, 13]; W_DA = [298, 321, 344, 370, 417]
w_oc = [o - s - d for o, s, d in zip(W_OCF, W_SBC, W_DA)]
w_sh = 283.117816 * 0.305
comb = C0 + avg(w_oc)
print(f"Essential owner cash after maintenance {w_oc} avg {avg(w_oc):.1f}; new AWK shares {w_sh:.2f}M")
print(f"MERGER beside, no-growth equity-only: combined ${comb/R/(SHARES+w_sh):.2f} vs AWK alone ${C0/R/SHARES:.2f}; at 10%: ${comb/FLOOR/(SHARES+w_sh):.2f}")
print(f"value given at the price: {w_sh*PRICE:,.0f}; Essential no-growth value at the long rate {avg(w_oc)/R:,.0f}")

# BESIDE: (c) taken literally (sale proceeds netted against purchases, 2022 tax left in operating cash)
acq_net = [q - s for q, s in zip(ACQ, SALES_PROCEEDS)]
GS0_lit = avg(gs) + avg(acq_net)
for g, lab in ((g_sales, "sales g"), (g_shown, "shown g")):
    ng = avg(oc_m_lit) / R / SHARES
    gr = pv_growth(avg(oc_m_lit), GS0_lit - credit0, g, R) / SHARES
    print(f"BESIDE literal (c), {lab}: net acquisitions avg {avg(acq_net):.1f}; no-growth ${ng:.2f} growth ${gr:.2f}")
# BESIDE: the seller-note interest taken out (7% on 720 in 2022-2023, 10% on 795 in 2024-2025), after the 21.9% rate
note_int = [0, 720*0.07, 720*0.07, 795*0.10, 795*0.10]
C0n = C0 - avg(note_int) * (1 - 0.219)
print(f"BESIDE seller-note interest removed: C0 {C0n:.1f}; no-growth ${C0n/R/SHARES:.2f}; growth (sales g) ${pv_growth(C0n, GS0-credit0, g_sales, R)/SHARES:.2f}")
print(f"growth spending charged: year 1 ${GS0*(1+g_sales):,.0f}M, year 10 ${GS0*(1+g_sales)**10:,.0f}M; debt credit year 1 ${credit0*(1+g_sales):,.0f}M, year 10 ${credit0*(1+g_sales)**10:,.0f}M")
# stated allowed debt shares, weighted by the rate base the 10-K states with them (IL, MO, KY, IA, TN, VA)
rb = {"IL": (2200, .51), "MO": (3200, .50), "KY": (667, .4774), "IA": (262, .4743), "TN": (300, .5581), "VA": (369, .5433)}
tot = sum(v[0] for v in rb.values()); w = sum(v[0]*v[1] for v in rb.values())/tot
print(f"stated allowed debt share, rate-base weighted over ${tot:,}M: {w*100:.1f}% (cap would be {w*GS0:,.0f})")
