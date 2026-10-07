import re
p='Screens/WATCHLIST RUN QUEUE.md'
raw=open(p,encoding='utf-8',newline='').read()
nl='\r\n' if '\r\n' in raw else '\n'
L=raw.split(nl)
h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']
assert len(h)==1, h
def count(L):
    h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE'][0]
    w=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')][0]
    ent=[l for l in L[h+1:w] if re.match(r'^- \*\*',l)]
    return len(ent), ent[0][:40], sum(1 for l in ent if l.startswith('- **PLUS ('))
before=count(L)
entry=open('Test Runs/_research 2026-09-28 PLUS/register_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:h[0]+1]+entry+L[h[0]+1:]
open(p,'w',encoding='utf-8',newline='').write(nl.join(L))
L2=open(p,encoding='utf-8',newline='').read().split(nl)
print('heading line', h[0]+1, 'before', before, 'after', count(L2))
