# COMPUTATION, NOT A CLEARANCE. Q7 range and Part VII fair price for GIC, beneath the Q2 stop.
ocf={2021:47.6,2022:49.8,2023:112.0,2024:50.4,2025:77.7}   # continuing ops, 10-K cash-flow statements (XBRL first-filed)
sbc={2021:2.9,2022:4.5,2023:3.0,2024:2.8,2025:7.4}
capex={2021:3.4,2022:7.4,2023:3.9,2024:3.8,2025:3.1}
acq={2021:0,2022:0,2023:72.3,2024:0,2025:4.0}
sales={2021:1063.1,2022:1166.1,2023:1274.3,2024:1315.9,2025:1379.1}
Y=sorted(ocf)
oc={y:ocf[y]-sbc[y]-capex[y] for y in Y}
oca={y:oc[y]-acq[y] for y in Y}
m=lambda d:sum(d.values())/len(d)
print('owner cash before purchases',{y:round(v,1) for y,v in oc.items()},'mean',round(m(oc),2))
print('owner cash after purchases ',{y:round(v,1) for y,v in oca.items()},'mean',round(m(oca),2))
print('owner cash / sales (before purchases) max', round(max(oc[y]/sales[y] for y in Y)*100,2),'%')
lit=(oca[2025]/oca[2021])**(1/4)-1
h1=(oca[2021]+oca[2022])/2; h2=(oca[2024]+oca[2025])/2; halves=(h2/h1)**(1/3)-1
sg=(sales[2025]/sales[2021])**(1/4)-1
org=(1.097*0.993*0.994*1.048)**(1/4)-1   # filer-reported organic sales growth 2022..2025 (10-Ks FY2022-FY2025 Item 7)
print('growth literal end-to-end (after purchases)',round(lit*100,2),'% ; halves',round(halves*100,2),'% ; sales',round(sg*100,2),'% ; organic sales',round(org*100,2),'%')
B=m(oca); Bpre=m(oc); ratio=Bpre/B
def pv(base,g,r,term_base_mult=1.0):
    v=0; c=base
    for t in range(1,11):
        c=c*(1+g); v+=c/(1+r)**t
    term=c*term_base_mult/r/(1+r)**10
    return v+term, c
r=0.056; SH=38.108; NETCASH=86.7; P=43.62
def report(label,r):
    lo=B/r                                  # no growth, purchases deducted (default pair, literal)
    lo_pre=Bpre/r                           # no growth, purchases stopped (beside)
    hi,c10=pv(B,halves,r,ratio)             # shown growth 10 yrs, then zero growth on owner cash before purchases
    hi_lit,_=pv(B,lit,r,ratio)
    o_lo=Bpre/r; o_hi,_=pv(Bpre,org,r)      # organic pair
    return dict(lo=lo,lo_pre=lo_pre,hi=hi,hi_lit=hi_lit,o_lo=o_lo,o_hi=o_hi,c10=c10)
a=report('sov',r)
print('\nAT THE SOVEREIGN 5.60% (whole business, $M):',{k:round(v,1) for k,v in a.items()})
ps=lambda v,cash=True:(v+(NETCASH if cash else 0))/SH
print('per share all-equity (+net cash 86.7): bottom %.2f top %.2f (top on literal growth %.2f); width %.2f to 1'%(ps(a['lo']),ps(a['hi']),ps(a['hi_lit']),ps(a['hi'])/ps(a['lo'])))
print('organic pair per share: %.2f to %.2f'%(ps(a['o_lo']),ps(a['o_hi'])))
print('no-growth with purchases stopped, per share %.2f'%ps(a['lo_pre']))
yr10_sales=sales[2025]*(1+sg)**10
print('cap check: year-10 owner cash after purchases %.1f, before %.1f; year-10 sales at own growth %.0f; share %.2f%% / %.2f%%'%(a['c10'],a['c10']*ratio,yr10_sales,100*a['c10']/yr10_sales,100*a['c10']*ratio/yr10_sales))
f=report('ten',0.10)
fair_ae=(ps(f['lo'])+ps(f['hi']))/2
fair_eq=(ps(f['lo'],False)+ps(f['hi'],False))/2
print('\nAT TEN PERCENT: ends per share all-equity %.2f and %.2f -> FAIR PRICE %.2f ; equity-only %.2f'%(ps(f['lo']),ps(f['hi']),fair_ae,fair_eq))
fo=(ps(f['o_lo'])+ps(f['o_hi']))/2
print('organic pair fair price (beside) %.2f'%fo)
# floor test at the price: does any case earn 10%? find r at which top case value = EV
EV=P*SH-NETCASH
def solve(fn):
    lo,hi=0.0001,0.5
    for _ in range(80):
        mid=(lo+hi)/2
        if fn(mid)>EV: lo=mid
        else: hi=mid
    return mid
print('\nEV at price %.1f; implied return top case %.2f%%, bottom case %.2f%%, organic top %.2f%%'%(EV,100*solve(lambda r: pv(B,halves,r,ratio)[0]),100*solve(lambda r:B/r),100*solve(lambda r: pv(Bpre,org,r)[0])))
