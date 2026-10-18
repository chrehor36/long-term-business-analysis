# Owner cash and the Q7 range for Alfa Laval, by hand from the annual reports (SEK million).
# Every input is typed from a filed statement; the source of each series is in notes.md.
import sys
sys.stdout.reconfigure(encoding="utf-8")
Y = list(range(2016, 2026))
# Ten-year overview, AR2025 p.150-151 (cash flow restated to the 2025 structure: interest and
# lease principal in financing)
ocf   = dict(zip(Y, [4979, 4463, 4883, 5784, 8154, 5658, 3737, 9694, 12778, 9166]))
capex = dict(zip(Y, [617, 675, 1490, 1337, 1232, 1229, 1853, 2440, 3336, 2660]))
sales = dict(zip(Y, [35634, 35314, 40666, 46517, 41468, 40911, 52135, 63598, 66954, 69674]))
ebitda = dict(zip(Y, [5323, 6239, 7495, 9251, 7569, 8113, 8911, 11780, 12853, 14252]))
ebita  = dict(zip(Y, [4680, 5610, 6869, 8178, 6435, 6922, 7462, 10221, 11089, 12334]))
# Cash flow statements of each year's report (AR2017, AR2019, AR2021, AR2022, AR2024, AR2025)
disp  = dict(zip(Y, [39, 23, 120, 7, 119, 24, 20, 90, 105, 155]))
acq   = dict(zip(Y, [230, 69, 0, 61, 70, 3828, 3685, 337, 50, 9412]))
divb  = dict(zip(Y, [13, 0, 77, 364, 125, 8, 0, 0, 0, 4]))
# old-structure OCF (lease principal inside operating liabilities); restated minus old = lease principal
old_ocf = {2019: 5223, 2020: 7723, 2021: 5264, 2022: 3291, 2023: 9169, 2024: 12159}
lease_p = {y: 0 for y in Y}
for y, v in old_ocf.items():
    lease_p[y] = ocf[y] - v
lease_p[2025] = 503                      # stated, AR2025 p.95
# lease interest, leasing notes (AR2019, AR2021, AR2022, AR2024, AR2025)
lease_i = {y: 0 for y in Y}
lease_i.update({2019: 71, 2020: 78, 2021: 74, 2022: 87, 2023: 94, 2024: 109, 2025: 159})
# right-of-use depreciation, same notes
rou_dep = {y: 0 for y in Y}
rou_dep.update({2019: 417, 2020: 436, 2021: 399, 2022: 470, 2023: 504, 2024: 565, 2025: 564})
# net interest paid incl. lease interest (financing section of each cash flow statement)
net_int = dict(zip(Y, [80, 46, 50, 161, 184, 131, 191, 321, 337, 357]))
dep_ex_stepup = {y: ebitda[y] - ebita[y] for y in Y}           # depreciation excl. step-up amortization
own_dep = {y: dep_ex_stepup[y] - rou_dep[y] for y in Y}         # owned PPE and intangibles

rows = []
for y in Y:
    oc_all = ocf[y] - capex[y] + disp[y] - lease_p[y] - lease_i[y]          # all spending, before purchases
    oc_mnt = ocf[y] - own_dep[y] + disp[y] - lease_p[y] - lease_i[y]        # maintenance only (guess = owned depreciation)
    net_acq = acq[y] - divb[y]
    oc_def = oc_all - net_acq                                              # default pair: purchases deducted
    eq_int = net_int[y] - lease_i[y]                                       # non-lease interest
    rows.append((y, oc_all, oc_mnt, net_acq, oc_def, eq_int))
print("year  OC_all  OC_maint  net_acq  OC_after_acq  nonlease_int  capex  own_dep  lease_p  lease_i  OC_all/sales")
for (y, a, m, q, d, e) in rows:
    print(f"{y}  {a:6d}  {m:8d}  {q:7d}  {d:12d}  {e:12d}  {capex[y]:5d}  {own_dep[y]:7d}  {lease_p[y]:7d}  {lease_i[y]:7d}  {a/sales[y]:.3f}")

W = [r for r in rows if r[0] >= 2021]
avg = lambda k: sum(r[k] for r in W) / len(W)
A_all, A_mnt, A_acq, A_def, A_int = avg(1), avg(2), avg(3), avg(4), avg(5)
growth_spend = A_mnt - A_all
print(f"\nwindow 2021-2025 averages: OC_all {A_all:.0f}  OC_maint {A_mnt:.0f}  growth spending {growth_spend:.0f}"
      f"  net_acq {A_acq:.0f}  OC_after_acq {A_def:.0f}  nonlease_int {A_int:.0f}")
sum_all = sum(r[1] for r in W); sum_acq = sum(r[3] for r in W)
print(f"serial-acquirer test: net purchases {sum_acq} vs half of OC before purchases {sum_all/2:.0f} -> {'SERIAL' if sum_acq > sum_all/2 else 'not serial'}")
g_end = (W[-1][1] / W[0][1]) ** (1 / 4) - 1
print(f"OC_all end-to-end growth 2021->2025 (aggregate): {g_end:.4f}")
org = {2022: 0.109, 2023: 0.123, 2024: 0.06, 2025: 0.08}   # filer's organic net sales growth
g_org = 1
for v in org.values():
    g_org *= 1 + v
g_org = g_org ** (1 / 4) - 1
g_sales = (sales[2025] / sales[2021]) ** (1 / 4) - 1
print(f"organic sales growth 2022-2025 compound: {g_org:.4f}; total sales growth 2021->2025: {g_sales:.4f}")
print(f"max OC_all/sales in filings read: {max(r[1]/sales[r[0]] for r in rows):.3f}")
# ten-year (cycle) base shown beside
T_all = sum(r[1] for r in rows) / 10; T_mnt = sum(r[2] for r in rows) / 10
print(f"ten-year averages 2016-2025: OC_all {T_all:.0f}  OC_maint {T_mnt:.0f}")

# ---------- valuation ----------
R = 0.03119
SH = 413.326315
ND = 12530          # net debt excl. leases, 2026-06-30 (Q2 2026 note 8); lease liabilities 3,484 left out
ND_incl = 16013
PRICE = 576.40
MCAP = PRICE * SH
EV = MCAP + ND

def pv(base, g, r, spend=0.0, spend_after=False):
    """ten years at g (cash base*(1+g)^t less growth spending spend*(1+g)^t), then flat on base*(1+g)^10
    (spend stops after year ten unless spend_after)."""
    v = 0.0
    for t in range(1, 11):
        v += (base - spend) * (1 + g) ** t / (1 + r) ** t
    c10 = (base - (spend if spend_after else 0)) * (1 + g) ** 10
    v += c10 / r / (1 + r) ** 10
    return v

def irr(base, g, price, spend=0.0, spend_after=False):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(base, g, mid, spend, spend_after) > price:
            lo = mid
        else:
            hi = mid
    return mid

print(f"\nprice {PRICE} x {SH} = MCAP {MCAP:.0f}; EV (excl. leases) {EV:.0f}")
cases = [
    ("CENTRAL organic pair, maintenance: no growth", A_mnt, 0.0, 0.0, False),
    ("CENTRAL organic pair, maintenance: organic growth, growth spending charged", A_mnt, g_org, growth_spend, False),
    ("beside: organic pair, all spending: no growth", A_all, 0.0, 0.0, False),
    ("beside: organic pair, all spending: organic growth (spending kept after yr10)", A_all, g_org, 0.0, False),
    ("beside: default pair (purchases deducted), no growth only (series changes sign)", A_def, 0.0, 0.0, False),
    ("beside: ten-year base maintenance, no growth", T_mnt, 0.0, 0.0, False),
]
res = {}
for name, b, g, s, sa in cases:
    v = pv(b, g, R, s, sa); v10 = pv(b, g, 0.10, s, sa)
    ps = (v - ND) / SH; ps10 = (v10 - ND) / SH
    e = irr(b, g, EV, s, sa)
    res[name] = (ps, ps10)
    print(f"{name}\n   base {b:.0f} g {g:.4f}: EV {v:.0f}  per share {ps:.2f}  | at 10%: {ps10:.2f}  | expected return at price {e:.4f}")

lo, hi = list(res.values())[0], list(res.values())[1]
print(f"\nCENTRAL range per share (all-equity, excl. leases): {lo[0]:.2f} to {hi[0]:.2f}  width {hi[0]/lo[0]:.2f}x")
print(f"FAIR (all-equity): ({lo[1]:.2f} + {hi[1]:.2f})/2 = {(lo[1]+hi[1])/2:.2f}")
# with leases counted in net debt instead (lease cash added back, lease liabilities in net debt) shown beside
LP = sum(lease_p[y] + lease_i[y] for y in range(2021, 2026)) / 5
lo_l = (pv(A_mnt + LP, 0, 0.10) - ND_incl) / SH
hi_l = (pv(A_mnt + LP, g_org, 0.10, growth_spend) - ND_incl) / SH
print(f"beside: leases as debt (lease cash {LP:.0f} added back, net debt {ND_incl}): fair {(lo_l+hi_l)/2:.2f}")
# equity-only: owner cash after non-lease interest, against market value, no net debt subtracted
E_mnt = A_mnt - A_int
elo = pv(E_mnt, 0, R) / SH; ehi = pv(E_mnt, g_org, R, growth_spend) / SH
elo10 = pv(E_mnt, 0, 0.10) / SH; ehi10 = pv(E_mnt, g_org, 0.10, growth_spend) / SH
print(f"EQUITY-ONLY range: {elo:.2f} to {ehi:.2f}; fair {(elo10+ehi10)/2:.2f}; expected return at price "
      f"{irr(E_mnt, 0, MCAP):.4f} / {irr(E_mnt, g_org, MCAP, growth_spend):.4f}")
print(f"owner-cash yield at price: maint {A_mnt/EV:.4f}  all {A_all/EV:.4f}")
