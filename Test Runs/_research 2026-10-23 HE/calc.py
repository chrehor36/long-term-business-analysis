# HE run 2026-10-23: Q7 arithmetic. USD millions. Sources in run file.
R=0.0529; F=0.10; SH=172.728; PX=8.75
# HEI continuing ops (filed): OCF, capex, SBC, pref div of subs, finance lease principal
yrs=[2021,2022,2023,2024,2025]
ocf  ={2022:333.682,2023:443.368,2024:428.110,2025:391.073}
capex={2022:339.333,2023:442.727,2024:344.251,2025:341.202}
sbc  ={2022:7.45,2023:6.78,2024:3.59,2025:3.43}
pref ={y:1.89 for y in yrs}
lease={2021:0.0,2022:0.85,2023:3.52,2024:4.68,2025:10.37}
dep  ={2022:244.48,2023:254.99,2024:261.70,2025:260.02}
# 2021: continuing not filed. Utilities filed (0000354707-22-000049): OCF 273.133, capex 292.000.
# CONVENTION of this run: other-segment OCF and capex = mean of (HEI continuing - Utilities) 2022-2024.
u_ocf={2022:327.930,2023:474.367,2024:465.733}; u_cap={2022:329.457,2023:438.775,2024:329.479}
d_ocf=sum(ocf[y]-u_ocf[y] for y in (2022,2023,2024))/3
d_cap=sum(capex[y]-u_cap[y] for y in (2022,2023,2024))/3
ocf[2021]=273.133+d_ocf; capex[2021]=292.000+d_cap; sbc[2021]=9.13*7.45/10.37
print(f"2021 est: other OCF {d_ocf:.1f}, other capex {d_cap:.1f} -> OCF {ocf[2021]:.1f} capex {capex[2021]:.1f} SBC {sbc[2021]:.2f}")
oc={y:ocf[y]-capex[y]-sbc[y]-pref[y]-lease[y] for y in yrs}
for y in yrs: print(y, f"OCF {ocf[y]:.1f} capex {capex[y]:.1f} SBC {sbc[y]:.2f} pref {pref[y]:.2f} lease {lease[y]:.2f} -> owner cash all-capex {oc[y]:.1f}")
avg5=sum(oc.values())/5; avg4=sum(oc[y] for y in yrs[1:])/4
print(f"avg all-capex, 5y {avg5:.1f}; 4y 2022-25 {avg4:.1f}")
# debt credit: Utilities long-term debt net, YE2020 1,561 -> YE2025 2,183 (and YE2021 1,676)
raised5=2183-1561; raised4=2183-1676
cap5=0.52*sum(capex.values()); cap4=0.52*sum(capex[y] for y in yrs[1:])
cr5=min(raised5,cap5)/5; cr4=min(raised4,cap4)/4
print(f"debt raised 5y {raised5} cap(52%) {cap5:.0f} credit/yr {cr5:.1f}; 4y {raised4} cap {cap4:.0f} credit/yr {cr4:.1f}")
c5=avg5+cr5; c4=avg4+cr4
mnt=sum(ocf[y]-dep[y]-sbc[y]-pref[y]-lease[y] for y in yrs[1:])/4
print(f"CENTRAL equity-only owner cash 5y {c5:.1f}; cycle base 2022-25 {c4:.1f}; maintenance-only (capex at depreciation, no credit) 2022-25 {mnt:.1f}")
# settlement: three installments of 479 in Apr 2027/28/29; after tax at 25.75% composite
t=[0.466,1.466,2.466]; at=479*(1-0.2575)
pv=lambda r: sum(at/(1+r)**x for x in t)
S_R, S_F = pv(R), pv(F)
asb=33.9+ (2.0/0.30-2.294)*14.75
print(f"settlement after-tax PV at {R}: {S_R:.1f}; at 10%: {S_F:.1f}; ASB stake+proceeds {asb:.1f}")
def val(c,g,r,yrs=10):
    v=0; x=c
    for i in range(1,yrs+1):
        x=c*(1+g)**i; v+=x/(1+r)**i
    return v + (c*(1+g)**yrs/r)/(1+r)**yrs if g else c/r
def ps(v): return v/SH
for name,c in [("central 5y",c5),("cycle base 4y",c4),("maint-only",mnt)]:
    for g in (0.0,0.02):
        eq=val(c,g,R)-S_R+asb; eqf=val(c,g,F)-S_F+asb
        print(f"{name:14s} g={g:.2f}: value ${ps(eq):6.2f}/sh at sovereign; ${ps(eqf):6.2f}/sh at 10%")
# expected return at price, no growth perpetuity: c / (mktcap + settlement - asb)
mc=SH*PX
for name,c in [("central",c5),("cycle",c4),("maint",mnt)]:
    print(f"yield at price {name}: {100*c/(mc+S_R-asb):.2f}% (mkt cap {mc:.0f})")
# growth needed to earn 10% at price (10y growth then flat), central
lo,hi=0,0.5
for _ in range(60):
    g=(lo+hi)/2
    if val(c5,g,F)-S_F+asb < mc: lo=g
    else: hi=g
print(f"growth for 10 yrs needed for central to earn 10% at price: {100*g:.1f}%/yr")
# all-equity beside: add back after-tax interest (borrowings mean paid 2023-25 114; finance lease 25.7)
ae=avg5+(114+25.7)*(1-0.2575)
nd=2265.630+499.402-238.732-asb
for r,s in ((R,S_R),(F,S_F)):
    print(f"all-equity at {r}: owner cash {ae:.1f}, EV {ae/r:.0f}, net debt {nd:.0f} + settlement {s:.0f} -> ${ps(ae/r-nd-s):.2f}/sh")
