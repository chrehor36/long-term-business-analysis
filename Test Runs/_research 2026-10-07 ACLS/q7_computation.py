# COMPUTATION, NOT A CLEARANCE (Q1 closed the file). Q7 construction per Framework v5 Part VI conventions.
# All figures USD millions from the filed cash-flow statements (XBRL first-filed vintage, cross-checked in run file).
r=0.0564; floor=0.10; shares=30.881489; netcash=154.996+247.220+174.829-(1.722+39.845)  # 2026-06-30 10-Q
OCF={2016:-8.8,2017:56.3,2018:47.0,2019:-13.6,2020:69.7,2021:150.2,2022:215.6,2023:156.9,2024:140.8,2025:118.3}
SBC={2016:5.2,2017:5.7,2018:7.8,2019:8.2,2020:10.5,2021:12.1,2022:13.4,2023:18.3,2024:21.0,2025:20.8}
CAPEX={2016:2.5,2017:7.3,2018:4.7,2019:12.0,2020:7.4,2021:8.7,2022:10.7,2023:20.7,2024:12.2,2025:11.3}
FLP={2016:0.0,2017:0.0,2018:0.0,2019:0.0,2020:0.4,2021:0.8,2022:1.0,2023:1.2,2024:1.5,2025:1.4}
II={2016:0.2,2017:0.7,2018:2.3,2019:3.0,2020:0.7,2021:0.2,2022:4.6,2023:18.199,2024:24.403,2025:21.484}
IE={2016:5.1,2017:5.1,2018:5.1,2019:5.2,2020:5.2,2021:4.8,2022:5.6,2023:5.347,2024:5.462,2025:5.364}
PRE={2016:11.0,2017:43.8,2018:54.7,2019:20.9,2020:55.9,2021:120.4,2022:204.9,2023:278.6,2024:230.3,2025:138.2}
TAX={2016:0.0,2017:-83.1,2018:8.8,2019:3.9,2020:5.9,2021:21.8,2022:21.8,2023:32.3,2024:29.3,2025:18.0}
lev={};unl={}
for y in OCF:
    oc=OCF[y]-SBC[y]-CAPEX[y]-FLP[y]
    t=TAX[y]/PRE[y] if PRE[y]>0 and TAX[y]>0 else 0.0
    lev[y]=oc; unl[y]=oc-(II[y]-IE[y])*(1-t)
    print(y, f"owner cash {oc:7.1f}  tax rate {t:5.3f}  unlevered {unl[y]:7.1f}")
def stream(c0,g,n=10): return [c0*(1+g)**t for t in range(1,n+1)]
def pv(cs,rate):
    v=sum(c/(1+rate)**(i+1) for i,c in enumerate(cs)); return v+cs[-1]/rate/(1+rate)**len(cs)
def report(name,base,g_lo,g_hi,cash_adj=True):
    lo=stream(base,g_lo); hi=stream(base,g_hi)
    vlo,vhi=pv(lo,r),pv(hi,r)
    if vlo>vhi: vlo,vhi,lo,hi=vhi,vlo,hi,lo
    mid=[(a+b)/2 for a,b in zip(lo,hi)]
    fair=pv(mid,floor)
    add=netcash if cash_adj else 0.0
    ps=lambda v:(v+add)/shares
    print(f"{name}: base {base:.1f}; growth ends {g_lo:+.3f}/{g_hi:+.3f}; value range ${ps(vlo):.2f} to ${ps(vhi):.2f} a share (width {vhi/vlo if vlo>0 else float('nan'):.2f}x on the business, {ps(vhi)/ps(vlo):.2f}x per share); midpoint ${ps((vlo+vhi)/2):.2f}; FAIR PRICE ${ps(fair):.2f}")
    return ps(vlo),ps(vhi),ps(fair)
print('net cash at 2026-06-30', round(netcash,1))
w=[2021,2022,2023,2024,2025]
b=sum(unl[y] for y in w)/5; g=(unl[2025]/unl[2021])**(1/4)-1
print('literal window unlevered avg',round(b,1),'growth 2021->2025',round(g,4))
report('A. ALL-EQUITY, literal five-year window (decline carried as bottom, no growth top)',b,g,0.0)
bl=sum(lev[y] for y in w)/5; gl=(lev[2025]/lev[2021])**(1/4)-1
print('literal window levered avg',round(bl,1),'growth',round(gl,4))
report('B. EQUITY-ONLY, literal window',bl,gl,0.0,cash_adj=False)
cyc=list(range(2019,2026)); prev=[2016,2017,2018]
bc=sum(unl[y] for y in cyc)/len(cyc); bp=sum(unl[y] for y in prev)/3
gc=(bc/bp)**(1/5)-1
print('cycle 2019-2025 unlevered avg',round(bc,1),'prior cycle 2016-2018 avg',round(bp,1),'growth between cycle averages',round(gc,4))
rev={2016:267.0,2017:410.6,2018:442.6,2019:343.0,2020:474.6,2021:662.4,2022:920.0,2023:1130.6,2024:1017.9,2025:839.0}
grev=((sum(rev[y] for y in cyc)/7)/(sum(rev[y] for y in prev)/3))**(1/5)-1
print('revenue growth between cycle averages',round(grev,4))
report('C. ALL-EQUITY, whole-cycle variant, growth cut back to revenue growth between cycles',bc,0.0,grev)
report('D. ALL-EQUITY, whole-cycle variant, no growth only',bc,0.0,0.0)
print('price 141.15; market cap',round(141.15*shares,1),'EV',round(141.15*shares-netcash,1))
blc=sum(lev[y] for y in cyc)/len(cyc); blp=sum(lev[y] for y in prev)/3
print('levered cycle avg',round(blc,1),'prior',round(blp,1))
report('E. EQUITY-ONLY, whole-cycle variant, growth cut back to revenue growth between cycles',blc,0.0,grev,cash_adj=False)
# the uncut shown rate, shown only to record why it was cut back
c10=bc*(1+gc)**10; print('uncut shown rate year-10 owner cash',round(c10),'against 2025 revenue 839')
c10r=bc*(1+grev)**10; print('cut-back year-10 owner cash',round(c10r))
