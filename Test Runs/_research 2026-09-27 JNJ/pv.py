import re,sys
sys.stdout.reconfigure(encoding='utf-8')
for y in range(2015,2026):
    t=open(f'cache/tenk_{y}.txt',encoding='utf-8').read()
    i=t.find('These sales changes consisted of the following')
    if i<0:
        i=t.find('Sales increase/(decrease) due to')
    if i<0: print(y,'NOT FOUND'); continue
    seg=t[i:i+1500]
    seg=re.sub(r'[|\n]+',' ',seg); seg=re.sub(r'\s+',' ',seg)
    j=seg.find('Total')
    print(y, seg[:j+40])
