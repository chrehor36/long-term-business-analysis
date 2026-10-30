# Q7 arithmetic for the PPL run, 2026-10-26. USD millions. Arithmetic only.
OCm=[425,512,471,1015,1268]            # OCF(continuing) - SBC - depreciation, 2021-2025
capex=[1973,2155,2390,2805,4030]; dep=[1082,1181,1254,1279,1312]
GS=[c-d for c,d in zip(capex,dep)]
base=sum(OCm)/5; gs=sum(GS)/5
ltd21=10666+474; ltd25=17990+904; ri_assumed=14+1496
debt_yr=(ltd25-ltd21-ri_assumed)/4
ltd_mid26=19789+469; eq_mid26=15045; share=ltd_mid26/(ltd_mid26+eq_mid26)
credit=min(debt_yr, share*gs); net_gs=gs-credit
shares=752.544841; price=35.13; mcap=shares*price
netdebt=65+ltd_mid26-332
intpaid=[191,462,604,670,745]; t=0.26
oc_allequity=base+sum(intpaid)/5*(1-t)
g_org=(9042/8312)**0.5-1; g_tot=(9042/5783)**0.25-1
rf=0.0533
def value(b,g,growth_spend,r,acq=0.0):
    # years 1..10: owner cash grows at g; growth spending (net) grows at g and stops after yr10;
    # after yr10: owner cash flat at yr10 level (zero nominal growth), no growth spending.
    pv=0
    for y in range(1,11):
        pv+=(b*(1+g)**y - growth_spend*(1+g)**y - acq*(1+g)**y)/(1+r)**y
    term=b*(1+g)**10/r/(1+r)**10
    return pv+term
def irr(b,g,gsp,p,acq=0.0):
    lo,hi=0.0005,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if value(b,g,gsp,m,acq)>p: lo=m
        else: hi=m
    return m
out=[]
P=lambda s:out.append(s)
P(f"base maintenance-only owner cash (equity-only) {base:.1f}; growth spending avg {gs:.1f}; GS by yr {GS}")
P(f"LTD increase/yr net of RI assumed debt {debt_yr:.1f}; own LTD share of LT capital 2026-06-30 {share:.4f}; cap x GS {share*gs:.1f}; credit {credit:.1f}; equity-funded growth spending {net_gs:.1f}")
P(f"market cap {mcap:.0f}; net debt 2026-06-30 {netdebt}; all-equity owner cash before interest {oc_allequity:.1f}")
P(f"organic growth (sales 2023-2025) {g_org:.4f}; total growth (sales 2021-2025) {g_tot:.4f}; shown owner-cash growth 2021-2025 {(1268/425)**0.25-1:.4f}")
P(f"cap test: base x (1+31.4%)^10 = {base*((1268/425)**0.25)**10:.0f} vs 2025 sales 9042 (highest owner-cash share of sales {max(o/s for o,s in zip(OCm,[5783,7902,8312,8462,9042])):.3f})")
cases={
 'EQ organic no-growth (central)':(base,0.0,0.0,0.0),
 'EQ organic growth (central)':(base,g_org,net_gs,0.0),
 'EQ default no-growth (purchases stop)':(base,0.0,0.0,0.0),
 'EQ default growth, RI deducted, total growth':(base,g_tot,net_gs,3660/5),
 'EQ literal window, shown growth uncapped 31.4% (shown beside, absurd)':(base,(1268/425)**0.25-1,net_gs,0.0),
 'EQ all spending, no growth':(sum(o-g for o,g in zip(OCm,GS))/5,0.0,0.0,0.0),
}
res={}
for k,(b,g,gsp,acq) in cases.items():
    v=value(b,g,gsp,rf,acq); f=value(b,g,gsp,0.10,acq)
    i=irr(b,g,gsp,mcap,acq) if b>0 else float('nan')
    res[k]=(v,f)
    P(f"{k:70s} at rf {v:9.0f} = ${v/shares:7.2f}/sh | at 10% {f:8.0f} = ${f/shares:6.2f}/sh | IRR at price {i*100:6.2f}%")
# all-equity beside
for k,(b,g,gsp,acq) in {'AE organic no-growth':(oc_allequity,0,0,0),'AE organic growth':(oc_allequity,g_org,gs,0),'AE default growth':(oc_allequity,g_tot,gs,3660/5)}.items():
    v=value(b,g,gsp,rf,acq)-netdebt; f=value(b,g,gsp,0.10,acq)-netdebt
    i=irr(b,g,gsp,mcap+netdebt,acq)
    P(f"{k:70s} at rf {v:9.0f} = ${v/shares:7.2f}/sh | at 10% {f:8.0f} = ${f/shares:6.2f}/sh | IRR on EV {i*100:6.2f}%")
lo=min(res['EQ organic no-growth (central)'][0],res['EQ organic growth (central)'][0]); hi=max(res['EQ organic no-growth (central)'][0],res['EQ organic growth (central)'][0])
fair=(res['EQ organic no-growth (central)'][1]+res['EQ organic growth (central)'][1])/2
P(f"CENTRAL range ${lo/shares:.2f} to ${hi/shares:.2f}; width {hi/lo:.3f}; fair price (avg of ends at 10%) ${fair/shares:.2f}")
fd=(res['EQ default no-growth (purchases stop)'][1]+res['EQ default growth, RI deducted, total growth'][1])/2
P(f"DEFAULT pair range ${res['EQ default no-growth (purchases stop)'][0]/shares:.2f} to ${res['EQ default growth, RI deducted, total growth'][0]/shares:.2f}; fair ${fd/shares:.2f}")
# growth spending year1/year10 (central)
P(f"central growth spending (equity-funded, net of credit): yr1 {net_gs*(1+g_org):.0f}, yr10 {net_gs*(1+g_org)**10:.0f}; gross growth spending yr1 {gs*(1+g_org):.0f}, yr10 {gs*(1+g_org)**10:.0f}; credit yr1 {credit*(1+g_org):.0f}, yr10 {credit*(1+g_org)**10:.0f}")
# 2025-only sensitivity
for b in [1268]:
    v=value(b,g_org,net_gs*(2718/1449),rf); i=irr(b,0,0,mcap)
    P(f"sensitivity: 2025 owner cash 1268 no growth: IRR at price {i*100:.2f}%; value at rf ${b/rf/shares:.2f}/sh")
open('q7_output.txt','w').write('\n'.join(out)+'\n'); print('\n'.join(out))
