import re, sys
sys.stdout.reconfigure(encoding='utf-8')
for y in range(2013, 2026):
    try: s=open(f'cache/t{y}.txt',encoding='utf-8').read()
    except: continue
    # only MD&A roughly: from 'Results of Operations' to 'Liquidity'
    sents=re.split(r'(?<=[.;])\s+', s)
    hits=[x for x in sents if re.search(r'(?i)\b(pric(e|es|ing)|price erosion|discount)', x) and re.search(r'(?i)margin|gross profit|net sales|organic', x) and len(x)<900]
    print('=====', y, len(hits))
    seen=set()
    for h in hits:
        h=re.sub(r'\s+',' ',h).strip()
        if h in seen: continue
        seen.add(h); print(' -', h[:700])
