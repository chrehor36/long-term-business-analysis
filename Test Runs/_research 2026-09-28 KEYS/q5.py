# Q5 arithmetic (after Q1-Q4). Owner earnings are after tax and interest, so capitalised values are equity values.
SH=170244745; P=362.15; CAP=P*SH/1e6; BOND=0.0549; FLOOR=0.10
W={'5y capex':967.0,'5y dep':1012.4,'3y capex':985.3,'3y dep':1019.3,'11y capex':682.8,'11y dep':709.2,'TTM capex':1255,'TTM dep':1240}
ORG=[0,-3,2,14,12,-3,15,12,3,-12,8]   # filer's revenue change less acquisitions and currency, FY2015-FY2025, percentage points
g_org=sum(ORG)/len(ORG)/100
print(f'cap {CAP:,.1f}  organic mean {100*g_org:.2f}%  compound {100*((1+sum(0 for _ in ORG))):.0f}')
import math
comp=math.prod(1+x/100 for x in ORG)**(1/len(ORG))-1; print(f'organic compound {100*comp:.2f}%')
for k,oe in W.items():
    y=oe/CAP; greq=(FLOOR*CAP-oe)/(CAP+oe)
    ps=lambda v: v*1e6/SH
    print(f"{k:10} OE {oe:7.1f} yield {100*y:.2f}%  vs bond {100*(y-BOND):+.2f} pts  expectancy(+{100*g_org:.1f}%) {100*(y+g_org):.2f}%  g needed at floor {100*greq:.2f}%  | no-growth $/sh floor {ps(oe/FLOOR):6.1f} bond {ps(oe/BOND):6.1f} | floor g=org {ps(oe*(1+g_org)/(FLOOR-g_org)):6.1f}  floor g=5% {ps(oe*1.05/(FLOOR-0.05)):6.1f}")
# bands: price at which the floor is met
for k,g in (('5y dep',g_org),('TTM capex',0.05)):
    oe=W[k]; v=oe*(1+g)/(FLOOR-g); print('band', k, f'g={100*g:.1f}%', f'${v*1e6/SH:.2f}')
