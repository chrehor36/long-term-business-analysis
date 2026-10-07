import re,glob,sys
sys.stdout.reconfigure(encoding='utf-8')
for f in sorted(glob.glob('cache/tenk_20*.txt')):
    s=open(f,encoding='utf-8').read()
    sents=re.split(r'(?<=[.;])\s+',s)
    hits=[x for x in sents if re.search(r'operating ratio (was|of) \d',x,re.I) or re.search(r'operating (income|loss) of \$',x,re.I) and re.search(r'ABF|Asset-Based|LTL',x)]
    print('=====',f)
    seen=set()
    for h in hits[:8]:
        h=re.sub(r'\s+',' ',h)[:500]
        if h in seen: continue
        seen.add(h); print(' -',h)
