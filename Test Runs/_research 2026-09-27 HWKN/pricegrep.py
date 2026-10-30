import re,sys
sys.stdout.reconfigure(encoding='utf-8')
for y in range(2004,2027):
    try: t=open(f'cache/tenk_{y}.txt',encoding='utf-8').read()
    except: continue
    t=re.sub(r'\s+',' ',t)
    i=t.find('MANAGEMENT’S DISCUSSION'); i=t.find('MANAGEMENT’S DISCUSSION',i+100) if t.find('MANAGEMENT’S DISCUSSION',i+100)>0 else i
    if i<0: i=t.upper().find("MANAGEMENT'S DISCUSSION")
    seg=t[i:i+60000] if i>0 else t
    sents=re.split(r'(?<=[.;])\s+(?=[A-Z])',seg)
    print('=====',y)
    seen=set()
    for s in sents:
        if re.search(r'selling price|pricing|price increase|prices|competitive|pass',s,re.I) and len(s)<900 and s not in seen:
            seen.add(s); print(' *',s.strip())
