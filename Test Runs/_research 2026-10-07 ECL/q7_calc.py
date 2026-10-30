# Q7 arithmetic for the ECL run of 2026-10-07. Inputs transcribed from the filed cash-flow statements
# (FY2022 10-K 0001558370-23-001969 for 2021-2022; FY2025 10-K 0001104659-26-018357 for 2023-2025),
# 10-Q 0001628280-26-053886 for net debt. Arithmetic only; no verdict.
r = 0.0564                      # US Treasury 30-year par yield, 2026-10-06
floor = 0.10                    # CONVENTION, Q7 floor
yrs = [2021, 2022, 2023, 2024, 2025]
ocf   = [2061.9, 1788.4, 2411.8, 2813.9, 2952.6]
sbc   = [89.5, 87.8, 95.1, 134.8, 136.6]
capex = [643.0, 712.8, 774.8, 994.5, 1048.3]
dep   = [604.4, 618.5, 616.7, 634.9, 672.6]
intpd = [208.7, 222.4, 324.8, 342.6, 302.6]      # net interest paid, supplemental cash flow
tax   = [270/1414, 234/1343, 362/1756, 439/2571, 455/2548]  # provision / pre-tax income, company's own rate
acq   = [3923.7, 7.2, 180.4, 312.9, 1621.3]      # acquisitions and investments in affiliates, net of cash acquired
div   = [0.0, 0.0, 0.0, 889.7, -14.9]            # divestitures, net
org   = [0.05, 0.13, 0.09, 0.04, 0.03]           # organic (acquisition-adjusted fixed-currency) sales change as filed
shares = 280.328603                               # cover, 10-Q 2026-06-30
price = 279.25                                    # aggregator quote 2026-10-07, flagged
debt = 1271.1 + 11905.1; cash = 5135.3; coolit = 4750.0
netdebt = debt - cash + coolit
eq_oc  = [o - s - c for o, s, c in zip(ocf, sbc, capex)]
ae_oc  = [e + i * (1 - t) for e, i, t in zip(eq_oc, intpd, tax)]
mnt_ae = [o - s - d + i * (1 - t) for o, s, d, i, t in zip(ocf, sbc, dep, intpd, tax)]
netacq = [a - v for a, v in zip(acq, div)]
avg = lambda x: sum(x) / len(x)
def cagr(x): return (x[-1] / x[0]) ** (1 / (len(x) - 1)) - 1
def value(base, g, rate):
    v, c = 0.0, base
    for t in range(1, 11):
        c *= (1 + g); v += c / (1 + rate) ** t
    return v + c / rate / (1 + rate) ** 10       # zero nominal growth after year ten
def show(label, base, g):
    lo, hi = value(base, 0, r), value(base, g, r)
    lo, hi = min(lo, hi), max(lo, hi)
    ps = lambda v: (v - netdebt) / shares
    print(f"{label:52s} base {base:8.1f} g {g:6.2%}  whole ${lo:9,.0f}-{hi:9,.0f}M  per share ${ps(lo):7.2f}-{ps(hi):7.2f}  width {hi/lo if lo>0 else float('nan'):.2f}")
    return lo, hi
for n, x in [("equity-only owner cash", eq_oc), ("all-equity owner cash", ae_oc), ("all-equity maintenance-only (dep.)", mnt_ae), ("net acquisitions", netacq)]:
    print(f"{n:38s}", " ".join(f"{v:8.1f}" for v in x), f" avg {avg(x):8.1f}")
g_tot = cagr(ae_oc); g_org = 1
for o in org: g_org *= (1 + o)
g_org = g_org ** (1 / 5) - 1
print(f"total growth all-equity 2021-25 {g_tot:.2%}; organic sales growth compound {g_org:.2%}; net debt ${netdebt:,.1f}M; EV at price ${price*shares+netdebt:,.0f}M")
print("--- ranges (all-equity, at the sovereign) ---")
A = show("default: acquisitions deducted, total growth", avg(ae_oc) - avg(netacq), g_tot)
B = show("beside: acquisitions left out, organic growth", avg(ae_oc), g_org)
C = show("beside: maintenance-only (depreciation), organic", avg(mnt_ae), g_org)
D = show("literal: acquisitions left out, TOTAL growth (not allowed)", avg(ae_oc), g_tot)
# fair price: the midpoint growth case discounted at the floor
def fair(base, g):
    gm = g / 2
    v = value(base, gm, floor)
    return v, (v - netdebt) / shares
for lab, base, g in [("default", avg(ae_oc) - avg(netacq), g_tot), ("organic pair", avg(ae_oc), g_org), ("maintenance-only", avg(mnt_ae), g_org)]:
    v, p = fair(base, g); print(f"fair price {lab:18s} whole ${v:9,.0f}M  per share ${p:8.2f}")
# equity-only figure beside: owner cash after interest, against market value only
eq_base_org = avg(eq_oc)
v = value(eq_base_org, g_org / 2, floor); print(f"fair price equity-only, organic pair: ${v/shares:8.2f} a share (no net debt deducted; owner cash after interest)")
v = value(avg(eq_oc) - avg(netacq), cagr(eq_oc) / 2, floor); print(f"fair price equity-only, default: ${v/shares:8.2f} a share")
print(f"return at price, no growth, organic base: {avg(ae_oc)/(price*shares+netdebt):.2%}")
