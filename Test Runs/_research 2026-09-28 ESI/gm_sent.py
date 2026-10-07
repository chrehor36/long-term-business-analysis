import re, sys
sys.stdout.reconfigure(encoding='utf-8')
for y in range(2016, 2026):
    s=open(f'cache/t{y}.txt',encoding='utf-8').read()
    sents=re.split(r'(?<=[.])\s+', s)
    print('=====', y)
    seen=set()
    for x in sents:
        x=re.sub(r'\s+',' ',x).strip()
        if re.search(r'(?i)(gross (profit|margin)|adjusted ebitda margin).{0,80}(increase|decrease|expan|contract|decline|improv)', x) and ('primarily' in x or 'driven' in x or 'due to' in x) and len(x)<1000 and x not in seen:
            seen.add(x); print(' -', x[:900])
