# GATX Q7 COMPUTATION, NOT A CLEARANCE. Inputs transcribed from the filed cash-flow statements, income statements and
# segment notes of the 10-Ks named in the run file (latest-filed figure for each year), $M.
# Every assumption is named; conventions of this run are marked CONV.
Y = list(range(2013, 2026))
OCF  = dict(zip(Y, [400.7, 449.2, 541.8, 629.4, 496.8, 485.2, 425.8, 436.8, 507.2, 533.5, 520.4, 602.1, 648.1]))
SBC  = dict(zip(Y, [13.1, 14.0, 11.6, 15.8, 9.9, 16.4, 12.3, 15.6, 17.4, 12.7, 18.3, 23.0, 25.0]))
DEP  = dict(zip(Y, [267.8, 287.0, 303.3, 310.2, 322.7, 327.3, 332.7, 342.8, 378.4, 371.3, 392.1, 421.4, 452.3]))
GAIN = dict(zip(Y, [80.7, 79.3, 99.7, 52.9, 52.5, 79.3, 56.2, 39.5, 99.4, 121.2, 130.9, 137.8, 140.0]))
# deferred income taxes in operating cash; 2017 filed -260.5 is the 2017 tax-law remeasurement (non-cash);
# CONV: replaced by the mean of 2016 and 2018 (72.8, 18.1) so that the charge is a normal year's
DEF  = dict(zip(Y, [53.6, 61.4, 90.2, 72.8, (72.8 + 18.1) / 2, 18.1, 33.8, 29.1, 34.2, 36.3, 38.3, 45.8, 53.2]))
INT  = dict(zip(Y, [166.6, 158.4, 155.1, 148.1, 160.5, 162.9, 180.5, 190.3, 204.0, 214.0, 263.4, 341.0, 391.5]))
REV  = dict(zip(Y, [1321.0, 1451.0, 1449.9, 1418.3, 1376.9, 1175.1, 1202.1, 1209.2, 1257.4, 1273.0, 1410.9, 1585.5, 1740.4]))
# fleet spending: "Portfolio investments and capital additions" (includes acquisitions of businesses and affiliates)
CAPX = dict(zip(Y, [859.6, 1030.5, 696.9, 620.7, 603.4, 927.6, 722.8, 1064.0, 1131.9, 1255.8, 1665.0, 1674.4, 1316.7]))
# purchases of leased-in assets / assets previously leased (investing or financing section as filed)
PLA  = dict(zip(Y, [61.4, 150.5, 118.4, 117.1, 111.8, 66.6, 12.3, 40.0, 77.2, 1.5, 0.0, 30.4, 15.0]))
# portfolio proceeds + proceeds from sales of other assets (sale-leaseback proceeds left out: a financing)
PROC = dict(zip(Y, [385.3 + 32.3, 264.0 + 26.9, 482.2 + 18.7, 223.7 + 23.0, 165.6 + 30.3, 234.4 + 37.3, 250.3 + 23.0,
                    131.1 + 26.0, 187.1 + 54.7, 269.6 + 31.1, 272.8 + 20.2, 230.6 + 24.9, 275.0 + 36.8]))
# CONV: tax on the interest add-back: 37% to 2017 (35% federal plus state), 24% from 2018 (21% plus state; the filed
# effective rates 2023-2025 were 22.6% to 23.9% of pre-tax income before affiliates)
T = {y: (0.37 if y <= 2017 else 0.24) for y in Y}

M_eq = {y: OCF[y] - SBC[y] - DEP[y] + GAIN[y] - DEF[y] for y in Y}          # maintenance case, after interest
M_u  = {y: M_eq[y] + INT[y] * (1 - T[y]) for y in Y}                          # maintenance case, before interest
A_eq = {y: OCF[y] - SBC[y] - CAPX[y] - PLA[y] + PROC[y] for y in Y}          # all-spending case, after interest
A_u  = {y: A_eq[y] + INT[y] * (1 - T[y]) for y in Y}
G    = {y: (CAPX[y] + PLA[y] - PROC[y]) - (DEP[y] - GAIN[y]) for y in Y}     # fleet spending beyond maintenance

print("year   M_eq    M_u    A_eq    A_u   growth-spend  M_u/rev")
for y in Y:
    print(y, f"{M_eq[y]:7.1f} {M_u[y]:7.1f} {A_eq[y]:7.1f} {A_u[y]:7.1f} {G[y]:8.1f} {M_u[y]/REV[y]*100:6.1f}%")
mean = lambda d, ys: sum(d[y] for y in ys) / len(ys)
W = range(2021, 2026); C = range(2014, 2024)
print(f"window 2021-25 mean: M_eq {mean(M_eq,W):.1f}  M_u {mean(M_u,W):.1f}  A_eq {mean(A_eq,W):.1f}  A_u {mean(A_u,W):.1f}")
print(f"cycle 2014-23 mean:  M_eq {mean(M_eq,C):.1f}  M_u {mean(M_u,C):.1f}  A_u {mean(A_u,C):.1f}")
g_shown = (M_u[2025] / M_u[2021]) ** 0.25 - 1
g_sales = (REV[2025] / REV[2021]) ** 0.25 - 1
r_inc = (M_u[2025] - M_u[2021]) / sum(G[y] for y in range(2022, 2026))
max_share = max(M_u[y] / REV[y] for y in Y)
print(f"shown growth of M_u 2021-25 {g_shown*100:.2f}%; sales growth {g_sales*100:.2f}%; highest M_u/sales {max_share*100:.1f}%")
print(f"return on growth spending 2022-25: {r_inc*100:.2f}% (increase in M_u / sum of growth spending)")

# GABX on its own filed record (10-Q 2026 Q2): six months: pre-tax 6.1, interest 80.5, fees paid to GATX 24.9 (eliminated
# in consolidation); annualised x2; tax 24% (CONV as above). 100% of GABX, the 66.5% minority claimed at book value below.
GABX_u = 2 * (6.1 + 80.5 + 24.9) * (1 - 0.24)
# pro forma 2025 (8-K/A Exhibit 99.2): pre-tax 20.1 incl. own SG&A, interest 148.6 -> lower figure, shown beside
GABX_u_pf = (20.1 + 148.6) * (1 - 0.24)
# GATX holders' after-interest share: 33.5% of GABX net income (1.7 for six months) + fees borne by Brookfield's 66.5%
GABX_eq = 0.335 * 2 * 1.7 + 0.665 * 2 * 24.9 * (1 - 0.24)
print(f"GABX unlevered owner cash: 2026 record {GABX_u:.1f}; 2025 pro forma {GABX_u_pf:.1f}; equity share to GATX {GABX_eq:.1f}")

r = 0.0543; FL = 0.10
NET_DEBT = 12333.3 - 747.1 - 0.1   # 10-Q 2026-06-30: debt less cash and restricted cash; operating leases left out
NCI = 805.5                         # Brookfield's share of GABX, book value at 2026-06-30
SH = 35.305058; MCAP = SH * 164.85

def value(c0, g, rate, rinc=None, years=10):
    """ten years at g then zero growth; growth spending (M_t - M_{t-1})/rinc charged in year t if rinc given"""
    v, m_prev = 0.0, c0
    for t in range(1, years + 1):
        m = c0 * (1 + g) ** t
        spend = (m - m_prev) / rinc if rinc else 0.0
        v += (m - spend) / (1 + rate) ** t
        m_prev = m
    return v + (c0 * (1 + g) ** years / rate) / (1 + rate) ** years

def ps(v, claims): return (v - claims) / SH

for label, base in [("WINDOW 2021-25", mean(M_u, W)), ("CYCLE 2014-23", mean(M_u, C))]:
    c0 = base + GABX_u
    ng = c0 / r
    gr = value(c0, g_sales, r, r_inc)
    print(f"\n{label}: owner cash before interest incl. GABX {c0:.1f}")
    print(f"  at {r*100:.2f}%: no-growth {ng:,.0f} -> {ps(ng, NET_DEBT+NCI):,.2f}/sh ; growth (g={g_sales*100:.2f}%, spend at {r_inc*100:.2f}%) {gr:,.0f} -> {ps(gr, NET_DEBT+NCI):,.2f}/sh")
    ng10 = c0 / FL; gr10 = value(c0, g_sales, FL, r_inc)
    print(f"  at 10%: no-growth {ps(ng10, NET_DEBT+NCI):,.2f}/sh ; growth {ps(gr10, NET_DEBT+NCI):,.2f}/sh ; FAIR (avg) {(ps(ng10,NET_DEBT+NCI)+ps(gr10,NET_DEBT+NCI))/2:,.2f}/sh")
    # expected return at the price: the yield on enterprise value of the no-growth case, and the rate that equates the growth case
    ev = MCAP + NET_DEBT + NCI
    print(f"  EV {ev:,.0f}; no-growth cash yield on EV {c0/ev*100:.2f}%")
    lo, hi = 0.0001, 0.5
    for _ in range(100):
        mid = (lo + hi) / 2
        if value(c0, g_sales, mid, r_inc) > ev: lo = mid
        else: hi = mid
    print(f"  growth case: rate at which value = EV {mid*100:.2f}%")

# all-spending case beside (window mean before interest, incl GABX)
c_all = mean(A_u, W) + GABX_u
print(f"\nALL-SPENDING window mean before interest incl GABX {c_all:.1f} -> value at {r*100:.2f}% no-growth {ps(c_all/r, NET_DEBT+NCI):,.2f}/sh")
# literal three-year window of tools/run.py basis is not used; shown in the run file as printed.

# EQUITY-ONLY beside: owner cash after interest against market value
e0 = mean(M_eq, W) + GABX_eq
g_eq = (M_eq[2025] / M_eq[2021]) ** 0.25 - 1
print(f"\nEQUITY-ONLY window: owner cash after interest incl GATX's GABX share {e0:.1f}; shown growth {g_eq*100:.2f}%")
print(f"  no-growth at {r*100:.2f}%: {e0/r/SH:,.2f}/sh ; at 10%: {e0/FL/SH:,.2f}/sh ; yield at price {e0/MCAP*100:.2f}%")
# equity growth case: growth carried at sales growth, the equity's part of growth spending charged (debt share of net
# fleet investment 2022-25 from the change in net debt ex-GABX)
nd21 = 5906 - 344; nd25 = (12534 - 2959) - 743
debt_share = (nd25 - nd21) / sum(G[y] for y in range(2022, 2026))
r_inc_eq = (M_eq[2025] - M_eq[2021]) / (sum(G[y] for y in range(2022, 2026)) * (1 - min(debt_share, 1)))
print(f"  debt share of growth spending 2022-25 {debt_share*100:.1f}% ; equity return on growth spending {r_inc_eq*100:.1f}%")
gq5 = value(e0, g_sales, r, r_inc_eq); gq10 = value(e0, g_sales, FL, r_inc_eq)
print(f"  growth at {r*100:.2f}%: {gq5/SH:,.2f}/sh ; at 10%: {gq10/SH:,.2f}/sh ; FAIR equity-only (avg at 10%) {((e0/FL)+gq10)/2/SH:,.2f}/sh")
