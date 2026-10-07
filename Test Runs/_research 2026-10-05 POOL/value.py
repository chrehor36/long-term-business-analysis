# Q7 arithmetic (COMPUTATION). r = US Treasury 30y par 5.66% 2026-10-05 (run.py line).
SH=36.340747  # millions, 10-Q cover 0001193125-26-322532
P=159.38
def pv(C,g,r,yrs=10):
    v=0;c=C
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    return v + c/r/(1+r)**yrs   # zero nominal growth after year 10
def irr(C,g,price_cap):
    lo,hi=0.001,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if pv(C,g,m)>price_cap: lo=m
        else: hi=m
    return m
r=0.0566
cases={
 'A 5yr capex no-growth':(472.6,0.0),
 'A 5yr capex shown 2.4%':(472.6,(286.8/260.6)**0.25-1),
 'B 10yr capex no-growth':(329.5,0.0),
 'B 10yr capex shown':(329.5,(286.8/121.1)**(1/9)-1),
 'C central normalized 360 g4%':(360.0,0.04),
 'C central normalized 360 g0':(360.0,0.0),
}
cap=P*SH
print('cap',round(cap,1))
for k,(C,g) in cases.items():
    v=pv(C,g,r); print(f"{k:32s} C={C} g={g*100:.1f}%  value ${v:8.0f}M  ${v/SH:7.2f}/sh  IRR at price {irr(C,g,cap)*100:5.2f}%  fair@10% ${pv(C,g,0.10)/SH:7.2f}")
