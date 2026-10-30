# NOA 2026-10-16: owner cash and the Q7 range, COMPUTATION, NOT A CLEARANCE (Q2 closed the file).
# All figures CAD millions, from the filed statements (40-F exhibits 99.3 and 99.4) as cited in the run file.
yrs=[2021,2022,2023,2024,2025]
ocf  =[165.2,169.2,278.1,241.2,264.1]   # 2023 as re-presented in the FY2024 40-F; 2024 restated (tires) in FY2025 40-F
sbc  =[11.6,4.8,15.8,8.7,-0.4]
sust =[102.2,113.1,168.6,223.9,213.2]   # management's sustaining capital additions (incl. finance-lease additions)
allc =[109.0,113.1,209.0,308.5,325.0]   # management's total capital additions (sustaining + growth)
acq  =[11.4,2.2,62.1,43.6,40.2]         # business purchases net of cash + payments of MacKellar contingent/deferred consideration
intp =[17.0,24.1,33.5,64.5,67.2]        # cash interest paid
dep  =[108.0,119.3,131.3,185.0,217.2]
t=0.23   # CONVENTION of this run: interest tax shield at 23% (Canada federal 15% per note 12, plus Alberta 8%)
sov=0.0419; floor=0.10
sh=26.829072  # shares net of treasury, 2026-06-30 (6-K 0001368519-26-000013)
price=16.27
netdebt=1087.415  # filer's own net debt at 2026-06-30 incl. contingent obligations 74.664
netdebt_borrow=netdebt-74.664
avg=lambda x: sum(x)/len(x)
eq_maint=[o-s-m for o,s,m in zip(ocf,sbc,sust)]
eq_all  =[o-s-m for o,s,m in zip(ocf,sbc,allc)]
eq_dep  =[o-s-d for o,s,d in zip(ocf,sbc,dep)]
shield=[i*(1-t) for i in intp]
ae_maint=[a+b for a,b in zip(eq_maint,shield)]
ae_all=[a+b for a,b in zip(eq_all,shield)]
growth_capex=[a-s for a,s in zip(allc,sust)]
def show(n,s): print(f'{n:34s}',' '.join(f'{v:7.1f}' for v in s),f'| avg {avg(s):7.1f}')
print('year',' '*29,' '.join(f'{y:7d}' for y in yrs))
for n,s in [('OCF',ocf),('SBC',sbc),('sustaining',sust),('all capital additions',allc),('growth capex',growth_capex),('acquisitions',acq),('interest paid',intp),('depreciation',dep),
            ('equity-only, maintenance',eq_maint),('equity-only, all spending',eq_all),('equity-only, depreciation variant',eq_dep),
            ('after-tax interest added',shield),('ALL-EQUITY, maintenance',ae_maint),('ALL-EQUITY, all spending',ae_all)]: show(n,s)
print('net purchases over window',round(sum(acq),1),'| owner cash before purchases, maintenance equity-only sum',round(sum(eq_maint),1),'half',round(sum(eq_maint)/2,1),'-> serial acquirer' if sum(acq)>sum(eq_maint)/2 else '')
g_ae=(ae_maint[-1]/ae_maint[0])**(1/4)-1; g_eq=(eq_maint[-1]/eq_maint[0])**(1/4)-1
print(f'shown growth, all-equity maintenance 2021->2025: {g_ae*100:.1f}%/yr; equity-only maintenance: {g_eq*100:.1f}%/yr')
def pv(base_before, purchases, gcap, g, r, growth_case):
    # years 1-10: growth case = base_before*(1+g)^t - purchases - growth capex; after 10: no growth, purchases and growth capex stop
    v=0
    for k in range(1,11):
        cf = base_before*(1+g)**k - purchases - gcap if growth_case else base_before
        v+=cf/(1+r)**k
    term = base_before*(1+g)**10 if growth_case else base_before
    v+= term/r/(1+r)**10
    return v
B=avg(ae_maint); P=avg(acq); G=avg(growth_capex)
Be=avg(eq_maint)
print(f'bases: all-equity maintenance {B:.1f}; purchases {P:.1f}; growth capex {G:.1f}; equity-only maintenance {Be:.1f}')
rows=[]
for label,base,nd in [('ALL-EQUITY',B,netdebt),('EQUITY-ONLY',Be,0.0)]:
    for r,rn in [(sov,'sovereign 4.19%'),(floor,'floor 10%')]:
        ng=pv(base,0,0,0,r,False)                 # organic pair, no growth (also the default pair's no-growth end: no purchases)
        gr=pv(base,P,G,g_ae if label=='ALL-EQUITY' else g_eq,r,True)  # default pair: purchases and growth capex deducted, total growth credited
        print(f'{label:11s} {rn:16s} no-growth value {ng:8.1f} -> per share {(ng-nd)/sh:7.2f} | growth (default pair) value {gr:8.1f} -> per share {(gr-nd)/sh:7.2f}')
        rows.append((label,rn,(ng-nd)/sh,(gr-nd)/sh))
mc=price*sh
print(f'market cap {mc:.1f}; EV (filer net debt) {mc+netdebt:.1f}; EV ex contingent {mc+netdebt_borrow:.1f}')
print(f'all-equity maintenance yield on EV: {B/(mc+netdebt)*100:.2f}%; equity-only maintenance yield on market cap: {Be/mc*100:.2f}%')
# all-spending case beside
Ba=avg(ae_all); print(f'all-spending all-equity avg {Ba:.1f}: value at sovereign {Ba/sov:.1f} -> per share {(Ba/sov-netdebt)/sh:.2f}; at floor per share {(Ba/floor-netdebt)/sh:.2f}')
# fair prices: each end at 10%, averaged
for label in ['ALL-EQUITY','EQUITY-ONLY']:
    f=[r for r in rows if r[0]==label and r[1].startswith('floor')][0]
    print(f'FAIR {label}: ends at 10% {f[2]:.2f} and {f[3]:.2f}; average {(f[2]+f[3])/2:.2f}')
# floor test at price: implied return of each case at the price
import math
def irr(fn,target):
    lo,hi=0.0001,0.5
    for _ in range(100):
        mid=(lo+hi)/2
        if fn(mid)>target: lo=mid
        else: hi=mid
    return mid
EVp=mc+netdebt
print('implied return at price, all-equity: no-growth %.2f%%, growth %.2f%%'%(irr(lambda r: pv(B,0,0,0,r,False),EVp)*100, irr(lambda r: pv(B,P,G,g_ae,r,True),EVp)*100))
print('implied return at price, equity-only: no-growth %.2f%%, growth %.2f%%'%(irr(lambda r: pv(Be,0,0,0,r,False),mc)*100, irr(lambda r: pv(Be,P,G,g_eq,r,True),mc)*100))
