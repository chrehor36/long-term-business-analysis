import re
for fy in list(range(2010,2020))+[2025]:
    s=open(f'10-K_FY{fy}.txt',encoding='utf-8').read().replace('\n',' ')
    sents=re.split(r'(?<=[.;])\s+',s)
    hits=[x for x in sents if re.search(r'(?i)price (reduction|decrease|increase|erosion|down)|pricing|selling price',x) and re.search(r'(?i)\d+(\.\d+)?\s*%|revenue',x) and len(x)<800 and not re.search(r'(?i)transaction price|Monte Carlo|option|risk factor',x)]
    seen=set(); print('=====',fy)
    for h in hits:
        k=h[:120]
        if k in seen: continue
        seen.add(k); print(' -',h.strip()[:700])
