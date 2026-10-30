# COMPUTATION - arithmetic for the ENSG run, 2026-10-05
ocf={2021:275.684,2022:272.513,2023:376.666,2024:347.186,2025:564.270}
sbc={2021:18.678,2022:22.720,2023:30.767,2024:36.226,2025:48.299}
capex={2021:69.550,2022:87.545,2023:106.180,2024:158.240,2025:193.557}
acq={2021:6.0+98.224,2022:16.4+84.736,2023:69.014,2024:156.547,2025:323.258}
da={2021:55.985,2022:62.355,2023:72.387,2024:84.138,2025:104.327}
A={};B={};C={}
for y in ocf:
    A[y]=ocf[y]-sbc[y]-capex[y]-acq[y]; B[y]=ocf[y]-sbc[y]-capex[y]; C[y]=ocf[y]-sbc[y]-da[y]
for n,d in [('all capital incl acquisitions',A),('all capex, before acquisitions',B),('depreciation variant',C)]:
    print(n,{y:round(v,1) for y,v in d.items()},'avg',round(sum(d.values())/5,1),'CAGR21-25', round(((d[2025]/d[2021])**0.25-1)*100,1) if d[2021]>0 and d[2025]>0 else 'n/a')
avgB=sum(B.values())/5; s_hist=sum(acq.values())/sum(B.values())
print('acq share of capex-variant owner cash',round(s_hist,3))
sh=58.282434
def value(oc0,g,s,r,years=10):
    pv=0;oc=oc0
    for t in range(1,years+1):
        oc*=1+g; pv+=oc*(1-s)/(1+r)**t
    pv+=oc/r/(1+r)**years
    return pv
def irr(price,oc0,g,s):
    lo,hi=0.0001,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if value(oc0,g,s,m)>price: lo=m
        else: hi=m
    return m
def price_at(rate,oc0,g,s): return value(oc0,g,s,rate)
rf=0.0563; P=173.25
cases={'no growth':(0,0),'central g10 s0.5':(0.10,0.5),'shown g14.5 s0.71':(0.145,s_hist)}
for k,(g,s) in cases.items():
    v=value(avgB,g,s,rf)
    print(f'{k}: value at sovereign ${v:,.0f}M = ${v/sh:,.2f}/sh ; IRR at ${P}: {irr(P*sh,avgB,g,s)*100:.2f}% ; price for 10%: ${price_at(0.10,avgB,g,s)/sh:,.2f} ; price for 15%: ${price_at(0.15,avgB,g,s)/sh:,.2f}')
