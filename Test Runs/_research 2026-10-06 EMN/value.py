# COMPUTATION - NOT A CLEARANCE. EMN owner cash and the Q7-convention range. USD millions.
import math
R=0.0566; SH=114.377421; PRICE=64.94
NETDEBT=4526; PENSION=85+144-55   # US pension -85, OPEB -144, non-US +55 at 2025-12-31 (10-K note 11)
CLAIMS=NETDEBT+PENSION
OCF={2016:1385,2017:1657,2018:1543,2019:1504,2020:1455,2021:1619,2022:975,2023:1374,2024:1287,2025:970}
SBC={2016:36,2017:52,2018:64,2019:59,2020:44,2021:70,2022:69,2023:64,2024:63,2025:48}
CAPEX={2016:626,2017:649,2018:528,2019:425+6,2020:383+13,2021:555+23,2022:611+13,2023:828+5,2024:599,2025:546}
DA={2016:580,2017:587,2018:604,2019:611,2020:574,2021:538,2022:477,2023:498,2024:509,2025:513}
DEP={2023:405,2024:419,2025:425}
TAX={2016:120,2017:97,2018:202,2019:217,2020:179,2021:122,2022:78,2023:158,2024:111,2025:159}
INT={2016:280,2017:263,2018:239,2019:235,2020:191,2021:170,2022:179,2023:214,2024:203,2025:215}
FACT={2019:169,2020:150,2021:239,2022:402,2023:397,2024:385,2025:346}  # factored receivables outstanding at year-end
T=0.16
def oc(y,basis='capex'):
    b={'capex':CAPEX[y],'da':DA[y],'maint':425}[basis]
    return OCF[y]-SBC[y]-b
def trend(vals):
    n=len(vals);xs=range(n);ys=[math.log(v) for v in vals];mx=sum(xs)/n;my=sum(ys)/n
    return math.exp(sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs))-1
def pv(c0,g,r=R,yrs=10):
    s=0;c=c0
    for t in range(1,yrs+1):
        c*=1+g; s+=c/(1+r)**t
    return s+(c/r)/(1+r)**yrs
yrs5=list(range(2021,2026)); yrs10=list(range(2016,2026))
print('owner cash by year (capex basis):',{y:oc(y) for y in yrs10})
print('owner cash by year (D&A basis):',{y:oc(y,'da') for y in yrs10})
for label,yrs,fadj in [('5-yr 2021-2025',yrs5,(FACT[2025]-FACT[2020])/5),('10-yr 2016-2025',yrs10,FACT[2025]/10)]:
    print('\n=====',label,' factoring lift per year removed:',round(fadj,1))
    tx=sum(TAX[y] for y in yrs)/len(yrs); it=sum(INT[y] for y in yrs)/len(yrs)
    for basis in ['capex','da','maint']:
        vals=[oc(y,basis) for y in yrs]
        avg=sum(vals)/len(vals)-fadj
        g_end=(vals[-1]/vals[0])**(1/(len(vals)-1))-1
        g_tr=trend(vals)
        unlev=avg+it*(1-T)
        lev_ng=avg/R/SH
        ng=(unlev/R-CLAIMS)/SH
        sg_tr=(pv(unlev,g_tr)-CLAIMS)/SH
        sg_end=(pv(unlev,g_end)-CLAIMS)/SH
        pretax_unlev=avg+tx+it
        fair=(pretax_unlev/0.10-CLAIMS)/SH
        pretax_eq=avg+tx
        fair_eq=(pretax_eq/0.10)/SH
        print(f" {basis:5s} avg {avg:6.0f} | g endpoints {g_end*100:5.1f}% trend {g_tr*100:5.1f}% | no-growth unlev ${ng:6.2f} (levered ${lev_ng:6.2f}) | shown-growth trend ${sg_tr:6.2f} endpoints ${sg_end:6.2f} | pre-tax unlev {pretax_unlev:5.0f} -> fair(EV basis) ${fair:6.2f}; pre-tax to equity {pretax_eq:5.0f} -> fair(equity basis) ${fair_eq:6.2f}")
        print(f"        pre-tax return at price on EV: {pretax_unlev/(PRICE*SH+CLAIMS)*100:5.2f}%   on equity: {pretax_eq/(PRICE*SH)*100:5.2f}%   avg tax {tx:.0f} int {it:.0f}")
print('\nmarket cap',round(PRICE*SH),'EV incl net debt and pension',round(PRICE*SH+CLAIMS))
