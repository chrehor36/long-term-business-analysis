import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
D = 'Test Runs/_research 2026-09-27 HWKN/'
# 1. register entry, by line
P = 'Screens/WATCHLIST RUN QUEUE.md'
raw = open(P, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl)
H = [i for i, x in enumerate(L) if x == '## COMPLETED FROM THE QUEUE']
W = [i for i, x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(H) == 1 and len(W) == 1 and H[0] < W[0], (H, W)
print('heading unique at line', H[0] + 1)
def count(lines, h, w):
    ent = [x for x in lines[h + 1:w] if re.match(r'^- \*\*', x)]
    k = [x for x in ent if x.startswith('- **HWKN ')]
    return len(ent), len(k), ent[0][:40] if ent else None
before = count(L, H[0], W[0]); print('before', before)
assert before[1] == 0, 'HWKN already entered'
assert before[2].startswith('- **KWR '), before
N = before[0] + 1
entry = open(D + 'register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
entry = [e.replace('@@N@@', str(N)).replace('@@B@@', str(before[0])).replace('@@H@@', str(H[0] + 1)) for e in entry]
L2 = L[:H[0] + 1] + entry + L[H[0] + 1:]
H2 = [i for i, x in enumerate(L2) if x == '## COMPLETED FROM THE QUEUE']
W2 = [i for i, x in enumerate(L2) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
after = count(L2, H2[0], W2[0]); print('after', after)
assert after[0] == N and after[1] == 1 and after[2].startswith('- **HWKN ')
open(P, 'w', encoding='utf-8', newline='').write(nl.join(L2))
# re-read and count back
L3 = open(P, encoding='utf-8', newline='').read().split(nl)
H3 = [i for i, x in enumerate(L3) if x == '## COMPLETED FROM THE QUEUE']; W3 = [i for i, x in enumerate(L3) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
print('count back', count(L3, H3[0], W3[0]))
# done file
DF = 'Screens/_daily/_wave7_done.txt'
d = open(DF, encoding='utf-8', newline='').read()
assert 'HWKN' not in d.split()
if not d.endswith('\n'): d += '\n'
d += 'HWKN\n'
open(DF, 'w', encoding='utf-8', newline='').write(d)
print('done file lines', len([x for x in d.splitlines() if x.strip()]), 'last', d.splitlines()[-1])
# survival shapes dated note
S = 'Screens/SURVIVAL SHAPES - index.md'
t = open(S, encoding='utf-8', newline='').read()
snl = '\r\n' if '\r\n' in t else '\n'
rows = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \|', t)]
print('shapes rows', len(rows), 'max', max(rows))
assert 'the HWKN fold' not in t
n = open(D + 'shapes_note.md', encoding='utf-8').read().replace('@@ROWS@@', str(len(rows))).replace('@@MAX@@', str(max(rows)))
if not t.endswith('\n'): t += snl
t += n.lstrip('\n').replace('\n', snl)
open(S, 'w', encoding='utf-8', newline='').write(t)
# reading list
R = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
r = open(R, encoding='utf-8', newline='').read()
nl2 = '\r\n' if '\r\n' in r else '\n'
assert 'UPDATE 2026-09-27 - HWKN' not in r
if not r.endswith('\n'): r += nl2
r += open(D + 'fold_note.md', encoding='utf-8').read().replace('@@N@@', str(N)).replace('\n', nl2)
open(R, 'w', encoding='utf-8', newline='').write(r)
print('appended; register entry', N)
