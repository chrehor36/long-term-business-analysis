"""PG competitor row: GAAP operating margin and pre-tax operating return on average NTOA (definition in peer_metrics.py,
unchanged from the CL run). Companyfacts fetched 2026-09-25. ARITHMETIC ONLY, NO CONCLUSION.
PG FY2012-FY2016 sales read from SalesRevenueNet because the 'Revenues' tag carries a non-total figure in those years."""
import json, peer_metrics as pm
from statistics import mean
out=[]
def rows(tk, yrs):
    r=dict(pm.metrics(tk, yrs)); return r
PGF=pm.load('PG')
sn=pm.first(PGF,['SalesRevenueNet'])
res={}
for tk,yrs in [('PG',range(2015,2027)),('CL',range(2015,2026)),('KMB',range(2015,2026)),('CHD',range(2015,2026)),('KVUE',range(2022,2026)),('EPC',range(2018,2026)),('EL',range(2015,2027)),('COTY',range(2016,2027))]:
    r=rows(tk,list(yrs))
    if tk=='PG':
        for y,m in r.items():
            if m and y<=2016 and y in sn:
                m['sales']=sn[y]/1e6; m['om']=m['op']/m['sales']
    res[tk]={y:m for y,m in r.items() if m and m.get('om') is not None and m.get('ret') is not None}
imp={2019:8345,2024:1341}  # PG filed impairment charges in operating income (FY2019 10-K, FY2026 10-K statements)
for tk,r in res.items():
    ys=sorted(r)
    line=f"{tk}: "+" ".join(f"{y}:{r[y]['om']*100:.1f}/{r[y]['ret']*100:.1f}" for y in ys)
    out.append(line)
def span(tk,a,b):
    r=res[tk]; ys=[y for y in range(a,b+1) if y in r]
    return ys, mean(r[y]['om'] for y in ys)*100, mean(r[y]['ret'] for y in ys)*100
out.append('')
for tk,(a5,b5),(a10,b10) in [('PG',(2022,2026),(2017,2026)),('CL',(2021,2025),(2016,2025)),('KMB',(2021,2025),(2016,2025)),('CHD',(2021,2025),(2016,2025)),('KVUE',(2023,2025),(2023,2025)),('EPC',(2021,2025),(2019,2025)),('EL',(2022,2026),(2017,2026)),('COTY',(2022,2026),(2017,2026))]:
    y5,o5,r5=span(tk,a5,b5); y10,o10,r10=span(tk,a10,b10)
    out.append(f"{tk} | 5y {y5[0]}-{y5[-1]} ({len(y5)}) om {o5:.1f} ret {r5:.1f} | long {y10[0]}-{y10[-1]} ({len(y10)}) om {o10:.1f} ret {r10:.1f}")
# PG ex-impairment
r=res['PG']
for y,c in imp.items():
    m=r[y]; op=m['op']+c
    # avg ntoa implied
    avg=m['op']/m['ret']
    out.append(f"PG {y} ex-impairment: op {op:,.0f} om {op/m['sales']*100:.1f} ret {op/avg*100:.1f}")
ex={y:(r[y]['op']+imp.get(y,0))/(r[y]['op']/r[y]['ret']) for y in r}
exo={y:(r[y]['op']+imp.get(y,0))/r[y]['sales'] for y in r}
for a,b in [(2022,2026),(2017,2026)]:
    ys=[y for y in range(a,b+1) if y in r]
    out.append(f"PG ex-impairment {a}-{b}: om {mean(exo[y] for y in ys)*100:.1f} ret {mean(ex[y] for y in ys)*100:.1f}")
open('row_out.txt','w').write('\n'.join(out)); print('\n'.join(out))
