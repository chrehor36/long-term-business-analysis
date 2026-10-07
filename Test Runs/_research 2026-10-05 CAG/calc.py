r=0.0563; sh=477.411517; price=13.15
def dcf(c,g,years=10):
    v=0; cf=c
    for t in range(1,years+1):
        cf=cf*(1+g); v+=cf/(1+r)**t
    v+= cf/r/(1+r)**years   # zero nominal growth after year 10
    return v
# income-statement figures (filed), USD m
GP={22:2838.8,23:3264.8,24:3333.4,25:3003.5,26:2698.4}
SGA={22:1492.8,23:1431.9,24:1487.5,25:1537.3,26:1439.4}  # FY23/24 as restated in FY25 10-K (impairments shown apart)
INT={22:379.9,23:409.6,24:430.5,25:416.7,26:382.6}
EQD={22:None,23:None,24:177.6+74.0,25:182.4-22.1,26:140.7+0.4}  # distributions = earnings + (earnings less than distributions)
DA={22:375,23:370,24:400.9,25:390.2,26:396.0}; CX={22:464,23:362,24:388.1,25:389.3,26:423.4}
OP={y:GP[y]-SGA[y] for y in GP}
print('operating profit before impairments/divestitures (GP-SG&A):',{y:round(OP[y]) for y in OP})
print('margin %',{y:round(OP[y]/s*100,1) for y,s in zip(GP,[11535.9,12277.0,12050.9,11612.8,11281.6])})
g_op=(OP[26]/OP[22])**(1/4)-1; print('op profit growth FY22-26 %/yr',round(g_op*100,2))
oc5=1005; oc5da=1024
for lab,c in [('5yr mean capex basis',1005),('5yr mean D&A basis',1024)]:
    for g in [0.0,g_op]:
        v=dcf(c,g); print(f'{lab} g={g*100:.2f}%  value {v:,.0f}m  per share {v/sh:.2f}')
# normalized owner cash from earnings: (OP + equity dividends(use earnings ~ distributions avg 165) - interest)*(1-0.24) + D&A - capex
eqd=184.3
norm={}
for y in OP:
    pre=OP[y]+eqd-INT[y]
    norm[y]=pre*(1-0.24)+DA[y]-CX[y]
print('normalized owner cash',{y:round(v) for y,v in norm.items()}, 'mean',round(sum(norm.values())/5))
nm=sum(norm.values())/5
for g in [0.0,g_op]:
    v=dcf(nm,g); print(f'normalized mean g={g*100:.2f}% value {v:,.0f} per share {v/sh:.2f}')
v=dcf(norm[26],g_op); print('FY26 run-rate normalized, decline', round(v), round(v/sh,2))
# fair price: after-tax owner cash yield + g = floor_after_tax
fl=0.10*(1-0.24); print('after-tax floor',fl)
for lab,c,g in [('5yr mean, no growth',1005,0),('5yr mean, decline',1005,g_op),('normalized mean, decline',nm,g_op),('FY26 normalized run-rate, decline',norm[26],g_op)]:
    P=c/(fl-g); print(f'fair {lab}: {P:,.0f}m  {P/sh:.2f}/sh   yield at price {c/(price*sh)*100:.1f}%  exp return {(c/(price*sh)+g)*100:.1f}% after tax, {(c/(price*sh)+g)/(1-0.24)*100:.1f}% pre-tax')
print('mkt cap',price*sh)
def solve(c,target):
    lo,hi=-0.9,0.2
    for _ in range(200):
        m=(lo+hi)/2
        if dcf(c,m)>target: hi=m
        else: lo=m
    return m
print('implied g (10y then flat) for 1005:',round(solve(1005,price*sh)*100,1),' for 764:',round(solve(764,price*sh)*100,1))
print('FY24-26 op decline %/yr', round(((1259/1846)**0.5-1)*100,1))
for c,g in [(764,-0.05),(764,-0.10)]:
    P=c/(fl-g); print('cheap test',c,g,round(P),round(P/sh,2))
print('Q1 op profit change', round((268.4/347.4-1)*100,1))
