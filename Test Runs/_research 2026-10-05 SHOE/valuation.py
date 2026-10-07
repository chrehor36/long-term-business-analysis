# COMPUTATION - NOT A CLEARANCE. Arithmetic for the Q7 convention and the owner's fair/cheap prices.
oc={2021:147.9-5.5-31.4,2022:50.4-5.4-77.3,2023:122.8-4.9-56.3,2024:102.6-7.7-33.2,2025:71.3-7.3-44.7}
ocd={2021:147.9-5.5-18.8,2022:50.4-5.4-23.2,2023:122.8-4.9-28.8,2024:102.6-7.7-31.1,2025:71.3-7.3-34.3}
avg=sum(oc.values())/5; avgd=sum(ocd.values())/5
print({k:round(v,1) for k,v in oc.items()}, 'avg capex basis',round(avg,1))
print({k:round(v,1) for k,v in ocd.items()}, 'avg D&A basis',round(avgd,1))
r=0.0563; sh=27.183815
sales={2021:1330.394,2025:1135.324}
g=(sales[2025]/sales[2021])**(1/4)-1
print('sales CAGR FY2021-25',round(g*100,2))
def pv(base,g,r,yrs=10):
    v=0;c=base
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    term=c/r/(1+r)**yrs   # zero nominal growth after year 10
    return v+term
for b,lab in [(avg,'capex'),(avgd,'D&A')]:
    ng=pv(b,0,r); sg=pv(b,g,r)
    print(lab,'no-growth $M',round(ng,1),'/sh',round(ng/sh,2),' shown-growth $M',round(sg,1),'/sh',round(sg/sh,2),' ratio',round(ng/sg,2))
cash=118.0; surplus=cash-60
print('surplus cash/sh',round(surplus/sh,2), 'all cash/sh', round(cash/sh,2))
# owner's fair price: central case pre-tax owner cash 35, declining 3%/yr, floor 10% pre-tax
for base,dec,lab in [(35,0.03,'central'),(25,0.05,'stress'),(45,0.0,'pre-covid normal, flat')]:
    ev=base/(0.10+dec); px=(ev+surplus)/sh
    print(lab,'EV at 10% floor',round(ev,1),'price',round(px,2))
price=12.76; mcap=price*sh; ev=mcap-surplus
print('mcap',round(mcap,1),'EV',round(ev,1),'central expected pre-tax return', round((35/ev-0.03)*100,2))
print('after-tax equiv of 10% at 25.7%', round(10*(1-0.257),2))
