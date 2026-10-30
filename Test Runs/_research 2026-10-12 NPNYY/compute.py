# NPNYY run 2026-10-12: owner cash and the Q7 COMPUTATION (reporting figures only).
# Source: NYK "IR Data Book 2026" (May 11, 2026), page 6, Consolidated Statements of Cash Flows, years ended March 31;
# cross-checked: OCF YE Mar-2026 473,358 = "Financial Results 2026" consolidated statement of cash flows.
yrs=list(range(2016,2027))  # year ended March 31
OCF=[142857,27924,89090,45260,116931,159336,507762,824853,401414,510755,473358]
CAPEX=[115913,156229,199240,169614,138766,102087,192726,198360,336281,206506,304502]
PROC=[74144,30509,70984,85356,70837,76026,35435,29009,79835,88346,82297]
LEASE=[0,0,0,2402,19275,19903,20389,24226,27037,25955,29405]
# subsidiaries bought (fee + revenue line) + payments on sale of subs - proceeds from sale of subs
ACQ=[0-9437, 475-35+1813, 8123+222, 2756+948-11414, 424-379, 579-1762-883, 0+56-36013, 23055-7286-2919, 13574+599-18182, 9981+1838-97643, 263061]
INTPD=[17205,15516,17422,23994,25866,16864,11795,14444,12615,20649,20849]
DA=[103347,92004,87839,89713,104057,98803,101596,121658,141605,154632,175182]
REV=[2272315,1923881,2183201,1829300,1668355,1608414,2280775,2616066,2387240,2588700,2423689]
T=0.288  # normal statutory rate YE Mar-2026, Financial Results 2026, note 22
oc=[o-c-l-a for o,c,l,a in zip(OCF,CAPEX,LEASE,ACQ)]
ocu=[x+i*(1-T) for x,i in zip(oc,INTPD)]
ocp=[x+p for x,p in zip(oc,PROC)]
ocd=[o-d-l-a for o,d,l,a in zip(OCF,DA,LEASE,ACQ)]
print("YE-Mar  OCF   capex  lease  netacq  OC(equity)  OC(all-eq)  +vessel-sale proceeds  D&A-variant  OC/rev")
for i,y in enumerate(yrs):
    print(y, OCF[i],CAPEX[i],LEASE[i],ACQ[i], round(oc[i]), round(ocu[i]), round(ocp[i]), round(ocd[i]), f"{oc[i]/REV[i]:.1%}")
def avg(xs): return sum(xs)/len(xs)
W=slice(6,11)        # literal window YE Mar-2022..2026
C=slice(1,9)         # cycle trough to trough YE Mar-2017..2024
A=slice(0,11)
for nm,s in [("literal 5y YE22-26",W),("cycle YE17-24",C),("all 11y YE16-26",A)]:
    print(nm, "OC eq", round(avg(oc[s])), "OC all-eq", round(avg(ocu[s])), "OC+proceeds", round(avg(ocp[s])), "D&A var", round(avg(ocd[s])))
r=0.04085   # MOF jgbcme.csv 30Y, 2026-10-09
ND=1361654-225987   # IBD incl leases less cash and deposits, June 30 2026 (Q1 tanshin, Aug 5 2026)
SH=405321700-1766082
PX=7358.0; FX=158.06; ADS=0.2
print("net debt", ND, "shares", SH, "mktcap", round(SH*PX/1e6))
def per(v_m): return v_m*1e6/SH
for nm,s in [("cycle base (central)",C),("literal window (beside)",W),("11y (beside)",A)]:
    u=avg(ocu[s]); e=avg(oc[s])
    val=per(u/r-ND); fair=per(u/0.10-ND); valeq=per(e/r); faireq=per(e/0.10)
    print(f"{nm}: no-growth value all-eq {val:,.0f} yen/sh; equity-only {valeq:,.0f}; FAIR all-eq {fair:,.0f}; equity-only {faireq:,.0f}; ADS fair ${fair*ADS/FX:.2f}; price {PX} (ADS ${PX*ADS/FX:.2f})")
    print(f"   earnings yield at price, all-eq: {u/(SH*PX/1e6+ND):.2%}; equity-only {e/(SH*PX/1e6):.2%}")

# --- Earlier cycle, YE Mar 2008-2015: NYK FACT BOOK 2018 (Fact Book II), consolidated statements of cash flows.
y0=list(range(2008,2016))
OCF0=[199525,150474,62105,174585,29837,93951,136522,136448]
CAPEX0=[501330,417555,237969,278570,309288,307050,233985,189981]
PROC0=[217084,248233,183732,121920,173272,158498,246586,185298]
ACQ0=[46,331,3358+2930-213,147-106,5412,250,923,70+1634]
oc0=[o-c-a for o,c,a in zip(OCF0,CAPEX0,ACQ0)]
print("\nYE-Mar 2008-2015 owner cash (gross capex):", dict(zip(y0,oc0)))
print("same, with vessel-sale proceeds:", dict(zip(y0,[x+p for x,p in zip(oc0,PROC0)])))
allg=oc0+oc; allp=[x+p for x,p in zip(oc0,PROC0)]+ocp
print("19y YE2008-2026 sum gross", sum(allg), "avg", round(avg(allg)), "| with proceeds sum", sum(allp), "avg", round(avg(allp)))
prev=oc0[2:]+oc[:1]   # YE2010..2016: trough (YE2010) to the year before the next trough (YE2017)
last=oc[1:8]          # YE2017..2023
print("previous cycle YE2010-2016 avg", round(avg(prev)), "| last cycle YE2017-2023 avg", round(avg(last)), "| YE2017-2024 avg", round(avg(oc[1:9])))

# --- Segment recurring profit, IR Data Book 2026 p.4, YE Mar 2022..2026 (billions of yen, from millions)
seg={"Liner trade":[734245,790637,67891,274366,49793],"Air cargo":[74068,61556,5758,21070,2158],
     "Logistics":[58727,54284,25950,21271,10215],
     "Bulk (Automotive+Dry bulk+Energy)":[139100,210440,105855+18040+46393,113380+18104+46172,97935+9574+54418],
     "Others (real estate, other services)":[2127-1231,1323+592,3627,6954,-31],"Elimination":[-3884,-9044,-12176,-10454,-12929]}
tot=[1003154,1109790,261341,490866,211135]
print("consolidated 5y", sum(tot), "check sum of parts", sum(sum(v) for v in seg.values()))
for k,v in seg.items(): print(f"{k}: {sum(v):,}  share of consolidated {sum(v)/sum(tot):.1%}")
print("Automotive 3y", 105855+113380+97935, "Dry bulk 3y", 18040+18104+9574, "Energy 3y", 46393+46172+54418)

# --- (c) purchases stop after year ten: ten years of owner cash with net acquisitions, then perpetuity before purchases
def val_stop(ocu_avg, acq_avg, rate):
    pv10=sum(ocu_avg/(1+rate)**t for t in range(1,11))
    tv=(ocu_avg+acq_avg)/rate/(1+rate)**10
    return pv10+tv
for nm,s in [("cycle YE17-24",C),("literal YE22-26",W)]:
    u=avg(ocu[s]); e=avg(oc[s]); a=avg(ACQ[s])
    v=per(val_stop(u,a,r)-ND); f=per(val_stop(u,a,0.10)-ND)
    ve=per(val_stop(e,a,r)); fe=per(val_stop(e,a,0.10))
    print(f"{nm} with year-10 stop: net acq avg {a:,.0f}; value all-eq {v:,.0f} (equity-only {ve:,.0f}); FAIR all-eq {f:,.0f} (equity-only {fe:,.0f}); ADS fair all-eq ${f*ADS/FX:.2f}, equity-only ${fe*ADS/FX:.2f}")
