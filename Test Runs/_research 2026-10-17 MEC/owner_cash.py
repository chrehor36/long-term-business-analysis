# Owner cash by year from the filed cash-flow statements (USD thousands). Sources: 10-K FY2019..FY2025, 10-Q Q2 2026.
data = {  # OCF, SBC, capex, PP&E proceeds, finance lease principal, acquisitions, interest paid
 2019: (33402, 3486, 25797, 76, 469, 2369, 6629),
 2020: (36523, 4732, 7794, 2020, 598, 0, 3011),
 2021: (14457, 4962, 39309, 5348, 544, 0, 2122),
 2022: (52426, 3759, 58610, 7942, 322, 0, 3670),
 2023: (40363, 4485, 16598, 1059, 404, 88593, 10669),
 2024: (89807, 5186, 12098, 386, 607, 0, 10267),
 2025: (38562, 3278, 11648, 72, 1034, 139954, 9710),
 "H1-2026": (-1325, 2302, 12263, 6, 1227, 0, 6981),
}
dep = {2019: 22296, 2020: 21383, 2021: 21077, 2022: 22359, 2023: 27338, 2024: 30655, 2025: 31570}
TAX = 0.25  # CONVENTION of this run: 21% federal plus state, see run file
oc, oc_pre, oc_dep = {}, {}, {}
for y, (ocf, sbc, cap, pro, fl, acq, intr) in data.items():
    oc[y] = ocf - sbc - cap + pro - fl
    oc_pre[y] = oc[y] + intr * (1 - TAX)
    if y in dep: oc_dep[y] = ocf - sbc - dep[y] - fl + intr * (1 - TAX)
    print(y, f"owner cash {oc[y]/1e3:7.1f}", f"before interest (after tax) {oc_pre[y]/1e3:7.1f}", f"D&A basis before interest {oc_dep.get(y, 0)/1e3:7.1f}", f"acq {acq/1e3:6.1f}")
def mean(d, ys): return sum(d[y] for y in ys) / len(ys) / 1e3
w5, cyc = range(2021, 2026), range(2020, 2026)
print("equity basis mean 2021-25", round(mean(oc, w5), 2), " cycle 2020-25", round(mean(oc, cyc), 2))
print("all-equity mean 2021-25", round(mean(oc_pre, w5), 2), " cycle 2020-25", round(mean(oc_pre, cyc), 2))
print("D&A-basis all-equity cycle 2020-25", round(mean(oc_dep, cyc), 2), " 2021-25", round(mean(oc_dep, w5), 2))
acq_w5 = sum(data[y][5] for y in w5) / 1e3; acq_c = sum(data[y][5] for y in cyc) / 1e3
pre_purch_w5 = sum(oc[y] for y in w5) / 1e3
print("net purchases 2021-25", acq_w5, " owner cash before purchases 2021-25", round(pre_purch_w5, 1), " serial acquirer:", acq_w5 > pre_purch_w5 / 2)
print("default pair base (acq deducted) cycle", round(mean(oc_pre, cyc) - acq_c / 6, 2), " window", round(mean(oc_pre, w5) - acq_w5 / 5, 2))
# Q7 arithmetic
r, floor, n10 = 0.0543, 0.10, 25.500331
net_debt = 125.718 + 1.375 + (1.047 + 1.857 + 8.150 - 1.227) - 2.203  # revolver + Fond du Lac note + finance leases est. - cash, 2026-06-30
mcap = n10 * 13.90; ev = mcap + net_debt
print("net debt", round(net_debt, 2), " mcap", round(mcap, 1), " EV", round(ev, 1))
for label, base in [("capex, cycle", mean(oc_pre, cyc)), ("capex, literal window", mean(oc_pre, w5)), ("D&A variant, cycle", mean(oc_dep, cyc))]:
    v = base / r; ps = (v - net_debt) / n10; fair = (base / floor - net_debt) / n10
    print(f"{label}: base {base:.2f}  value at sovereign {v:.1f}  per share {ps:.2f}  yield on EV {base/ev*100:.2f}%  fair at 10% {fair:.2f}")
eq_cyc = mean(oc, cyc)
print("equity-only: base", round(eq_cyc, 2), " fair at 10% per share", round(eq_cyc / floor / n10, 2), " yield on mcap", round(eq_cyc / mcap * 100, 2))
