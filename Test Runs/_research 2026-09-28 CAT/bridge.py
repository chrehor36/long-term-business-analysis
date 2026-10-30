import re,sys
sys.stdout.reconfigure(encoding='utf-8')
for y in range(2016,2026):
    t=open(f'cache/k_{y}.txt',encoding='utf-8').read()
    t=re.sub(r'[\s|]+',' ',t)
    print('=====',y)
    for m in re.finditer(r'Sales Volume Price Realization Currency',t):
        seg=t[max(0,m.start()-120):m.end()+700]
        if 'Quarter' in seg[:200]: continue
        print('  ',seg[:820]); print()
