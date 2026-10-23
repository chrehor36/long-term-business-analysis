# COMPUTATION for Q7 of the MGEE run, 2026-10-23. Filed figures only (USD millions); every input is from the
# FY2022/FY2025 10-K statements or SEC XBRL as tabulated in the run file. No number is added by this script.
years = [2021, 2022, 2023, 2024, 2025]
ocf = [137.527, 153.735, 237.561, 277.784, 263.234]
capex = [153.169, 175.030, 222.071, 236.925, 343.220]
atc = [4.027, 5.185, 6.995, 4.792, 9.496]          # capital contributions to ATC and other investments
oth = [0.221, 0.070, -0.954, 0.230, 2.155]         # other investing, inflow positive
fl = [1.495, 1.304, 1.322, 1.323, 1.430]           # finance-lease principal
da = [76.983, 85.549, 100.352, 108.581, 114.324]
ltd_iss = [100.0, 25.0, 139.3, 50.0, 50.0]
ltd_rep = [4.771, 4.889, 54.314, 5.146, 5.285]
int_paid = [23.502, 25.957, 29.526, 34.306, 35.755]
taxcredit_sales = [0, 0, 0, 18.501, 10.996]        # deferred-tax line "proceeds from renewable tax credits transferred"
rev = [606.584, 714.519, 690.431, 676.944, 743.654]
ni = [105.761, 110.952, 117.699, 120.569, 135.889]
price, shares = 74.24, 37.784012
mcap = price * shares
r_gov, r_floor = 0.0529, 0.10
debt_share = 1 - 0.5606                             # PSCW 2025 test-year equity component 56.06%
net_debt = 879.104 + 20.509 + 34.750 - 16.621 + 19.588   # 10-Q 2026-06-30 debt less cash, plus finance leases (10-K 2025)
tax = 0.21 + 0.079 * (1 - 0.21)                     # federal plus Wisconsin 7.9% net of federal benefit
n = len(years)
avg = lambda xs: sum(xs) / len(xs)

oc_all = [ocf[i] - capex[i] - atc[i] + oth[i] - fl[i] for i in range(n)]
oc_maint = [ocf[i] - da[i] + oth[i] - fl[i] for i in range(n)]
net_ltd = sum(ltd_iss) - sum(ltd_rep)
gross_ltd = sum(ltd_iss)
cap_all = debt_share * sum(capex)
credit_all = min(net_ltd, cap_all)
growth_spend = [capex[i] - da[i] + atc[i] for i in range(n)]
cap_growth = debt_share * sum(capex[i] - da[i] for i in range(n))
credit_growth = min(net_ltd, cap_growth)
eq_growth_spend = (sum(growth_spend) - credit_growth) / n

print("market cap", round(mcap, 1), " net debt", round(net_debt, 1), " tax", round(tax, 4))
for i in range(n):
    print(years[i], "OC_all %.1f  OC_maint %.1f  OC_maint/sales %.1f%%  growth spend %.1f" %
          (oc_all[i], oc_maint[i], 100 * oc_maint[i] / rev[i], growth_spend[i]))
print("avg OC_all %.1f  avg OC_maint %.1f" % (avg(oc_all), avg(oc_maint)))
print("net LTD raised %.1f (gross %.1f); cap on all capex %.1f; cap on growth capex %.1f" % (net_ltd, gross_ltd, cap_all, cap_growth))
oc_all_cr = avg(oc_all) + credit_all / n
oc_all_cr_gross = avg(oc_all) + min(gross_ltd, cap_all) / n
print("OC all-spending with debt credit (net) %.1f; with gross issuance %.1f" % (oc_all_cr, oc_all_cr_gross))
print("equity-funded growth spend per year %.1f (credit %.1f)" % (eq_growth_spend, credit_growth))

# growth measures
g_oc = (oc_maint[-1] / oc_maint[0]) ** (1 / 4) - 1
g_rev = (rev[-1] / rev[0]) ** (1 / 4) - 1
g_ni = (ni[-1] / ni[0]) ** (1 / 4) - 1
print("shown growth OC_maint %.1f%%, sales %.2f%%, net income %.2f%%" % (100 * g_oc, 100 * g_rev, 100 * g_ni))
hi_share = max(oc_maint[i] / rev[i] for i in range(n))
base = avg(oc_maint)
print("OC_maint base x (1+g_oc)^10 = %.0f vs highest share of sales x sales10 = %.0f" %
      (base * (1 + g_oc) ** 10, hi_share * rev[-1] * (1 + g_rev) ** 10))

def pv_nogrowth(oc, r):
    return oc / r

def pv_growth(base, spend, g, r):
    pv = 0.0
    for t in range(1, 11):
        pv += (base * (1 + g) ** t - spend * (1 + g) ** (t - 1)) / (1 + r) ** t
    term = base * (1 + g) ** 10 / r   # zero growth after year ten; growth spending stops with growth
    return pv + term / (1 + r) ** 10

def irr(f, target):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > target: lo = mid
        else: hi = mid
    return mid

g = g_rev
cases = {
    "A no-growth, maintenance only (equity-only)": lambda r: pv_nogrowth(base, r),
    "B shown growth (sales-capped), growth spend charged net of debt credit (equity-only)": lambda r: pv_growth(base, eq_growth_spend, g, r),
}
print("\n-- central basis: equity-only (regulated utility), owner cash after interest and company tax --")
res = {}
for k, f in cases.items():
    v5, v10 = f(r_gov), f(r_floor)
    res[k] = (v5, v10)
    print("%s: at 5.29%% %.0fM = $%.2f/sh; at 10%% %.0fM = $%.2f/sh; IRR at price %.2f%%" %
          (k, v5, v5 / shares, v10, v10 / shares, 100 * irr(f, mcap)))
vals5 = sorted(v[0] / shares for v in res.values())
fair = avg([v[1] / shares for v in res.values()])
print("RANGE $%.2f to $%.2f; width %.2fx; FAIR (avg of ends at 10%%) $%.2f vs price $%.2f" % (vals5[0], vals5[1], vals5[1] / vals5[0], fair, price))
# forward settlement beside
sh2 = shares + 2.310232
print("with forwards settled (+2.310M sh, +$168.4M cash, equity-only adds the cash): fair $%.2f" %
      (avg([(v[1] + 168.4) / sh2 for v in res.values()])))

print("\n-- beside: all-spending case, equity-only with debt credit (no growth; series changes sign) --")
print("OC %.1f -> at 5.29%% $%.2f/sh, at 10%% $%.2f/sh; IRR %.2f%%" % (oc_all_cr, pv_nogrowth(oc_all_cr, r_gov) / shares,
      pv_nogrowth(oc_all_cr, r_floor) / shares, 100 * oc_all_cr / mcap))
print("same with gross issuance credited: OC %.1f -> $%.2f/sh at 5.29%%" % (oc_all_cr_gross, pv_nogrowth(oc_all_cr_gross, r_gov) / shares))

print("\n-- beside: all-equity basis (owner cash before interest, after tax; less net debt) --")
ati = avg(int_paid) * (1 - tax)
baseA = base + ati
casesA = {
    "A' no-growth maintenance": lambda r: pv_nogrowth(baseA, r) - net_debt,
    "B' growth, all growth spend charged (no debt credit)": lambda r: pv_growth(baseA, avg(growth_spend), g, r) - net_debt,
}
for k, f in casesA.items():
    print("%s: at 5.29%% $%.2f/sh; at 10%% $%.2f/sh; IRR %.2f%%" % (k, f(r_gov) / shares, f(r_floor) / shares, 100 * irr(lambda r: f(r) + net_debt, mcap + net_debt)))
print("all-equity fair $%.2f" % avg([f(r_floor) / shares for f in casesA.values()]))
oc_allA = avg(oc_all) + ati
print("all-equity all-spending OC %.1f -> at 5.29%% $%.2f/sh" % (oc_allA, (oc_allA / r_gov - net_debt) / shares))

print("\n-- beside: without the tax-credit sale proceeds (OBBBA phase-out) --")
base2 = base - avg(taxcredit_sales)
print("OC_maint ex credits %.1f; A $%.2f, B $%.2f at 5.29%%; fair $%.2f" % (base2, base2 / r_gov / shares,
      pv_growth(base2, eq_growth_spend, g, r_gov) / shares, avg([base2 / r_floor / shares, pv_growth(base2, eq_growth_spend, g, r_floor) / shares])))
print("\n-- beside: growth at net-income rate %.2f%% instead of sales --" % (100 * g_ni))
print("B at 5.29%% $%.2f; at 10%% $%.2f" % (pv_growth(base, eq_growth_spend, g_ni, r_gov) / shares, pv_growth(base, eq_growth_spend, g_ni, r_floor) / shares))
print("\nliteral window, net income (not used): avg NI %.1f -> /5.29%% $%.2f/sh" % (avg(ni), avg(ni) / r_gov / shares))

print("\n-- beside: IRR at price of the net-income-growth variant --")
print("IRR %.2f%%" % (100 * irr(lambda r: pv_growth(base, eq_growth_spend, g_ni, r), mcap)))
print("-- beside: 2021 working-capital draw ($36.5M, tied by the filer to the Feb 2021 gas-price event) added back --")
b3 = base + 36.5 / n
print("base %.1f; A $%.2f, B $%.2f at 5.29%%; IRR B %.2f%%" % (b3, b3 / r_gov / shares, pv_growth(b3, eq_growth_spend, g, r_gov) / shares,
      100 * irr(lambda r: pv_growth(b3, eq_growth_spend, g, r), mcap)))
print("dividend yield at price: %.2f%% (annualized $0.5083 x 4)" % (100 * 0.5083 * 4 / price))
