import sys,re
sys.stdout.reconfigure(encoding="utf-8")
f=sys.argv[1]; pat=re.compile(sys.argv[2],re.I); w=int(sys.argv[3]) if len(sys.argv)>3 else 220
s=open(f,encoding='utf-8').read()
seen=set()
for m in pat.finditer(s):
    a=max(0,m.start()-w); b=min(len(s),m.end()+w)
    key=a//400
    if key in seen: continue
    seen.add(key)
    print('...'+s[a:b].replace('\n',' ')+'...\n')
