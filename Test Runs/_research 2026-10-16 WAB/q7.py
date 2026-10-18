# Q7 arithmetic for the WAB run of 2026-10-16. COMPUTATION only; every input is a filed figure (USD millions).
# Sources: consolidated statements of cash flows and income, FY2022 10-K (0001628280-23-003675) for 2021-2022,
# FY2025 10-K (0001628280-26-008067) for 2023-2025; organic sales bridges from the FY2021-FY2025 10-Ks (Item 7);
# net debt from the 10-Q to 2026-06-30 (0001628280-26-049139); shares from its cover.
R = 0.0543          # 30-year US Treasury par yield, 2026-10-15
FLOOR = 0.10        # Q7 floor CONVENTION, about ten percent
YEARS = [2021, 2022, 2023, 2024, 2025]
OCF   = [1073, 1038, 1201, 1834, 1759]
SBC   = [46, 41, 47, 66, 80]            # cash-flow add-back
CAPEX = [130, 149, 186, 207, 260]
DA    = [491, 479, 531, 503, 501]
AMORT = [287, 291, 321, 303, 300]       # amortization expense line (purchased intangibles)
INT   = [177, 186, 218, 201, 225]       # interest expense, net
TAX   = [172, 213, 267, 343, 409]
PBT   = [737, 854, 1092, 1410, 1592]
ACQ   = [435, 89, 308, 168, 2520]       # acquisitions of businesses, net of cash acquired
DISP  = [0, 0, 0, 19, 8]                # proceeds from dispositions of businesses
FXACQ = [0, 0, 0, 0, 20]                # settlement of FX derivatives related to acquisition (inflow)
CONT  = [99, 101, 112, 42, 0]           # contingent consideration paid (GE Transportation deal)
SALES = [7822, 8362, 9677, 10387, 11167]
ORG   = [-6/7556, 757/7822, 1204/8362, 662/9677, 464/10387]   # filer's organic sales change by year
NET_DEBT = 1656 + 4915 - 670            # 2026-06-30: current + long-term debt less cash
SHARES = 168.910851
PRICE = 287.32
MCAP = PRICE * SHARES
EV = MCAP + NET_DEBT

dep = [d - a for d, a in zip(DA, AMORT)]
etr = [t / p for t, p in zip(TAX, PBT)]
ati = [i * (1 - e) for i, e in zip(INT, etr)]
oc_all = [o - s - c + x for o, s, c, x in zip(OCF, SBC, CAPEX, ati)]      # all spending, before interest
oc_mnt = [o - s - d + x for o, s, d, x in zip(OCF, SBC, dep, ati)]        # maintenance = depreciation
acq_net = [a - d - f + k for a, d, f, k in zip(ACQ, DISP, FXACQ, CONT)]
avg = lambda v: sum(v) / len(v)

def cagr(a, b, n): return (b / a) ** (1 / n) - 1
g_org = 1.0
for x in ORG[1:]: g_org *= (1 + x)
g_org = g_org ** (1 / 4) - 1                       # 2021 -> 2025, four steps
g_sales = cagr(SALES[0], SALES[-1], 4)
g_tot = cagr(oc_mnt[0], oc_mnt[-1], 4)

def value(c0, g, r, purchases0=0.0, c0_before=None):
    """c0 grows at g for ten years then is flat; discounted at r. purchases0 (if given) is deducted
    in years 1-10, growing at g, and stops after year ten (terminal on c0_before)."""
    v, c, p = 0.0, c0, purchases0
    cb = c0_before if c0_before is not None else c0
    for t in range(1, 11):
        c *= (1 + g); p *= (1 + g); cb *= (1 + g) if c0_before is not None else 1
        v += (c - p) / (1 + r) ** t
    term = (cb if c0_before is not None else c) / r
    return v + term / (1 + r) ** 10

def irr(fn, target):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if fn(mid) > target: lo = mid
        else: hi = mid
    return mid

out = []
P = lambda *a: out.append(" ".join(str(x) for x in a))
P("year      " + " ".join(f"{y:>8}" for y in YEARS) + "   avg")
for name, s in [("oc_all", oc_all), ("oc_mnt", oc_mnt), ("dep", dep), ("ati", ati), ("acq_net", acq_net)]:
    P(f"{name:10}" + " ".join(f"{x:8.1f}" for x in s) + f" {avg(s):8.1f}")
P(f"etr {[round(e,3) for e in etr]}")
P(f"g_org {g_org:.4f}  g_sales {g_sales:.4f}  g_total_ownercash(mnt) {g_tot:.4f}")
P(f"price {PRICE} shares {SHARES} mcap {MCAP:.0f} net_debt {NET_DEBT} EV {EV:.0f}")

base_m = avg(oc_mnt); base_a = avg(oc_all); base_acq = avg(acq_net)
avg_sales = avg(SALES)
hi_share = max(o / s for o, s in zip(oc_mnt, SALES))
P(f"base maintenance {base_m:.1f}; all-spending {base_a:.1f}; avg net purchases {base_acq:.1f}; highest owner-cash share of sales {hi_share:.3f}")

# cap test (f) for organic growth: share of sales after ten years if sales grow at the same organic rate
share10_org = base_m * (1 + g_org) ** 10 / (avg_sales * (1 + g_org) ** 10)
P(f"cap test organic: share at year 10 {share10_org:.3f} (sales at the same organic rate) vs highest {hi_share:.3f}")
share10_tot = base_m * (1 + g_tot) ** 10 / (avg_sales * (1 + g_sales) ** 10)
P(f"cap test total: owner cash at total growth {g_tot:.4f} vs sales at {g_sales:.4f}: share at year 10 {share10_tot:.3f}")
g_def = g_sales if share10_tot > hi_share else g_tot
P(f"default-pair growth carried: {g_def:.4f} ({'cut to sales growth' if g_def == g_sales else 'shown rate'})")

cases = {}
# ORGANIC PAIR (central under the serial-acquirer convention), maintenance case central
cases["org_mnt_nog"] = lambda r: value(base_m, 0.0, r)
cases["org_mnt_g"]   = lambda r: value(base_m, g_org, r)
cases["org_all_nog"] = lambda r: value(base_a, 0.0, r)
cases["org_all_g"]   = lambda r: value(base_a, g_org, r)
# DEFAULT PAIR beside: purchases deducted, total growth credited (cut by the cap), purchases stop after year ten
cases["def_nog"] = lambda r: value(base_m, 0.0, r)
cases["def_g"]   = lambda r: value(base_m, g_def, r, purchases0=base_acq, c0_before=base_m)
for k, f in cases.items():
    v_r = f(R); v_f = f(FLOOR); ret = irr(f, EV)
    P(f"{k:12} value@{R:.4f} {v_r:9.0f}  per share {(v_r-NET_DEBT)/SHARES:8.2f} | value@10% {v_f:9.0f} | expected return at EV {ret:.4f}")

def fair(nog, g):
    return ((cases[nog](FLOOR) + cases[g](FLOOR)) / 2 - NET_DEBT) / SHARES
P(f"FAIR all-equity organic maintenance (central): {fair('org_mnt_nog','org_mnt_g'):.2f}")
P(f"FAIR all-equity organic all-spending: {fair('org_all_nog','org_all_g'):.2f}")
P(f"FAIR all-equity default pair: {fair('def_nog','def_g'):.2f}")

# EQUITY-ONLY beside: owner cash after interest, against market value, no net debt
base_eq = base_m - avg(ati)
ve = lambda g, r: value(base_eq, g, r)
fair_eq = ((ve(0, FLOOR) + ve(g_org, FLOOR)) / 2) / SHARES
ret_eq_g = irr(lambda r: ve(g_org, r), MCAP); ret_eq_n = irr(lambda r: ve(0, r), MCAP)
P(f"equity-only base {base_eq:.1f}; range per share @R {ve(0,R)/SHARES:.2f} to {ve(g_org,R)/SHARES:.2f}; FAIR equity-only {fair_eq:.2f}; expected return at market cap {ret_eq_n:.4f} / {ret_eq_g:.4f}")

# Range per share (all-equity) at the long rate
lo = (cases["org_mnt_nog"](R) - NET_DEBT) / SHARES; hi = (cases["org_mnt_g"](R) - NET_DEBT) / SHARES
P(f"RANGE central (organic, maintenance) per share: {lo:.2f} to {hi:.2f}; width {hi/lo:.2f}x; price {PRICE}")
lo2 = (cases["org_all_nog"](R) - NET_DEBT) / SHARES; hi2 = (cases["org_all_g"](R) - NET_DEBT) / SHARES
P(f"RANGE all-spending beside: {lo2:.2f} to {hi2:.2f}")
lo3 = (cases["def_nog"](R) - NET_DEBT) / SHARES; hi3 = (cases["def_g"](R) - NET_DEBT) / SHARES
P(f"RANGE default pair beside: {lo3:.2f} to {hi3:.2f}")
# Sensitivity, not a price figure: what owner cash before interest would the 10% floor need at today's EV, at organic growth?
need = EV / value(1.0, g_org, FLOOR)
P(f"owner cash needed (base, growing at organic rate) for 10% at EV: {need:.0f} vs base {base_m:.0f}")
open("q7_output.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out))
