# Q7 arithmetic for OGS run 2026-10-27. All inputs from filed statements (accessions in run file). USD millions.
yrs=[2021,2022,2023,2024,2025]
NI=[206.434,221.742,231.232,222.850,264.224]
DA=[207.233,228.479,279.830,296.699,317.256]
CAPEX=[495.246,609.486,666.634,703.165,707.226]
REMOV=[49.029,47.032,62.023,58.952,52.268]
OCF=[-1535.657,1570.842,939.532,368.411,578.833]
DEFTAX=[43.449,-22.034,24.773,106.522,49.507]
SBC=[10.498,10.741,12.184,13.733,14.791]
PROV=[9.131,6.003,9.698,6.705,8.207]
SECPROC=[0,1330.582,197.366,0,0]
INTEXP=[60.3,77.5,115.339,147.235,142.809]
TAX=[40.3,46.5,40.495,36.386,57.235]
# KGSS-I securitized intangible amortization (balance-sheet differences; 2022 from issuance 335.931 net proceeds less 323.838 year-end, an approximation)
KGSS_AM=[0,335.931-323.838,323.838-293.619,293.619-265.951,265.951-233.786]
KS_BOND_ISSUE=335.931; KS_BOND_REPAY=[0,0,20.716,27.939,29.493]
n=5
avg=lambda x:sum(x)/len(x)
SPEND=[c+r for c,r in zip(CAPEX,REMOV)]
MAINT=[d-k for d,k in zip(DA,KGSS_AM)]
GROWSP=[s-m for s,m in zip(SPEND,MAINT)]
OC_M=[ni+d-k-m for ni,d,k,m in zip(NI,DA,KGSS_AM,MAINT)]   # equity-only, after maintenance (= NI)
OC_ALL=[ni+d-k-s for ni,d,k,s in zip(NI,DA,KGSS_AM,SPEND)]
# working capital over window (non-Uri): OCF less noncash items less securitization proceeds plus removal (removal treated as capex), plus Kansas bond proceeds (Uri recovery booked in financing)
WC=[o-(ni+d+dt+sb+pv+sp)+r for o,ni,d,dt,sb,pv,sp,r in zip(OCF,NI,DA,DEFTAX,SBC,PROV,SECPROC,REMOV)]
WC_net_window=sum(WC)+sum(SECPROC)+KS_BOND_ISSUE
print('year spend maint growsp OC_maint OC_all WC(incl Uri)')
for i in range(n): print(yrs[i],round(SPEND[i],1),round(MAINT[i],1),round(GROWSP[i],1),round(OC_M[i],1),round(OC_ALL[i],1),round(WC[i],1))
print('avg',round(avg(SPEND),1),round(avg(MAINT),1),round(avg(GROWSP),1),round(avg(OC_M),1),round(avg(OC_ALL),1))
print('WC change over window incl Uri flows in OCF:',round(sum(WC),1),' net of Uri recoveries (OCF proceeds + KS bonds):',round(WC_net_window,1),' per year',round(WC_net_window/5,1))
lit=[o-c for o,c in zip(OCF,CAPEX)]
print('literal OCF-capex by year',[round(x,1) for x in lit],'avg',round(avg(lit),1))
# growth
g=(OC_M[-1]/OC_M[0])**(1/4)-1
print('shown growth OC_maint 2021->2025 CAGR %.4f'%g)
h1=avg(OC_M[:2]); h2=avg(OC_M[3:]); print('halves', h1,h2)
# debt credit: other LT debt (excl. KGSS-I), incl current maturities. 2020: 1582.4 noncurrent, 0 current; 2025: 2133.018+249.674
LT20=1582.4; LT25=2133.018+249.674
credit=(LT25-LT20)/5
credit_ex_tl=(LT25-250-LT20)/5
w_debt=(2453*0.41+1887*0.40)/(2453+1887)
print('LT debt increase per year',round(credit,1),' excl term loan',round(credit_ex_tl,1),' cap share %.4f'%w_debt,' cap amount on avg growth spending',round(w_debt*avg(GROWSP),1))
rf=0.0531; shares=62.856270; price=78.36
base=avg(OC_M); gs=avg(GROWSP); cr=min(credit,w_debt*gs)
def growth_case(r,base,gs,cr,g):
    pv=0
    for t in range(1,11):
        pv+=(base*(1+g)**t-gs*(1+g)**t+cr*(1+g)**t)/(1+r)**t
    term=base*(1+g)**10/r/(1+r)**10
    return pv+term
def nogrowth(r,base): return base/r
for label,r in (('sovereign',rf),('floor10',0.10)):
    ng=nogrowth(r,base); gc=growth_case(r,base,gs,cr,g)
    print(f'{label}: no-growth {ng:,.0f} (${ng/shares:.2f})  growth {gc:,.0f} (${gc/shares:.2f})')
    if label=='floor10': print('FAIR (equity-only) $%.2f'%((ng+gc)/2/shares))
    if label=='sovereign': lo,hi=sorted([ng/shares,gc/shares]); print('range %.2f-%.2f width %.3f price %.2f'%(lo,hi,hi/lo,price))
# implied return at price: solve r for no-growth and growth case
def solve(f):
    lo,hi=0.001,0.5
    for _ in range(100):
        m=(lo+hi)/2
        if f(m)>price*shares: lo=m
        else: hi=m
    return m
print('return at price: no-growth %.4f growth %.4f'%(solve(lambda r:nogrowth(r,base)),solve(lambda r:growth_case(r,base,gs,cr,g))))
# variants beside
print('-- variants --')
print('cash tax (deferred tax added back): base',round(base+avg(DEFTAX),1), ' no-growth at rf $%.2f'%((base+avg(DEFTAX))/rf/shares))
print('credit excl term loan: growth case at rf $%.2f'%(growth_case(rf,base,gs,min(credit_ex_tl,w_debt*gs),g)/shares))
print('all spending, no growth, with credit: annual',round(base-gs+cr,1),' no credit',round(base-gs,1))
ws=base+WC_net_window/5*-1 if WC_net_window<0 else base-WC_net_window/5
print('working capital charged per year',round(-WC_net_window/5,1),'-> base',round(base+WC_net_window/5,1),' no-growth $%.2f'%((base+WC_net_window/5)/rf/shares))
# all-equity beside: owner cash before interest, effective tax over window
pretax=[ni+t for ni,t in zip(NI,TAX)]; eff=sum(TAX)/sum(pretax)
ocu=[o+i*(1-eff) for o,i in zip(OC_M,INTEXP)]
gu=(ocu[-1]/ocu[0])**0.25-1
# net debt at 2026-06-30 (10-Q): senior notes 2150 + term loan 250 + CP 770.8 + KGSS-I bonds (face) ; cash
print('eff tax %.3f'%eff,' unlevered OC by year',[round(x,1) for x in ocu],' avg',round(avg(ocu),1),' growth %.4f'%gu)
print('-- all-equity beside --')
ND=2133.688+249.918+770.800-7.858   # 2026-06-30, KGSS-I bonds left out with their dedicated charge
gcap=min(gu,g)  # see run file: unlevered rate inflated by Uri financing interest; both shown
for gg,lab in ((gu,'shown unlevered %.4f'%gu),(g,'equity series rate %.4f'%g)):
    for r in (rf,0.10):
        ng=nogrowth(r,avg(ocu))-ND; gc=growth_case(r,avg(ocu),gs,0,gg)-ND
        print(lab,'r=%.4f'%r,'no-growth $%.2f growth $%.2f'%(ng/shares,gc/shares), ' avg $%.2f'%((ng+gc)/2/shares) if r==0.10 else '')
print('ND',round(ND,1))
