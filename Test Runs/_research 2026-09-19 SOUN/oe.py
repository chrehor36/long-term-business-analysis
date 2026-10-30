# SOUN owner earnings from the filed cash-flow faces ($M): OCF - SBC - (c).
# (c) capex end = PP&E purchases + capitalised software (cash) + finance-lease principal; D&A end = depreciation and amortisation
# (mostly amortisation of acquired intangibles from FY2024). SBC = the cash-flow add-back plus SBC capitalised into software (FY2025 on).
# Sources: FY2022 10-K (FY2021-22), FY2025 10-K (FY2023-25), Q2 2026 10-Q (H1 2026, H1 2025).
Y = {  # ocf, sbc_addback, sbc_capitalised, ppe, capsw, fin_lease, da
 "FY2021": (-66.177, 6.322, 0.0, 0.636, 0.0, 2.575, 5.502),
 "FY2022": (-94.019, 28.792, 0.0, 1.329, 0.0, 1.303, 4.037),
 "FY2023": (-68.265, 27.931, 0.0, 0.392, 0.0, 0.159, 2.313),
 "FY2024": (-108.878, 33.145, 0.0, 0.640, 0.0, 0.125, 16.054),
 "FY2025": (-98.222, 80.620, 2.431, 0.902, 4.000, 0.169, 34.130),
}
H1_26 = (-59.969, 39.168, 1.889, 0.822, 5.404, 0.197, 21.071)
H1_25 = (-43.682, 41.250, 0.0, 0.354, 0.0, 0.029, 15.529)
TTM = tuple(a - b + c for a, b, c in zip(Y["FY2025"], H1_25, H1_26))
rows = dict(Y); rows["TTM 2026-06"] = TTM; rows["H1 2026"] = H1_26
oe = {}
for k, (o, s1, s2, ppe, csw, fl, da) in rows.items():
    s = s1 + s2; cx = ppe + csw + fl
    oe[k] = (o - s - cx, o - s - da)
    print(f"{k:12s} OCF {o:8.1f} SBC {s:6.1f} capex-end(c) {cx:5.1f} D&A {da:5.1f} | OE capex-end {o-s-cx:8.1f} | OE D&A-end {o-s-da:8.1f} | SBC/|OCF| n/a (OCF<0)")
def mean(keys, i): return sum(oe[k][i] for k in keys) / len(keys)
w5 = ["FY2021","FY2022","FY2023","FY2024","FY2025"]; w3 = w5[2:]; w4 = w5[1:]
for nm, w in (("5y FY2021-25", w5), ("4y FY2022-25", w4), ("3y FY2023-25", w3)):
    print(f"{nm}: capex-end {mean(w,0):8.1f}  D&A-end {mean(w,1):8.1f}")
caps = {"cover 444,109,844": 5.93*444109844/1e6, "pro forma 484.0M": 5.93*484.0e6/1e6, "pro forma 486.8M": 5.93*486.77e6/1e6}
for cn, cap in caps.items():
    print(f"cap {cn}: ${cap:,.1f}M")
    for nm, w in (("5y", w5), ("3y", w3)):
        print("  ", nm, "yield capex-end", f"{mean(w,0)/cap:.1%}", "D&A-end", f"{mean(w,1)/cap:.1%}")
    print("   TTM yield", f"{oe['TTM 2026-06'][0]/cap:.1%}", f"{oe['TTM 2026-06'][1]/cap:.1%}")
    print("   floor needs +", f"{0.10*cap:,.1f}", "a year; sovereign-equal needs +", f"{0.0534*cap:,.1f}")
# grant value of RSUs [E3-70]
print("RSU grant value FY2024", 14009111*4.14/1e6, "FY2025", 13628889*12.34/1e6)
print("5y SBC sum", sum(Y[k][1]+Y[k][2] for k in w5), "5y OCF sum", sum(Y[k][0] for k in w5))
