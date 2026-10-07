import json,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
d={int(k):v for k,v in json.load(open('cf_text.json')).items()}
d[1991].update({'ocf':20.739})
CAP=7038.99; SOV=5.49
rows={}
for y in range(1991,2026):
    r=d[y]; ocf=r['ocf']; capex=-r['capex']; da=r['da']; sbc=r.get('sbc',0.0)
    leg=r.get('plp',0)+r.get('ins',0)+r.get('contr',0)  # legacy cash flows filed separately (negative = outflow)
    rows[y]=dict(ocf=ocf,sbc=sbc,capex=capex,da=da,leg=leg,
        oe_cap=ocf-sbc-capex, oe_da=ocf-sbc-da, oex_cap=ocf-leg-sbc-capex, oex_da=ocf-leg-sbc-da)
print('FY | OCF | SBC | capex | D&A | legacy PL cash | OE capex end | OE D&A end | ex-legacy capex | ex-legacy D&A')
for y,r in rows.items():
    print(y,' | '.join(f"{r[k]:.1f}" for k in ['ocf','sbc','capex','da','leg','oe_cap','oe_da','oex_cap','oex_da']))
ttm=dict(ocf=363.867+171.063-129.051,sbc=15.197+11.621-7.999,capex=68.438+23.260-40.118,da=71.591+37.674-34.350)
ttm['oe_cap']=ttm['ocf']-ttm['sbc']-ttm['capex']; ttm['oe_da']=ttm['ocf']-ttm['sbc']-ttm['da']
print('TTM',{k:round(v,1) for k,v in ttm.items()})
print('\nwindow | capex end | D&A end | ex-legacy capex | ex-legacy D&A   (pct of cap %.1f)'%CAP)
W={}
for n in range(1,36):
    ys=range(2026-n,2026)
    m={k:sum(rows[y][k] for y in ys)/n for k in ['oe_cap','oe_da','oex_cap','oex_da']}
    W[n]=m
    print(f"{n}y FY{2026-n}-25 | "+' | '.join(f"${m[k]:.1f}M ({m[k]/CAP*100:.2f}%)" for k in ['oe_cap','oe_da','oex_cap','oex_da']))
allv=[v for n in W for k,v in W[n].items() if k in('oe_cap','oe_da')]
allx=[v for n in W for k,v in W[n].items()]
print('as filed range',round(min(allv),1),round(max(allv),1),'; incl ex-legacy',round(min(allx),1),round(max(allx),1))
neg=[y for y,r in rows.items() if r['oe_cap']<0 or r['oe_da']<0]; print('negative years',neg)
# rolling five-year
for e in range(1995,2026,5):
    ys=range(e-4,e+1); print('5y ending',e, round(sum(rows[y]['oe_cap'] for y in ys)/5,1), round(sum(rows[y]['oe_da'] for y in ys)/5,1))
json.dump({'rows':rows,'ttm':ttm},open('oe_rows.json','w'),indent=0)
