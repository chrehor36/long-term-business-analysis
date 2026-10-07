import re
T = 'EGAN'
Q = '../../Screens/WATCHLIST RUN QUEUE.md'
raw = open(Q, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl)
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
assert len(h) == 1, h
def count(L):
    e = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(e) == 1
    s = L[h[0] + 1:e[0]]
    return [l for l in s if re.match(r'^- \*\*[A-Z0-9.\-]+ \(', l)]
before = count(L)
assert not any(e.startswith('- **%s (' % T) for e in before)
entry = open('register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h[0] + 1] + entry + L[h[0] + 1:]
after = count(L)
print('heading line', h[0] + 1, 'before', len(before), 'after', len(after), '| first', after[0][:30], '| second', after[1][:30], '| count', sum(e.startswith('- **%s (' % T) for e in after))
assert len(after) == len(before) + 1 and after[0].startswith('- **EGAN (') and after[1].startswith('- **CW (')
open(Q, 'w', encoding='utf-8', newline='').write(nl.join(L))
# done file
D = '../../Screens/_daily/_wave7_done.txt'
d = open(D, encoding='utf-8', newline='').read()
dnl = '\r\n' if '\r\n' in d else '\n'
assert d.endswith(dnl) and (T + dnl) not in d and d.rstrip().split()[-1] == 'CW'
open(D, 'w', encoding='utf-8', newline='').write(d + T + dnl)
dl = open(D).read().split()
ol = open('../../Screens/_daily/_wave7_order.txt').read().split()
print('done lines', len(dl), 'last', dl[-1], 'equals order first', dl == ol[:len(dl)], 'next', ol[len(dl)])
assert len(dl) == 106 and dl == ol[:106]
# reading list
R = '../../Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
r = open(R, encoding='utf-8', newline='').read()
rnl = '\r\n' if '\r\n' in r else '\n'
assert '## UPDATE 2026-09-28 - EGAN' not in r
note = open('fold_note.md', encoding='utf-8').read()
note = note.replace('Next in the order file: TECH.', 'Next in the order file: %s.' % ol[106])
body = r.rstrip('\r\n') + rnl + note.rstrip('\n').replace('\n', rnl) + rnl
open(R, 'w', encoding='utf-8', newline='').write(body)
print('reading list ends:', repr(body[-40:]))
# survival shapes
S = '../../Screens/SURVIVAL SHAPES - index.md'
s = open(S, encoding='utf-8', newline='').read()
snl = '\r\n' if '\r\n' in s else '\n'
rows = [l for l in s.split(snl) if re.match(r'^\| \d+ \|', l)]
print('shape rows', len(rows), 'max', max(int(re.match(r'^\| (\d+) \|', l).group(1)) for l in rows))
assert len(rows) == 30
assert 'the EGAN fold' not in s
sn = open('shape_note.md', encoding='utf-8').read()
s2 = s.rstrip('\r\n') + snl + sn.rstrip('\n').replace('\n', snl) + snl
open(S, 'w', encoding='utf-8', newline='').write(s2)
print('ok')
