import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
T = 'ECL'
NEXT = 'CLB'
Q = 'Screens/WATCHLIST RUN QUEUE.md'
RL = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
DONE = 'Screens/_daily/_wave7_done.txt'
ORDER = 'Screens/_daily/_wave7_order.txt'
RUN = 'Test Runs/2026-09-28 Run - ECL Ecolab.md'
R = 'Test Runs/_research 2026-09-28 ECL/'
SH = 'Screens/SURVIVAL SHAPES - index.md'
AL = 'tools/alerts.json'
PF = 'PORTFOLIO.md'

# 1 register entry, by line (line-exact heading, asserted unique, inserted first, counted back)
raw = open(Q, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl)
H = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
assert len(H) == 1, H
W = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(W) == 1, W
h, w = H[0], W[0]
before = sum(1 for l in L[h + 1:w] if l.startswith('- **'))
assert not any(l.startswith('- **%s ' % T) for l in L[h + 1:w])
after_expected = before + 1
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n')
entry = entry.replace('%AFTER%', str(after_expected)).replace('%BEFORE%', str(before)).replace('%HLINE%', str(h + 1))
entry = entry.split('\n')
L = L[:h + 1] + entry + L[h + 1:]
open(Q, 'w', encoding='utf-8', newline='').write(nl.join(L))
L2 = open(Q, encoding='utf-8', newline='').read().split(nl)
H2 = [i for i, l in enumerate(L2) if l == '## COMPLETED FROM THE QUEUE']
W2 = [i for i, l in enumerate(L2) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(H2) == 1 and len(W2) == 1
ents = [l for l in L2[H2[0] + 1:W2[0]] if l.startswith('- **')]
after = len(ents)
print('heading line', H2[0] + 1, 'before', before, 'after', after, 'first', ents[0][:30], 'second', ents[1][:30])
assert after == after_expected and ents[0].startswith('- **%s ' % T) and sum(e.startswith('- **%s ' % T) for e in ents) == 1
assert ents[1].startswith('- **OII ')

# 2 done file
d = open(DONE, encoding='utf-8').read()
assert d.endswith('\n') and T not in d.split()
open(DONE, 'a', encoding='utf-8', newline='').write(T + '\n')
dl = open(DONE, encoding='utf-8').read().split()
ol = open(ORDER, encoding='utf-8').read().split()
print('done', len(dl), dl[-1], 'prefix', dl == ol[:len(dl)], 'next', ol[len(dl)])
assert dl == ol[:len(dl)] and len(dl) == 100 and ol[len(dl)] == NEXT

# 3 reading list
rl = open(RL, encoding='utf-8', newline='').read()
rnl = '\r\n' if '\r\n' in rl else '\n'
assert rl.rstrip().endswith('Next in the order file: %s.' % T)
note = open(R + 'fold_note.md', encoding='utf-8').read()
if rnl == '\r\n':
    note = note.replace('\n', '\r\n')
if not rl.endswith(rnl):
    rl += rnl
open(RL, 'w', encoding='utf-8', newline='').write(rl + note)
print('RL ends', open(RL, encoding='utf-8').read().rstrip()[-40:])

# 4 alerts (gate-clearer)
a = json.load(open(AL, encoding='utf-8'))
n0 = len(a['alerts'])
ids = {x['id'] for x in a['alerts']}
assert 'ECL-rerun-band' not in ids and 'ECL-floor-band' not in ids
bands = json.load(open(R + 'bands.json', encoding='utf-8'))
a['alerts'].extend(bands)
open(AL, 'w', encoding='utf-8').write(json.dumps(a, indent=1, ensure_ascii=False) + '\n')
json.load(open(AL, encoding='utf-8'))
print('alerts', n0, '->', len(a['alerts']))

# 4b PORTFOLIO row after MSA
p = open(PF, encoding='utf-8', newline='').read()
pnl = '\r\n' if '\r\n' in p else '\n'
P = p.split(pnl)
ci = [i for i, l in enumerate(P) if l.startswith('| - | MSA |')]
assert len(ci) == 1
assert not any(l.startswith('| - | ECL |') for l in P)
row = open(R + 'portfolio_row.md', encoding='utf-8').read().strip('\n')
P = P[:ci[0] + 1] + [row] + P[ci[0] + 1:]
open(PF, 'w', encoding='utf-8', newline='').write(pnl.join(P))
print('portfolio row at line', ci[0] + 2)

# 5 survival shapes index: count first, then enter ECL in #10's instances and add the dated note
t = open(SH, encoding='utf-8', newline='').read()
snl = '\r\n' if '\r\n' in t else '\n'
S = t.split(snl)
rows = [l for l in S if re.match(r'^\| \d+ \|', l)]
mx = max(int(re.match(r'^\| (\d+) \|', l).group(1)) for l in rows)
print('shape rows', len(rows), 'max', mx)
assert len(rows) == 30 and mx == 30
k = [i for i, l in enumerate(S) if l.startswith('| 10 | **The camouflage**')]
assert len(k) == 1
line = S[k[0]].rstrip()
assert line.endswith('|')
add = open(R + 'shape_add.md', encoding='utf-8').read().strip('\n')
S[k[0]] = line[:-1].rstrip() + add + ' |'
snote = open(R + 'shape_note.md', encoding='utf-8').read().strip('\n') % (len(rows), mx)
while S and S[-1] == '':
    S.pop()
S += ['', snote, '']
open(SH, 'w', encoding='utf-8', newline='').write(snl.join(S))
print('shapes updated')

# 6 run file self-audit: the fold line
s = open(RUN, encoding='utf-8').read()
a0 = '- **Ledger ids resolved by script** (`qcheck.py`)'
assert s.count(a0) == 1
fold_line = ('- [x] Fold: register entry %d (%d before, heading unique at line %d, ECL first and once, OII second), done file %d lines ending ECL and equal to the order file\'s first %d, next %s; bands `ECL-rerun-band` $165.71 and `ECL-floor-band` $115.22 armed and a `PORTFOLIO.md` row added after MSA (a gate-clearer); survival-shapes index: ECL entered in #10\'s instances with a dated note (%d rows, maximum %d, counted before writing); ECL in no tier roster (the whole queue file searched)\n'
             % (after, before, H2[0] + 1, len(dl), len(dl), NEXT, len(rows), mx))
s = s.replace(a0, fold_line + a0)
open(RUN, 'w', encoding='utf-8').write(s)
print('run file updated')
