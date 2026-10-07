# COMPUTATION - NOT A CLEARANCE. OSIS run 2026-10-05. Inputs from filed cash-flow statements (USD M).
ocf  ={2017:62.8,2018:133.1,2019:119.1,2020:129.2,2021:139.1,2022:63.8,2023:94.8,2024:-87.5,2025:97.6,2026:275.9}
sbc  ={2017:26.1,2018:23.8,2019:25.3,2020:23.8,2021:26.8,2022:28.1,2023:29.1,2024:28.7,2025:32.0,2026:26.4}
capex={2017:17.1,2018:43.2,2019:27.4,2020:21.1,2021:16.9,2022:14.9,2023:15.8,2024:22.1,2025:23.8,2026:30.6}
oth  ={2017:5.1,2018:2.5,2019:2.8,2020:13.4,2021:13.8,2022:15.6,2023:16.4,2024:17.3,2025:17.7,2026:18.0}
ni   ={2017:21.1,2018:-29.1,2019:64.8,2020:75.3,2021:74.0,2022:115.3,2023:91.8,2024:128.2,2025:149.6,2026:154.7}
da   ={2017:68.2,2018:69.8,2019:56.2,2020:49.8,2021:43.9,2022:38.7,2023:38.5,2024:42.2,2025:43.6,2026:42.6}
oc={y:ocf[y]-sbc[y]-capex[y]-oth[y] for y in ocf}
dv={y:ni[y]+da[y]-capex[y]-oth[y] for y in ni}
print("owner cash (OCF-SBC-capex-other productive assets):",{y:round(v,1) for y,v in oc.items()})
print("depreciation variant (NI+D&A-capex-other):",{y:round(v,1) for y,v in dv.items()})
f5=[2022,2023,2024,2025,2026]
a5=sum(oc[y] for y in f5)/5; d5=sum(dv[y] for y in f5)/5
a10=sum(oc.values())/10
print(f"5y avg owner cash {a5:.1f}; 10y avg {a10:.1f}; 5y avg dep variant {d5:.1f}")
g=(dv[2026]/dv[2022])**0.25-1
print(f"shown growth, dep variant FY22->FY26: {g*100:.2f}%/yr")
SH=15.941968; r=0.0563; P=197.93
def val(cf,g,r,n=10):
    v=0;c=cf
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+r)**t
    v+=c/r/(1+r)**n   # zero nominal growth after year ten
    return v
for name,base in (("cash basis",a5),("dep variant",d5)):
    lo=base/r; hi=val(base,g,r)
    print(f"{name}: no-growth {lo:.0f}M = ${lo/SH:.0f}/sh ; shown-growth {hi:.0f}M = ${hi/SH:.0f}/sh")
# central case: dep variant less working capital at pre-Mexico intensity
wc=0.35; sales26=1786.0; dsales=sales26*g
central=d5-wc*dsales
tax=0.197
pre=central/(1-tax)
print(f"central after-tax {central:.1f}, pre-tax {pre:.1f}, WC charge {wc*dsales:.1f}")
fair=val(pre,g,0.10)
print(f"FAIR (10% pre-tax, {g*100:.1f}% x10y then flat): {fair:.0f}M = ${fair/SH:.0f}/sh")
cheap=pre/0.10
print(f"CHEAP (no-growth pre-tax yield 10%): {cheap:.0f}M = ${cheap/SH:.0f}/sh")
# expected return at price
import math
lo_,hi_=0.0,0.5
for _ in range(100):
    m=(lo_+hi_)/2
    if val(pre,g,m)>P*SH: lo_=m
    else: hi_=m
print(f"pre-tax expected return on central case at ${P}: {m*100:.2f}%")
print(f"market cap {P*SH:.0f}M")
