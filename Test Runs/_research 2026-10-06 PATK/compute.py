# COMPUTATION - NOT A CLEARANCE. Arithmetic for the PATK run of 2026-10-06. Inputs from XBRL facts (facts.json,
# peers/LCII_facts.json) cross-checked against the filed statements; price aggregator-flagged.
r=0.0566          # 30-yr Treasury par yield 2026-10-05 (tools/run.py, Treasury curve)
price=66.59; sh=32.118   # cover count 2026-07-31 (10-Q 0000076605-26-000075)
netdebt=1429.3-29.2      # 10-Q June 28, 2026: total debt principal 1,429.3; cash 29.2
interest=74.5; tax=0.237 # FY2025 interest expense net; FY2025 effective tax rate (10-K)
P={ # year: rev, ocf, sbc, capex, acq, da, amort
2009:(212.5,3.9,0.1,0.3,0.0,None,0.4),2010:(278.2,7.9,0.2,1.4,5.8,5.0,0.6),2011:(307.8,11.8,0.3,2.4,7.3,4.9,0.8),
2012:(437.4,21.0,0.8,7.9,29.3,5.6,1.5),2013:(594.9,22.4,1.3,8.7,16.5,7.3,2.4),2014:(735.7,45.7,3.3,6.5,72.1,10.4,4.5),
2015:(920.3,65.6,4.7,8.0,140.2,16.8,8.8),2016:(1221.9,97.1,6.5,15.4,138.8,24.4,13.4),2017:(1635.7,99.9,10.4,22.5,251.9,33.5,19.4),
2018:(2263.1,200.0,14.0,34.5,343.3,55.1,34.2),2019:(2337.1,192.4,15.4,27.7,56.0,62.8,35.9),2020:(2486.6,160.2,7.2,32.1,306.0,73.3,40.9),
2021:(4078.1,252.1,22.9,64.8,508.1,104.8,56.3),2022:(4881.9,411.7,21.8,79.9,248.9,130.8,73.2),2023:(3468.0,408.7,19.4,59.0,25.9,144.5,78.7),
2024:(3715.7,326.8,16.8,75.7,411.7,166.5,96.3),2025:(3950.8,329.4,19.1,82.9,121.7,170.2,97.3)}
L={2016:(1678.9,203.4,15.4,44.7,48.7),2017:(2147.8,155.1,20.0,87.2,60.6),2018:(2475.8,156.6,14.1,119.8,184.8),2019:(2371.5,269.5,16.1,58.2,447.8),
2020:(2796.2,231.4,18.5,57.3,182.1),2021:(4472.7,-111.6,27.2,98.5,194.1),2022:(5207.1,602.5,23.7,130.6,108.5),2023:(3784.8,527.2,18.2,62.2,25.9),
2024:(3741.2,370.3,18.7,42.3,20.0),2025:(4122.0,331.0,22.7,52.6,112.7)}
oe={y:v[1]-v[2]-v[3] for y,v in P.items()}
print("PATK owner cash (OCF-SBC-capex), margin, after acquisitions:")
for y in sorted(P): print(y, f"{oe[y]:7.1f} {100*oe[y]/P[y][0]:5.1f}%  after acq {oe[y]-P[y][4]:7.1f}")
w=range(2021,2026)
avg5=sum(oe[y] for y in w)/5; acq5=sum(P[y][4] for y in w)/5
dep={y:P[y][5]-P[y][6] for y in w}
avgDA=sum(P[y][1]-P[y][2]-P[y][5] for y in w)/5; avgDep=sum(P[y][1]-P[y][2]-dep[y] for y in w)/5
print(f"5yr avg capex basis {avg5:.1f}; D&A variant {avgDA:.1f}; depreciation-only variant {avgDep:.1f}; avg acquisitions {acq5:.1f}; avg capex {sum(P[y][3] for y in w)/5:.1f} vs avg depreciation {sum(dep.values())/5:.1f}")
g=(oe[2025]/oe[2021])**0.25-1; print(f"growth shown 2021->2025 aggregate owner cash {100*g:.2f}%/yr")
m10=sum(oe[y]/P[y][0] for y in range(2016,2026))/10; m17=sum(oe[y]/P[y][0] for y in range(2009,2026))/17
print(f"cycle margins: 2016-25 {100*m10:.2f}%  2009-25 {100*m17:.2f}%")
wc=m10*P[2025][0]; st=m17*P[2025][0]; print(f"whole-cycle owner cash {wc:.1f}; stress {st:.1f}")
def nogrowth(c): return c/r
def growth(c,g,acq=0.0):
    v=0; x=c
    for t in range(1,11):
        x*=1+g; v+=(x-acq)/(1+r)**t
    v+=x/r/(1+r)**10
    return v
ps=lambda v: v/sh
print("VALUE (equity, levered owner cash, at the long bond):")
for name,c in [("5yr capex",avg5),("5yr D&A",avgDA),("whole-cycle",wc),("stress",st)]:
    print(f"  no-growth {name:12s} {nogrowth(c):8.0f}  ${ps(nogrowth(c)):6.1f}")
print(f"  shown growth uncapped (acquisitions not deducted) {growth(avg5,g):8.0f} ${ps(growth(avg5,g)):6.1f}")
print(f"  shown growth capped (acquisitions {acq5:.0f}/yr deducted 10 yrs) {growth(avg5,g,acq5):8.0f} ${ps(growth(avg5,g,acq5)):6.1f}")
def fair(c, enterprise=True, floor=0.10):
    pre=c/(1-tax)
    if enterprise: return ((pre+interest)/floor-netdebt)/sh
    return pre/floor/sh
for name,c in [("5yr capex",avg5),("whole-cycle (central)",wc),("stress",st),("5yr D&A",avgDA)]:
    print(f"FAIR {name:22s} enterprise ${fair(c):6.1f}   equity-only ${fair(c,False):6.1f}   pre-tax yield on EV at price {(c/(1-tax)+interest)/(price*sh+netdebt)*100:5.1f}%")
# pro forma combined (computation only)
lo={y:v[1]-v[2]-v[3] for y,v in L.items()}
l5=sum(lo[y] for y in w)/5; lm=sum(lo[y]/L[y][0] for y in L)/10; lwc=lm*L[2025][0]
print(f"LCII 5yr owner cash {l5:.1f}; 10yr margin {100*lm:.2f}%; whole-cycle {lwc:.1f}; LCII 10yr sum {sum(lo.values()):.0f} vs PATK 10yr sum {sum(oe[y] for y in range(2016,2026)):.0f}")
pfsh=62.443; pfnd=2133.7+6.7-59.3; pfint=74.5+35.7
c=wc+lwc; pre=c/(1-tax)
print(f"PRO FORMA central owner cash {c:.1f}; per basic share ${c/pfsh:.2f} vs standalone ${wc/sh:.2f}; 5yr ${ (avg5+l5)/pfsh:.2f} vs ${avg5/sh:.2f}")
print(f"PRO FORMA fair enterprise ${((pre+pfint)/0.10-pfnd)/pfsh:.1f}; equity-only ${pre/0.10/pfsh:.1f}; net debt {pfnd:.0f}")
cheap1=fair(st); cheap2=0.5*ps(nogrowth(wc)); print(f"CHEAP: stress clears floor (enterprise) ${cheap1:.1f}; half of whole-cycle no-growth value ${cheap2:.1f}; rule takes the lower")
print(f"market cap {price*sh:.0f}; EV {price*sh+netdebt:.0f}; owner-cash yield (5yr) {avg5/(price*sh)*100:.1f}%")
