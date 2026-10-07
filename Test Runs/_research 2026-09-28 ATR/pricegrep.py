import re,glob,sys
sys.stdout.reconfigure(encoding='utf-8')
pats=sys.argv[1]; n=int(sys.argv[2]); files=sorted(glob.glob('cache/k_*.txt'))
pat=re.compile(pats,re.I)
for p in files:
    s=re.sub(r'\s*\|\s*',' ',open(p,encoding='utf-8').read()); s=re.sub(r'\s+',' ',s)
    seen=set(); c=0
    for x in re.split(r'(?<=[.!?])\s+',s):
        if pat.search(x) and x not in seen and len(x)<1500:
            seen.add(x); print(p[8:12],'|',x[:900]); c+=1
            if c>=n: break
