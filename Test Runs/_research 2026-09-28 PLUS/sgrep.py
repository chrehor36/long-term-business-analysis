import re,sys
sys.stdout.reconfigure(encoding='utf-8')
pat=re.compile(sys.argv[1],re.I); n=int(sys.argv[2]) if len(sys.argv)>2 else 10
for p in sys.argv[3:]:
    s=re.sub(r'\s*\|\s*',' ',open(p,encoding='utf-8').read()); s=re.sub(r'\s+',' ',s)
    seen=set(); c=0
    for x in re.split(r'(?<=[.!?])\s+',s):
        if pat.search(x) and x not in seen:
            seen.add(x); print(p.split('/')[-1][:14],'|',x[:700]); c+=1
            if c>=n: break
