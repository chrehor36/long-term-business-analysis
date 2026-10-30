import re,json
blocks=re.split(r'\n== ',open('cf_blocks.txt',encoding='utf-8').read())
NUM=r'(\(?\s?[\d,]+\s?\)?|—|-)'
labs={
 'ocf':r'Net cash provided by operating activities(?: from continuing operations)? ',
 'sbc':r'(?<!from )(?:Share|Stock)-based compensation(?: expense)? ',
 'dep':r' Depreciation ',
 'amo':r' Amortization ',
 'capex':r'Purchased property, plant and equipment ',
 'ppe_sale':r'Proceeds from (?:the )?sales? of property, plant and equipment ',
 'acq':r'Purchased business(?:es)?, net of cash acquired ',
 'div':r'Dividends paid ',
 'rep':r'Repurchases? of common stock ',
 'opt':r'Proceeds from stock options exercised ',
}
def val(t):
    t=t.strip()
    if t in ('—','-'): return 0.0
    neg=t.startswith('(')
    v=float(re.sub(r'[^\d]','',t))
    return -v if neg else v
res={}
for b in blocks:
    m=re.match(r'=?=? ?tenk_(\d{4})',b)
    if not m: continue
    y=int(m.group(1))
    r={}
    for k,l in labs.items():
        mm=re.search(l+NUM,b)
        r[k]=val(mm.group(1))/1000 if mm else None
    res[y]=r
    print(y,r)
json.dump(res,open('cf_parsed.json','w'),indent=1)
