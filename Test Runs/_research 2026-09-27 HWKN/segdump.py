import re,sys
sys.stdout.reconfigure(encoding='utf-8')
for y in range(2004,2027):
    try: t=open(f'cache/tenk_{y}.txt',encoding='utf-8').read()
    except: continue
    idx=[m.start() for m in re.finditer(r'(?i)identifiable assets',t)]
    if not idx: print('=====',y,'none'); continue
    i=idx[0]
    j=t.rfind('Reportable Segments',0,i)
    if j<0 or i-j>6000: j=i-3000
    seg=t[j:i+1600]
    seg=re.sub(r'[\s|$]+',' ',seg)
    print('=====',y)
    print(seg)
