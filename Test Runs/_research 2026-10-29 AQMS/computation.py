# AQMS Q7 COMPUTATION, NOT A CLEARANCE (run of 2026-10-29). Figures USD millions, from the 10-K cash-flow
# statements as transcribed by tools/run.py and checked for FY2025 against 0001437749-26-010705.
years = [2021, 2022, 2023, 2024, 2025]
ocf   = [-7.06, -10.15, -3.19, -13.63, -10.25]   # net cash used in operating activities
sbc   = [2.20, 2.25, 2.53, 2.74, 2.27]          # stock-based compensation (2025 excludes 0.261 stock for consultants)
capex = [2.35, 4.77, 5.60, 7.92, 0.42]          # purchases of property, plant and equipment
intp  = [0.084, 0.084, 0.480, 0.333, 0.528]     # interest paid, net (XBRL InterestPaidNet)
oe = [o - s - c for o, s, c in zip(ocf, sbc, capex)]
oe_alt = [x - 0.261 if y == 2025 else x for x, y in zip(oe, years)]  # consulting stock counted as pay
mean_eq = sum(oe) / 5
mean_ae = sum(o + i for o, i in zip(oe, intp)) / 5
sov, floor = 0.0537, 0.10
shares = 3.563531                                # cover, 10-Q 0001437749-26-025091, as of 2026-07-24
cash, fin_lease = 4.744, 0.122                   # 2026-06-30 balance sheet, same 10-Q
net_debt = fin_lease - cash
price = 1.45
def pv(cf, r):  # ten years flat then zero nominal growth = a perpetuity
    return cf / r
print("owner cash by year:", dict(zip(years, [round(x, 2) for x in oe])))
print("alt (consulting stock counted):", [round(x, 2) for x in oe_alt])
print("five-year mean, equity-only: %.2f  all-equity (interest added back): %.2f" % (mean_eq, mean_ae))
print("halves: first two years %.2f, last two %.2f" % (sum(oe[:2]) / 2, sum(oe[3:]) / 2))
for lab, m in (("all-equity", mean_ae), ("equity-only", mean_eq)):
    v_sov = pv(m, sov); v_10 = pv(m, floor)
    if lab == "all-equity":
        ps_sov = (v_sov - net_debt) / shares; ps_10 = (v_10 - net_debt) / shares
    else:
        ps_sov = v_sov / shares; ps_10 = v_10 / shares
    print("%s: value at sovereign %.1fM -> %.2f/share; at 10%% %.1fM -> fair %.2f/share" % (lab, v_sov, ps_sov, v_10, ps_10))
print("market cap %.2fM; net debt %.3fM (net cash)" % (price * shares, net_debt))
print("expected owner-cash return at the price, all-equity: %.0f%%" % (100 * mean_ae / (price * shares + net_debt)))
