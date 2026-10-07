import re,json
def toks_rows(seg):
    toks=[t.strip() for t in re.split(r'[|\n]',seg)]
    rows=[];cur=None
    for t in toks:
        if not t or t in ('$',')'): continue
        t2=t.replace('$','').strip()
        m=re.fullmatch(r'\(?\s*([\d,]+(\.\d+)?)\s*\)?',t2)
        if m and cur is not None:
            v=float(m.group(1).replace(',',''))
            if t2.startswith('('): v=-v
            cur[1].append(v)
        elif t2 in ('—','-','–'):
            if cur is not None: cur[1].append(0)
        elif re.search(r'[A-Za-z]',t2):
            if cur and not cur[1]: cur=(cur[0]+' '+t2,cur[1]); rows[-1]=cur
            else: cur=(t2,[]); rows.append(cur)
    return rows
res={}
for fy in range(2006,2026):
    s=open(f'tenk_FY{fy}.txt',encoding='utf-8').read()
    best=None
    for m in re.finditer(r'(?i)consolidated statements? of (operations|income)',s):
        seg=s[m.start():m.start()+9000]
        if re.search(r'(?i)net sales',seg[:3000]) and re.search(r'(?i)cost of',seg[:5000]):
            best=seg;break
    rows=toks_rows(best)
    r={}
    for l,v in rows:
        L=l.lower()
        if not v: continue
        for k,p in [('sales',r'total (net )?sales|^net sales$|total net revenue'),('products',r'^products'),('tooling',r'^tooling'),('cogs',r'cost of'),('gm',r'gross margin|gross profit'),('sga',r'selling, general'),('oi',r'(income|loss).*from operations|operating (income|loss)')]:
            if k not in r and re.search(p,L): r[k]=v
    res[fy]=r
    print(fy,{k:v[:3] for k,v in r.items()})
json.dump(res,open('is_parsed.json','w'),indent=0)
