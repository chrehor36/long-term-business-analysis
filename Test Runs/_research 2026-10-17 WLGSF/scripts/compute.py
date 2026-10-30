"""COMPUTATION, NOT A CLEARANCE. Owner cash and the Q7 arithmetic from the filed statements (USD, as filed).
Sources: FY2024 20-F 0001641172-25-010670 (FY2022-2024); F-1/A 0001493152-23-009252 (FY2020-2021)."""
yrs = [2020, 2021, 2022, 2023, 2024]
ocf = {2020: -74380, 2021: -482801, 2022: -352764, 2023: -3814384, 2024: -1569940}
capex = {2020: 2926, 2021: 0, 2022: 0, 2023: 0, 2024: 0}
interest_paid = {2020: 49229, 2021: 13312, 2022: 35377, 2023: 59976, 2024: 127173}
net_inc = {2020: 278018, 2021: -354743, 2022: -596881, 2023: -648854, 2024: -2543959}
dep = {2020: 6196, 2021: 3629, 2022: 2603, 2023: 32413, 2024: 15037}
listing = {2020: 0, 2021: 354743, 2022: 328699, 2023: 1241199, 2024: 190506}
rev = {2020: 4074258, 2021: 4135059, 2022: 4169931, 2023: 6825879, 2024: 3951649}
oc = {y: ocf[y] - capex[y] for y in yrs}
avg = lambda d: sum(d[y] for y in yrs) / 5
print("owner cash (OCF less capex):", oc, "avg", round(avg(oc)))
ocb = {y: oc[y] + interest_paid[y] for y in yrs}
print("owner cash before interest:", ocb, "avg", round(avg(ocb)))
nwc = {y: net_inc[y] + dep[y] for y in yrs}
print("variant before working capital (net income + depreciation):", nwc, "avg", round(avg(nwc)))
nl = {y: nwc[y] + listing[y] for y in yrs}
print("variant before working capital, listing fees added back:", nl, "avg", round(avg(nl)))
print("revenue CAGR 2020-2024: %.2f%%" % (((rev[2024] / rev[2020]) ** 0.25 - 1) * 100))
# net debt at 2024-12-31 (FY2024 balance sheet) plus the subsequent event the filing states
borrow = 1890316 + 447086; fin_lease = 11125 + 24489; cash = 4304514; director = 1366738
solar = 1935484
nd_core = borrow + fin_lease - cash
nd_dir = nd_core + director
nd_all = nd_dir + solar
print("net debt: bank+finance lease-cash", nd_core, "| with director payables", nd_dir, "| with Solar HK note (stated subsequent event)", nd_all)
for r, lab in ((0.0543, "USD 30y stand-in 5.43%"), (0.10, "floor 10%")):
    v_ae = avg(ocb) / r - nd_all          # all-equity basis, no growth, perpetuity at zero nominal growth
    v_eq = avg(oc) / r                    # equity-only: owner cash after interest
    print(f"{lab}: whole-business value all-equity {avg(ocb)/r:,.0f}; less net debt -> equity {v_ae:,.0f}; equity-only {v_eq:,.0f}")
    for sh, sl in ((17357924, "17,357,924 (FY2024 cover)"), (698719, "698,719 (post-combination, 6-K 2025-08-21)")):
        print(f"   per share on {sl}: all-equity {v_ae/sh:,.4f}; equity-only {v_eq/sh:,.4f}")
