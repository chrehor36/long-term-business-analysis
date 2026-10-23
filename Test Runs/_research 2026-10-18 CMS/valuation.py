# CMS Energy, COMPUTATION, NOT A CLEARANCE. USD millions. Source lines: CMS 10-K FY2025 (0000811156-26-000004)
# for 2023-2025, 10-K FY2022 (0000811156-23-000014) for 2021-2022; 10-Q Q2 2026 (0000811156-26-000028) for net debt.
yrs=[2021,2022,2023,2024,2025]
OCF=[1819,855,2309,2370,2235]
SBC=[22,26,28,27,25]                 # Note 12, compensation expense recognized
PREF_NCI=[0,14,22,22,24]             # preferred dividends (10 from 2022) + distributions to NCI (4,12,12,14)
CAPEX=[2076,2374,2407,3018,3824]
RETIRE=[133,107,167,160,214]         # cost to retire property and other investing
ACQ_NET=[-898,-5,812,-124,0]         # Covert bought 2023; EnerBank (2021, 2022 true-up) and ASP sold
DA=[1114,1126,1180,1240,1306]
WC=[-46,-1113,416,262,-61]           # changes in assets and liabilities lines of the cash-flow statement
INT=[489,490,607,677,741]            # interest paid net of capitalized
DEBT_NET=[335-235+0,1899-106+20,3551-2132+73,1962-952-28,3609-1150-65]
SHARES=313.577; PRICE=68.70; MCAP=SHARES*PRICE
NET_DEBT=870+18172+259-241-104      # 2026-06-30
PREF=224; NCI=625
r=0.0543; FLOOR=0.10
avg=lambda a:sum(a)/len(a)
n=len(yrs)
maint=[OCF[i]-SBC[i]-PREF_NCI[i]-DA[i] for i in range(n)]
premaint=[maint[i]-WC[i] for i in range(n)]
spend=[CAPEX[i]+RETIRE[i]+ACQ_NET[i] for i in range(n)]
spend_exEB=[CAPEX[i]+RETIRE[i]+(ACQ_NET[i] if yrs[i] not in (2021,2022) else 0) for i in range(n)]
debt_credit_total=min(sum(DEBT_NET), 0.51*sum(CAPEX[i]+RETIRE[i]+max(ACQ_NET[i],0) for i in range(n)))
print('maint series',maint,'avg',round(avg(maint),1))
print('pre-WC maint series',premaint,'avg',round(avg(premaint),1))
print('sum debt raised',sum(DEBT_NET),'cap at 0.51 of fixed-asset spend',round(0.51*sum(CAPEX[i]+RETIRE[i]+max(ACQ_NET[i],0) for i in range(n))),'cap at 0.65',round(0.65*sum(CAPEX[i]+RETIRE[i]+max(ACQ_NET[i],0) for i in range(n))),'credit',debt_credit_total)
allsp=[OCF[i]-SBC[i]-PREF_NCI[i]-spend[i] for i in range(n)]
print('all-spending before debt credit',allsp,'avg',round(avg(allsp),1))
M0=avg(maint)
G0=avg(spend)-avg(DA)-debt_credit_total/n            # equity share of growth spending
G0x=avg(spend_exEB)-avg(DA)-debt_credit_total/n
print('M0',round(M0,1),'growth spend equity G0',round(G0,1),'ex-EnerBank',round(G0x,1))
print('all-spending equity owner cash',round(M0-G0,1),'ex-EnerBank',round(M0-G0x,1))
g=(premaint[-1]/premaint[0])**(1/4)-1
gx=(premaint[-1]/(premaint[0]+111))**(1/4)-1
print('growth pre-WC maint 2021-2025',f'{g:.2%}','ex 2021 disc ops',f'{gx:.2%}')
rev=[7329,8596,7462,7515,8539]; gs=(rev[-1]/rev[0])**(1/4)-1
print('sales growth',f'{gs:.2%}', 'max maint share of sales',max(maint[i]/rev[i] for i in range(n)))
def pv_nogrowth(m,rate): return m/rate
def pv_growth(m,gsp,gr,rate,years=10):
    v=0
    for t in range(1,years+1):
        v+=(m*(1+gr)**t - gsp*(1+gr)**t)/(1+rate)**t
    v+= (m*(1+gr)**years)/rate/(1+rate)**years
    return v
def irr(f,lo=0.0001,hi=1.0):
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)>0: lo=mid
        else: hi=mid
    return mid
for label,GG in (('central (net of businesses sold)',G0),('ex-EnerBank',G0x)):
  for gr,gl in ((g,'shown'),(gx,'ex-disc')):
    ng=pv_nogrowth(M0,r); gv=pv_growth(M0,GG,gr,r)
    print(f'[{label}, g {gl} {gr:.2%}] equity-only no-growth {ng:,.0f} = ${ng/SHARES:.2f}/sh; growth {gv:,.0f} = ${gv/SHARES:.2f}/sh')
    i_ng=M0/MCAP; i_g=irr(lambda x: pv_growth(M0,GG,gr,x)-MCAP)
    print(f'   expected return at price: no-growth {i_ng:.2%}, growth {i_g:.2%}')
    fp=(pv_nogrowth(M0,FLOOR)+pv_growth(M0,GG,gr,FLOOR))/2/SHARES
    print(f'   fair price equity-only (avg of ends at 10%): ${fp:.2f}')
# all-equity beside: add back interest after 21% tax, growth spending without debt credit
t=0.21
U0=M0+avg(INT)*(1-t)
Gu=avg(spend)-avg(DA)
EVclaims=NET_DEBT+PREF+NCI
for gr,gl in ((g,'shown'),(gx,'ex-disc')):
    ng=pv_nogrowth(U0,r)-EVclaims; gv=pv_growth(U0,Gu,gr,r)-EVclaims
    fp=((pv_nogrowth(U0,FLOOR)-EVclaims)+(pv_growth(U0,Gu,gr,FLOOR)-EVclaims))/2/SHARES
    print(f'[all-equity g {gl}] U0 {U0:,.0f} Gu {Gu:,.0f}: no-growth ${ng/SHARES:.2f}/sh, growth ${gv/SHARES:.2f}/sh, fair ${fp:.2f}; EV at price {MCAP+EVclaims:,.0f}, unlevered yield {U0/(MCAP+EVclaims):.2%}')
print('MCAP',round(MCAP),'net debt',NET_DEBT,'pref',PREF,'NCI',NCI)
# literal window, all spending equity-only with per-year debt credit
lit=[OCF[i]-SBC[i]-PREF_NCI[i]-spend[i]+DEBT_NET[i] for i in range(n)]
print('literal all-spending equity-only per year',lit,'avg',round(avg(lit),1))
