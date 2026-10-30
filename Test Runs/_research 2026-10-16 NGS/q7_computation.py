# COMPUTATION, NOT A CLEARANCE: NGS Q7 arithmetic beneath the Q2 stop (USD millions)
import json
from facts import annual
d=json.load(open('cache/peers/NGS.json'))
def g(t): return {k:v[0]/1e6 for k,v in annual(d,t).items()}
ocf=g('NetCashProvidedByUsedInOperatingActivities'); sbc=g('ShareBasedCompensation'); da=g('DepreciationDepletionAndAmortization')
cap=g('PaymentsToAcquirePropertyPlantAndEquipment'); ip=g('InterestPaidNet'); ip.update({k:v for k,v in g('InterestPaid').items() if k not in ip})
T=0.21  # interest add-back at the federal statutory rate (NGS paid almost no cash tax; NOLs do not expire)
def oe_da_ae(y): return ocf[y]-sbc[y]-da[y]+ip.get(y,0)*(1-T)       # maintenance = depreciation, before interest
def oe_da_eq(y): return ocf[y]-sbc[y]-da[y]                          # same, after interest as paid
def oe_all_ae(y): return ocf[y]-sbc[y]-cap[y]+ip.get(y,0)*(1-T)      # all capital spending, before interest
yrs=[str(y) for y in range(2014,2026)]; win=[str(y) for y in range(2021,2026)]; prev=[str(y) for y in range(2009,2015)]
m=lambda f,ys: sum(f(y) for y in ys)/len(ys)
filer_maint={'2024':11.4,'2025':11.7}
oe_fm={y: ocf[y]-sbc[y]-filer_maint[y]+ip[y]*(1-T) for y in filer_maint}
flat_ae=5.919*(1-0.249)            # Flatrock FY2025 operating income after NGS's FY2025 effective rate (8-K/A ex.99.1)
flat_eq=flat_ae-108.928*0.0648*(1-T)  # less NGS's cost of the cash paid, at the 10-Q's 6.48% facility rate
ND=328.0-0.084; SH=12.898; P=30.96; R=0.0543; F=0.10
def pv(c,gr,r):
    v=sum(c*(1+gr)**t/(1+r)**t for t in range(1,11)); return v + c*(1+gr)**10/r/(1+r)**10
cyc=m(oe_da_ae,yrs); cyc_prev=m(oe_da_ae,prev); wnd=m(oe_da_ae,win); fm=sum(oe_fm.values())/2
gr=(cyc/cyc_prev)**(1/8)-1   # midpoints 2011.5 -> 2019.5 (approx.; 2009-2014 six years, 2014-2025 twelve)
print(f"cycle base 2014-2025 (maint=D&A, all-equity): {cyc:.2f}; previous cycle 2009-2014: {cyc_prev:.2f}; growth between cycles {100*gr:.1f}%/yr")
print(f"window 2021-2025 (maint=D&A, all-equity): {wnd:.2f}; per year " + ", ".join(f"{y} {oe_da_ae(y):.1f}" for y in win))
print(f"window all-spending all-equity mean: {m(oe_all_ae,win):.2f}; filer-maintenance 2024-25 mean {fm:.2f} ({oe_fm})")
print(f"Flatrock all-equity {flat_ae:.2f}; after its financing {flat_eq:.2f}")
print(f"EV at price {P*SH+ND:.1f}; market cap {P*SH:.1f}; net debt {ND:.1f}")
cases={'central top: cycle base, no growth':(cyc+flat_ae,0.0),'central bottom: cycle base, decline between cycles':(cyc+flat_ae,gr),
       'window beside: 2021-25, no growth (growth meaningless, (b))':(wnd+flat_ae,0.0),'filer-maintenance variant beside: 2024-25, no growth':(fm+flat_ae,0.0)}
for k,(c,gg) in cases.items():
    ev=pv(c,gg,R); ev10=pv(c,gg,F)
    print(f"{k}: cash {c:.2f}  EV@5.43% {ev:.1f} -> ${ (ev-ND)/SH:.2f}/sh ; EV@10% {ev10:.1f} -> ${(ev10-ND)/SH:.2f}/sh ; yield on EV at price {100*c/(P*SH+ND):.1f}%")
# fair price (Part VII): each end of the central range valued at 10%, averaged, all-equity less net debt
top10=pv(cyc+flat_ae,0,F); bot10=pv(cyc+flat_ae,gr,F)
print(f"FAIR (central, all-equity): ${((top10+bot10)/2-ND)/SH:.2f}/sh")
# equity-only beside: owner cash after interest as paid (cycle base) plus Flatrock after its financing, against market cap
eq_c=m(oe_da_eq,yrs)+flat_eq
print(f"equity-only cash (cycle base, after interest as paid) {eq_c:.2f}; at 10% no growth ${eq_c/F/SH:.2f}/sh; decline case ${pv(eq_c,gr,F)/SH:.2f}/sh; fair ${(eq_c/F+pv(eq_c,gr,F))/2/SH:.2f}/sh")
cur_int=328.0*0.0648*(1-T); print(f"current after-tax interest on June-2026 debt {cur_int:.2f}; central all-equity cash less it {cyc+flat_ae-cur_int:.2f}")
print(f"cash needed for the floor at the price, no growth: {F*(P*SH+ND):.1f} all-equity")
