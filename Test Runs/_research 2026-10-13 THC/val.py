# Q7 range by the v5 range convention, COMPUTATION. USD millions except per share.
def pv(c0,g,r,yrs=10):
    v=0;c=c0
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    return v + c/r/(1+r)**yrs      # zero nominal growth after year ten
R=0.056; FLOOR=0.10
SH=80.519; PRICE=269.14
ND=13248-2170          # 10-Q 2026-06-30: total long-term debt incl. finance leases, less cash; Sept-2026 notes refinance only
CHI=414+828            # CHI note receivable carrying amount, shown beside, not in central
def show(lbl,c0,g,nd):
    lo=pv(c0,0,R) if g>=0 else pv(c0,g,R); hi=pv(c0,g,R) if g>=0 else pv(c0,0,R)
    f0=pv(c0,0,FLOOR); fg=pv(c0,g,FLOOR); fair=((f0+fg)/2-nd)/SH
    print(f"{lbl}: base {c0:.0f} g {g*100:.2f}% | range EV {min(lo,hi):,.0f}-{max(lo,hi):,.0f} | per share {(min(lo,hi)-nd)/SH:,.2f} to {(max(lo,hi)-nd)/SH:,.2f} | fair {fair:,.2f} | width {(max(lo,hi)-nd)/(min(lo,hi)-nd) if min(lo,hi)>nd else float('nan'):.2f}")
    # expected return at the price on each end: solve r such that pv(c0,g,r)=price*SH+nd
    for gg in (0,g):
        lo_r,hi_r=0.001,0.5
        tgt=PRICE*SH+nd
        for _ in range(100):
            m=(lo_r+hi_r)/2
            if pv(c0,gg,m)>tgt: lo_r=m
            else: hi_r=m
        print(f"   expected return at {PRICE} with g={gg*100:.2f}%: {m*100:.2f}%")
import statistics as s
AE=[1669,1142,1249,1001,1892]; EQ=[957,498,579,354,1235]; AEpre=[1643,1239,1526,1749,2212]
g_ae=(AE[-1]/AE[0])**(1/4)-1; g_eq=(EQ[-1]/EQ[0])**(1/4)-1
g_ae_h=((AE[3]+AE[4])/(AE[0]+AE[1]))**(1/3)-1
print('growth AE end-years',round(g_ae*100,2),'halves',round(g_ae_h*100,2),'EQ end-years',round(g_eq*100,2))
show('ALL-EQUITY central (acq deducted, total growth)',s.mean(AE),g_ae,ND)
show('ALL-EQUITY, CHI note counted (beside)',s.mean(AE),g_ae,ND-CHI)
show('ALL-EQUITY halves growth (beside)',s.mean(AE),g_ae_h,ND)
show('EQUITY-ONLY (beside)',s.mean(EQ),g_eq,0)
show('ALL-EQUITY literal 2024 divestiture (beside)',s.mean([1669,1142,1249,1001+4160,1892]),g_ae,ND)
