# Q7 arithmetic for the ORLY run of 2026-10-10. USD millions. Sources: XBRL first-filed (facts.json), checked
# against the FY2025 10-K cash-flow statement for 2023-2025. Conventions: Framework v5 Q7 (range, six specifics,
# floor, all-equity basis). This is arithmetic only.
yrs=list(range(2016,2026))
OCF=dict(zip(yrs,[1454,1404,1728,1708,2837,3207,3148,3034,3050,2762]))
SBC=dict(zip(yrs,[19,19,20,22,23,25,26,28,29,35]))
DA =dict(zip(yrs,[218,234,259,271,315,328,358,409,462,511]))
CPX=dict(zip(yrs,[476,466,504,628,466,443,563,1006,1023,1169]))
TCI=dict(zip(yrs,[0,0,0,33.8,164.1,180.3,188.3,4.2,-1.5,0]))    # investment in tax credit equity investments (investing), 10-Ks FY2019, FY2022, FY2025
ACQ=dict(zip(yrs,[58.9,2.7,34.8,142.0,1.0,1.9,3.2,3.2,161.3,14.4]))  # "Other, including acquisitions" (investing), 10-Ks FY2017, FY2019, FY2022, FY2025
PROC=dict(zip(yrs,[5.1,4.5,4.8,7.1,15.8,9.5,14.8,17.7,16.4,30.8]))  # proceeds from sale of property and equipment
INTP=dict(zip(yrs,[64,78,118,135,160,144,156,190,209,227]))   # interest paid, XBRL InterestPaidNet
TAXR=0.225   # company's own effective rate, 2026 guidance 22.5% (8-K 2026-07-29 ex 99.1); used only to put interest after tax
R=0.056; FLOOR=0.10
NETDEBT=6752.4; SHARES=808.961; PRICE=86.45
def series(maint):
    # tax-credit fund investments are the cost of a tax saving that shows in OCF: deducted in both cases.
    # maintenance-only: depreciation as the maintenance guess; acquisitions are growth spending, not deducted.
    # all-spending: capital spending net of asset-sale proceeds, and acquisitions deducted (specific (c), total growth credited).
    if maint: return {y: OCF[y]-SBC[y]-TCI[y]-DA[y] for y in yrs}
    return {y: OCF[y]-SBC[y]-TCI[y]-(CPX[y]-PROC[y])-ACQ[y] for y in yrs}
def unlev(s): return {y: s[y]+INTP[y]*(1-TAXR) for y in yrs}
def avg(s,ys): return sum(s[y] for y in ys)/len(ys)
def pv(c0,g,r,years=10):
    v=0; c=c0
    for t in range(1,years+1):
        c=c*(1+g); v+=c/(1+r)**t
    term=c/r/(1+r)**years   # zero nominal growth after year ten
    return v+term
H1=range(2016,2021); H2=range(2021,2026)
def g_of(s): return (avg(s,H2)/avg(s,H1))**(1/5)-1
M=series(True); A=series(False); Mu=unlev(M); Au=unlev(A)
for nm,s_ in [('maintenance-only',M),('all-spending',A)]:
    print(nm,'equity by year',{y:round(s_[y]) for y in yrs})
    u=unlev(s_); print(nm,'unlevered by year',{y:round(u[y]) for y in yrs})
    print(f"  2021-25 avg unlevered {avg(u,H2):.0f}, equity {avg(s_,H2):.0f}; 2016-20 avg unlevered {avg(u,H1):.0f}; growth between averages {g_of(u)*100:.2f}%; literal 2021->2025 {((u[2025]/u[2021])**0.25-1)*100:.2f}%")
ps=lambda ev:(ev-NETDEBT)/SHARES
gA=g_of(Au); gM=g_of(Mu)
ends={'maint no-growth':pv(avg(Mu,H2),0,R),'all-spend growth':pv(avg(Au,H2),gA,R),
      'all-spend no-growth':pv(avg(Au,H2),0,R),'maint growth':pv(avg(Mu,H2),gM,R)}
for k,v in ends.items(): print(f"  {k:22s} EV {v:8.0f}  per share ${ps(v):7.2f}")
lo,hi=sorted([ps(ends['maint no-growth']),ps(ends['all-spend growth'])])
print(f"CENTRAL RANGE (all-equity basis, sovereign {R*100}%): ${lo:.2f} to ${hi:.2f}  ratio {hi/lo:.2f}  price ${PRICE}")
print(f"BESIDE all-spending both ends: ${ps(ends['all-spend no-growth']):.2f} to ${ps(ends['all-spend growth']):.2f}")
gl=(Au[2025]/Au[2021])**0.25-1; gml=(Mu[2025]/Mu[2021])**0.25-1
print(f"LITERAL WINDOW (growth 2021->2025 negative, carried as bottom; no growth top): all-spending ${ps(pv(avg(Au,H2),gl,R)):.2f} to ${ps(ends['all-spend no-growth']):.2f}; maintenance ${ps(pv(avg(Mu,H2),gml,R)):.2f} to ${ps(ends['maint no-growth']):.2f}")
# fair price: the price at which the midpoint of the range earns the floor
f_ev=(pv(avg(Mu,H2),0,FLOOR)+pv(avg(Au,H2),gA,FLOOR))/2
print(f"FAIR all-equity: EV {f_ev:.0f} -> ${ps(f_ev):.2f} a share")
geA=g_of(A)
f_eq=(pv(avg(M,H2),0,FLOOR)+pv(avg(A,H2),geA,FLOOR))/2
print(f"FAIR equity-only (owner cash after interest, growth {geA*100:.2f}%): equity value {f_eq:.0f} -> ${f_eq/SHARES:.2f} a share")
ev=PRICE*SHARES+NETDEBT; a,b=0.001,0.5
for _ in range(200):
    m=(a+b)/2; v=(pv(avg(Mu,H2),0,m)+pv(avg(Au,H2),gA,m))/2
    a,b=(m,b) if v>ev else (a,m)
print(f"EV at price {ev:.0f}; implied return on the midpoint of the two end streams at the price: {m*100:.2f}%")
# sensitivity: growth excluding the 2016-17 pre-tax-reform years: compare 2018-20 avg to 2023-25 avg over 5 years
gx=((avg(Au,range(2023,2026))/avg(Au,range(2018,2021)))**(1/5)-1)
print(f"sensitivity: all-spending growth 2018-20 avg to 2023-25 avg {gx*100:.2f}%: top ${ps(pv(avg(Au,H2),gx,R)):.2f}")
