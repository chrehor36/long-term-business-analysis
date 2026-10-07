import re,sys
sys.stdout.reconfigure(encoding='utf-8')
for y in range(2014,2026):
    t=open(f'cache/tenk_{y}.txt',encoding='utf-8').read()
    i=t.find('Executive Summary')
    seg=t[i:i+6000]
    sents=re.split(r'(?<=\.)\s+(?=[A-Z])',seg)
    print('=====',y)
    for s in sents[:12]:
        if re.search(r'net sales|volume|price',s,re.I): print(' *',s.strip()[:700])
