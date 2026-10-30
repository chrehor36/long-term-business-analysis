# Owner cash and COMPUTATION, NOT A CLEARANCE. USD millions. Sources: 10-K cash flow statements as filed
# FY2021-22: 0001410578-23-000153 (FY2022 10-K); FY2023: 0001410578-24-000124; FY2024-25: 0001104659-26-020655 (FY2025 10-K, 2024 as re-presented)
ocf  ={2021:5.151,2022:-1.216,2023:5.903,2024:34.864,2025:46.752}
sbc  ={2021:1.750,2022:3.283,2023:4.027,2024:3.998,2025:11.144}
capex={2021:4.368,2022:6.526,2023:5.564,2024:7.741,2025:11.104}
da   ={2021:2.869,2022:3.889,2023:4.716,2024:5.796,2025:6.889}
ltob ={2021:0.691,2022:0.639,2023:0.452,2024:0.362,2025:0.420}   # payment of long-term obligations (vendor-financed licences)
netint={2021:0.0,2022:0.0,2023:-0.179,2024:0.149,2025:1.552}     # net interest income (+) / expense (-), segment tables; 2021-22 not separated, cash interest paid <0.03
rev  ={2021:69.755,2022:79.001,2023:86.775,2024:170.461,2025:251.663}
T=0.21
yrs=range(2021,2026)
oc_eq ={y:ocf[y]-sbc[y]-capex[y]-ltob[y] for y in yrs}          # equity-only (after interest)
oc_ae ={y:oc_eq[y]-netint[y]*(1-T) for y in yrs}                 # all-equity (before interest, after tax at 21% statutory)
oc_da ={y:ocf[y]-sbc[y]-da[y]-ltob[y]-netint[y]*(1-T) for y in yrs}
def avg(d): return sum(d.values())/len(d)
for nm,d in [("all-equity, all capex",oc_ae),("equity-only",oc_eq),("all-equity, D&A variant",oc_da)]:
    print(nm, {y:round(v,2) for y,v in d.items()}, "avg", round(avg(d),3))
print("owner cash / sales", {y:f"{oc_ae[y]/rev[y]*100:.1f}%" for y in yrs})
h1=(oc_ae[2021]+oc_ae[2022])/2; h2=(oc_ae[2024]+oc_ae[2025])/2
print("halves", round(h1,2), round(h2,2), "-> sign change: growth meaningless (specific (b))")
r=0.0530; floor=0.10
cash=240.278+10.093; debt=1.665           # 10-Q 30 Jun 2026, 0001104659-26-092021
netcash=cash-debt
sh=34.382651                              # cover, 31 Jul 2026
price=44.74
oc=avg(oc_ae); oce=avg(oc_eq)
V=oc/r; Vf=oc/floor
print("net cash", round(netcash,3))
print("ALL-EQUITY  value range (no-growth only): business", round(V,1), "+ net cash ->", round((V+netcash)/sh,2), "/sh")
print("ALL-EQUITY  fair price (10%):", round((Vf+netcash)/sh,2))
print("EQUITY-ONLY value:", round(oce/r/sh,2), " fair:", round(oce/floor/sh,2))
adv=66.962; ap=61.8
print("beside, cash less customer advance:", round((V+netcash-adv)/sh,2), " fair", round((Vf+netcash-adv)/sh,2))
mcap=price*sh; ev=mcap-netcash
print("mcap", round(mcap,1), "EV", round(ev,1), "return on EV at avg owner cash", f"{oc/ev*100:.2f}%", "FY2025 alone", f"{oc_ae[2025]/ev*100:.2f}%")
# what growth (10 yrs then flat) would the price need at 10%? solve on all-equity, FY2025 base and 5-yr base
def pv(base,g,disc):
    v=0;c=base
    for t in range(1,11):
        c*=1+g; v+=c/(1+disc)**t
    return v + c/disc/(1+disc)**10
for base,lab in [(oc,"5yr avg"),(oc_ae[2025],"FY2025")]:
    lo,hi=0,2
    for _ in range(100):
        m=(lo+hi)/2
        if pv(base,m,floor)<ev: lo=m
        else: hi=m
    print("growth needed for 10% at price, base",lab, f"{m*100:.1f}% a year for ten years")
# beside, D&A variant
od=avg(oc_da); print("D&A variant value", round((od/r+netcash)/sh,2), "fair", round((od/floor+netcash)/sh,2))
