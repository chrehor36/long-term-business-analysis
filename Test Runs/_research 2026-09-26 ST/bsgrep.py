import re
def norm(s):
    s=s.replace('\n',' ')
    s=re.sub(r'\(\s*([\d,\.]+)\s*\|?\s*\)',r'(\1)',s)
    return re.sub(r'[|\s$]+',' ',s)
def num(x):
    x=x.strip(); neg=x.startswith('(')
    try: v=float(x.strip('()').replace(',',''))
    except: return None
    return -v if neg else v
def two(seg,label,k=2):
    m=re.search(label,seg)
    if not m: return None
    toks=re.findall(r'\([\d,\.]+\)|[\d,]+\.?\d*|—',seg[m.end():m.end()+120])
    out=[]
    for t in toks:
        if t=='—': out.append(0.0)
        else:
            v=num(t)
            if v is not None: out.append(v)
        if len(out)==k: break
    return out
res={}
for fy in range(2010,2026):
    s=norm(open(f'10-K_FY{fy}.txt',encoding='utf-8').read())
    bs=None
    for m in re.finditer(r'Consolidated Balance Sheets',s):
        if 'Total current assets' in s[m.start():m.start()+3000]: bs=s[m.start():m.start()+6000]; break
    ist=None
    for m in re.finditer(r'Consolidated Statements of Operations',s):
        if 'Cost of revenue' in s[m.start():m.start()+2500]: ist=s[m.start():m.start()+5000]; break
    sc=1000 if fy<=2024 and fy>=2010 and ('Thousands' in (bs or '')[:300] or 'thousands' in (bs or '')[:300]) else 1
    r={'scale':sc}
    for k,L in [('ppe',r'Property, plant and equipment, net'),('ar',r'Accounts receivable, net( of allowances[^0-9]*[\d\.,]+ and [\d\.,]+( as of [A-Za-z0-9 ,]+?respectively)?)?'),('inv',r'Inventories'),('ap',r'Accounts payable'),('gw',r'Goodwill'),('intg',r'Other intangible assets, net( of accumulated amortization[^0-9]*[\d\.,]+ and [\d\.,]+( as of [A-Za-z0-9 ,]+?respectively)?)?'),('eq',r"Total (shareholders|stockholders)['’]? equity")]:
        r[k]=two(bs or '',L)
    for k,L in [('rev',r'Net revenue'),('cor',r'Cost of revenue'),('amort',r'Amortization of intangible assets'),('imp',r'(Goodwill impairment charge|Impairment of goodwill[^0-9(—]*)'),('restr',r'Restructuring and other charges, net|Restructuring and special charges|Restructuring( and other)? charges'),('opinc',r'Operating income( \(loss\))?|Operating income/\(loss\)')]:
        r[k]=two(ist or '',L,3)
    res[fy]=r
    print(fy,r)
import json; json.dump(res,open('bs_is.json','w'))
