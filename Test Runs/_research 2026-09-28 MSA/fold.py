import json, re
Q = 'Screens/WATCHLIST RUN QUEUE.md'
RL = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
DONE = 'Screens/_daily/_wave7_done.txt'
ORDER = 'Screens/_daily/_wave7_order.txt'
RUN = 'Test Runs/2026-09-28 Run - MSA MSA Safety.md'
R = 'Test Runs/_research 2026-09-28 MSA/'
SH = 'Screens/SURVIVAL SHAPES - index.md'
AL = 'tools/alerts.json'
PF = 'PORTFOLIO.md'

# 1 register entry, by line
raw = open(Q, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl)
H = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
assert len(H) == 1, H
W = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(W) == 1, W
h, w = H[0], W[0]
before = sum(1 for l in L[h + 1:w] if l.startswith('- **'))
assert not any(l.startswith('- **MSA ') for l in L[h + 1:w])
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h + 1] + entry + L[h + 1:]
open(Q, 'w', encoding='utf-8', newline='').write(nl.join(L))
L2 = open(Q, encoding='utf-8', newline='').read().split(nl)
H2 = [i for i, l in enumerate(L2) if l == '## COMPLETED FROM THE QUEUE']
W2 = [i for i, l in enumerate(L2) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(H2) == 1 and len(W2) == 1
ents = [l for l in L2[H2[0] + 1:W2[0]] if l.startswith('- **')]
after = len(ents)
print('heading line', H2[0] + 1, 'before', before, 'after', after, 'first', ents[0][:30], 'second', ents[1][:30])
assert after == before + 1 and ents[0].startswith('- **MSA ') and sum(e.startswith('- **MSA ') for e in ents) == 1

# 2 done file
d = open(DONE, encoding='utf-8').read()
assert d.endswith('\n') and 'MSA' not in d.split()
open(DONE, 'a', encoding='utf-8', newline='').write('MSA\n')
dl = open(DONE, encoding='utf-8').read().split()
ol = open(ORDER, encoding='utf-8').read().split()
print('done', len(dl), dl[-1], 'prefix', dl == ol[:len(dl)], 'next', ol[len(dl)])
assert ol[len(dl)] == 'XPEL'

# 3 reading list
rl = open(RL, encoding='utf-8', newline='').read()
rnl = '\r\n' if '\r\n' in rl else '\n'
assert rl.rstrip().endswith('Next in the order file: MSA.')
note = open(R + 'fold_note.md', encoding='utf-8').read()
if rnl == '\r\n':
    note = note.replace('\n', '\r\n')
if not rl.endswith(rnl):
    rl += rnl
open(RL, 'w', encoding='utf-8', newline='').write(rl + note)
print('RL ends', open(RL, encoding='utf-8').read().rstrip()[-40:])

# 4 alerts (gate-clearer)
a = json.load(open(AL, encoding='utf-8'))
ids = {x['id'] for x in a['alerts']}
assert 'MSA-rerun-band' not in ids and 'MSA-floor-band' not in ids
bands = json.load(open(R + 'bands.json', encoding='utf-8'))
a['alerts'].extend(bands)
open(AL, 'w', encoding='utf-8').write(json.dumps(a, indent=1, ensure_ascii=False) + '\n')
json.load(open(AL, encoding='utf-8'))
print('alerts', len(a['alerts']))

# 4b PORTFOLIO row after CAT
p = open(PF, encoding='utf-8', newline='').read()
pnl = '\r\n' if '\r\n' in p else '\n'
P = p.split(pnl)
ci = [i for i, l in enumerate(P) if l.startswith('| - | CAT |')]
assert len(ci) == 1
assert not any(l.startswith('| - | MSA |') for l in P)
row = open(R + 'portfolio_row.md', encoding='utf-8').read().strip('\n')
P = P[:ci[0] + 1] + [row] + P[ci[0] + 1:]
open(PF, 'w', encoding='utf-8', newline='').write(pnl.join(P))
print('portfolio row at line', ci[0] + 2)

# 5 survival shapes index
t = open(SH, encoding='utf-8', newline='').read()
snl = '\r\n' if '\r\n' in t else '\n'
S = t.split(snl)
rows = [l for l in S if re.match(r'^\| \d+ \|', l)]
mx = max(int(re.match(r'^\| (\d+) \|', l).group(1)) for l in rows)
print('shape rows', len(rows), 'max', mx)
k = [i for i, l in enumerate(S) if l.startswith('| 7 | **The long tail on a short cycle**')]
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

# 6 run file self-audit
s = open(RUN, encoding='utf-8').read()
a0 = '- [x] Run committed to git (commits listed in the register entry and the fold)'
assert s.count(a0) == 1
new = ('- [x] Run committed to git (commits `53ce46ab` claim, `a00cc542` Step 0 and Q1, `75a8cfde` Q2, `af0e48f7` Q3-Q6 and the audit, then the fold)\n'
       '- [x] Fold: register entry %d (%d before, heading unique at line %d, MSA first and once), done file %d lines ending MSA and equal to the order file\'s first %d, next XPEL; bands `MSA-rerun-band` $169.89 and `MSA-floor-band` $115.14 armed and a `PORTFOLIO.md` row added (a gate-clearer); survival-shapes index: MSA entered in #7\'s instances with a dated note; MSA in no tier roster'
       % (after, before, H2[0] + 1, len(dl), len(dl)))
s = s.replace(a0, new)
open(RUN, 'w', encoding='utf-8').write(s)
print('run file updated')
