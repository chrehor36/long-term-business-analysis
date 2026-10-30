import re
L=open('Screens/WATCHLIST RUN QUEUE.md',encoding='utf-8').read().split('\n')
h=[i for i,l in enumerate(L) if l.rstrip('\r')=='## COMPLETED FROM THE QUEUE']
assert len(h)==1, h
e=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(e)==1
ents=[l for l in L[h[0]+1:e[0]] if l.startswith('- **')]
print('heading line', h[0]+1, 'end line', e[0]+1, 'entries', len(ents))
print('first', ents[0][:40]); print('second', ents[1][:40])
print('POWL entries', sum(1 for l in ents if l.startswith('- **POWL')))
print('POWL anywhere', [i+1 for i,l in enumerate(L) if 'POWL' in l])
