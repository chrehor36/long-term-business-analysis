# GWRS Q7 arithmetic (USD thousands). Inputs transcribed from the filed 10-Ks (accessions in the run file).
yrs=[2021,2022,2023,2024,2025]
ocf=[20386,23336,25393,21785,20168]          # net cash from operating activities
sbc=[2884,1529,1325,1029,861]                # stock/deferred-comp add-back (full add-back charged)
capex=[18250,33984,22312,32324,67321]
acq=[2068,180,6246,150,8098]
fl=[147,0,525,273,401]                       # finance-lease principal (financing section)
da=[9490,9889,11437,12720,14998]             # depreciation, amortization (and accretion) as filed
buck=[1400,2500,2400,2916,2412]              # Buckeye growth premiums received (non-utility, ends 2034)
intexp=[5201,4759,4882,6098,5964]            # interest expense as filed (2022 restated in FY2023 10-K)
tax=0.258                                    # 2025 effective rate (statutory 21% + AZ 4% net)
aiac_net=[3817-1007-1364,2344-1140,1510+6700-1171,10627-1355,6165-1427]  # developer cash in, less refunds (beside only)
rate=0.053; floor=0.10
sh=(28795352+1129944)/1000.0       # thousands of shares: cover 2026-08-07 + private placement 2026-08-20
price=7.74
mean=lambda a:sum(a)/len(a)
maint=[o-s-d-f-b for o,s,d,f,b in zip(ocf,sbc,da,fl,buck)]
allsp=[o-s-c-a-f-b for o,s,c,a,f,b in zip(ocf,sbc,capex,acq,fl,buck)]
print('maintenance owner cash ex-Buckeye (equity-only):',maint,'mean',round(mean(maint)))
print('all-spending owner cash ex-Buckeye (equity-only):',allsp,'mean',round(mean(allsp)))
g=(maint[-1]/maint[0])**(1/4)-1; print('shown growth, maintenance case, compound 2021->2025: %.1f%%'%(g*100))
h1=mean(maint[:2]); h2=mean(maint[3:]); print('halves: first %.0f second %.0f'%(h1,h2))
# debt credit (regulated utility section, 2026-10-23): LT debt incl. current and finance leases, end-2020 to end-2025
ltd2020=115003; ltd2025=133698+1179
credit=(ltd2025-ltd2020)/5
growth_sp=mean([c+a for c,a in zip(capex,acq)])-mean(da)
cap=0.45*growth_sp
credit=min(credit,cap)
print('growth spending/yr %.0f; LT debt credit/yr %.0f (cap 45%% = %.0f)'%(growth_sp,credit,cap))
def pv(cfs,r,term=None):
    v=sum(cf/(1+r)**(t+1) for t,cf in enumerate(cfs))
    if term is not None: v+=term/r/(1+r)**len(cfs)
    return v
# Buckeye stream 2026-2034 at window mean, capped at $45.0M less $16.1M received
bm=mean(buck); n=9; tot=min(bm*n,45000-16100)
bstream=[tot/n]*n
pvb_s=pv(bstream,rate); pvb_f=pv(bstream,floor)
print('Buckeye mean %.0f, 9 yrs, PV@5.3%% %.0f, PV@10%% %.0f'%(bm,pvb_s,pvb_f))
M=mean(maint)
def growth_case(r):
    cfs=[];
    for t in range(1,11):
        oc=M*(1+g)**t; gs=growth_sp*(1+g)**t; cr=credit*(1+g)**t
        cfs.append(oc-gs+cr)
    term=M*(1+g)**10
    return pv(cfs,r,term)
top_s=M/rate+pvb_s; bot_s=growth_case(rate)+pvb_s
top_f=M/floor+pvb_f; bot_f=growth_case(floor)+pvb_f
print('EQUITY-ONLY (central, regulated utility): top %.0f ($%.2f/sh)  bottom %.0f ($%.2f/sh)'%(top_s,top_s/sh,bot_s,bot_s/sh))
print('  fair: top@10%% %.0f ($%.2f) bottom@10%% %.0f ($%.2f) average $%.2f'%(top_f,top_f/sh,bot_f,bot_f/sh,(top_f+bot_f)/2/sh))
# all-spending variant (literal, beside)
A=mean(allsp)+credit
print('all-spending + credit mean %.0f -> no-growth value @5.3%% %.0f ($%.2f)'%(A,A/rate+pvb_s,(A/rate+pvb_s)/sh))
# floor test at price
mcap=price*sh  # USD thousands
print('market value %.0f; top case yield incl Buckeye mean: %.2f%%'%(mcap,(M+bm)/mcap*100))
print('with developer cash net beside: %.2f%%'%((M+bm+mean(aiac_net))/mcap*100), 'aiac_net',aiac_net,round(mean(aiac_net)))
# ALL-EQUITY beside: add back after-tax interest; net debt at 2026-06-30 + PP proceeds
ai=mean(intexp)*(1-tax); Mae=M+ai
nd=127828+3947+5800+1179-1458-10000
print('all-equity: after-tax interest %.0f; owner cash %.0f; net debt %.0f'%(ai,Mae,nd))
def gc_ae(r):
    cfs=[Mae*(1+g)**t - growth_sp*(1+g)**t for t in range(1,11)]
    return pv(cfs,r,Mae*(1+g)**10)
t_ae=Mae/rate+pvb_s-nd; b_ae=gc_ae(rate)+pvb_s-nd
tf_ae=Mae/floor+pvb_f-nd; bf_ae=gc_ae(floor)+pvb_f-nd
print('ALL-EQUITY beside: top $%.2f bottom $%.2f; fair top@10 $%.2f bottom@10 $%.2f avg $%.2f'%(t_ae/sh,b_ae/sh,tf_ae/sh,bf_ae/sh,(tf_ae+bf_ae)/2/sh))
print('EV yield at price (all-equity top): %.2f%%'%((Mae+bm)/(mcap+nd)*100))
# check: full allowed return on an approximate rate base (not a case)
rb=441851-155414-37857-9699-22772
print('approx rate base %.0f; 55%% x 9.6%% = %.0f; yield on market value %.2f%%'%(rb,rb*0.55*0.096,rb*0.55*0.096/mcap*100))
