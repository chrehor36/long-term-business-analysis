import re
p='Screens/WATCHLIST RUN QUEUE.md'
t=open(p,encoding='utf-8').read()
nl='\r\n' if '\r\n' in t else '\n'
L=t.split(nl)
def count(L):
    h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']; w=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(h)==1 and len(w)==1, (h,w)
    sl=L[h[0]+1:w[0]]
    ent=[l for l in sl if re.match(r'^- \*\*',l)]
    return h[0],ent
h,ent=count(L); before=len(ent)
assert not any(e.startswith('- **KEX ') for e in ent)
new=open('Test Runs/_research 2026-09-26 KEX/_reg_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:h+1]+new+L[h+1:]
h2,ent2=count(L)
print('heading line',h+1,'before',before,'after',len(ent2),'first',ent2[0][:40], 'KEX count',sum(1 for e in ent2 if e.startswith('- **KEX ')))
open(p,'w',encoding='utf-8',newline='').write(nl.join(L))
