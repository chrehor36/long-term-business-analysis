import re,glob
for fy in range(2010,2026):
    s=open(f'10-K_FY{fy}.txt',encoding='utf-8').read()
    a=[m.start() for m in re.finditer(r'(?i)ITEM\s*7\.\s*MANAGEMENT',s)]
    b=[m.start() for m in re.finditer(r'(?i)ITEM\s*7A\.',s)]
    if not a: print(fy,'no mdna'); continue
    md=s[a[-1]:(b[-1] if b and b[-1]>a[-1] else a[-1]+150000)]
    sents=re.split(r'(?<=[.;])\s+',md.replace('\n',' '))
    hits=[x for x in sents if re.search(r'(?i)pric(e|ing)',x) and re.search(r'(?i)revenue|decline|increase|reduction|margin|inflation|customer',x) and len(x)<700]
    print('=====',fy,len(md))
    for h in hits[:14]: print(' -',h.strip()[:600])
