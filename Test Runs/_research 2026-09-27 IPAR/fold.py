import re
p = '../../Screens/WATCHLIST RUN QUEUE.md'
L = open(p, encoding='utf-8').read().split('\n')
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
assert len(h) == 1, h
entry = open('register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
assert L[h[0] + 1].startswith('- **MEDP'), L[h[0] + 1][:40]
L = L[:h[0] + 1] + entry + L[h[0] + 1:]
open(p, 'w', encoding='utf-8').write('\n'.join(L))
# verify
L = open(p, encoding='utf-8').read().split('\n')
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
w = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(h) == 1 and len(w) == 1
ent = [l for l in L[h[0] + 1:w[0]] if re.match(r'^- \*\*[A-Z0-9]', l)]
print('entries', len(ent), 'first', ent[0][:40], 'second', ent[1][:40], 'IPAR count', sum(1 for l in ent if l.startswith('- **IPAR')))
