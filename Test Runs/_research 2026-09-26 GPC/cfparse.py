import re,json
L={'ocf':r'Net cash provided by operating activities',
   'da':r'Depreciation and amortization',
   'sbc':r'(?:Share-based compensation|Stock-based compensation|Share based compensation)',
   'capex':r'Purchases of property,? plant,? and equipment',
   'disp':r'Proceeds from sale of property,? plant,? and equipment',
   'acq':r'Acquisitions? of businesses(?:, net of cash acquired)?',
   'intpaid':r'Interest',
   'tax':r'Income taxes'}
num=r'\(?\s*-?[\d,]+(?:\.\d+)?\s*\)?|—|-'
def val(t):
    t=t.strip()
    if t in ('—','-'): return 0.0
    neg=t.startswith('(')
    v=float(re.sub(r'[^\d.]','',t))
    return -v if neg else v
out={}
for y in range(2006,2026):
    try: s=open(f'tenk_{y}-12-31.txt',encoding='utf-8').read()
    except: continue
    s=re.sub(r'[\s|$]+',' ',s)
    i=[m.start() for m in re.finditer(r'(?i)cash flows? from operating activities|Operating activities:',s)]
    # choose the statement: position where 'Net cash provided by operating activities' followed by 3 numbers and near 'Investing'
    best=None
    for m in re.finditer(r'Net cash provided by operating activities ((?:(?:%s) ){3})'%num,s):
        best=m
        break
    if not best: print(y,'no ocf'); continue
    st=s.rfind('perating activities',0,best.start()-50)
    blk=s[max(0,best.start()-6000):best.start()+6000]
    r={}
    for k,p in L.items():
        mm=re.search(p+r' ((?:(?:%s) ){3})'%num,blk)
        if mm:
            vals=re.findall(num,mm.group(1)); r[k]=[val(v) for v in vals[:3]]
    out[y]=r
    print(y,{k:v[0] for k,v in r.items()})
json.dump(out,open('cf_raw.json','w'),indent=0)
