print("COMPUTATION, NOT A CLEARANCE (operator rule 3): computed before Q1 to Q4 closed; no entry language.")
# Q7 arithmetic for AVA (USD millions). Inputs transcribed from the filed statements (see run file).
yrs=[2021,2022,2023,2024,2025]
ocf=[267.3,124,447,534,469]; sbc=[4.7,9,8,9,9]; capex=[439.9,452,499,533,570]
da=[232.2,253,265,274,289]; intp=[98.6,107,132,141,144]; rev=[1438.9,1710,1752,1938,1964]
T=0.21
eq_all=[o-s-c for o,s,c in zip(ocf,sbc,capex)]
eq_mnt=[o-s-d for o,s,d in zip(ocf,sbc,da)]
ati=[i*(1-T) for i in intp]
ae_all=[a+b for a,b in zip(eq_all,ati)]
ae_mnt=[a+b for a,b in zip(eq_mnt,ati)]
gcap=[c-d for c,d in zip(capex,da)]
m=lambda x: sum(x)/len(x)
for n,s in [('equity all-spending',eq_all),('equity maintenance (D&A)',eq_mnt),('after-tax interest',ati),('all-equity all-spending',ae_all),('all-equity maintenance',ae_mnt),('growth capex (capex-D&A)',gcap)]:
    print(f"{n:28s}", [round(v,1) for v in s], 'mean', round(m(s),1))
g_sales=(rev[-1]/rev[0])**(1/4)-1
print('sales CAGR 2021-25', round(100*g_sales,2),'%')
# halves test
for n,s in [('all-equity maintenance',ae_mnt),('equity maintenance',eq_mnt)]:
    h1=m(s[:2]); h2=m(s[3:]); print(n,"halves",round(h1,1),round(h2,1),"implied annual over 3 yrs", (round(100*((h2/h1)**(1/3)-1),1) if h1>0 else "meaningless (first half negative)"))
NETDEBT=3335.0; SH=83.75283; PRICE=36.67
def pv_nogrowth(b,r): return b/r
def pv_growth(b,gc,g,r,gc_grows=True):
    v=0
    for t in range(1,11):
        cf=b*(1+g)**t - (gc*(1+g)**t if gc_grows else gc)
        v+=cf/(1+r)**t
    term=b*(1+g)**10/r
    v+=term/(1+r)**10
    return v
for r in (0.0543,0.10):
    print(f"--- discount {r}")
    B=m(ae_mnt); GC=m(gcap)
    ng=pv_nogrowth(B,r)
    for lab,gg in [('sales g',g_sales),('rate-base g',(6319/5225.5)**(1/4)-1)]:
        gw=pv_growth(B,GC,gg,r); gw2=pv_growth(B,GC,gg,r,False)
        print(lab, round(100*gg,2),'% growth case EV',round(gw),' (growth capex flat:',round(gw2),')',' per share',round((gw-NETDEBT)/SH,2),round((gw2-NETDEBT)/SH,2))
    print('no-growth maintenance EV',round(ng),'per share',round((ng-NETDEBT)/SH,2))
    # equity-only
    Be=m(eq_mnt); nge=Be/r
    print('equity-only no-growth', round(nge), 'per share', round(nge/SH,2))
    gwe=pv_growth(Be,GC,g_sales,r); print('equity-only growth (sales g)', round(gwe),'per share',round(gwe/SH,2))
# expected returns at the price
EV=PRICE*SH+NETDEBT
print('mkt cap',round(PRICE*SH),'EV',round(EV))
print('all-equity maintenance yield at price', round(100*m(ae_mnt)/EV,2),'%; equity maintenance yield', round(100*m(eq_mnt)/(PRICE*SH),2),'%')
# IRR of growth case at the price (all-equity)
def irr_growth(b,gc,g,price):
    lo,hi=-0.5,0.5
    for _ in range(200):
        mid=(lo+hi)/2
        if mid<=0: 
            lo=mid; continue
        if pv_growth(b,gc,g,mid)>price: lo=mid
        else: hi=mid
    return mid
print('IRR no-growth all-equity', round(100*m(ae_mnt)/EV,2))
print('IRR growth case all-equity (sales g)', round(100*irr_growth(m(ae_mnt),m(gcap),g_sales,EV),2))
print('IRR growth case all-equity (rate base g)', round(100*irr_growth(m(ae_mnt),m(gcap),(6319/5225.5)**(1/4)-1,EV),2))
print('IRR growth case equity (sales g)', round(100*irr_growth(m(eq_mnt),m(gcap),g_sales,PRICE*SH),2))
