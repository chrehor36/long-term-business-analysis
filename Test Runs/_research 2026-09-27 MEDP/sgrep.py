import re, glob, sys
pat=re.compile(sys.argv[1], re.I); files=sys.argv[2] if len(sys.argv)>2 else 'filings/*_10-K_*'
seen={}
for f in sorted(glob.glob(files)):
    t=re.sub(r'\s+',' ',open(f,encoding='utf-8').read())
    sents=re.split(r'(?<=[.;])\s+(?=[A-Z•])',t)
    for s in sents:
        if pat.search(s) and len(s)<1500:
            k=s[:200]
            seen.setdefault(k,[s,[]])[1].append(f[8:18])
for k,(s,fs) in seen.items():
    print('[%s..%s x%d] %s'%(fs[0],fs[-1],len(fs),s[:900]))
