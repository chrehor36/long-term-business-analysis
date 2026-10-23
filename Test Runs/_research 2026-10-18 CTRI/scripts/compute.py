# CTRI owner cash and the Q7 COMPUTATION. All $ millions. Sources: 424B4 0001193125-24-100835 (FY2021-2023 cash flow),
# 10-K FY2025 0001981599-26-000020 (FY2023-2025), 10-Q 0001981599-26-000089 (net debt at 2026-06-28, JJ White subsequent event).
import sys; sys.stdout.reconfigure(encoding="utf-8")
Y=[2021,2022,2023,2024,2025]
OCF=[109.480,94.626,167.465,158.230,78.121]
SECZ=[0,0,0,-125.0,0]          # initial sale of receivables into the securitization facility, Sept 2024 (10-K FY2025 MD&A)
SBC=[1.732,1.652,1.851,2.231,8.079]
CAPEX=[110.417,129.587,106.650,99.333,86.325]
PROC=[16.010,12.526,11.800,9.958,43.953]
SLB=[0,0,0,0,37.8]             # sale-leaseback proceeds inside 2025 proceeds (10-K FY2025 MD&A), excluded
FINL=[3.547,11.985,12.113,11.293,9.418]
ACQ=[822.173,0,0,0,45.832]; NCI=[0,39.649,39.894,92.916,0]
# pre-working-capital operating cash: net income + non-cash items - operating lease payments (statement lines)
PREWC=[46.937+100.327+17.316+2.744+0+1.732-6.906+11.877+15.772-14.669,
       -164.986+125.594+29.759+4.894+177.086+1.652-6.362+14.465-7.138-16.725,
       -184.506+118.776+26.670+4.482+213.992+1.851-4.547+17.373-7.827-21.908,
       -6.822+108.703+26.642+5.306+1.726+2.231-3.634+20.682-5.099+0.841-26.451,
       22.650+111.512+27.281+3.585+2.742+8.079-7.403+22.419-14.111-27.847]
INTCASH=[20.999-2.744,61.371-4.894,98.342,78.265,67.009]  # interest paid 2023-25 (10-K supplemental); 2021-22 expense less debt-cost amortization
T=0.25  # CONVENTION of the run: the company's own blended statutory rate (10-K FY2025 non-GAAP note (1))
REV=[2158.661,2760.327,2899.276,2637.229,2982.781]
r=0.0543; floor=0.10
shares=100.963053; price=19.73
debt=22.915+608.972+85.855+7.126+6.873; cash=40.458; jjw=62.0; secz_off=165.0
nd=debt-cash+jjw
mcap=shares*price; ev=mcap+nd
def avg(x): return sum(x)/len(x)
allsp_eq=[OCF[i]+SECZ[i]-SBC[i]-CAPEX[i]+PROC[i]-SLB[i]-FINL[i] for i in range(5)]
maint_eq=[PREWC[i]-SBC[i]-CAPEX[i]+PROC[i]-SLB[i]-FINL[i] for i in range(5)]
ati=[INTCASH[i]*(1-T) for i in range(5)]
allsp_ae=[allsp_eq[i]+ati[i] for i in range(5)]
maint_ae=[maint_eq[i]+ati[i] for i in range(5)]
acqd_ae=[allsp_ae[i]-ACQ[i]-NCI[i] for i in range(5)]
print("year  OCF  allsp_eq maint_eq  aTint  allsp_AE  maint_AE  acq-deducted_AE  WCchange(maint-allsp) rev")
for i in range(5): print(Y[i], f"{OCF[i]:7.1f} {allsp_eq[i]:8.1f} {maint_eq[i]:8.1f} {ati[i]:6.1f} {allsp_ae[i]:8.1f} {maint_ae[i]:8.1f} {acqd_ae[i]:9.1f} {maint_eq[i]-allsp_eq[i]:8.1f} {REV[i]:8.1f}")
for n,s in [("allsp_eq",allsp_eq),("maint_eq",maint_eq),("allsp_AE",allsp_ae),("maint_AE",maint_ae),("acqded_AE",acqd_ae)]:
    h1=avg(s[:2]); h2=avg(s[3:]); h1b=avg(s[1:3]); 
    print(f"{n:10s} 5yr avg {avg(s):8.1f}  halves(21-22 vs 24-25) {h1:7.1f}->{h2:7.1f}  post-acq (22-23 vs 24-25) {h1b:7.1f}->{h2:7.1f} g={((h2/h1b)**0.5-1)*100 if h1b>0 and h2>0 else float('nan'):.2f}%/yr")
print(f"net debt {nd:.1f} (debt {debt:.1f} - cash {cash:.1f} + JJW {jjw}); securitized receivables off-sheet {secz_off}; mcap {mcap:.1f}; EV {ev:.1f}")
def pv(c0,g,rate,stop_after10=True,term=None):
    v=0;c=c0
    for t in range(1,11):
        c=c*(1+g); v+=c/(1+rate)**t
    tc = term if term is not None else c
    return v + tc/rate/(1+rate)**10
def ps(evv,netd=nd): return (evv-netd)/shares
M=avg(maint_ae); A=avg(allsp_ae); Me=avg(maint_eq); Ae=avg(allsp_eq)
# growth measured on post-acquisition full years (serial-acquirer organic pair)
gM=(avg(maint_ae[3:])/avg(maint_ae[1:3]))**0.5-1
gA=(avg(allsp_ae[3:])/avg(allsp_ae[1:3]))**0.5-1
print(f"g maint_AE {gM*100:.2f}%  g allsp_AE {gA*100:.2f}%")
cases={
 "TOP  maintenance-only, no growth (AE)": pv(M,0,r),
 "     maintenance-only, shown growth (AE)": pv(M,gM,r),
 "BOT  all spending, shown growth, growth spending stops after yr10 (AE)": pv(A,gA,r,term=M*(1+gA)**10),
 "     all spending, no growth forever (AE)": pv(A,0,r),
}
for k,v in cases.items(): print(f"{k:72s} EV {v:8.1f}  per share {ps(v):7.2f}")
# floor test: expected return at today's EV on each case (IRR)
def irr(c0,g,term):
    lo,hi=-0.5,1.0
    for _ in range(200):
        m=(lo+hi)/2; v=pv(c0,g,m,term=term)
        if v>ev: lo=m
        else: hi=m
    return m
print(f"IRR at price: maint no-growth {M/ev*100:.2f}% ; all-spend no growth {A/ev*100:.2f}% ; maint growth {irr(M,gM,M*(1+gM)**10)*100:.2f}% ; allsp growth {irr(A,gA,M*(1+gA)**10)*100:.2f}%")
# fair price: each end at 10%, averaged, less net debt
top10=pv(M,0,floor); bot10=pv(A,gA,floor,term=M*(1+gA)**10)
print(f"FAIR (AE) top@10% {ps(top10):.2f} bottom@10% {ps(bot10):.2f} avg {(ps(top10)+ps(bot10))/2:.2f}")
# equity-only beside
gMe=(avg(maint_eq[3:])/avg(maint_eq[1:3]))**0.5-1
topE=Me/r; botE=pv(Ae,0,r)
print(f"EQUITY-ONLY: maint avg {Me:.1f} (g {gMe*100:.2f}%) allsp avg {Ae:.1f}; top {topE/shares:.2f}/sh  bottom(no growth) {botE/shares:.2f}/sh; fair: top {Me/floor/shares:.2f} bottom {Ae/floor/shares:.2f} avg {(Me/floor+Ae/floor)/2/shares:.2f}")
print(f"DEFAULT PAIR (acquisitions deducted, total growth credited) avg AE {avg(acqd_ae):.1f}/yr -> no-growth EV {avg(acqd_ae)/r:.1f}")
print(f"net purchases {sum(ACQ)+sum(NCI):.1f} vs half of owner cash before purchases {sum(allsp_ae)/2:.1f} -> serial acquirer: {sum(ACQ)+sum(NCI) > sum(allsp_ae)/2}")
print(f"owner cash (maint AE)/revenue by year: "+" ".join(f'{maint_ae[i]/REV[i]*100:.1f}%' for i in range(5)))
print(f"literal window, all spending as filed (no securitization or SLB adjustment), equity-only avg: {avg([OCF[i]-SBC[i]-CAPEX[i] for i in range(5)]):.1f}")
print("---- range as adopted in the run file ----")
gW=(avg(maint_ae[3:])/avg(maint_ae[:2]))**(1/3)-1
def irr2(c0,g,term):
    lo,hi=0.0001,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c0,g,m,term=term)>ev: lo=m
        else: hi=m
    return m
top=pv(M,0,r); bot=pv(A,0,r); dec=pv(M,gM,r); win=pv(M,gW,r)
print(f"TOP maint no-growth {ps(top):.2f}; BOTTOM all-spending no-growth {ps(bot):.2f}; beside: maint post-acq decline {gM*100:.2f}% -> {ps(dec):.2f}; maint window-halves {gW*100:.2f}% -> {ps(win):.2f}")
print(f"expected return at price: top {irr2(M,0,M)*100:.2f}%  bottom {irr2(A,0,A)*100:.2f}%  decline {irr2(M,gM,M*(1+gM)**10)*100:.2f}%  window-growth {irr2(M,gW,M*(1+gW)**10)*100:.2f}%")
ft=ps(M/floor); fb=ps(A/floor)
print(f"FAIR PRICE all-equity: top@10% {ft:.2f}  bottom@10% {fb:.2f}  average {(ft+fb)/2:.2f}")
print(f"FAIR PRICE equity-only: top@10% {Me/floor/shares:.2f} bottom@10% {Ae/floor/shares:.2f} average {(Me/floor+Ae/floor)/2/shares:.2f}")
print(f"with securitized receivables {secz_off} counted as debt: top/share {ps(top,nd+secz_off):.2f}; fair AE avg {(ps(M/floor,nd+secz_off)+ps(A/floor,nd+secz_off))/2:.2f}")
print(f"interest cover pre-tax earnings/interest: 2025 {(14.587+78.428)/78.428:.2f}x  2024 {(-3.356+90.515)/90.515:.2f}x ; operating income/interest 2025 {92.821/78.428:.2f}x")
