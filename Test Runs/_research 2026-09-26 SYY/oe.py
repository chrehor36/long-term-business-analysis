import json
cf=json.load(open('cf_parsed.json'))
Y={}
for k10,base in [('2011',2011),('2014',2014),('2017',2017),('2020',2020),('2023',2023),('2026',2026)]:
    r=cf[k10]
    for j in range(3):
        y=base-j
        Y[y]={k:(v[j] if v else None) for k,v in r.items()}
amort={2009:15.7,2010:20.9,2011:21.9,2012:24.9,2013:32.1,2014:42.2,2015:40.0,2016:37.3,2017:112.9,2018:114.7,2019:92.3,2020:95.3,2021:103.5,2022:132.9,2023:126.3,2024:142,2025:147,2026:154}
flease={2020:17.0,2021:8.7,2022:191.5,2023:114.1,2024:115,2025:202,2026:55}
CAP=38558.5
rows=[]
print('FY | OCF | SBC | D&A | amort | D&A ex-amort | capex gross | proceeds | fin-lease adds | WC five lines | OE D&A end | OE capex end | OE capex end, WC stripped')
for y in range(2009,2027):
    d=Y[y]; ocf=d['ocf']; sbc=d['sbc']; da=d['da']; cx=-d['capex']; pr=d['proc']
    wc=sum(d[k] for k in ['rec','inv','pre','ap','acc'])
    fl=flease.get(y,0.0)
    oe_da=ocf-sbc-(da-amort[y]); oe_cx=ocf-sbc-cx-fl; oe_cx_s=oe_cx-wc
    rows.append((y,oe_da,oe_cx,oe_cx_s,ocf,wc))
    print(f"{y} | {ocf:,.1f} | {sbc:.1f} | {da:.1f} | {amort[y]:.1f} | {da-amort[y]:.1f} | {cx:.1f} | {pr:.1f} | {fl:.1f} | {wc:,.1f} | {oe_da:,.1f} | {oe_cx:,.1f} | {oe_cx_s:,.1f}")
print()
print('window | capex end | D&A end | yield capex | yield D&A | capex end WC-stripped')
res=[]
for n in range(3,19):
    w=[r for r in rows if r[0]>2026-n]
    a=sum(r[2] for r in w)/n; b=sum(r[1] for r in w)/n; c=sum(r[3] for r in w)/n
    res.append((n,a,b,c))
    print(f"{n}y FY{2027-n}-26 | {a:,.1f} | {b:,.1f} | {100*a/CAP:.2f}% | {100*b/CAP:.2f}% | {c:,.1f}")
lo=min(min(x[1],x[2]) for x in res); hi=max(max(x[1],x[2]) for x in res)
print('range all windows both ends', round(lo,1), round(hi,1), f"{100*lo/CAP:.2f}%-{100*hi/CAP:.2f}%")
# excluding pandemic
w=[r for r in rows if r[0] not in (2020,2021)]
print('18y ex FY2020-21 capex end', round(sum(r[2] for r in w)/len(w),1))
print('SBC share of OCF 18y', round(100*sum(Y[y]['sbc'] for y in Y)/sum(Y[y]['ocf'] for y in Y),1))
