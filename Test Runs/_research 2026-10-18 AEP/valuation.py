"""Q7 range for AEP: COMPUTATION, NOT A CLEARANCE (the file closed at Q5). USD millions. python -I valuation.py"""
r=0.0543; FLOOR=0.10
SH=544.397; PRICE=127.14; MCAP=SH*PRICE
NET_DEBT=2028+50808+155-375-72-228      # 10-Q 2026-06-30 debt + finance leases (2025-12-31) - cash, restricted cash, other temporary investments
NCI_CLAIM=2820                          # CONVENTION of the run: the 19.9% Midwest Transmission stake at the price the partners paid
NCI_BOOK=1210
GM_SHARE=0.07                           # Generation & Marketing, 7.0% of five-year segment earnings: open castle, carried at no growth
eq_maint_x=[2416,1915,759,2959,3072]     # owner cash after maintenance only, equity basis, deferred fuel excluded, 2021-2025 (owner_cash_out.txt)
eq_maint_lit=[768,1596,1652,3236,3205]   # literal window
ai=[1137*0.79,1286*0.79,1674*0.79,1838*0.79,1894*0.79]
GROWTH_SPEND=4761                        # all capital spending less D&A and nuclear fuel, 2021-2025 average
REV25=21876; REVG=0.068
REV=[16792,19640,18982,19721,21876]
# highest share of sales of each owner-cash measure in the filings read, 2016-2025 (owner_cash_out.txt / revenue)
MAX_SHARE={'ALL-EQUITY':4688/19721,'EQUITY-ONLY':2825/16196}
avg=lambda x:sum(x)/len(x)
def halves(x): return ((x[3]+x[4])/2/((x[0]+x[1])/2))**(1/3)-1
def pv_case(base,g,rate,spend):
    v=0; c=base
    for t in range(1,11):
        c_t=base*((1-GM_SHARE)*(1+g)**t+GM_SHARE)
        v+= (c_t-spend)/(1+rate)**t
    v+= c_t/rate/(1+rate)**10        # zero nominal growth after year ten; growth spending stops with growth
    return v
def irr(base,g,spend,price):
    lo,hi=0.0005,1.0
    for _ in range(200):
        m=(lo+hi)/2
        (lo,hi)=(m,hi) if pv_case(base,g,m,spend)>price else (lo,m)
    return m
print(f"market cap {MCAP:,.0f}; net debt 2026-06-30 {NET_DEBT:,.0f}; NCI claim {NCI_CLAIM:,} (book {NCI_BOOK:,}); EV at price {MCAP+NET_DEBT+NCI_CLAIM:,.0f}")
for label,eq in [('cycle base (deferred fuel excluded)',eq_maint_x),('literal window',eq_maint_lit)]:
    ae=[a+b for a,b in zip(eq,ai)]
    B_ae=avg(ae); B_eq=avg(eq)
    g_ae=halves(ae); g_eq=halves(eq)
    print(f"\n== {label}: all-equity base {B_ae:,.0f}, equity-only base {B_eq:,.0f}; growth between halves all-equity {g_ae*100:.1f}%, equity-only {g_eq*100:.1f}%")
    # cap (f): equity owner cash share of sales in year ten at shown growth
    def capped(name,B,g):
        share10=B*(1+g)**10/(REV25*(1+REVG)**10)
        cut=share10>MAX_SHARE[name]
        print(f"  (f) {name}: owner cash in year ten at shown {g*100:.1f}% = {share10*100:.1f}% of sales grown at {REVG*100:.1f}% vs highest filed share {MAX_SHARE[name]*100:.1f}% -> {'CUT to sales growth' if cut else 'not cut'}")
        return min(g,REVG) if cut else g
    g_ae=capped('ALL-EQUITY',B_ae,g_ae); g_eq=capped('EQUITY-ONLY',B_eq,g_eq)
    claims=NET_DEBT+NCI_CLAIM
    for basis,B,g,deduct,px in [('ALL-EQUITY',B_ae,g_ae,claims,MCAP+claims),('EQUITY-ONLY',B_eq,g_eq,0,MCAP)]:
        ng=pv_case(B,0,r,0); gr=pv_case(B,g,r,GROWTH_SPEND)
        ng10=pv_case(B,0,FLOOR,0); gr10=pv_case(B,g,FLOOR,GROWTH_SPEND)
        ps=lambda v:(v-deduct)/SH
        lo,hi=sorted([ps(ng),ps(gr)])
        fair=(ps(ng10)+ps(gr10))/2
        print(f"  {basis}: no-growth {ps(ng):8.2f}/sh; growth-with-spending {ps(gr):8.2f}/sh  => range {lo:.2f} to {hi:.2f}")
        print(f"     expected return at price: no-growth {irr(B,0,0,px)*100:.1f}%; growth case {irr(B,g,GROWTH_SPEND,px)*100:.1f}%")
        print(f"     fair price (each end at 10%, averaged): {fair:.2f}/sh  [no-growth {ps(ng10):.2f}, growth {ps(gr10):.2f}]")
        print(f"     maintenance-only growth case WITHOUT charging growth spending (not a case the convention allows; shown for scale): {ps(pv_case(B,g,r,0)):.2f}/sh")
# forwards beside
SH2=SH+45; ND2=NET_DEBT-5034
print(f"\nforwards settled beside: shares {SH2:.1f}M, net debt {ND2:,.0f}")
B=avg([a+b for a,b in zip(eq_maint_x,ai)])
print(f"  all-equity no-growth with forwards: {(pv_case(B,0,r,0)-ND2-NCI_CLAIM)/SH2:.2f}/sh")
print(f"  NCI at book instead of price paid: all-equity no-growth {(pv_case(B,0,r,0)-NET_DEBT-NCI_BOOK)/SH:.2f}/sh")
