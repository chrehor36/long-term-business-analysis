import glob,re,sys
pat=re.compile(sys.argv[1],re.I)
fs=sorted(glob.glob(sys.argv[2] if len(sys.argv)>2 else 'filings/*_10-K_*.txt'))
seen=set()
for f in fs:
    t=open(f,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'\s+',' ',t)
    for s in re.split(r'(?<=[.;])\s+(?=[A-Z])',t):
        if pat.search(s) and len(s)<1500:
            k=s[:200]
            if k in seen: continue
            seen.add(k); print(f[8:18],'|',s.strip())
