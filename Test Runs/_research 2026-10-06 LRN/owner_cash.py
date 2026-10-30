# Owner cash after every real cost, FY2012-FY2026, USD millions. Sources: XBRL companyfacts (first-filed vintage)
# cross-read against the filed cash-flow statements (10-K accessions listed in the run file).
yrs=list(range(2012,2027))
rev=[708.4,848.2,919.6,948.3,872.7,888.5,917.7,1015.8,1040.8,1536.8,1686.7,1837.4,2040.1,2405.3,2518.1]
opi=[29.0,45.7,22.9,18.4,13.9,13.1,25.5,45.5,32.5,110.5,156.6,165.5,249.6,360.1,450.8]
ocf=[33.0,95.3,123.5,120.1,121.8,88.7,103.6,141.6,80.4,134.2,206.9,203.2,278.8,432.8,433.8]
sbc=[10.1,14.4,22.8,21.3,18.6,22.6,20.8,16.7,23.6,39.3,18.6,20.3,31.5,36.8,40.3]
ppe=[10.5,8.3,7.4,9.9,5.0,2.2,8.7,5.5,1.7,3.6,9.7,4.3,2.3,1.8,0.6]
sw =[22.0,23.4,26.6,33.8,36.3,26.9,24.5,26.3,24.0,31.3,42.2,45.0,40.7,36.4,61.6]
cur=[16.1,18.6,15.4,18.1,21.6,19.1,9.9,16.6,19.3,17.4,15.7,17.2,18.7,21.8,16.7]
lease=[16.6,20.3,22.7,21.9,17.4,15.7,13.3,21.0,27.7,24.3,33.0,43.0,40.9,41.5,56.9]
da=[58.0,65.7,86.3,83.8,68.2,74.3,75.3,71.4,72.1,90.1,97.9,110.4,109.7,114.7,126.6]
oc=[];print("FY    rev    opinc  opm%   OCF   SBC  capex_all  D&A  ownercash  oc%rev")
for i,y in enumerate(yrs):
    cap=ppe[i]+sw[i]+cur[i]+lease[i]
    o=ocf[i]-sbc[i]-cap; oc.append(o)
    print(f"{y} {rev[i]:7.1f} {opi[i]:6.1f} {100*opi[i]/rev[i]:5.1f} {ocf[i]:6.1f} {sbc[i]:5.1f} {cap:8.1f} {da[i]:6.1f} {o:9.1f} {100*o/rev[i]:6.1f}")
import statistics as st
avg5=st.mean(oc[-5:]); avg15=st.mean(oc)
m15=st.mean([oc[i]/rev[i] for i in range(15)]); m_pre=st.mean([oc[i]/rev[i] for i in range(9)])
print(f"5yr avg FY22-26 owner cash {avg5:.1f}; 15yr avg {avg15:.1f}; 15yr avg oc margin {100*m15:.2f}%; FY12-20 avg margin {100*m_pre:.2f}%")
g_oc=(oc[-1]/oc[-5])**(1/4)-1; g_rev=(rev[-1]/rev[-5])**(1/4)-1
print(f"growth shown FY22->FY26: owner cash {100*g_oc:.1f}%/yr; revenue {100*g_rev:.1f}%/yr")
# value: 10 yrs at g then zero nominal growth, at r
def val(c0,g,r,n=10):
    pv=0;c=c0
    for t in range(1,n+1):
        c*=1+g; pv+=c/(1+r)**t
    return pv + c/r/(1+r)**n
r=0.0566; sh=41.559845; price=78.88
excess=749.6-420.0   # cash+securities at the seasonal low (2025-09-30) less the convertible principal
excess_hi=1034.1-420.0
for lab,c0,g in [("no-growth (5yr avg)",avg5,0.0),("shown growth capped at revenue growth",avg5,g_rev),("whole-cycle no-growth (15yr margin x FY26 rev)",m15*rev[-1],0.0),("whole-cycle at capped growth",m15*rev[-1],g_rev)]:
    v=val(c0,g,r); print(f"{lab:48s} c0={c0:7.1f} g={100*g:4.1f}%  EV={v:8.0f}  per share (excess {excess:.0f}) = {(v+excess)/sh:7.2f}  (excess {excess_hi:.0f}) = {(v+excess_hi)/sh:7.2f}")
t=0.233; r_at=0.10*(1-t)
print(f"floor after tax {100*r_at:.2f}%")
fair=(avg5/r_at+excess)/sh; cheap=(m15*rev[-1]/r_at+excess)/sh
print(f"FAIR (5yr avg flat, 10% pre-tax) = {fair:.2f}; CHEAP (whole-cycle margin flat, 10% pre-tax) = {cheap:.2f}")
mc=price*sh; ev=mc-excess
print(f"market cap {mc:.0f}; EV net of excess {ev:.0f}; owner cash yield on EV: 5yr {100*avg5/ev:.2f}% ; FY26 {100*oc[-1]/ev:.2f}% ; whole-cycle {100*m15*rev[-1]/ev:.2f}%")
print(f"pre-tax equivalent of 5yr yield: {100*avg5/ev/(1-t):.2f}%")
# capex vs D&A
print("capex_all vs D&A FY22-26:",[round(ppe[i]+sw[i]+cur[i]+lease[i],1) for i in range(10,15)],[da[i] for i in range(10,15)])
