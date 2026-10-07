import re,sys
for fy in sys.argv[1:]:
    t=open(f'tenk_{fy}.txt',encoding='utf-8').read()
    # find cash flow statement: the occurrence of 'OPERATING ACTIVITIES' followed within 600 chars by 'Net income'
    ms=[m.start() for m in re.finditer(r'(?i)operating activities',t)]
    best=None
    for s in ms:
        seg=t[s:s+800]
        if re.search(r'(?i)net income',seg) and re.search(r'(?i)depreciation',t[s:s+3000]):
            best=s;break
    seg=t[best-600:best+14000]
    seg=re.sub(r'\s*\|\s*',' ',seg); seg=re.sub(r'\$\s*','',seg); seg=re.sub(r'\s+',' ',seg)
    open(f'cf_{fy}_flat.txt','w',encoding='utf-8').write(seg)
    print('=====',fy); print(seg[:7000]); print()
