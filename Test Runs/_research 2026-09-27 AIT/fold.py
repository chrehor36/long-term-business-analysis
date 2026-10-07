import re
base = r'C:\Users\chreh\OneDrive\Documents\BRK'
Q = base + r'\Screens\WATCHLIST RUN QUEUE.md'
E = base + r'\Test Runs\_research 2026-09-27 AIT\register_entry.md'
L = open(Q, encoding='utf-8').read().split('\n')
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
assert len(h) == 1, h
w = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(w) == 1
before = [l for l in L[h[0] + 1:w[0]] if l.startswith('- **')]
assert not any(l.startswith('- **AIT ') for l in before)
new = open(E, encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h[0] + 1] + new + L[h[0] + 1:]
open(Q, 'w', encoding='utf-8').write('\n'.join(L))
L2 = open(Q, encoding='utf-8').read().split('\n')
h2 = [i for i, l in enumerate(L2) if l == '## COMPLETED FROM THE QUEUE']
w2 = [i for i, l in enumerate(L2) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
after = [l for l in L2[h2[0] + 1:w2[0]] if l.startswith('- **')]
print('before', len(before), 'after', len(after), 'first', after[0][:40], 'AIT count', sum(1 for l in after if l.startswith('- **AIT ')), 'heading line', h2[0] + 1)
# done file
D = base + r'\Screens\_daily\_wave7_done.txt'
s = open(D, encoding='utf-8').read()
if not s.endswith('\n'): s += '\n'
lines = [x for x in s.split('\n') if x]
assert 'AIT' not in lines
open(D, 'w', encoding='utf-8', newline='\n').write(s + 'AIT\n')
d2 = [x for x in open(D, encoding='utf-8').read().split('\n') if x]
print('done file lines', len(d2), 'last', d2[-1])
