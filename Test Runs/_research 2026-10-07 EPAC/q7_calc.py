"""COMPUTATION, NOT A CLEARANCE. Q7 arithmetic for the EPAC run, first run at about 10:20 local on 2026-10-07,
before Q2 to Q6 were written (declared in the run file's self-audit). It carries no entry language; the judgments are in the run file.
All USD millions from the filed 10-K cash-flow statements (continuing operations) as cited in the run file.
"""
R = 0.0564          # US Treasury 30-year par yield, 2026-10-06 (tools/sources.py)
FLOOR = 0.10        # Q7 floor CONVENTION, about ten percent
SH = 51.137646      # cover shares, 10-Q filed 2026-07-09
PRICE = 35.23       # aggregator, 2026-10-07, live quote only
NET_DEBT = 184.8 - 115.7   # debt less cash at 2026-05-31 (10-Q / earnings release); operating leases left out
STAT = 0.21

yrs = [2021, 2022, 2023, 2024, 2025]
ocf   = {2021: 54.9, 2022: 52.2, 2023: 78.6, 2024: 84.0, 2025: 111.3}   # continuing ops
sbc   = {2021: 9.2,  2022: 13.6, 2023: 8.6,  2024: 10.9, 2025: 13.0}
capex = {2021: 12.0, 2022: 8.4,  2023: 9.4,  2024: 11.4, 2025: 19.3}
fin   = {2021: 5.0,  2022: 4.0,  2023: 12.0, 2024: 14.0, 2025: 9.9}    # financing costs, net
pretax= {2021: 44.0, 2022: 24.0, 2023: 68.9, 2024: 105.5, 2025: 120.7}
taxpd = {2021: 7.8,  2022: 5.7,  2023: 2.7,  2024: 23.8, 2025: 26.6}
acq_net = {2021: 0.0, 2022: 0.0, 2023: -20.1, 2024: 1.4 + 1.1, 2025: 26.7}  # paid for businesses less sold
sales = {2021: 528.7, 2025: 616.9}

oc_eq = {y: ocf[y] - sbc[y] - capex[y] for y in yrs}
tax_adj = {y: (taxpd[y] - STAT * pretax[y]) if y in (2021, 2022, 2023) else 0.0 for y in yrs}  # shelter years at statutory
oc_eq_t = {y: oc_eq[y] + tax_adj[y] for y in yrs}
oc_ae = {y: oc_eq_t[y] + fin[y] * (1 - STAT) for y in yrs}       # all-equity: before interest, after tax

def avg(d, ys): return sum(d[y] for y in ys) / len(ys)
acq_avg = avg(acq_net, yrs)

def pv(base, g, r, n=10):
    v, c = 0.0, base
    for t in range(1, n + 1):
        c = c * (1 + g); v += c / (1 + r) ** t
    return v + (c / r) / (1 + r) ** n   # then zero nominal growth

def report(label, base, g):
    lo = pv(base, 0.0, R); hi = pv(base, g, R)
    if hi < lo: lo, hi = hi, lo
    ps = lambda v: (v - NET_DEBT) / SH
    # fair price: the price at which the midpoint case earns the floor -> midpoint growth stream discounted at FLOOR
    mid_g = g / 2
    fair_ev = pv(base, mid_g, FLOOR)
    print(f"{label}: base {base:.1f}  g {g*100:.1f}%  EV {lo:.0f}-{hi:.0f}  per share {ps(lo):.2f}-{ps(hi):.2f}  "
          f"width {hi/lo:.2f}x  fair (all-equity) {ps(fair_ev):.2f}")
    return ps(lo), ps(hi), ps(fair_ev)

print("owner cash, equity basis (OCF-SBC-capex):", {y: round(v, 1) for y, v in oc_eq.items()})
print("tax adj (shelter yrs at 21%):", {y: round(v, 1) for y, v in tax_adj.items()})
print("all-equity owner cash:", {y: round(v, 1) for y, v in oc_ae.items()})
print("net acquisitions avg/yr:", round(acq_avg, 2))
g_cash = (oc_ae[2025] / oc_ae[2021]) ** 0.25 - 1
g_sales = (sales[2025] / sales[2021]) ** 0.25 - 1
print(f"shown growth aggregate owner cash {g_cash*100:.1f}%/yr (cut back as absurd); sales {g_sales*100:.1f}%/yr")
# halves method shown beside: first half 2021-22 vs second half 2024-25
h1 = avg(oc_ae, [2021, 2022]); h2 = avg(oc_ae, [2024, 2025]); g_h = (h2 / h1) ** (1 / 3) - 1
print(f"halves growth {g_h*100:.1f}%/yr")

base_lit = avg(oc_ae, yrs) - acq_avg
base_post = avg(oc_ae, [2023, 2024, 2025]) - avg(acq_net, [2023, 2024, 2025])
print()
A = report("A literal FY21-25 all-equity, acq deducted, sales growth", base_lit, g_sales)
B = report("B post-ASCEND FY23-25 all-equity, acq deducted, sales growth", base_post, g_sales)
# TTM to 2026-05-31: FY25 + 9M26 - 9M25
ttm_ocf = 111.3 - 56.0 + 69.3; ttm_capex = 19.3 - 16.4 + 9.2; ttm_sbc = 13.0 - 9.5 + 9.4; ttm_fin = 9.9 - 7.5 + 6.6
ttm = ttm_ocf - ttm_sbc - ttm_capex + ttm_fin * (1 - STAT)
C = report("C TTM May-2026 all-equity (beside only)", ttm, g_sales)
# equity-only figures (after interest), literal window
base_eq = avg(oc_eq_t, yrs) - acq_avg
lo = pv(base_eq, 0, R); hi = pv(base_eq, g_sales, R)
print(f"equity-only literal: {lo/SH:.2f}-{hi/SH:.2f}  fair {pv(base_eq, g_sales/2, FLOOR)/SH:.2f}")
base_eq_p = avg(oc_eq_t, [2023, 2024, 2025]) - avg(acq_net, [2023, 2024, 2025])
lo = pv(base_eq_p, 0, R); hi = pv(base_eq_p, g_sales, R)
print(f"equity-only post: {lo/SH:.2f}-{hi/SH:.2f}  fair {pv(base_eq_p, g_sales/2, FLOOR)/SH:.2f}")
# expected return at price, literal and post, all-equity: solve r such that pv(base,g/2,r)=EV at price
ev = PRICE * SH + NET_DEBT
for lab, b in (("literal", base_lit), ("post", base_post), ("ttm", ttm)):
    lo_r, hi_r = 0.001, 0.5
    for _ in range(100):
        mid = (lo_r + hi_r) / 2
        if pv(b, g_sales / 2, mid) > ev: lo_r = mid
        else: hi_r = mid
    print(f"expected return at price, midpoint case, {lab}: {mid*100:.2f}%  (EV {ev:.0f})")
# SFE pro forma per specific (c) by analogy: financing added to net debt, credited at nothing
sfe = 451.4
print(f"SFE pro forma: subtract {sfe/SH:.2f} per share from every figure")
