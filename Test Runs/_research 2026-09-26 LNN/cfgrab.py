import re
def num(s):
    s=s.replace(',','').replace(' ','')
    neg=s.startswith('(')
    v=float(s.strip('()'))
    return -v if neg else v
N=r'(\(? ?[\d,]+ ?\)?|—)'
lines={'OCF':r'Net cash provided by operating activities','CAPEX':r'Purchases of property,? plant,? and equipment','SBC':r'Share-based compensation expense','DA':r'Depreciation and amortization'}
res={}
for fy in range(2012,2026):
    t=open(f'tenk_FY{fy}.txt',encoding='utf-8').read(); t=re.sub(r'[\s|​\xa0]+',' ',t)
    k=[m.start() for m in re.finditer(r'CASH FLOWS FROM OPERATING ACTIVITIES',t,re.I)]
    k=[x for x in k if 'Net earnings' in t[x:x+200]][0]
    seg=t[k:k+5000]
    row={}
    for key,pat in lines.items():
        m=re.search(pat+r' \$? ?'+N+r' \$? ?'+N+r' \$? ?'+N,seg)
        row[key]=[0.0 if x=='—' else num(x) for x in m.groups()] if m else None
    for i,y in enumerate((fy,fy-1,fy-2)):
        res[(y,fy)]={k:(v[i] if v else None) for k,v in row.items()}
    print(fy,row)
import json
json.dump({f'{y}|{fy}':v for (y,fy),v in res.items()},open('cf_parsed.json','w'),indent=0)
