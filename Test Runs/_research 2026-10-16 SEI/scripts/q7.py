# COMPUTATION, NOT A CLEARANCE: Q7's range convention applied beneath the Q2 stop. USD millions.
# Sources: FY2022 10-K (2020-2022 cash flows, acc 0001558370-23-003344); FY2025 10-K (2023-2025, acc 0001628280-26-012501).
yrs = [2021, 2022, 2023, 2024, 2025]
ocf   = [16.473, 67.996, 89.353, 59.367, 209.104]
sbc   = [5.210, 6.092, 7.741, 10.592, 23.371]
capex = [19.638, 81.411, 64.388, 188.419, 646.757]
dna   = [27.210, 30.433, 36.185, 47.218, 84.285]
fl    = [0.030, 1.610, 2.502, 2.991, 3.240]          # finance-lease principal
disp  = [0.0, 0.0, 2.385, 5.452, 3.389]               # disposal proceeds (2024 incl. Kingfisher sale 5.0)
acq   = [0.0, 0.0, 0.0, 122.065, 29.200]              # cash paid for businesses (MER 2024, HVMVLV 2025)
# all-equity: add back net cash interest after tax at the 21% federal statutory rate (interest paid less received)
intpaid = [0.0, 0.0, 2.958, 11.458, 22.406]; intrec = [0.0, 0.0, 0.143, 1.464, 6.729]   # 2021-22 not read; debt under $10M
iat = [(p - r) * 0.79 for p, r in zip(intpaid, intrec)]
sales = [159.2, 320.0, 292.9, 313.1, 622.2]
R = 0.0543; F = 0.10
oc_all = [o - s - c - f + d - a + i for o, s, c, f, d, a, i in zip(ocf, sbc, capex, fl, disp, acq, iat)]
oc_mnt = [o - s - m - f + i for o, s, m, f, i in zip(ocf, sbc, dna, fl, iat)]
oc_mnt_eq = [x - i for x, i in zip(oc_mnt, iat)]
avg = lambda v: sum(v) / len(v)
print("year  OC all-spending  OC maintenance(D&A proxy)  share of sales")
for y, a, m, s in zip(yrs, oc_all, oc_mnt, sales): print(y, round(a, 1), round(m, 1), f"{m/s*100:.1f}%")
A, M, Me = avg(oc_all), avg(oc_mnt), avg(oc_mnt_eq)
print(f"five-year average: all-spending {A:.1f}; maintenance-only {M:.1f}; maintenance-only after interest {Me:.1f}")
# growth shown on the maintenance series: sign change -> halves (2021-22 vs 2024-25), three years apart
h1, h2 = avg(oc_mnt[:2]), avg(oc_mnt[3:]); g_shown = (h2 / h1) ** (1/3) - 1
g_sales = (sales[-1] / sales[0]) ** (1/4) - 1
print(f"halves {h1:.1f} -> {h2:.1f}: shown growth {g_shown*100:.1f}%/yr; sales growth 2021-25 {g_sales*100:.1f}%/yr")
best_share = max(m / s for m, s in zip(oc_mnt, sales))
oc10 = M * (1 + g_shown) ** 10; s10 = sales[-1] * (1 + g_sales) ** 10
print(f"cap (f): OC in year 10 at shown growth {oc10:.0f} vs {best_share*100:.1f}% of year-10 sales {s10*best_share:.0f} -> cut")
g = min(g_sales, R)   # the cut: own sales growth, never above the discount rate
print(f"growth carried after the cut: {g*100:.2f}%")
# incremental return the growth spending bought: rise in maintenance OC between halves per dollar of growth spending
growth_spend = sum(c - m for c, m in zip(capex, dna)) + sum(acq)
inc = (h2 - h1) / growth_spend
print(f"growth spending 2021-25 {growth_spend:.1f}; rise in OC {h2-h1:.1f}; incremental after-tax return {inc*100:.1f}%")
def pv(cfs, r, terminal):
    v = sum(c / (1 + r) ** (t + 1) for t, c in enumerate(cfs))
    return v + terminal / r / (1 + r) ** len(cfs)
def cases(base, r):
    nog = base / r                                       # no-growth, maintenance-only
    flows = []; oc = base
    for t in range(10):
        add = oc * g; spend = add / inc                  # spending needed to buy the growth at the shown return
        flows.append(oc - spend); oc += add
    gro = pv(flows, r, oc)                               # growth charged with its spending, flat after year 10
    return nog, gro
net_debt = (1300.0 + 339.7 + 902.5 + 5.478) - 824.101 + 52.4 + 21.0 + 77.0   # 6/30 face debt less cash; GESA cash, Stateline draw, Omega cash
nci_stateline = 86.0
shares = 80.165591
print(f"net debt (all-equity basis) {net_debt:.1f}; Stateline minority (MZX 49.9%, book) {nci_stateline}")
for lab, base in (("all-equity", M), ("equity-only", Me)):
    for r in (R, F):
        n, gcase = cases(base, r)
        claims = (net_debt + nci_stateline) if lab == "all-equity" else nci_stateline
        ps = [(x - claims) / shares for x in (n, gcase)]
        print(f"{lab} at {r*100:.2f}%: business no-growth {n:.0f}, growth-charged {gcase:.0f}; per share {ps[0]:.2f} / {ps[1]:.2f}")
# literal window beside: all-spending five-year average is negative -> no positive value on any growth
print(f"literal window (all spending, acquisitions deducted): average {A:.1f} -> value negative on every case")
# cycle base (a): 2019-2023 maintenance OC (2019 OCF 114.9, SBC 4.5, D&A 26.9; 2020 OCF 43.9, SBC 4.7, D&A 27.0)
cyc = [114.9-4.5-26.9, 43.853-4.735-27.021] + oc_mnt[:3]
print(f"cycle 2019-2023 maintenance OC average {avg(cyc):.1f}")
# what the price asks: enterprise value at the price
ev = shares * 65.16 + net_debt + nci_stateline
print(f"EV at $65.16: {ev:.0f}; maintenance OC needed for 10% at no growth: {ev*F:.0f}/yr vs five-year average {M:.1f}")
