import re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
fn=sys.argv[1]; pat=sys.argv[2]
s=re.sub(r'\s+',' ',open(fn,encoding='utf-8').read())
seen=set()
for m in re.finditer(pat,s):
    k=s[max(0,m.start()-300):m.start()]
    if k in seen: continue
    seen.add(k); print('-',s[max(0,m.start()-450):m.start()+300],'\n')
