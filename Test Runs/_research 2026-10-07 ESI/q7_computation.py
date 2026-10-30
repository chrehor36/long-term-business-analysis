# ESI run 2026-10-07: Q7 arithmetic. Inputs are filed figures (10-K FY2021-FY2025, 10-Q 2026-06-30); see run file.
# COMPUTATION, NOT A CLEARANCE when the file closed before Q7.
r = 0.0564          # US Treasury 30-year par yield, 2026-10-06 (tools/sources.py)
floor = 0.10        # Q7 floor CONVENTION, about ten percent
tax = 0.21          # CONVENTION of this run: net interest added back at the US statutory 21%
yrs = [2021, 2022, 2023, 2024, 2025]
ocf = [326.0, 295.9, 333.6, 362.0, 289.8]
sbc = [40.1, 17.7, 9.4, 14.8, 59.1]
capex = [46.3, 47.8, 52.7, 68.4, 62.2]
netint = [54.2, 51.2, 49.3, 56.3, 53.4]          # interest expense, net (income statement)
acq = [536.5, 22.6, 214.8, 3.9, -321.2]          # businesses bought, net of businesses sold
org = {2022: .05, 2023: -.05, 2024: .04, 2025: .06}  # organic net sales growth as filed (2021: +13%)
shares = 243.690914  # cover, 10-Q filed 2026-07-28
net_debt = 2119.4 - 189.6   # total debt less cash, 2026-06-30
deals_after = 367 + 494     # EFC + Micromax purchase prices, 10-Q note 2
price = 36.62

oc = [o - s - c for o, s, c in zip(ocf, sbc, capex)]
ocu = [x + i * (1 - tax) for x, i in zip(oc, netint)]
mean = lambda v: sum(v) / len(v)
def cagr(a, b, n): return (b / a) ** (1 / n) - 1
def value(c, g, rate):
    s = sum(c * (1 + g) ** t / (1 + rate) ** t for t in range(1, 11))
    return s + c * (1 + g) ** 10 / rate / (1 + rate) ** 10
print("owner cash after interest", [round(x, 1) for x in oc], "mean", round(mean(oc), 1))
print("owner cash before interest", [round(x, 1) for x in ocu], "mean", round(mean(ocu), 1))
print("acquisitions net mean", round(mean(acq), 1))
g_lit_u = cagr(ocu[0], ocu[-1], 4); g_half_u = cagr(mean(ocu[:2]), mean(ocu[3:]), 3)
g_lit_e = cagr(oc[0], oc[-1], 4); g_half_e = cagr(mean(oc[:2]), mean(oc[3:]), 3)
g_org = 1
for y in (2022, 2023, 2024, 2025): g_org *= 1 + org[y]
g_org = g_org ** 0.25 - 1
print(f"growth unlevered literal {g_lit_u:.2%} halves {g_half_u:.2%}; equity literal {g_lit_e:.2%} halves {g_half_e:.2%}; organic {g_org:.2%}")
def report(label, base, g_ends, less, extra_less=0.0):
    lo_g, hi_g = min(g_ends), max(g_ends)
    v = sorted(value(base, g, r) for g in (lo_g, hi_g))
    ps = [(x - less - extra_less) / shares for x in v]
    mid_g = (lo_g + hi_g) / 2
    fair = (value(base, mid_g, floor) - less - extra_less) / shares
    print(f"{label}: base {base:.1f}, growth ends {lo_g:.2%}..{hi_g:.2%}: whole {v[0]:.0f}..{v[1]:.0f}M -> ${ps[0]:.2f}..${ps[1]:.2f}/sh; fair price (midpoint growth {mid_g:.2%} at 10%) ${fair:.2f}")
print("--- ALL-EQUITY basis (central): owner cash before interest, less net debt at 2026-06-30", round(net_debt, 1))
report("default, cycle reading (halves)", mean(ocu) - mean(acq), (g_half_u, 0.0), net_debt)
report("default, literal window", mean(ocu) - mean(acq), (g_lit_u, 0.0), net_debt)
report("organic pair", mean(ocu), (g_org, 0.0), net_debt)
print("--- EQUITY-ONLY (beside): owner cash after interest, less the 2026 deals' price", deals_after)
report("default, cycle reading (halves)", mean(oc) - mean(acq), (g_half_e, 0.0), 0, deals_after)
report("default, literal window", mean(oc) - mean(acq), (g_lit_e, 0.0), 0, deals_after)
report("organic pair", mean(oc), (g_org, 0.0), 0, deals_after)
print("market cap", round(price * shares, 0), "EV", round(price * shares + net_debt, 0))
print("owner cash yield on EV (before interest, 5yr mean)", f"{mean(ocu)/(price*shares+net_debt):.2%}")
