# LCID owner earnings from the filed cash-flow faces ($M): OCF - SBC - (c), (c) at the capex end and the D&A end.
# Sources: FY2025 10-K (FY2023-25), FY2023 10-K (FY2021-22 D&A, SBC, capex), Q2 2026 10-Q (H1 2026, H1 2025).
Y = {  # ocf, sbc, capex, da
 "FY2021": (-1058.133, 516.757, 421.220, 62.907),
 "FY2022": (-2226.258, 423.500, 1074.852, 186.583),
 "FY2023": (-2489.753, 257.283, 910.644, 233.531),
 "FY2024": (-2019.674, 285.872, 883.841, 295.337),
 "FY2025": (-2931.912, 271.275, 868.158, 451.243),
}
H1_26 = (-2407.890, 107.639, 506.994, 238.634); H1_25 = (-1258.854, 83.834, 343.904, 209.047)
TTM = tuple(a - b + c for a, b, c in zip(Y["FY2025"], H1_25, H1_26))
rows = dict(Y); rows["TTM 2026-06"] = TTM; rows["H1 2026"] = H1_26
oe = {}
for k, (o, s, cx, da) in rows.items():
    oe[k] = (o - s - cx, o - s - da)
    print(f"{k:12s} OCF {o:9.1f} SBC {s:7.1f} capex {cx:8.1f} D&A {da:6.1f} | OE capex-end {o-s-cx:9.1f} | OE D&A-end {o-s-da:9.1f}")
def mean(keys, i): return sum(oe[k][i] for k in keys) / len(keys)
w5 = ["FY2021","FY2022","FY2023","FY2024","FY2025"]; w4 = w5[1:]; w3 = w5[2:]
for nm, w in (("5y FY2021-25", w5), ("4y FY2022-25", w4), ("3y FY2023-25", w3)):
    print(f"{nm}: capex-end {mean(w,0):9.1f}  D&A-end {mean(w,1):9.1f}")
cap = 4.09 * 394070176 / 1e6
print(f"cap {cap:.1f}")
for nm, w in (("5y", w5), ("3y", w3)):
    print(nm, "yield capex-end", f"{mean(w,0)/cap:.1%}", "D&A-end", f"{mean(w,1)/cap:.1%}")
print("TTM yield", f"{oe['TTM 2026-06'][0]/cap:.1%}", f"{oe['TTM 2026-06'][1]/cap:.1%}")
print("floor needs +", f"{0.10*cap:.1f}", "a year; sovereign-equal needs +", f"{0.0534*cap:.1f}")
# the preferred's accruing claim: 9% compounding on $3,069.9M
print("preferred PIK at 9% on 3069.9:", round(0.09*3069.913,1))
