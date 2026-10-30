import re
L = open('../../Screens/WATCHLIST RUN QUEUE.md', encoding='utf-8').read().split('\n')
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
w = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(h) == 1 and len(w) == 1, (h, w)
sl = L[h[0] + 1:w[0]]
ent = [l for l in sl if re.match(r'^- \*\*[A-Z0-9]', l)]
print('heading line', h[0] + 1, 'write-early line', w[0] + 1, 'entries', len(ent))
print('first', ent[0][:90])
print('second', ent[1][:90])
ip = [l[:80] for l in ent if l.startswith('- **IPAR')]
print('IPAR entries', len(ip), ip)
