# Q7 arithmetic for the LNT run, 2026-10-18. Figures typed from the filed cash-flow statements:
# COMPUTATION, NOT A CLEARANCE. Written while Q1 to Q4 were open (2026-10-18) to see what arithmetic the filings allow; it carries no verdict.
# FY2025 10-K 0000352541-26-000007 (2023-2025), FY2022 10-K 0000352541-23-000017 (2020-2022),
# FY2019 10-K 0000352541-20-000021 (2017-2019); SBC and interest paid from XBRL (run.py / companyfacts), transcription.
yrs=[2017,2018,2019,2020,2021,2022,2023,2024,2025]
OCF ={2017:521.6,2018:527.7,2019:660.4,2020:501,2021:582,2022:486,2023:867,2024:1167,2025:1169}
RCV ={2017:461.8,2018:605.3,2019:413.2,2020:458,2021:502,2022:598,2023:453,2024:593,2025:628}   # cash receipts on sold receivables (investing)
CXU ={2017:1281.8,2018:1568.3,2019:1538.4,2020:1293,2021:1070,2022:1392,2023:1731,2024:2052,2025:2277}
CXO ={2017:185.1,2018:65.6,2019:101.7,2020:73,2021:99,2022:92,2023:123,2024:197,2025:206}
DA  ={2017:461.8,2018:506.9,2019:567.2,2020:615,2021:657,2022:671,2023:676,2024:772,2025:846}
SBC ={2017:15.1,2018:17.0,2019:26.0,2020:16,2021:14,2022:13,2023:12,2024:12,2025:22}
INT ={2017:212.6,2018:247.5,2019:267.9,2020:274,2021:272,2022:311,2023:378,2024:434,2025:500}  # interest paid
REV ={2017:3382,2018:3534,2019:3648,2020:3416,2021:3669,2022:4205,2023:4027,2024:3981,2025:4362}
T=0.21  # CONVENTION of the run: interest added back after the 21% statutory federal rate
r=0.0543; floor=0.10
sh=259.284699; price=68.32
netdebt=374+708+400+10636+190-25   # 10-Q 2026-06-30 borrowings + 10-K finance leases - cash
fwd_cash=1233+504; fwd_sh=18.668448+6.912857  # forward sale agreements as of 2026-06-30 (10-Q note 5); 2026 program cash approximated, see run
print('net debt',netdebt)
rows={}
print(' yr   OCFadj  allspend_eq  maint_eq  allspend_ae  maint_ae  growthspend  maint_ae/rev')
for y in yrs:
    a=OCF[y]+RCV[y]-SBC[y]
    asp=a-CXU[y]-CXO[y]; mnt=a-DA[y]; ia=INT[y]*(1-T)
    rows[y]=dict(asp=asp,mnt=mnt,aspA=asp+ia,mntA=mnt+ia,gs=CXU[y]+CXO[y]-DA[y])
    print(y,'%7.0f %10.0f %9.0f %11.0f %9.0f %11.0f   %.1f%%'%(a+SBC[y],asp,mnt,asp+ia,mnt+ia,CXU[y]+CXO[y]-DA[y],(mnt+ia)/REV[y]*100))
W=[2021,2022,2023,2024,2025]
m=lambda k:sum(rows[y][k] for y in W)/5
M_ae,M_e,G,ASP_ae,ASP_e=m('mntA'),m('mnt'),m('gs'),m('aspA'),m('asp')
g_shown=(rows[2025]['mntA']/rows[2021]['mntA'])**0.25-1
g_sales=(REV[2025]/REV[2021])**0.25-1
print('means: maint all-equity %.0f, maint equity %.0f, growth spend %.0f, all-spend all-equity %.0f, all-spend equity %.0f'%(M_ae,M_e,G,ASP_ae,ASP_e))
print('shown growth maint all-equity %.2f%%, sales growth %.2f%%'%(g_shown*100,g_sales*100))
print('share-of-sales test: base*(1+g)^10 =%.0f vs sales yr10 %.0f -> %.0f%% of sales; highest share in 2017-2025 = %.1f%%'%(M_ae*(1+g_shown)**10, REV[2025]*(1+g_sales)**10, 100*M_ae*(1+g_shown)**10/(REV[2025]*(1+g_sales)**10), max(100*rows[y]['mntA']/REV[y] for y in yrs)))
def val(base,g,spend,rate):
    v=0
    for t in range(1,11): v+=(base*(1+g)**t-spend)/(1+rate)**t
    v+=base*(1+g)**10/rate/(1+rate)**10
    return v
def ps(ev,nd=netdebt,s=sh): return (ev-nd)/s
cases={}
for lab,base,nd in [('all-equity',M_ae,netdebt),('equity-only',M_e,0)]:
    top=val(base,0,0,r); bot=val(base,g_sales,G,r); gen=val(base,g_sales,0,r)
    print('\n',lab,'at %.2f%%: no-growth maint %.0f -> $%.2f/sh ; growth case w/ growth spend %.0f -> $%.2f/sh ; [beside: growth credited, spend not charged %.0f -> $%.2f]'%(r*100,top,ps(top,nd),bot,ps(bot,nd),gen,ps(gen,nd)))
    t10=val(base,0,0,floor); b10=val(base,g_sales,G,floor)
    print('   at 10%%: no-growth $%.2f ; growth case $%.2f ; FAIR (average) $%.2f'%(ps(t10,nd),ps(b10,nd),(ps(t10,nd)+ps(b10,nd))/2))
    if lab=='all-equity':
        nd2=nd-fwd_cash; s2=sh+fwd_sh
        print('   beside, forward sales settled: range $%.2f to $%.2f; fair $%.2f'%(ps(bot,nd2,s2),ps(top,nd2,s2),(ps(t10,nd2,s2)+ps(b10,nd2,s2))/2))
    # all-spending case literal
    asp=ASP_ae if lab=='all-equity' else ASP_e
    print('   all-spending case (beside): mean owner cash %.0f -> no-growth value %.0f -> $%.2f/sh'%(asp,asp/r,ps(asp/r,nd)))
ev=price*sh+netdebt
print('\nEV at price %.0f; maint owner cash yield (all-equity) %.2f%%; 2025 %.2f%%; equity-only yield %.2f%%'%(ev,100*M_ae/ev,100*rows[2025]['mntA']/ev,100*M_e/(price*sh)))
# expected return at the price, growth credited 10 yrs at sales growth without charging spend (most generous): IRR
def irr(base,g,spend,pv):
    lo,hi=0.0001,0.5
    for _ in range(200):
        mid=(lo+hi)/2
        if val(base,g,spend,mid)>pv: lo=mid
        else: hi=mid
    return mid
print('IRR at price: no-growth maint %.2f%%; growth+spend %.2f%%; growth no spend (not admitted) %.2f%%'%(100*irr(M_ae,0,0,ev),100*irr(M_ae,g_sales,G,ev),100*irr(M_ae,g_sales,0,ev)))
# literal window base vs 2023-2025 (aberration check, shown beside)
M3=sum(rows[y]['mntA'] for y in [2023,2024,2025])/3
print('beside: 3-yr (2023-25) maint all-equity mean %.0f -> no-growth $%.2f/sh at 5.43%%'%(M3,ps(M3/r)))
