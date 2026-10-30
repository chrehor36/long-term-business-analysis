# Q7 arithmetic for the AEE run (COMPUTATION; the verdict is written in the run file)
yrs=[2021,2022,2023,2024,2025]
OCF={2021:1661,2022:2263,2023:2564,2024:2763,2025:3353}
SBC={2021:22,2022:24,2023:26,2024:28,2025:28}
DA ={2021:1219,2022:1438,2023:1432,2024:1524,2025:1612}
CAP={2021:2954,2022:3351,2023:3597,2024:4319,2025:4128}
INT={2021:426,2022:476,2023:546,2024:611,2025:755}   # interest paid, net of capitalized (cash-flow supplement)
REV={2021:6394,2022:7957,2023:7500,2024:7623,2025:8799}
T=0.26   # filer's 2025 blended federal and state statutory rate (10-K Item 7)
r=0.0543; floor=0.10
shares=276.843; price=106.08
netdebt=1524+19064+1220-12   # 10-Q 2026-06-30: current LTD + LTD + short-term debt - cash
mc=shares*price
def ser(basis,allequity):
    out={}
    for y in yrs:
        sp = CAP[y] if basis=='all' else DA[y]
        v=OCF[y]-SBC[y]-sp + (INT[y]*(1-T) if allequity else 0)
        out[y]=v
    return out
def mean(d): return sum(d.values())/len(d)
G=mean(CAP)-mean(DA)
def pv_growth(B,g,G,rate):
    pv=0
    for t in range(1,11):
        pv+=(B*(1+g)**t - G)/(1+rate)**t
    pv+=B*(1+g)**10/rate/(1+rate)**10
    return pv
def pv_nogrowth(B,rate): return B/rate
print(f"market cap {mc:,.0f}  net debt {netdebt:,.0f}  EV {mc+netdebt:,.0f}")
for ae in (True,False):
    tag='ALL-EQUITY' if ae else 'EQUITY-ONLY'
    m=ser('maint',ae); a=ser('all',ae)
    print(f"\n== {tag}")
    print(' maint-basis series', {y:round(v,1) for y,v in m.items()}, 'mean', round(mean(m),1))
    print(' all-spend series  ', {y:round(v,1) for y,v in a.items()}, 'mean', round(mean(a),1))
    B=mean(m); Ba=mean(a)
    shown=(m[2025]/m[2021])**0.25-1
    salesg=(REV[2025]/REV[2021])**0.25-1
    g=min(salesg,r)
    print(f" shown growth (maint basis, 2021-25) {shown*100:.1f}%; halves {(((m[2024]+m[2025])/2)/((m[2021]+m[2022])/2))**(1/3)*100-100:.1f}%; sales growth {salesg*100:.2f}%; carried g {g*100:.2f}%")
    print(f" highest share of sales: {max(m[y]/REV[y] for y in yrs)*100:.1f}%; year-10 at shown rate {B*(1+shown)**10:,.0f} vs sales at same rate {REV[2025]*(1+shown)**10:,.0f}")
    print(f" growth spending G (mean capex - mean D&A) {G:,.1f}")
    sub = netdebt if ae else 0
    for rate,lab in ((r,'at sovereign 5.43%'),(floor,'at 10% (fair-price ends)')):
        ng=pv_nogrowth(B,rate); gr=pv_growth(B,g,G,rate); grfree=pv_growth(B,g,0,rate)
        allsp=pv_nogrowth(Ba,rate)
        print(f"  {lab}: no-growth maint {ng:,.0f} -> per share {(ng-sub)/shares:,.2f}; growth with G charged {gr:,.0f} -> {(gr-sub)/shares:,.2f};"
              f" [growth, G not charged {grfree:,.0f} -> {(grfree-sub)/shares:,.2f}]; all-spending no-growth {allsp:,.0f} -> {(allsp-sub)/shares:,.2f}")
    # floor test: expected return at the price for each case = IRR of paying EV (or mc) for the case's cash
    cost = mc+netdebt if ae else mc
    def irr(f):
        lo,hi=0.0005,1.0
        for _ in range(200):
            mid=(lo+hi)/2
            if f(mid)>cost: lo=mid
            else: hi=mid
        return mid
    print(f"  return at the price: no-growth maint {B/cost*100:.2f}%; growth with G {irr(lambda x: pv_growth(B,g,G,x))*100:.2f}%; growth G not charged {irr(lambda x: pv_growth(B,g,0,x))*100:.2f}%")
    # forward-sale settlement beside (all-equity): +17.4M shares, net debt -1.6B -0.158B(July at 112.62)
    if ae:
        sh2=shares+16.0+1.4; nd2=netdebt-1600-1.4*112.62
        ng=pv_nogrowth(B,r); gr=pv_growth(B,g,G,r)
        print(f"  forwards settled beside: no-growth {(ng-nd2)/sh2:,.2f}; growth {(gr-nd2)/sh2:,.2f} per share")
# owner cash for 10% at the price (all-equity)
print(f"\nowner cash before interest needed for 10% on EV with no growth: {(mc+netdebt)*0.10:,.0f}")
