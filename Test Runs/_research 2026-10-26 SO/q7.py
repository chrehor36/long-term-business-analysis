# Q7 range and fair price, Southern Company, USD millions. COMPUTATION from the filed statements (see oc.py).
OCm=[2202,1925,2217,4205,3436]   # owner cash after maintenance only, equity-only: OCF - SBC - net NCI flows - D&A (maintenance guess)
base=sum(OCm)/5
CAPSP=[8287,8721,9850,9780,13346]; DA=[3973,4064,4986,5266,6030]
ACQNET=[-917,-275,-164,-369,920]
GS=(sum(CAPSP)-sum(DA)+sum(ACQNET))/5          # growth spending above maintenance, net acquisitions included
SALES=[23113,29279,25253,26724,29553]
g=(OCm[-1]/OCm[0])**(1/4)-1
gs=(SALES[-1]/SALES[0])**(1/4)-1
maxshare=max(o/s for o,s in zip(OCm,SALES))
y10=base*(1+g)**10; s10=SALES[-1]*(1+gs)**10
print(f'base {base:.0f}  shown growth {g*100:.2f}%  sales growth {gs*100:.2f}%  y10 OC {y10:.0f} = {y10/s10*100:.2f}% of y10 sales vs max share {maxshare*100:.2f}%')
if y10/s10>maxshare: g=gs; print('CAP applied: growth cut to sales growth')
LTD20=3507+45073; LTD25=6220+65649
ltdinc=(LTD25-LTD20)/5
cap=0.44; credit=min(ltdinc,cap*GS); credit_own=min(ltdinc,(LTD25/(LTD25+36016))*GS)
print(f'GS {GS:.0f}/yr; LTD increase {ltdinc:.0f}/yr; credit at 44% {credit:.0f}; own LTD share {LTD25/(LTD25+36016)*100:.1f}% credit {credit_own:.0f}')
SH=1150.362966; PRICE=92.69; MCAP=SH*PRICE
def value(r,oc0,gs0,grow,yrs=10):
    v=0
    for t in range(1,yrs+1):
        f=(1+grow)**t
        v+=(oc0*f-gs0*f)/(1+r)**t
    oc10=oc0*(1+grow)**yrs
    v+=oc10/r/(1+r)**yrs
    return v
R=0.0533
for lab,cr in [('central (cap 44%)',credit),('own LTD share',credit_own),('no credit',0)]:
    ng=base/R; gr=value(R,base,GS-cr,g)
    ng10=base/0.10; gr10=value(0.10,base,GS-cr,g)
    print(f'{lab}: range ${ng/SH:.2f} to ${gr/SH:.2f}  (equity {ng:,.0f} / {gr:,.0f}); fair ${(ng10+gr10)/2/SH:.2f}; net GS y1 {(GS-cr)*(1+g):.0f} y10 {(GS-cr)*(1+g)**10:.0f}')
# implied return at price
def irr(oc0,gs0,grow):
    lo,hi=0.001,0.5
    for _ in range(100):
        m=(lo+hi)/2
        if value(m,oc0,gs0,grow)>MCAP: lo=m
        else: hi=m
    return m
print(f'mcap {MCAP:,.0f}; implied return no-growth {base/MCAP*100:.2f}%  growth case {irr(base,GS-credit,g)*100:.2f}%')
# literal window shown beside = same window (no cycle base); D&A not charged variant
# all-equity beside
INT=[1718,1758,2184,2538,2692]; t=0.21
OCa=base+sum(INT)/5*(1-t)
ND=4694+2132+68756-2984
for r in [R,0.10]:
    ng=OCa/r-ND; gr=value(r,OCa,GS,g)-ND
    print(f'all-equity at {r}: no-growth ${ng/SH:.2f}  growth ${gr/SH:.2f}')
print('net debt 2026-06-30',ND)
# sensitivity: book tax instead of cash tax (deferred taxes charged)
DEF=[-49,670,63,626,618]; b2=base-sum(DEF)/5
print(f'book-tax sensitivity base {b2:.0f}: no-growth ${b2/R/SH:.2f} growth ${value(R,b2,GS-credit,g)/SH:.2f}')
