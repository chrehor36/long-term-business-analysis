import json
cf={int(k):v for k,v in json.load(open('cf_parsed.json')).items()}
amort={2015:8.5,2016:8.5,2017:11.3,2018:16.8,2019:15.0,2020:9.2,2021:7.8,2022:7.6,2023:8.1,2024:8.6,2025:8.7}  # AmortizationOfIntangibleAssets tag, $M
CAP=6804.9
rows={}
print('year | OCF | SBC | capex | proceeds | net capex | D&A | intangible amort | depreciation used | OE capex end | OE D&A end | acquisitions line | capex/dep')
for y in range(2006,2026):
    r=cf[y]; ocf=r['ocf']/1e3; sbc=r['sbc']/1e3; cap=-r['capex']/1e3; pr=r['proc']/1e3; da=r['da']/1e3; acq=-r.get('acq',0)/1e3
    am=amort.get(y,0.0); dep=da-am; net=cap-pr
    oec=ocf-sbc-net; oed=ocf-sbc-dep
    rows[y]=dict(oec=oec,oed=oed,net=net,dep=dep,acq=acq,ocf=ocf,sbc=sbc,da=da)
    print(y,'|',f'{ocf:.1f} | {sbc:.1f} | {cap:.1f} | {pr:.1f} | {net:.1f} | {da:.1f} | {am if am else "n/t"} | {dep:.1f} | {oec:.1f} | {oed:.1f} | {acq:.1f} | {net/dep:.2f}')
print()
print('window | capex end | D&A end | yield capex | yield D&A | capex/dep | capex end incl. acquisitions line')
res=[]
for n in range(3,21):
    ys=list(range(2026-n,2026))
    c=sum(rows[y]['oec'] for y in ys)/n; d=sum(rows[y]['oed'] for y in ys)/n
    ca=sum(rows[y]['oec']-rows[y]['acq'] for y in ys)/n
    ratio=sum(rows[y]['net'] for y in ys)/sum(rows[y]['dep'] for y in ys)
    res+= [c,d]
    print(f'{n}y {ys[0]}-{ys[-1]} | {c:.1f} | {d:.1f} | {c/CAP*100:.2f}% | {d/CAP*100:.2f}% | {ratio:.2f} | {ca:.1f}')
print('range',min(res),max(res), min(res)/CAP*100, max(res)/CAP*100)
# screen reproduction: D&A end with amortisation left in
for n in (3,5):
    ys=list(range(2026-n,2026))
    print('screen-style',n,'y capex end',sum(rows[y]['ocf']-rows[y]['sbc']-(-cf[y]['capex']/1e3) for y in ys)/n,
          'capex net',sum(rows[y]['oec'] for y in ys)/n,
          'D&A incl amort',sum(rows[y]['ocf']-rows[y]['sbc']-rows[y]['da'] for y in ys)/n)
print()
ref={2020:30.6,2021:119.5,2023:70.4}  # CARES-Act carryback refunds named in the 10-Ks (2021 incl. interest; 2023 excl. interest)
print('window | capex end, refunds stripped | D&A end, refunds stripped')
lo=[];
for n in range(3,21):
    ys=list(range(2026-n,2026))
    c=sum(rows[y]['oec']-ref.get(y,0) for y in ys)/n; d=sum(rows[y]['oed']-ref.get(y,0) for y in ys)/n
    lo+=[c,d]; print(f'{n}y | {c:.1f} | {d:.1f} | {c/CAP*100:.2f}% | {d/CAP*100:.2f}%')
print('stripped range',min(lo),max(lo))
