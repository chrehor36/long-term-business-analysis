import re,sys
for fy in sys.argv[1:]:
    t=open(f'tenk_{fy}.txt',encoding='utf-8').read()
    ms=[m.start() for m in re.finditer(r'(?i)cash flows? from operating activities|operating activities:',t)]
    best=None
    for s in ms:
        w=t[s:s+4000]
        if re.search(r'(?i)net income',w) and re.search(r'(?i)depreciation',w) and re.search(r'(?i)share-based|stock-based',w):
            best=s;break
    seg=t[best-300:best+9000]
    seg=re.sub(r'\s*\|\s*',' ',seg); seg=re.sub(r'\$\s*','',seg); seg=re.sub(r'\s+',' ',seg)
    open(f'cf_{fy}_flat.txt','w',encoding='utf-8').write(seg)
    print('=====',fy); print(seg[:5200]); print()
