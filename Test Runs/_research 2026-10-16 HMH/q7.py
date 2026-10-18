# Q7 COMPUTATION, NOT A CLEARANCE (figures in $ thousands, from the filed statements)
yrs=[2022,2023,2024,2025]
ocf  =[974,25574,34861,88310]
ppe  =[7534,14116,16096,9617]
dev  =[7457,10541,2244,6649]
intang=[0,0,192,715]
sale =[1056,601,213,338]
acq  =[3254,0,19624,4457]
cint =[18604,26159,23284,28024]   # cash paid for interest
iexp =[32725,46269,37255,43352]   # interest expense, net (income statement)
rev  =[677213,785446,843363,821754]
sbc_pre=22775/4                   # pre-IPO awards recognised Q2 2026, spread over the four award years (CONVENTION of this run)
T=0.25                            # tax shield on interest at the prospectus's blended statutory rate (CONVENTION of this run)
r=0.0543; floor=0.10
shares=12201501+31891652
netdebt=197836-119705
price=17.34
eq_before_acq=[o-p-d-i+s-sbc_pre for o,p,d,i,s in zip(ocf,ppe,dev,intang,sale)]
ae_before_acq=[e+c*(1-T) for e,c in zip(eq_before_acq,cint)]
ae=[a-q for a,q in zip(ae_before_acq,acq)]
for y,a,b,c in zip(yrs,eq_before_acq,ae_before_acq,ae): print(y,'eq-only pre-acq',round(a),'all-eq pre-acq',round(b),'all-eq after acq',round(c),'share of sales',round(b/rev[yrs.index(y)]*100,1))
avg=lambda v: sum(v)/len(v)
C=avg(ae); print('central base (all-equity, acquisitions deducted, 4-yr avg)',round(C))
print('acq share of owner cash before purchases', round(sum(acq)/sum(ae_before_acq)*100,1),'%')
# growth: series changes sign -> halves (specific b)
h1=avg(ae[:2]); h2=avg(ae[2:]); print('halves',round(h1),round(h2), 'growth/yr', round(((h2/h1)**(1/2)-1)*100,1) if h1>0 else 'n/a')
g_sales=(rev[-1]/rev[0])**(1/3)-1; print('sales CAGR 2022-25',round(g_sales*100,2))
g=min(g_sales,r); print('growth carried (cut to sales growth, capped at discount rate)',round(g*100,2))
def val(C,g,rate,yrs=10):
    pv=sum(C*(1+g)**t/(1+rate)**t for t in range(1,yrs+1))
    term=C*(1+g)**yrs/rate/(1+rate)**yrs
    return pv+term
def ps(ev): return (ev-netdebt)/shares*1000
lo=val(C,0,r); hi=val(C,g,r)
print('EV no-growth',round(lo),'per share',round(ps(lo),2))
print('EV growth',round(hi),'per share',round(ps(hi),2), 'width',round(hi/lo,2))
f_lo=val(C,0,floor); f_hi=val(C,g,floor); fair=(f_lo+f_hi)/2
print('fair all-equity per share',round(ps(fair),2))
# implied return at price: solve rate where avg of two ends = market EV
ev_mkt=price*shares/1000+netdebt; print('market cap',round(price*shares/1000),'EV',round(ev_mkt))
def solve(Cx,gx):
    lo_,hi_=0.0001,0.5
    for _ in range(200):
        m=(lo_+hi_)/2
        if val(Cx,gx,m)>ev_mkt: lo_=m
        else: hi_=m
    return m
print('expected return at price: no-growth',round(solve(C,0)*100,2),'% growth case',round(solve(C,g)*100,2),'%')
# equity-only
eq_filed=[a-ie*(1-T)-q for a,ie,q in zip(ae_before_acq,iexp,acq)]
Ce=avg(eq_filed); print('equity-only, filed interest, avg',round(Ce))
cur_int=200000*0.07875*(1-T); Ce2=C-cur_int; print('equity-only, interest on today bonds, base',round(Ce2))
fe=(val(Ce2,0,floor)+val(Ce2,g,floor))/2; print('fair equity-only (today interest) per share',round(fe/shares*1000,2))
fe1=(val(Ce,0,floor)+val(Ce,g,floor))/2; print('fair equity-only (filed interest) per share',round(fe1/shares*1000,2))
# depreciation variant: PP&E depreciation instead of PP&E capex+dev
# TTM beside (not chosen)
ttm_ocf=88310+7552+25156; ttm_capex=(9617-4840+2086)+(6649-1073+5896)+715-338
ttm_int=28024-13700+9195; ttm_acq=4457+770
ttm=ttm_ocf-ttm_capex-sbc_pre+ttm_int*(1-T)-ttm_acq; print('TTM June 2026 all-equity owner cash (beside, not chosen)',round(ttm))
print('no-growth per share on TTM',round(ps(val(ttm,0,r)),2),'fair on TTM',round(ps((val(ttm,0,floor)+val(ttm,g,floor))/2),2))
# Beside, not chosen: owner cash before working-capital changes (specific (d) counts them; shown only for sensitivity)
wc=[-30500,-36586,-82281,-33984]   # sum of 'changes in operating assets and liabilities' lines, filed cash-flow statements
pre_wc=[a-w for a,w in zip(ae,wc)]
print('pre-WC all-equity after acq',[round(x) for x in pre_wc],'avg',round(avg(pre_wc)), 'sum WC',sum(wc))
Cw=avg(pre_wc)
print('pre-WC no-growth per share',round(ps(val(Cw,0,r)),2),'growth',round(ps(val(Cw,g,r)),2),'fair',round(ps((val(Cw,0,floor)+val(Cw,g,floor))/2),2))
dep=[40867-21575,37951-19938,39402-19263,42460-24347]
cap=[p+d+i-s for p,d,i,s in zip(ppe,dev,intang,sale)]
print('PP&E depreciation',dep,'avg',round(avg(dep)),'capex net',cap,'avg',round(avg(cap)))
