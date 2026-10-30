import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
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
    k = [x for x in ent if x.startswith('- **KWR ')]
    return len(ent), len(k), ent[0][:40] if ent else None
before = count(L, H[0], W[0]); print('before', before)
assert before[1] == 0, 'KWR already entered'
entry = open('Test Runs/_research 2026-09-27 KWR/register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
entry = [e.replace('@@N@@', str(before[0] + 1)).replace('@@B@@', str(before[0])) for e in entry]
L2 = L[:H[0] + 1] + entry + L[H[0] + 1:]
H2 = [i for i, x in enumerate(L2) if x == '## COMPLETED FROM THE QUEUE']
W2 = [i for i, x in enumerate(L2) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
after = count(L2, H2[0], W2[0]); print('after', after)
assert after[0] == before[0] + 1 and after[1] == 1 and after[2].startswith('- **KWR ')
open(P, 'w', encoding='utf-8', newline='').write(nl.join(L2))
print('written; register entry', after[0])
