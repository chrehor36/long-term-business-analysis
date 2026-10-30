# COMPUTATION - NOT A CLEARANCE. Owner cash = OCF - SBC - capex - net deferred-comp trust funding (USD m), from the filed cash-flow statements.
oc = {2016:(442.081,42.699,82.956,27.079),2017:(452.991,42.191,40.753,56.924-20.340),2018:(572.322,44.953,42.484,69.716-23.691),
      2019:(519.629,48.300,59.464,71.432-28.758),2020:(596.528,52.486,33.377,64.351-123.025),2021:(603.136,55.932,36.611,85.432-34.434),
      2022:(683.750,57.663,61.120,67.388-30.869),2023:(636.881,61.139,45.874,102.969-37.628),2024:(410.469,63.448,56.318,69.237-38.700),
      2025:(319.965,59.416,53.155,80.078-58.251)}
dep = {2021:52.210,2022:47.398,2023:51.364,2024:52.053,2025:50.031,2016:None}
own = {y:v[0]-v[1]-v[2]-v[3] for y,v in oc.items()}
for y in sorted(own): print(y, round(own[y],1), 'trust net', round(oc[y][3],1))
own_da = {y:oc[y][0]-oc[y][1]-dep[y]-oc[y][3] for y in range(2021,2026)}
print('D&A basis 2021-25', {y:round(v,1) for y,v in own_da.items()}, 'avg', round(sum(own_da.values())/5,1))
S=102.361828; P=34.34; r=0.0566; tax=0.30; cash=464.435
def pv(base,g,r=r,yrs=10):
    v=0; c=base
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    v+= c/r/(1+r)**yrs   # zero nominal growth after year 10
    return v
def show(label,base,g):
    v=pv(base,g); print(f'{label}: base {base:.1f} g {g*100:.1f}% value {v:.0f}m  ${v/S:.2f}/sh')
    return v/S
a5=sum(own[y] for y in range(2021,2026))/5; a10=sum(own.values())/10
g5=(own[2025]/own[2021])**(1/4)-1; g10=(own[2025]/own[2016])**(1/9)-1
print('avg5',round(a5,1),'g5',round(g5*100,1),'avg10',round(a10,1),'g10',round(g10*100,1))
hi5=show('5y no growth',a5,0.0); lo5=show('5y shown growth',a5,g5)
hi10=show('10y no growth',a10,0.0); lo10=show('10y shown growth',a10,g10)
print('ratio 5y', round(hi5/lo5,2), 'ratio 10y', round(hi10/lo10,2))
# fair price: central case = 10y whole-cycle average, no growth; pre-tax = after-tax/(1-tax); price where pre-tax yield = 10%
fair = a10/(1-tax)/0.10/S
print('fair (10y avg, no growth, 10% pretax)', round(fair,2))
fair5 = a5/(1-tax)/0.10/S; print('fair variant 5y avg', round(fair5,2))
trough = own[2025]/(1-tax)/0.10/S; print('2025 run-rate at 10% pretax', round(trough,2))
print('cheap = min(bottom 5y range, 2025 trough at 10% pretax)', round(min(lo5,trough),2))
print('yield at price on 5y avg', round(a5/(P*S)*100,2), 'on 2025', round(own[2025]/(P*S)*100,2), 'pretax on 10y', round(a10/(1-tax)/(P*S)*100,2))
print('net cash per share', round(cash/S,2))
# expected pre-tax return at price, central case, no growth = pretax yield
print('--- fair price, central case = 10y average carried at 10y shown growth, pre-tax at 10%')
c = pv(a10/(1-tax), g10, r=0.10)/S; print('fair central', round(c,2))
c2 = pv(a10/(1-tax), g10, r=0.10/(1)) ; 
# after-tax equivalent check: after-tax stream at 7% (10% x (1-0.30))
c3 = pv(a10, g10, r=0.07)/S; print('after-tax stream at 7%', round(c3,2))
# expected pre-tax return at today's price for central case: solve r
lo,hi=0.0,0.5
for _ in range(100):
    m=(lo+hi)/2
    if pv(a10/(1-tax),g10,r=m)/S > P: lo=m
    else: hi=m
print('pre-tax return at price, central', round(m*100,2))
for lab,base,g in [('5y shown',a5,g5),('2025 flat',own[2025],0.0)]:
    lo,hi=0.0,0.5
    for _ in range(100):
        m=(lo+hi)/2
        if pv(base/(1-tax),g,r=m)/S > P: lo=m
        else: hi=m
    print('pre-tax return at price,',lab, round(m*100,2))
print('cheap: worst shown case (5y avg at 5y shown growth) at 10% pre-tax', round(pv(a5/(1-tax),g5,r=0.10)/S,2))
