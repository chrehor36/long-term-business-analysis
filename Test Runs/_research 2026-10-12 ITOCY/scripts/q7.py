# Q7 arithmetic for the ITOCY run, yen billions. Every input is from the company's filed statements (see _notes.md).
yrs=[2022,2023,2024,2025,2026]
OCF  =[801.163,938.058,978.108,997.278,1131.837]
CAPEX=[157.142,194.081,202.546,227.465,284.991]
PPES =[32.259,28.360,66.162,34.831,24.908]
LEASE=[266.974,261.271,252.580,260.320,259.227]
NCID =[20.897,28.547,21.404,25.626,25.887]
INTP =[29.807,57.855,96.119,102.845,101.803]
INTR =[19.706,35.029,61.789,47.839,40.850]
LINT =[12.961,13.559,14.948,17.495,20.825]
DA   =[404.184,409.962,420.343,450.007,458.696]
# acquisitions (cash for business interests, net of sales), incl. equity transactions with NCI
EQP=[-34.723,-328.634,-60.260,-214.130,-318.088]; EQS=[101.766,33.744,37.334,83.918,215.430]
OIP=[-70.381,-60.776,-66.479,-129.397,-138.317]; OIS=[184.158,39.585,42.090,54.653,99.462]
SUB=[-30.433,-26.033+70.161,-36.180,-109.847,0.0]; NCI=[-14.093,54.766,-387.845,-45.755,-57.557]
REV=[12293.348,13945.633,14029.910,14724.234,14823.087]
NP =[820.269,800.519,801.770,880.251,900.283]
t=0.31
oc=[OCF[i]-CAPEX[i]+PPES[i]-LEASE[i]-NCID[i] for i in range(5)]
ni=[(INTP[i]-LINT[i]-INTR[i])*(1-t) for i in range(5)]
acq=[EQP[i]+EQS[i]+OIP[i]+OIS[i]+SUB[i]+NCI[i] for i in range(5)]
acq_x=[EQP[i]+EQS[i]+OIP[i]+OIS[i]+SUB[i] for i in range(5)]
mnt=[DA[i]-LEASE[i] for i in range(5)]  # maintenance guess: D&A less lease principal (proxy for ROU depreciation)
gcap=[CAPEX[i]-mnt[i] for i in range(5)]
avg=lambda x:sum(x)/len(x)
for i,y in enumerate(yrs):
    print(f"FY{y}: owner cash (equity-only, before purchases) {oc[i]:8.1f}  after-tax net interest {ni[i]:6.1f}  net purchases {acq[i]:8.1f} (excl NCI {acq_x[i]:8.1f})  maint guess {mnt[i]:6.1f} growth capex {gcap[i]:6.1f}  OC/rev {oc[i]/REV[i]*100:4.2f}%  NP {NP[i]}")
A_oc,A_ni,A_acq,A_g=avg(oc),avg(ni),avg(acq),avg(gcap)
print(f"5y avg: OC {A_oc:.1f}  int {A_ni:.1f}  purchases {A_acq:.1f}  growth capex {A_g:.1f}  NP {avg(NP):.1f}")
print(f"net purchases over window {sum(acq):.1f} vs half OC before purchases {sum(oc)/2:.1f} (all-equity {(sum(oc)+sum(ni))/2:.1f}); excl NCI {sum(acq_x):.1f}")
g_lit=(oc[-1]/oc[0])**0.25-1
g_half=(avg(oc[3:5])/avg(oc[0:2]))**(1/3)-1
g_rev=(REV[-1]/REV[0])**0.25-1
print(f"growth: literal {g_lit*100:.2f}%  halves {g_half*100:.2f}%  revenue {g_rev*100:.2f}%")
# cap test (f): shown growth for 10y vs highest share of sales earned
hi=max(o/r for o,r in zip(oc,REV)); hi=max(hi,0.0423)
proj=oc[-1]*(1+g_lit)**10/(REV[-1]*(1+g_rev)**10)
print(f"share of sales after 10y at literal growth {proj*100:.2f}% vs highest earned {hi*100:.2f}% -> cut to sales growth, capped at discount rate")
r=0.04136
g=min(g_rev,r)
print(f"rate {r*100:.3f}%  growth carried {g*100:.3f}%")
SH=6899.334417  # million shares -> bn when multiplied by yen
ND=3610.0
def pv(c_years, terminal, rate):
    v=sum(c/(1+rate)**(t+1) for t,c in enumerate(c_years))
    return v+terminal/rate/(1+rate)**10
def cases(base_before, purchases, growth_capex, rate, central=True):
    # no-growth: owner cash before purchases (and, central (e), after maintenance only)
    ng_base = base_before + (growth_capex if central else 0)
    ng = ng_base/rate
    # growth: years 1-10 grow at g with purchases (and growth capex) deducted; after year 10 no growth, no purchases
    yrs_c=[(base_before+purchases)*(1+g)**t for t in range(1,11)]
    term=ng_base*(1+g)**10
    gr=pv(yrs_c,term,rate)
    return ng,gr
for label,base,central in [("ALL-EQUITY, central (e) maintenance-only",A_oc+A_ni,True),("ALL-EQUITY, all-spending beside",A_oc+A_ni,False),("EQUITY-ONLY, central (e)",A_oc,True),("EQUITY-ONLY, all-spending",A_oc,False)]:
    nd = ND if label.startswith("ALL") else 0.0
    ng,gr=cases(base,A_acq,A_g,r,central)
    lo,hi_=sorted([ng,gr])
    print(f"\n{label}: base before purchases {base:.1f}")
    print(f"  range at {r*100:.3f}%: whole {lo:,.0f} to {hi_:,.0f} bn; less net debt {nd:,.0f}: per share Y{(lo-nd)/SH*1000:,.0f} to Y{(hi_-nd)/SH*1000:,.0f}  (no-growth {ng:,.0f}, growth {gr:,.0f}); width {hi_/lo:.2f}x")
    ng10,gr10=cases(base,A_acq,A_g,0.10,central)
    fair=((ng10+gr10)/2-nd)/SH*1000
    print(f"  at 10%: no-growth {ng10:,.0f}, growth {gr10:,.0f}; fair price Y{fair:,.0f} per share (${fair/158.56:.2f} per ADS at 158.56)")
    # expected return at price: solve rate where avg of cases = price*shares+nd
    mv=2155*SH/1000+nd
    for case in ("ng","gr"):
        lo_r,hi_r=0.001,0.5
        for _ in range(100):
            m=(lo_r+hi_r)/2; a,b=cases(base,A_acq,A_g,m,central); v=a if case=="ng" else b
            if v>mv: lo_r=m
            else: hi_r=m
        print(f"  expected return at Y2,155 ({case}): {m*100:.2f}%")
# beside: Dentsu Soken signed, unclosed: 74.71M shares x 2,880 added to net debt, credited at nothing
ds=74.71*2.880
print(f"\nDentsu Soken beside: financing {ds:.1f} bn -> -Y{ds/SH*1000:.0f} per share on every figure")

# Sensitivity: purchases excluding equity transactions with non-controlling interests
A_acq_x=avg(acq_x)
for label,base,central in [("ALL-EQUITY central, purchases excl. NCI buy-outs",A_oc+A_ni,True)]:
    ng,gr=cases(base,A_acq_x,A_g,r,central); ng10,gr10=cases(base,A_acq_x,A_g,0.10,central)
    print(f"\n{label}: purchases {A_acq_x:.1f}; range Y{(min(ng,gr)-ND)/SH*1000:,.0f} to Y{(max(ng,gr)-ND)/SH*1000:,.0f}; fair Y{((ng10+gr10)/2-ND)/SH*1000:,.0f}")
# Literal growth uncut, shown only to show what the cut removes (all-equity central)
g_save=g
g=g_lit
ng,gr=cases(A_oc+A_ni,A_acq,A_g,r,True)
print(f"\nLiteral growth {g_lit*100:.2f}% uncut (not used; (f) cuts it): growth case Y{(gr-ND)/SH*1000:,.0f} per share; expected-return check at price below")
g=g_save
g=g_lit
mv=2155*SH/1000+ND
lo_r,hi_r=0.001,0.5
for _ in range(100):
    m=(lo_r+hi_r)/2; a,b=cases(A_oc+A_ni,A_acq,A_g,m,True)
    if b>mv: lo_r=m
    else: hi_r=m
print(f"expected return at Y2,155 on the uncut literal-growth case: {m*100:.2f}%")
g=g_save
