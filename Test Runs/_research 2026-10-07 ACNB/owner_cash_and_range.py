# ACNB owner cash (bank recast) and the Q7 range. Arithmetic only; every input from the filings named in the run file.
# USD millions. Tax 21% (federal statutory, 10-K FY2025 MD&A footnote).
T=0.21
NCO_NORMAL=0.0018   # mean net charge-offs / average loans 2006-2025 (selected data FY2010, FY2015, FY2019 10-Ks; FY2021/22/25 10-Ks)
y   =[2018,2019,2020,2021,2022,2023,2024,2025]
NI  =[21.748,23.721,18.394,27.834,35.752,31.688,31.846,37.051]
PROV=[1.620,0.600,9.140,0.050,0.000,0.844,-2.763,4.730]   # provision for credit losses incl. unfunded commitments
AMORT=[0.745,0.621,1.264,1.164,1.492,1.424,1.244,4.257]   # intangible amortization (paid for at the deal; deal counted as capital)
AVGL=[1258.0,1288.7,1671.4,1552.1,1506.4,1573.6,1668.5,2304.3]
AVGA=[1620.4,1688.7,2364.7,2698.0,2721.0,2392.3,2435.4,3198.9]
oc=[]; 
print("year  NI    normCredit  OC    OC/avgA%")
for i in range(len(y)):
    norm=NCO_NORMAL*AVGL[i]
    v=NI[i]+(PROV[i]-norm)*(1-T)+AMORT[i]*(1-T)
    oc.append(v); print(y[i], f"{NI[i]:6.2f} {norm:6.2f} {v:7.2f} {v/AVGA[i]*100:6.3f}")
roa=[oc[i]/AVGA[i] for i in range(len(y))]
lit=sum(oc[3:])/5; lit_roa=sum(roa[3:])/5; cyc_roa=sum(roa)/len(roa)
print("literal 5-yr (2021-25) mean OC", round(lit,2), "mean OC/assets %", round(lit_roa*100,3))
print("cycle 2018-25 mean OC/assets %", round(cyc_roa*100,3))
A_NOW=(3228.126+3318.863)/2   # mean of 31 Dec 2025 and 30 Jun 2026 total assets (10-Q Q2 2026)
TCE_RATIO=(423.279-64.449-20.351)/(3318.863-64.449-20.351)  # tangible common equity / tangible assets, 30 Jun 2026
print("assets base", round(A_NOW,1), "TCE ratio %", round(TCE_RATIO*100,2))
r=0.0564
def value(oc0, g, retain_ratio):
    # ten years at g, owner cash after equity retained to carry growth (g x TCE), then zero nominal growth forever
    pv=0; ocy=oc0; A=A_NOW
    for t in range(1,11):
        ocy=oc0*(1+g)**t; retained=g*TCE_RATIO*A*(1+g)**(t-1)
        pv+=(ocy-retained)/(1+r)**t
    term=oc0*(1+g)**10/r/(1+r)**10
    return pv+term
shares=10.169930
for label,roa_used in (("cycle base 2018-25",cyc_roa),("literal window 2021-25",lit_roa)):
    oc0=roa_used*A_NOW
    v0=value(oc0,0.0,TCE_RATIO); vg=value(oc0,0.02,TCE_RATIO)
    print(label, "OC0", round(oc0,2), "no-growth", round(v0,1), round(v0/shares,2), "/sh", " 2% growth", round(vg,1), round(vg/shares,2), "/sh")
# literal aggregate window, as-reported (pre-merger years at standalone size)
print("literal as-reported aggregate mean OC", round(lit,2), "no-growth value/sh", round(lit/r/shares,2))
# fair price: price at which the midpoint earns ~10% pre-holder-tax on owner cash after company tax

print("\n--- all-equity basis (holding-company debt is the financing; deposits and FHLB advances are the bank's raw material) ---")
HOLDCO_DEBT=15.0+5.376      # 5.875% sub notes (8-K 2026-03-12; replaced the 4.00% notes 31 Mar 2026) + trust preferred (10-K FY2025 Note 11)
PARENT_CASH=24.519          # parent-only cash 31 Dec 2025 (10-K FY2025 Note 21); latest parent-only statement filed
net_debt=HOLDCO_DEBT-PARENT_CASH
int_at=(15.0*0.05875+6.0*0.0561)*(1-T)  # after-tax interest on holding-company debt at the 2026 coupons
print("holding-company net debt", round(net_debt,2), "after-tax holdco interest", round(int_at,2))
def stream_value(oc0,g,rate,A=A_NOW):
    pv=0
    for t in range(1,11):
        pv+=(oc0*(1+g)**t - g*TCE_RATIO*A*(1+g)**(t-1))/(1+rate)**t
    return pv + oc0*(1+g)**10/rate/(1+rate)**10
for label,roa_used in (("cycle base",cyc_roa),("literal window",lit_roa)):
    oc_eq=roa_used*A_NOW; oc_ae=oc_eq+int_at
    lo=stream_value(oc_ae,0.0,r)-net_debt; hi=stream_value(oc_ae,0.02,r)-net_debt
    print(label,"all-equity OC",round(oc_ae,2),"range/sh",round(lo/shares,2),"to",round(hi/shares,2))
    # fair price: midpoint case (g=1%) priced to earn 10%
    fair_ev=stream_value(oc_ae,0.01,0.10); fair_eq=fair_ev-net_debt
    fair_eqonly=stream_value(oc_eq,0.01,0.10)
    print("  fair price all-equity", round(fair_eq/shares,2), " equity-only", round(fair_eqonly/shares,2))
price=63.73; mcap=price*shares; ev=mcap+net_debt
# expected return at price on midpoint case: solve rate
def irr(target, oc0):
    lo,hi=0.01,0.5
    for _ in range(100):
        m=(lo+hi)/2
        if stream_value(oc0,0.01,m)>target: lo=m
        else: hi=m
    return m
print("mcap", round(mcap,1), "EV", round(ev,1))
print("expected return at price, midpoint case, all-equity", round(irr(ev,cyc_roa*A_NOW+int_at)*100,2), "%; equity-only", round(irr(mcap,cyc_roa*A_NOW)*100,2),"%")
print("owner-cash yield at price (cycle base, equity)", round(cyc_roa*A_NOW/mcap*100,2),"%")
print("\n--- Q6 deal test (Traditions, closed 1 Feb 2025, 2,035,246 shares at $41.10) ---")
A24=2435.358; sh24=8.553785
oc_sa=cyc_roa*A24
print("standalone OC", round(oc_sa,2), "value/sh at 5.64%", round(oc_sa/0.0564/sh24,2), " at 10%", round(oc_sa/0.10/sh24,2))
print("issue price/no-growth value at 5.64%", round(41.10/(oc_sa/0.0564/sh24),3))
