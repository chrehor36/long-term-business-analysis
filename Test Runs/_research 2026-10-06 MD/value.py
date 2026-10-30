# COMPUTATION - NOT A CLEARANCE. Owner cash (USD M) = continuing OCF - SBC - capex - acquisition payments
oc={2021:113.760-18.968-32.249-29.930,2022:182.312-16.127-29.708-28.167,2023:146.081-12.323-33.328-6.667,
    2024:217.250-11.868-22.022-8.167,2025:274.739-18.045-18.458-23.196}
da={2021:32.147,2022:35.636,2023:36.171,2024:32.226,2025:21.827}
capex={2021:32.249,2022:29.708,2023:33.328,2024:22.022,2025:18.458}
for y in oc: print(y,round(oc[y],1),'D&A variant',round(oc[y]+capex[y]-da[y],1))
avg5=sum(oc.values())/5; avg4=sum(oc[y] for y in (2022,2023,2024,2025))/4
avgda=sum(oc[y]+capex[y]-da[y] for y in oc)/5
print('avg5',round(avg5,1),'avg ex-2021',round(avg4,1),'avg5 D&A basis',round(avgda,1))
r=0.0566; sh=81.253; tax=0.266
def pv(c,g,n=10):
    v=0;x=c
    for t in range(1,n+1):
        x*=1+g; v+=x/(1+r)**t
    return v+x/r/(1+r)**n
# whole-cycle: avg adjusted continuing op margin 2018-2025
m=[248.388/1723.107,171.756/1779.759,(98.132+73.801)/1733.951,202.9/1911.2,172.7/1972.0,(7.321+148.312+2.219)/1994.640,183.7/2012.919,231.1/1913.849]
mm=sum(m)/len(m); print('margins',[round(x*100,1) for x in m],'avg',round(mm*100,1))
wc=((1913.849*mm-36.0)*(1-tax)+21.8-18.5-19.0)
print('whole-cycle owner cash',round(wc,1))
for name,c in [('five-yr avg',avg5),('ex-2021',avg4),('whole-cycle',wc)]:
    lo=pv(c,0,0) if False else c/r; hi=pv(c,0.03)
    print(f'{name}: no-growth {lo:.0f}M ${lo/sh:.2f}; 3% shown growth {hi:.0f}M ${hi/sh:.2f}; ratio {hi/lo:.2f}')
# fair price: central case owner cash = midpoint of avg5 and ex-2021, growth g; equity floor 10% pre-tax expected = pretax yield + g
cen=(avg5+avg4)/2; print('central',round(cen,1))
for g in (0,0.015,0.03):
    pre=cen/(1-tax); eq=pre/(0.10-g); print(f' g={g}: fair equity {eq:.0f}M ${eq/sh:.2f}')
# floor on equity plus net debt (6/30/26): debt 584.2, cash+ST inv 404.2
nd=584.243-404.198; pre_ev=cen/(1-tax)+36.0
for g in (0,0.015):
    ev=pre_ev/(0.10-g); print(f' EV basis g={g}: EV {ev:.0f} equity {ev-nd:.0f}M ${(ev-nd)/sh:.2f}')
# cheap: lower of (a) low case (whole-cycle, no growth) at 10% pre-tax yield; (b) 2/3 of bottom of the convention range
a=wc/(1-tax)/0.10; b=(avg5/r)*2/3
print(f'cheap a {a:.0f}M ${a/sh:.2f}; b {b:.0f}M ${b/sh:.2f}')
print('price yield: owner cash avg5 / mcap', round(avg5/(26.10*sh)*100,2),'% after tax; pre-tax',round(avg5/(1-tax)/(26.10*sh)*100,2))
