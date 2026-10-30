# All figures $M, read by hand off the filed cash-flow statements (10-K FY2023 for FY21-22,
# 10-K FY2025 for FY23-25, the 10-Qs for YTD interim). Arithmetic only.
A = {  # year: OCF, AP, accruals, DefRev, DefRevRP(or payables+DR RP pre-FY23), inventory, NI, D&A, SBC, capex_ppe, capex_sw, noncash_other
 "FY2021": (-265.269, 73.914, 21.286, -52.476, 205.461, -366.674, -162.003, 5.112, 0.0, 4.292, 0.0, 14.197-1.346+27.161),
 "FY2022": (-282.385, 152.467, -32.361, 201.028, 78.422, -265.477, -289.177, 7.108, 44.131, 7.934, 0.0, 0.778+2.529+0.516+30.032),
 "FY2023": (-111.927, -242.268, -12.360, -6.934, -191.431, 432.767, -104.818, 10.665, 26.920, 2.989, 9.235, 0.914-1.029+2.542),
 "FY2024": (79.685, 370.124, 160.206, -9.796, -72.201, 21.731, 30.367, 14.482, 23.855, 8.115, 10.860, 3.091+23.972-6.719),
 "FY2025": (-145.538, -119.228, -93.586, 361.903, 41.725, -278.729, -67.989, 29.343, 19.540, 14.884, 14.915, 4.217+6.959+6.351),
}
print("ANNUAL")
print(f"{'yr':7}{'OCF':>9}{'AP':>9}{'accr':>9}{'custmoney':>10}{'OCF-AP':>9}{'OCF-AP-acc-cust':>16}{'preWC':>9}{'WC':>9}{'AP/OCF%':>9}")
tot = [0]*6
for y,(o,ap,ac,dr,drp,inv,ni,da,sbc,cp,cs,oth) in A.items():
    cust = dr+drp
    pre = ni+da+sbc+oth
    wc = o-pre
    net = o-ap-ac-cust
    print(f"{y:7}{o:9.1f}{ap:9.1f}{ac:9.1f}{cust:10.1f}{o-ap:9.1f}{net:16.1f}{pre:9.1f}{wc:9.1f}{(ap/o*100 if o else 0):9.0f}")
    for k,v in enumerate((o,ap,ac,cust,pre,wc)): tot[k]+=v
print("sum FY21-25", [round(x,1) for x in tot])
print()
print("OWNER EARNINGS by year = OCF - SBC - (c); (c) low = D&A, high = total capex (PPE + software)")
oe = {}
for y,(o,ap,ac,dr,drp,inv,ni,da,sbc,cp,cs,oth) in A.items():
    lo = o - sbc - max(da, cp+cs); hi = o - sbc - min(da, cp+cs)
    oe[y]=(lo,hi); print(y, f"OCF {o:.1f} SBC {sbc:.1f} D&A {da:.1f} capex {cp+cs:.1f} -> OE {lo:.1f} .. {hi:.1f}")
import statistics as st
for w in (["FY2023","FY2024","FY2025"], ["FY2021","FY2022","FY2023","FY2024","FY2025"]):
    print(w[0],"-",w[-1], "mean", round(st.mean(oe[y][0] for y in w),1), "..", round(st.mean(oe[y][1] for y in w),1))
# TTM to 2026-06-30
o = -145.538 - (-411.281) + (-366.534); sbc = 19.540 - 15.459 + 14.118
da = 29.343 - 18.929 + 30.723; cap = (14.884+14.915) - (10.024+10.023) + (9.678+11.656)
print("TTM Jun-26: OCF", round(o,1), "SBC", round(sbc,1), "D&A", round(da,1), "capex", round(cap,1), "OE", round(o-sbc-max(da,cap),1), "..", round(o-sbc-min(da,cap),1))

print("\nQUARTERLY (de-cumulated YTD): OCF, AP, accruals, cust money (DR+DR RP), inventory, NI")
Y = { # YTD
 "FY24": [(19.363,254.781,0.190,99.051,147.814,-336.408,-25.556),(90.248,182.569,-11.449,114.568,-63.607,-96.382,-38.432),(69.156,256.264,37.139,131.073,-73.564,-257.916,-37.357),(79.685,370.124,160.206,-9.796,-72.201,21.731,30.367)],
 "FY25": [(-211.232,-333.593,139.064,316.723,-4.959,-368.763,-57.013),(-257.416,-202.860,40.728,383.120,-3.376,-520.237,-98.945),(-411.281,-180.842,-118.359,264.498,9.598,-469.694,-92.051),(-145.538,-119.228,-93.586,361.903,41.725,-278.729,-67.989)],
 "FY26": [(-226.792,-182.749,33.761,163.257,-21.301,-77.365,-62.588),(-347.905,-127.999,9.647,165.516,-13.533,-299.626,-91.827),(-366.534,-22.215,26.317,318.984,-22.379,-321.405,-136.103)],
}
for fy, rows in Y.items():
    prev = (0,)*7
    for q,r in enumerate(rows):
        d = [a-b for a,b in zip(r,prev)]; prev = r
        o,ap,ac,dr,drp,inv,ni = d; cust = dr+drp
        print(f"{fy}Q{q+1}: OCF {o:8.1f} | AP {ap:8.1f} | accr {ac:7.1f} | cust {cust:7.1f} | inv {inv:8.1f} | NI {ni:6.1f} | OCF ex AP,accr,cust {o-ap-ac-cust:8.1f} | cust/OCF {('%.0f%%'%(cust/o*100)) if o else ''}")
