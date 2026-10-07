# Owner earnings for BX, $M, from filed faces (FY2022 10-K for FY2020-22, FY2025 10-K for FY2023-25, Q2 2026 10-Q, Q2 2026 EX-99.1)
Y  = [2020, 2021, 2022, 2023, 2024, 2025]
OCF= [1935.945, 3985.988, 6336.253, 4056.906, 3481.662, 4663.161]
SBC= [438.341, 637.441, 846.349, 987.549, 1168.435, 1445.352]
CAP= [111.650, 64.316, 235.497, 224.231, 61.409, 115.703]
DA_T=[106.153, 127.071, 136.297, 134.175, 134.765, 134.023]   # tagged D&A incl. amortization of intangibles (companyfacts)
PUR= [7179.951, 7439.964, 5228.723, 5010.341, 2429.824, 3807.149]
PRO= [9242.426, 11971.409, 10368.172, 7189.240, 4342.636, 6679.186]
NCIc=[581.077, 1275.211, 1268.297, 708.410, 907.267, 2525.477]
NCId=[747.491, 1347.631, 1271.907, 1003.715, 874.024, 1035.141]
DE = [3341.596, 6170.837, 6632.780, 5060.955, 5966.742, 7110.864]
DAp= [35.136, 52.187, 69.219, 94.124, 98.756, 98.985]           # "Depreciation and Amortization (p)" in the Adjusted EBITDA reconciliation
FRE= [2370.054, 4050.799, 4412.645, 4349.328, 5282.065, 5737.537]
RPR= [1865.993, 3883.112, 4461.338, 2061.102, 2287.031, 2815.529]
RPC= [714.347, 1557.570, 1814.097, 896.017, 951.246, 1090.595]
RPI= [158.933, 587.766, 396.256, 110.932, 92.526, 419.743]
TAX= [304.127, 759.682, 791.868, 670.510, 710.197, 690.349]
rows = {}
print("year | A: OCF-SBC-D&A | A: OCF-SBC-capex | inv. turnover (proceeds-purchases) | A ex turnover (capex end) | B: DE-SBC (D&A end) | B: DE+D&A(p)-SBC-capex | B fee-only pre-tax FRE-SBC-capex+D&A(p) | net realizations")
for i,y in enumerate(Y):
    a_da = OCF[i]-SBC[i]-DA_T[i]; a_cx = OCF[i]-SBC[i]-CAP[i]; turn = PRO[i]-PUR[i]
    b_da = DE[i]-SBC[i]; b_cx = DE[i]+DAp[i]-SBC[i]-CAP[i]
    fee = FRE[i]-SBC[i]+DAp[i]-CAP[i]; nr = RPR[i]-RPC[i]+RPI[i]
    rows[y]=(a_da,a_cx,turn,a_cx-turn,b_da,b_cx,fee,nr)
    print(y, " | ".join(f"{v:,.1f}" for v in rows[y]))
def mean(ys, k): return sum(rows[y][k] for y in ys)/len(ys)
for lab, ys in [("5y FY2021-25", [2021,2022,2023,2024,2025]), ("3y FY2023-25", [2023,2024,2025]), ("6y FY2020-25", Y)]:
    print(lab, "A D&A", f"{mean(ys,0):,.1f}", "A capex", f"{mean(ys,1):,.1f}", "A ex-turnover capex", f"{mean(ys,3):,.1f}", "B D&A", f"{mean(ys,4):,.1f}", "B capex", f"{mean(ys,5):,.1f}", "fee-only pre-tax", f"{mean(ys,6):,.1f}", "net realiz", f"{mean(ys,7):,.1f}")
# TTM to 2026-06-30
ocf_t = 4663.161 - 1997.721 + 2932.450; sbc_t = 1445.352 - 783.445 + 915.468; cap_t = 115.703 - 69.424 + 65.372
de_t = 7110.864 - 2976.568 + 3742.087
print("TTM OCF", round(ocf_t,1), "SBC", round(sbc_t,1), "capex", round(cap_t,1), "DE", round(de_t,1))
print("TTM A capex end", round(ocf_t - sbc_t - cap_t,1), "TTM B D&A end (DE-SBC)", round(de_t - sbc_t,1))
print("SBC / OCF by year", [round(100*SBC[i]/OCF[i],1) for i in range(6)])
print("SBC / DE by year", [round(100*SBC[i]/DE[i],1) for i in range(6)])
