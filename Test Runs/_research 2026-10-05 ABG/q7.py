# COMPUTATION - NOT A CLEARANCE. Owner cash = adjusted OCF (all new-vehicle floor plan operating; offset = cash;
# used floor plan and acquisition/divestiture floor plan = financing) - SBC - capex excl. real estate. USD M.
adj={2019:282.3,2020:442.6,2021:632.1,2022:987.0,2023:705.4,2024:688.4,2025:651.4}
sbc={2019:12.5,2020:12.6,2021:16.2,2022:20.6,2023:23.5,2024:26.7,2025:27.7}
cap={2019:57.6,2020:46.5,2021:74.2,2022:94.6,2023:142.3,2024:162.6,2025:186.0}
da={2019:36.2,2020:38.5,2021:41.9,2022:69.0,2023:67.7,2024:75.0,2025:82.4}
oc={y:adj[y]-sbc[y]-cap[y] for y in adj}; ocd={y:adj[y]-sbc[y]-da[y] for y in adj}
for y in adj: print(y, f"owner cash capex basis {oc[y]:7.1f}   D&A basis {ocd[y]:7.1f}")
w=range(2021,2026); base=sum(oc[y] for y in w)/5; based=sum(ocd[y] for y in w)/5
g=(oc[2025]/oc[2021])**(1/4)-1; gd=(ocd[2025]/ocd[2021])**(1/4)-1
print(f"5y mean capex {base:.1f}  D&A {based:.1f}; shown growth 2021-25 capex {g*100:.2f}%  D&A {gd*100:.2f}%")
r=0.0563; sh=17.951917; px=171.62; mc=px*sh
def pv(b,g,r,n=10):
    v=0; c=b
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+r)**t
    return v + c/r/(1+r)**n
def ps(v): return v/sh
print(f"market cap {mc:.0f}")
for lab,b,gg in [("5y capex",base,g),("5y D&A",based,gd)]:
    hi=b/r; lo=pv(b,gg,r)
    print(f"{lab}: no-growth {hi:.0f} (${ps(hi):.0f})  shown-growth {lo:.0f} (${ps(lo):.0f})  width {hi/lo:.2f}")
# whole-cycle
pre={2015:(118.9,10.0,71.7,1060.8),2016:(260.5,12.0,81.4,1058.7),2017:(195.6,13.6,42.3,1055.9),2018:(181.6,10.5,40.3,1103.0),2019:(282.3,12.5,57.6,1168.9)}
ocp=[a-s-c for a,s,c,_ in pre.values()]; gpp=[x[3] for x in pre.values()]
ratio=sum(ocp)/sum(gpp); print('pre-peak owner cash', [round(x,1) for x in ocp], 'ratio %.3f'%ratio)
gp_ttm=3071.7-1476.1+1480.0
newgp_ttm=621.9-(4442.0-4138.9)+(4431.0-4164.3)
print(f"TTM GP {gp_ttm:.1f}  TTM new GP {newgp_ttm:.1f}")
# normalize new GPU to 2015-19 mean 1,704 on TTM units ~ (181,204 - H1'25 units + H1'26 units) use 2025 units as proxy
pre_gpu=(1915+1828+1690+1569+1516)/5
units=181204
newgp_norm=pre_gpu*units/1e6
gp_wc=gp_ttm-(newgp_ttm-newgp_norm)-30
wc=ratio*gp_wc
print(f"pre-peak new GPU {pre_gpu:.0f}; normalized new GP {newgp_norm:.0f}; whole-cycle GP {gp_wc:.0f}; whole-cycle owner cash {wc:.0f}")
hi=wc/r; lo=pv(wc,g,r)
print(f"whole-cycle: no-growth {hi:.0f} (${ps(hi):.0f}) shown-growth {lo:.0f} (${ps(lo):.0f}) width {hi/lo:.2f}")
# floor: 10% pre-tax ~ after-tax at ETR 25.7%
etr=0.257; fl=0.10*(1-etr); print(f"floor after-tax {fl*100:.2f}%")
def price_at(b,g,rate): return ps(pv(b,g,rate))
def irr(b,g,price):
    lo,hi=0.0001,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(b,g,m)/sh>price: lo=m
        else: hi=m
    return m
for lab,b,gg in [("whole-cycle no growth",wc,0.0),("whole-cycle central (half shown decline)",wc,g/2),("whole-cycle shown decline",wc,g),("5y no growth",base,0),("5y shown",base,g)]:
    print(f"{lab}: after-tax return at ${px} = {irr(b,gg,px)*100:.2f}%  (pre-tax ~{irr(b,gg,px)/(1-etr)*100:.1f}%); price at floor ${price_at(b,gg,fl):.0f}")
# H1 2026 run-rate
rr=(305.2-17.2-117.4)*2; print('H1 2026 annualised owner cash', rr)
# all-equity check (L2017-004): EV / unlevered after-tax owner cash
debt=3010.0+447.7; ev=mc+debt; unlev=wc+187.5*(1-etr)
print(f"EV {ev:.0f}; unlevered whole-cycle owner cash {unlev:.0f}; EV multiple {ev/unlev:.1f}x; pre-tax multiple {ev/(unlev/(1-etr)):.1f}x")
# buyback prices vs ranges
print('buyback avg H1 2026', 277.6/1.346359, 'Q2', 130.6/0.668116)
print('--- extras')
stress=wc-0.743*41.8  # +200bp on $2.09B floating debt (10-Q Item 3: $20.9M per 100bp), after tax at 25.7%
print(f"stressed whole-cycle base {stress:.1f}; cheap price (bottom case at floor) ${price_at(stress,g,fl):.0f}; unstressed bottom at floor ${price_at(wc,g,fl):.0f}")
print(f"5y central (half decline) price at floor ${price_at(base,g/2,fl):.0f}")
print(f"whole-cycle central value at sovereign ${ps(pv(wc,g/2,r)):.0f}; 5y central at sovereign ${ps(pv(base,g/2,r)):.0f}")
# retention test
ni={2021:532.4,2022:997.3,2023:602.5,2024:430.3,2025:492.0}
bb={2021:10.4,2022:287.4+9.2,2023:267.7+11.4,2024:183.0+10.2,2025:99.9+12.8}
kept=sum(ni.values())-sum(bb.values()); print('NI 2021-25',sum(ni.values()),'returned',sum(bb.values()),'kept',kept,'plus equity raised 666.9 ->',kept+666.9)
mc20=145.74*(41.133668-21.848314); mc_now=mc; print('mcap end-2020',mc20,'now',mc_now,'change',mc_now-mc20)
print('owner cash/share 2020', 383.5/(41.133668-21.848314), '2025', 437.7/(41.338419-22.109690), 'whole-cycle now', wc/sh)
# coverage
print('pretax/other interest 2025', (662.2+187.5)/187.5, 'ex gains & impairments', (662.2-80.2+141.0+187.5)/187.5, 'incl floor plan', (662.2+187.5+91.2)/(187.5+91.2))
# return on tangible capital ABG 2025, 2024 (OI - floor plan interest)/(equity+debt-goodwill-franchise)
for y,oi,fpi,eq,ltd,cur,gw,fr in [(2025,860.6,91.2,3891.9,3092.8,479.2,2281.3,2097.6),(2024,835.6,89.9,3502.1,3023.9,114.7,2044.7,1911.7),(2019,325.0,37.9,646.3,907.0,32.4,201.7,121.7)]:
    tc=eq+ltd+cur-gw-fr; print(y,'tangible capital',round(tc,1),'(OI-FPI)/TC %.1f%%'%((oi-fpi)/tc*100), 'all capital incl goodwill %.1f%%'%((oi-fpi)/(eq+ltd+cur)*100))
acq=210.0+954.1+3660.4+5.0+1500.0+4.7+1761.8; div=39.1+177.9+21.3+701.2+30.7+196.3+566.5+361.5
print('acquisitions 2019-2025',acq,'divestitures 2019-H1 2026',div,'net',acq-div)
print('pretax ex gains/impairments 2019', 243.9-11.7+7.1, '2025', 662.2-80.2+141.0)
