import sys,re
f=sys.argv[1]; pats=sys.argv[2:]
s=open(f,encoding='utf-8',errors='replace').read()
s=re.sub(r'\s*\|\s*',' | ',s); s=re.sub(r'\s+',' ',s)
for p in pats:
    for m in list(re.finditer(p,s,re.I))[:3]:
        print('>>',p,':',s[max(0,m.start()-300):m.start()+1500]); print()
