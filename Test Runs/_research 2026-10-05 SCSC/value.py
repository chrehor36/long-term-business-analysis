# COMPUTATION - NOT A CLEARANCE. Q7 convention arithmetic for SCSC, 2026-10-05.
r=0.0563; sh=20.142812  # cover shares 2026-08-17 (millions)
price=61.01
def pv(oc,g,r=r,n=10):
    v=0; c=oc
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+r)**t
    return v + (c/r)/(1+r)**n   # after year 10: zero nominal growth
ocf=[-124.354,-35.769,371.647,112.349,123.131]
sbc=[11.663,11.219,9.537,11.062,14.063]
cx=[6.849,9.979,8.555,8.286,9.286]
da=[29.884,28.614,28.009,30.195,23.633]
oc_cx=sum(o-s-c for o,s,c in zip(ocf,sbc,cx))/5
oc_da=sum(o-s-d for o,s,d in zip(ocf,sbc,da))/5
pre=[137.947,129.835,106.783,124.656,128.827]  # OCF before working-capital changes (filed statements)
prov=[1.514,2.785,8.317,8.351,5.956]
acq=[0,0,0,56.673,18.220]
wc_pre=sum(p-s-c-v for p,s,c,v in zip(pre,sbc,cx,prov))/5
sales26=3226.062; nwc_int=538.8/sales26
def show(name,oc,gs):
    print(f"{name}: owner cash {oc:.1f}M")
    for g in gs:
        v=pv(oc,g); print(f"   g={g*100:.1f}%  value {v:,.0f}M  ${v/sh:,.2f}/sh  ({price/(v/sh)*100:.0f}% of value at ${price})")
show('A. convention, capex basis (5-yr FY22-26)',oc_cx,[0,0.0047,0.01])
show('B. convention, D&A basis',oc_da,[0,0.0047,0.01])
g=0.0047
wc_growth=sales26*g*nwc_int
wc1=wc_pre-wc_growth
wc2=wc1-sum(acq)/5
show('C. whole-cycle, WC at cycle intensity, before acquisitions',wc1,[0,g])
show('D. whole-cycle, after acquisitions',wc2,[0,g])
print('wc_pre',round(wc_pre,1),'wc for growth',round(wc_growth,1),'nwc intensity',round(nwc_int*100,1))
tax=0.24
for name,oc,gg in [('central D',wc2,g),('convention A',oc_cx,0.01),('C',wc1,g)]:
    pretax=oc/(1-tax); cap=pretax/(0.10-gg)
    print(f"FAIR ({name}): pre-tax owner cash {pretax:.1f}; cap at 10% pre-tax incl growth {gg*100:.2f}% = {cap:,.0f}M = ${cap/sh:.2f}; cheap (half) ${cap/sh/2:.2f}")
# implied: what does the price assume
mc=price*sh; print('market cap',round(mc,1))
for name,oc in [('A',oc_cx),('C',wc1),('D',wc2)]:
    print(name,'after-tax owner-cash yield at price',round(oc/mc*100,2),'% ; pre-tax',round(oc/(1-tax)/mc*100,2),'%')
