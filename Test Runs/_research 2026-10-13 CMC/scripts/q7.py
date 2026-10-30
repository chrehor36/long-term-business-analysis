"""COMPUTATION, NOT A CLEARANCE. CMC owner cash and the Q7 range by the framework's convention. $M."""
yrs = list(range(2016, 2026))
ocf  = dict(zip(yrs, [586.9, -523.3, -433.9, 37.0, 791.2, 228.5, 700.3, 1344.1, 899.7, 715.1]))
sec  = dict(zip(yrs, [0, 616.0, 670.5, 367.5, 0, 0, 0, 0, 0, 0]))       # securitization collections put in investing
sbc  = dict(zip(yrs, [26.3, 30.3, 23.9, 25.1, 31.9, 43.7, 47.0, 60.5, 45.1, 37.1]))
capex= dict(zip(yrs, [163.3, 213.1, 174.7, 138.8, 187.6, 184.2, 450.0, 606.7, 324.3, 402.8]))
gov  = dict(zip(yrs, [0, 0, 0, 0, 0, 0, 0, 5.0, 0, 50.0]))            # government assistance for PP&E
flp  = dict(zip(yrs, [0, 0, 0, 0, 12.8, 16.0, 17.8, 22.8, 34.5, 40.6]))  # finance-lease principal
intp = dict(zip(yrs, [74.7, 65.7, 40.0, 65.2, 59.7, 58.3, 47.3, 64.4, 49.5, 51.1]))  # cash paid for interest
dna  = dict(zip(yrs, [126.9, 125.1, 131.7, 158.7, 165.8, 167.6, 175.0, 218.8, 280.4, 285.9]))
acq  = dict(zip(yrs, [0, 56.1, 7.0, 700.9, 18.1, 1.9, 552.4, 234.7, 0, 0]))
div  = dict(zip(yrs, [4.3, 163.4, 75.5, 1.9, 0, 0, 0, 0, 0, 0]))         # proceeds from businesses / equity investments sold
sales= dict(zip(yrs, [3596.1, 3844.1, 4643.7, 5829.0, 5476.5, 6729.8, 8913.5, 8799.5, 7926.0, 7798.5]))
T = 0.236   # CONVENTION of the run: FY2024 effective rate, for after-tax interest
oc_eq, oc_un, oc_dep = {}, {}, {}
for y in yrs:
    base = ocf[y] + sec[y] - sbc[y] + gov[y] - flp[y]
    oc_eq[y] = base - capex[y]                    # owner cash after interest (equity-only)
    oc_un[y] = oc_eq[y] + intp[y] * (1 - T)       # before interest, after company tax (all-equity)
    oc_dep[y] = base + intp[y]*(1-T) - dna[y]     # depreciation variant, all-equity
print("year  OCFadj  capex  D&A  ownerEq  ownerUnlev  depVariant  netAcq  sales  ownerUnlev/sales")
for y in yrs:
    print(y, round(ocf[y]+sec[y],1), capex[y], dna[y], round(oc_eq[y],1), round(oc_un[y],1), round(oc_dep[y],1), round(acq[y]-div[y],1), sales[y], f"{oc_un[y]/sales[y]*100:.1f}%")
def avg(d, ys): return sum(d[y] for y in ys)/len(ys)
W = [2021, 2022, 2023, 2024, 2025]; C = list(range(2017, 2026))
for name, ys in (("literal window FY2021-25", W), ("cycle FY2017-25", C), ("ten years FY2016-25", yrs)):
    na = avg({y: acq[y]-div[y] for y in yrs}, ys)
    print(f"{name}: unlev {avg(oc_un, ys):.1f} | equity {avg(oc_eq, ys):.1f} | dep variant {avg(oc_dep, ys):.1f} | net acquisitions {na:.1f} | unlev after acq {avg(oc_un, ys)-na:.1f} | sales {avg(sales, ys):.0f} | maintenance-only (capex=D&A) unlev {avg({y: oc_un[y]+capex[y]-dna[y] for y in yrs}, ys):.1f}")
# halves growth for cycle window
h1 = [2017, 2018, 2019, 2020]; h2 = [2022, 2023, 2024, 2025]
for lab, d in (("unlev after acq", {y: oc_un[y]-(acq[y]-div[y]) for y in yrs}), ("unlev before acq", oc_un), ("sales", sales)):
    a, b = avg(d, h1), avg(d, h2)
    g = (b/a)**(1/5)-1 if a > 0 and b > 0 else None
    print(lab, "halves", round(a,1), round(b,1), "rate over 5 yrs between half-midpoints", None if g is None else f"{g*100:.1f}%")
max_share = max(oc_un[y]/sales[y] for y in yrs)
print("highest owner-cash share of sales", f"{max_share*100:.1f}%")
