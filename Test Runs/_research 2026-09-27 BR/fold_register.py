"""Insert the BR register entry immediately under the line-exact register heading, counting entries in the
slice from that heading to the write-early heading before and after (the USNA/USAR trap: match by line)."""
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
P = 'Screens/WATCHLIST RUN QUEUE.md'
raw = open(P, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl)
H = [i for i, x in enumerate(L) if x == '## COMPLETED FROM THE QUEUE']
W = [i for i, x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(H) == 1 and len(W) == 1 and H[0] < W[0], (H, W)
def count(lines, h, w):
    sl = lines[h + 1:w]
    ent = [x for x in sl if re.match(r'^- \*\*', x)]
    ngvc = [x for x in ent if x.startswith('- **BR (')]
    return len(ent), len(ngvc), ent[0][:40] if ent else None
before = count(L, H[0], W[0])
print('before', before)
assert before[1] == 0, 'BR already entered'
entry = open('Test Runs/_research 2026-09-27 BR/register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
entry = [e.replace('@@N@@', str(before[0] + 1)).replace('@@B@@', str(before[0])) for e in entry]
L2 = L[:H[0] + 1] + entry + L[H[0] + 1:]
H2 = [i for i, x in enumerate(L2) if x == '## COMPLETED FROM THE QUEUE']
W2 = [i for i, x in enumerate(L2) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
after = count(L2, H2[0], W2[0])
print('after', after)
assert after[0] == before[0] + 1 and after[1] == 1 and after[2].startswith('- **BR (')
open(P, 'w', encoding='utf-8', newline='').write(nl.join(L2))
print('written; register entry', after[0])
