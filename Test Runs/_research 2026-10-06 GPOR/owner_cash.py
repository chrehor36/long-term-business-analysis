# Owner cash and value arithmetic for the GPOR run. Every input is a filed figure (USD millions) cited in the run file.
# COMPUTATION ONLY: no verdict is drawn here.
yrs = ['2021c','2022','2023','2024','2025']
ocf   = {'2021c':172.2+293.0,'2022':739.1,'2023':723.2,'2024':650.0,'2025':803.2}
sbc   = {'2021c':1.2+2.0,'2022':5.7,'2023':9.5,'2024':11.0,'2025':12.2}
capex = {'2021c':102.3+207.1,'2022':460.8,'2023':537.4,'2024':454.1,'2025':527.6}
dda   = {'2021c':62.8+160.9,'2022':267.8,'2023':319.7,'2024':325.7,'2025':304.2}
pref  = {'2021c':1.5,'2022':5.4,'2023':4.8,'2024':4.2,'2025':1.7}
cashpsu={'2021c':0,'2022':0,'2023':0,'2024':0,'2025':12.3}
prod  = {'2021c':366.3,'2022':358.9,'2023':384.8,'2024':385.8,'2025':379.2}  # Bcfe
oc={};od={}
print('year   OCF    SBC  capex   pref  cashPSU  OWNER(capex)  OWNER(D&A)  per Mcfe')
for y in yrs:
    oc[y]=ocf[y]-sbc[y]-capex[y]-pref[y]-cashpsu[y]
    od[y]=ocf[y]-sbc[y]-dda[y]-pref[y]-cashpsu[y]
    print(f"{y:6}{ocf[y]:7.1f}{sbc[y]:6.1f}{capex[y]:7.1f}{pref[y]:6.1f}{cashpsu[y]:7.1f}{oc[y]:12.1f}{od[y]:12.1f}{oc[y]/prod[y]:8.2f}")
avg=sum(oc.values())/5; avgd=sum(od.values())/5
avg4=sum(oc[y] for y in yrs[1:])/4
print(f"5-yr mean owner cash (all capex) {avg:.1f}; D&A variant {avgd:.1f}; 4 successor full years {avg4:.1f}")
# predecessor
pocf={'2014':409.9,'2015':322.2,'2016':337.8,'2017':679.9,'2018':786.3,'2019':724.0,'2020':95.3}
psbc={'2014':8.9,'2015':8.6,'2016':7.4,'2017':6.4,'2018':6.8,'2019':4.9,'2020':0.0}
pcap={'2014':1329.3,'2015':1579.1,'2016':724.9,'2017':1064.7,'2018':899.1,'2019':720.1,'2020':367.3}
tot=0
for y in pocf:
    v=pocf[y]-psbc[y]-pcap[y]; tot+=v; print('pred',y,round(v,1))
print('pred 2014-2020 sum',round(tot,1))
# growth shown on aggregate owner cash
g=(oc['2025']/oc['2021c'])**(1/4)-1
print('owner cash CAGR 2021c->2025', round(g*100,1),'%')
gp=(1039/983)**(1/3)-1
print('production CAGR 2022->2025 (983 -> 1,039 MMcfe/d)', round(gp*100,2),'%')
r=0.0566; sh=17.683866; netdebt=797.0-1.8
def val(base,g,years=10,r=r,term_g=0.0):
    v=0;c=base
    for t in range(1,years+1):
        c*=1+g; v+=c/(1+r)**t
    v+= c*(1+term_g)/(r-term_g)/(1+r)**years
    return v
def life(base,years,r=r):
    return sum(base/(1+r)**t for t in range(1,years+1))
for label,base in [('5yr mean',avg),('4yr successor',avg4)]:
    lo=val(base,0.0); hi=val(base,gp)
    print(f"{label}: base {base:.1f}  no-growth {lo:.0f} (${lo/sh:.2f}/sh)  shown-growth(prod {gp*100:.2f}%) {hi:.0f} (${hi/sh:.2f}/sh)")
    hi2=val(base,g)
    print(f"   shown growth on owner cash {g*100:.1f}% x10y then flat: {hi2:.0f} (${hi2/sh:.2f}/sh)")
    for L in (11,15,20):
        v=life(base,L); print(f"   reserve-life variant {L} yrs then zero: {v:.0f} (${v/sh:.2f}/sh)")
# whole-cycle variant: realized price incl. hedges, GPOR own filings, 2015-2025 (2015-2017 as first reported, net of some transport)
pr={'2015':3.13,'2016':2.69,'2017':2.85,'2018':3.25,'2019':2.94,'2020':2.53,'2021':(3.03*134.735+3.33*231.594)/366.329,'2022':3.55,'2023':3.13,'2024':3.14,'2025':3.64}
wc=sum(pr.values())/len(pr); win=sum(pr[k] for k in ['2021','2022','2023','2024','2025'])/5
print(f"realized incl hedges: 2015-2025 mean {wc:.2f}; 2021-2025 mean {win:.2f}")
# per-Mcfe owner cash at 2025 volume and cost structure: price - cash costs - G&A - interest - maintenance capex - sbc
vol=379.2; cash=1.25; ga=0.11; intr=0.14; maint=(400+430)/2/ (1.0425*365)  # 2026 guide midpoint over guided volume
print('maintenance capex per Mcfe (2026 guide midpoint over guided volume)', round(maint,3))
for p in (2.60,2.94,3.10,3.30,3.64):
    pc=(p-cash-ga-intr-maint)*vol
    print(f"  price {p:.2f}: pre-tax owner cash {pc:.0f}M; perpetuity at 5.66% {pc/r:.0f}M (${pc/r/sh:.2f}/sh); 10% pre-tax price ${pc/0.10/sh:.2f}/sh")
# fair price: central case owner cash / 10% pre-tax, on equity (after interest)
for label,base in [('5yr mean',avg),('4yr successor',avg4)]:
    print(f"fair (10% pre-tax on equity, no growth) from {label}: ${base/0.10/sh:.2f}/sh")
# EV basis check
intpaid=54.3
print('fair on EV basis (owner cash + interest)/10% - net debt, 5yr:', round(((avg+intpaid)/0.10-netdebt)/sh,2))
# cheap: PV-10 of proved developed reserves less net debt
pdp=2291.0
print('cheap: PDP PV-10 less net debt', round((pdp-netdebt)/sh,2))
print('market cap at 157.84', round(157.84*sh,0))
