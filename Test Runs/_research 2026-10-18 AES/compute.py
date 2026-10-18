# COMPUTATION, NOT A CLEARANCE. AES 2026-10-18. All $M. Sources: filed cash-flow statements,
# 10-K FY2023 (2021-2022 columns, acc 0000874761-24-000011) and 10-K FY2025 (2023-2025, acc 0000874761-26-000063).
Y=[2021,2022,2023,2024,2025]
OCF   =[1902,2715,3034,2752,4306]
CAPEX =[2116,4551,7724,7392,5929]
FINCAPEX=[24,33,10,127,53]          # payments for financed capital expenditures (financing section)
EMIS  =[265,488,268,206,309]        # purchase of emissions allowances (investing)
ACQ   =[658,243,542,246,108]        # acquisitions of business interests, net of cash
SOLD  =[95,1,254,423,108]           # proceeds from sale of business interests, net
AFFIN =[427,232,178,103,19]         # contributions and loans to equity affiliates
AFFOUT=[320,149,5,0,0]              # affiliate repayments and returns of capital (line not shown 2024-25)
NCIDIST=[284,265,323,430,912]       # distributions to noncontrolling interests
FLP   =[0,0,5,7,21]                 # finance lease principal (not separately shown 2021-22)
SBC   =[14,23,2,12,14]
INTPAID=[815,928,1317,1268,1210]    # cash interest, net of capitalized
DA    =[1056,1053,1147,1264,1457]
REV   =[11141,12617,12668,12278,12233]
NCI_SALES=[173,742,1938,1247,2084]  # sales to noncontrolling interests (financing)
NCI_CONTR=[365,233,102,222,437]     # contributions from NCI (tax equity etc.)
NCI_ACQ=[117,602,127,0,143]
PREF_SUB=[153,60,421,0,992]
T=0.21  # CONVENTION of the run: interest added back after the US statutory rate
r=0.0543; floor=0.10
shares=713.43863
mcap=14.95*shares
debt=300+5800+3162+22855
cash=1800+53
netdebt=debt-cash
restricted=530
def avg(x): return sum(x)/len(x)
eq_all=[OCF[i]-SBC[i]-CAPEX[i]-FINCAPEX[i]-EMIS[i]-(ACQ[i]-SOLD[i])-(AFFIN[i]-AFFOUT[i])-NCIDIST[i]-FLP[i] for i in range(5)]
ae_all=[eq_all[i]+INTPAID[i]*(1-T) for i in range(5)]
eq_da=[OCF[i]-SBC[i]-DA[i]-EMIS[i]-NCIDIST[i]-FLP[i] for i in range(5)]
ae_da=[eq_da[i]+INTPAID[i]*(1-T) for i in range(5)]
recyc=[NCI_SALES[i]+NCI_CONTR[i]+PREF_SUB[i]-NCI_ACQ[i] for i in range(5)]
ae_alt=[ae_all[i]+recyc[i] for i in range(5)]
eq_alt=[eq_all[i]+recyc[i] for i in range(5)]
def show(name,s):
    print(f"{name:42s}", ' '.join(f"{v:7.0f}" for v in s), f" avg {avg(s):7.0f}  1st-half(21-22) {avg(s[:2]):7.0f} 2nd-half(24-25) {avg(s[3:]):7.0f}")
print("year".ljust(42),' '.join(f"{y:7d}" for y in Y))
show("all-equity, all spending (central)",ae_all)
show("equity-only, all spending",eq_all)
show("all-equity, D&A variant",ae_da)
show("equity-only, D&A variant",eq_da)
show("capital recycled from partners (net)",recyc)
show("all-equity, all spending + recycling",ae_alt)
show("equity-only, all spending + recycling",eq_alt)
print("revenue growth 2021-2025 CAGR", (REV[-1]/REV[0])**(1/4)-1)
print(f"mcap {mcap:.0f} debt {debt} cash {cash} netdebt {netdebt} EV {mcap+netdebt:.0f}")
def case(avgoe, g, rate, years=10):
    # g growth for 10 years then zero nominal growth; value at 'rate'
    v=0; cf=avgoe
    for t in range(1,years+1):
        cf=cf*(1+g); v+=cf/(1+rate)**t
    v+= (cf/rate)/(1+rate)**years
    return v
for label,series,isAE in [("all-equity all spending",ae_all,True),("equity-only all spending",eq_all,False),("all-equity D&A",ae_da,True),("equity-only D&A",eq_da,False),("all-equity +recycling",ae_alt,True),("equity-only +recycling",eq_alt,False)]:
    a=avg(series)
    base= mcap+netdebt if isAE else mcap
    yld=a/base
    v_r=case(a,0,r); v_f=case(a,0,floor)
    ps_r=(v_r-(netdebt if isAE else 0))/shares; ps_f=(v_f-(netdebt if isAE else 0))/shares
    print(f"{label:28s} avg {a:7.0f} yield on price {yld*100:6.2f}%  no-growth value/sh at 5.43% {ps_r:8.2f}  at 10% {ps_f:8.2f}")
print("--- D&A variant: shown growth and the cap (f) ---")
for label,series,isAE in [("all-equity D&A",ae_da,True),("equity-only D&A",eq_da,False)]:
    g_shown=(series[-1]/series[0])**(1/4)-1
    a=avg(series); share_hi=max(series[i]/REV[i] for i in range(5))
    implied=a*(1+g_shown)**10
    g=0.023651672574271032
    v_r=case(a,g,r); v_f=case(a,g,floor)
    ps_r=(v_r-(netdebt if isAE else 0))/shares; ps_f=(v_f-(netdebt if isAE else 0))/shares
    base= mcap+netdebt if isAE else mcap
    # IRR: price = PV of flows (growth g 10y then flat)
    lo,hi=0.0001,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if case(a,g,m)>base: lo=m
        else: hi=m
    lo0,hi0=0.0001,0.5
    for _ in range(200):
        m0=(lo0+hi0)/2
        if case(a,0,m0)>base: lo0=m0
        else: hi0=m0
    print(f"{label}: shown growth {g_shown*100:.1f}%/yr; yr-10 owner cash at that rate {implied:.0f} vs 2025 revenue {REV[-1]} (highest share of sales earned {share_hi*100:.1f}%) -> cut to sales growth {g*100:.2f}%")
    print(f"   capped-growth case value/sh at 5.43% {ps_r:.2f}; at 10% {ps_f:.2f}; expected return at price: growth case {m*100:.2f}%, no-growth {m0*100:.2f}%")
