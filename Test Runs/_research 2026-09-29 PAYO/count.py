import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
L = open('Screens/WATCHLIST RUN QUEUE.md', encoding='utf-8').read().split('\n')
h = [i for i, x in enumerate(L) if x == '## COMPLETED FROM THE QUEUE']
w = [i for i, x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(h) == 1 and len(w) == 1, (h, w)
ent = [i for i in range(h[0]+1, w[0]) if L[i].startswith('- **')]
print('heading line', h[0]+1, 'write-early line', w[0]+1, 'entries', len(ent))
for i in ent[:3]: print('  ', i+1, L[i][:70])
print('PAYO entries:', [i+1 for i in ent if L[i].startswith('- **PAYO')])
print('PAYO mentions anywhere:', [i+1 for i, x in enumerate(L) if re.search(r'\bPAYO\b', x)])
