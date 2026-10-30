# FOLD RESTATEMENT 2026-10-26 of q7_compute.py: one input changed, D = the increase in long-term debt only (short-term borrowings
# of 503.0 and 736.0 left out), under the reading of 2026-10-23 (commit da11a073), as the utility addendum of that day applied it.
# Everything else is the run's own. The run file is not edited (operator rule 6).
# COMPUTATION, NOT A CLEARANCE: written during Q4 (before Q5 closed); its figures enter the run only at Q7.
# NI run 2026-10-23: Q7 arithmetic. All figures USD millions from the filed cash-flow statements:
# 2023-2025 from FY2025 10-K (0001111711-26-000027); 2021-2022 from FY2023 10-K (0001111711-24-000011).
# Maintenance capex = the filer's own "Maintenance" lines incl. Corporate and Other Maintenance (MD&A capex tables,
# FY2021-FY2025 10-Ks); these are segment-basis figures, not cash-flow basis (the filer's note (2)).
import statistics as st
Y=[2021,2022,2023,2024,2025]
OCF=[1217.9,1409.4,1935.1,1781.5,2362.3]
SBC=[24.3,24.9,33.5,43.6,50.9]           # stock compensation and 401(k) profit sharing contribution (in stock)
CAPEX=[1838.0,2203.1,2645.8,2614.0,2782.3]
REMOVAL=[121.1,151.7,160.8,166.8,188.3]
DEVPAY=[240.4,323.9,761.4,482.0,1098.7]  # milestone and final payments to renewable generation asset developers (investing)
DEPOSITS=[0,0,0,29.0,373.8]
OTHERINV=[1.0,-1.3,0.7,-3.4,26.4]        # other investing outflow (+) / inflow (-)
DEVOBL=[0,0,347.2,0,0]                   # payment of obligation to renewable generation asset developer (financing)
CONTRACT=[40.5,66.1,66.6,0,0]            # contract liability payment (financing)
FLP=[25.7,60.3,33.1,25.6,22.0]           # finance lease principal (2021-22: combined line with LT debt repayments, taken whole)
PREF=[55.1,55.1,43.8,8.2,0]
NCIDIST=[0.6,6.0,14.1,66.4,88.8]
NCICONT=[245.1,21.2,240.9,99.5,231.4]    # excl. the 2023 NIPSCO stake sale proceeds of 2,161.9
MAINT=[235.6+172.0+160.9, 329.7+164.2+161.6, 328.4+284.6+236.3, 286.0+492.0+231.1, 387.5+596.8+329.7]
DA=[748.4,820.8,908.2,1043.2,1167.6]
DEFTAX=[111.9,156.9,134.1,168.0,235.8]
REV=[4899.6,5850.6,5505.4,5455.1,6642.2]  # total operating revenues (10-K income statements)
DEBT_2020=9219.8+23.3; DEBT_2025=15457.8+19.7   # RESTATED 2026-10-26: long-term debt and its current portion only, short-term borrowings out (the 2026-10-23 reading of The regulated utility)
net_debt_raised=DEBT_2025-DEBT_2020
# latest filed balance sheet 2026-06-30 (10-Q 0001111711-26-000088)
DEBT_Q=15612.6+1098.4+692.0; CASH_Q=70.0; EQ_TOT_Q=11894.4; EQ_NI_Q=9574.6
debt_share=DEBT_Q/(DEBT_Q+EQ_TOT_Q)
spend_all=[CAPEX[i]+REMOVAL[i]+DEVPAY[i]+DEPOSITS[i]+OTHERINV[i]+DEVOBL[i]+CONTRACT[i]+FLP[i] for i in range(5)]
spend_maint=[MAINT[i]+REMOVAL[i]+FLP[i] for i in range(5)]
partner=[-PREF[i]-NCIDIST[i]+NCICONT[i] for i in range(5)]
base=[OCF[i]-SBC[i] for i in range(5)]
oc_all_noCredit=[base[i]-spend_all[i]+partner[i] for i in range(5)]
oc_maint_noCredit=[base[i]-spend_maint[i]+partner[i] for i in range(5)]
cap_all=debt_share*sum(spend_all); credit_all=min(net_debt_raised,cap_all)
cap_m=debt_share*sum(spend_maint); credit_m=min(net_debt_raised,cap_m)
oc_all=[oc_all_noCredit[i]+credit_all/5 for i in range(5)]
oc_maint=[oc_maint_noCredit[i]+credit_m/5 for i in range(5)]
def p(name,xs): print(f"{name:34s}"+' '.join(f"{x:9.1f}" for x in xs)+f"   avg {st.mean(xs):9.1f}")
print(' '*34+' '.join(f"{y:9d}" for y in Y))
for n,x in [('OCF',OCF),('SBC',SBC),('all capital spending',spend_all),('maintenance spending (filer)',spend_maint),('D&A',DA),('pref/NCI dist net of NCI contrib',partner),
            ('owner cash, all spending, no credit',oc_all_noCredit),('owner cash, maint only, no credit',oc_maint_noCredit),('owner cash, all spending + credit',oc_all),('owner cash, maint only + credit',oc_maint)]:
    p(n,x)
print(f"net debt raised 2021-2025 {net_debt_raised:,.1f}; debt share at 2026-06-30 {debt_share:.3f}; cap(all) {cap_all:,.1f}; credit(all) {credit_all:,.1f}; cap(maint) {cap_m:,.1f}; credit(maint) {credit_m:,.1f}")
print(f"spending sums: all {sum(spend_all):,.1f} maint {sum(spend_maint):,.1f}; capex/D&A avg {st.mean(spend_all)/st.mean(DA):.2f}")
# valuation
SH=479.5601+2.390057+2.2+2.151874; fwd_cash=99.7+100.0+99.2
r=0.0529
def pv(c0,g,rate,years=10):
    v=0; c=c0
    for t in range(1,years+1):
        c=c*(1+g); v+=c/(1+rate)**t
    tv=c/rate/(1+rate)**years   # zero nominal growth after year ten
    return v+tv
price=43.69; mcap=price*479.5601
print(f"shares incl forwards {SH:.3f}M; market cap at cover count {mcap:,.0f}")
for label,series in [('all spending + credit',oc_all),('maint only + credit',oc_maint),('all spending, no credit',oc_all_noCredit)]:
    a=st.mean(series)
    h1=st.mean(series[:2]); h2=st.mean(series[3:])
    print(label, 'avg',round(a,1),'first-half avg',round(h1,1),'second-half avg',round(h2,1))
    for nm,g in [('no growth',0.0)]:
        v=pv(a,g,r); vf=pv(a,g,0.10)
        print(f"   {nm}: value equity {v:,.0f} -> per share {(v+fwd_cash)/SH:.2f}; at 10% {(vf+fwd_cash)/SH:.2f}")
# revenue growth 2021-2025
print('revenue CAGR 2021-2025', round(((REV[-1]/REV[0])**(1/4)-1)*100,2),'%')

print('\n=== RANGE (equity-only central, the regulated-utility basis) ===')
INT=[322.4+9.4,343.8+8.5,433.9+8.6,468.2+11.2,557.1+14.5]  # cash interest paid on debt + finance leases
mo=oc_maint_noCredit; ac=oc_all
g_m=(mo[-1]/mo[0])**(1/4)-1
gs=[ (spend_all[i]-spend_maint[i]) for i in range(5)]   # growth spending
gnet=[ac[i]-mo[i] for i in range(5)]                   # growth spending net of the debt credit (negative)
print(f"maint-only owner cash CAGR 2021-25 {g_m*100:.2f}%  (end years {mo[0]:.1f} -> {mo[-1]:.1f}); halves {st.mean(mo[:2]):.1f} -> {st.mean(mo[3:]):.1f}")
print(f"growth spending avg {st.mean(gs):.1f}; net of debt credit avg {st.mean(gnet):.1f}")
rev_g=(REV[-1]/REV[0])**(1/4)-1
share=[mo[i]/REV[i] for i in range(5)]; print('maint-only owner cash / revenue', [round(s*100,1) for s in share])
def growth_case(c0,gnet0,g,rate):
    v=0;c=c0;n=gnet0
    for t in range(1,11):
        c*=1+g; n*=1+g
        v+=(c+n)/(1+rate)**t
    v+= c/rate/(1+rate)**10   # growth and its spending stop after year ten
    return v
fwd=fwd_cash
a_m=st.mean(mo); a_n=st.mean(gnet)
for rate,lab in [(r,'sovereign 5.29%'),(0.10,'ten percent')]:
    top=a_m/rate
    gro=growth_case(a_m,a_n,g_m,rate)
    gro_flat=growth_case(a_m,a_n,0.0,rate)  # growth spending kept with no growth credited
    allsp=st.mean(ac)/rate
    print(f"[{lab}] maint-only no-growth: {(top+fwd)/SH:7.2f}/sh | growth case (maint cash and net growth spend both at {g_m*100:.1f}%, stop yr10): {(gro+fwd)/SH:7.2f}/sh | all-spending+credit no growth: {(allsp+fwd)/SH:7.2f}/sh")
    # with credit applied to maintenance too (the rule's literal words), beside
    print(f"     beside: maint-only with debt credit no-growth {(st.mean(oc_maint)/rate+fwd)/SH:7.2f}/sh")
    # all-equity beside: owner cash before interest after statutory 21% shield, less net debt
    nd=DEBT_Q-CASH_Q
    ae_m=st.mean([mo[i]+INT[i]*(1-0.21) for i in range(5)])
    ae_all=st.mean([oc_all_noCredit[i]+INT[i]*(1-0.21) for i in range(5)])
    print(f"     all-equity: maint-only no growth {(ae_m/rate-nd+fwd)/SH:7.2f}/sh; all spending no growth {(ae_all/rate-nd+fwd)/SH:7.2f}/sh (net debt {nd:,.1f})")
print('mean cash interest', round(st.mean(INT),1))
# price yields
EV=price*SH-fwd
print(f"equity value at price incl forward shares {EV:,.0f}; maint-only yield {a_m/EV*100:.2f}%; with credit {st.mean(oc_maint)/EV*100:.2f}%")

print('\n=== ALL-EQUITY BESIDE, growth case ===')
nd=DEBT_Q-CASH_Q
ae_m=st.mean([mo[i]+INT[i]*(1-0.21) for i in range(5)])
gross=-st.mean(gs)
for rate in (r,0.10):
    gc=growth_case(ae_m,gross,g_m,rate)
    print(f"rate {rate}: all-equity growth case {(gc-nd+fwd)/SH:.2f}/sh; no-growth {(ae_m/rate-nd+fwd)/SH:.2f}/sh")
fair_eq=( (a_m/0.10+fwd)/SH + (growth_case(a_m,a_n,g_m,0.10)+fwd)/SH )/2
fair_ae=( (ae_m/0.10-nd+fwd)/SH + (growth_case(ae_m,gross,g_m,0.10)-nd+fwd)/SH )/2
print(f"FAIR PRICE equity-only (central) {fair_eq:.2f}; all-equity beside {fair_ae:.2f}")

