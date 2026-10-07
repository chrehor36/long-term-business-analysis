import re
Q = '../../Screens/WATCHLIST RUN QUEUE.md'
raw = open(Q, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl)
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
assert len(h) == 1, h
w = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
def count(L):
    s = L[h[0] + 1:[i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')][0]]
    return [l for l in s if re.match(r'^- \*\*[A-Z0-9.\-]+ \(', l)]
before = count(L)
assert not any(e.startswith('- **CW (') for e in before)
entry = open('register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h[0] + 1] + entry + L[h[0] + 1:]
after = count(L)
print('line', h[0] + 1, 'before', len(before), 'after', len(after), 'first', after[0][:40], 'second', after[1][:40], 'CW count', sum(e.startswith('- **CW (') for e in after))
open(Q, 'w', encoding='utf-8', newline='').write(nl.join(L))
# done file
D = '../../Screens/_daily/_wave7_done.txt'
d = open(D, encoding='utf-8', newline='').read()
assert d.endswith('\r\n') and 'CW\r\n' not in d
open(D, 'w', encoding='utf-8', newline='').write(d + 'CW\r\n')
dl = open(D).read().split()
ol = open('../../Screens/_daily/_wave7_order.txt').read().split()
print('done lines', len(dl), 'last', dl[-1], 'equals order first', dl == ol[:len(dl)], 'next', ol[len(dl)])
