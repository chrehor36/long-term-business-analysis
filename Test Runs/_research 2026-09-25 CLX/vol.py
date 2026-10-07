import re,glob,sys
fs=sorted(glob.glob('CLX_10K_FY20*'))
fs=[f for f in fs if ('EX991' in f or 'ex991' in f or 'exhibit99-1' in f or 'ex99110k' in f)]
for f in fs:
    t=re.sub(r'\s+',' ',open(f,encoding='utf-8').read())
    sents=re.split(r'(?<=\.)\s',t)
    hits=[s for s in sents if re.search(r'\b[Vv]olume (increased|decreased|was|grew|declined)',s)][:3]
    print('===',f)
    for h in hits: print('  -',h[:500])
