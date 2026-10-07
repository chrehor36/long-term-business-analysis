# The six-step fold for TECH, adapted from Test Runs/_research 2026-09-28 MA/fold.py (ticker, previous entry EGAN, count 107, next PFGC, shape #10, bands, PORTFOLIO neighbour MA and the fold line re-checked by hand).
# Original header: The six-step fold for ESI, adapted from Test Runs/_research 2026-09-28 KEYS/fold.py (every ticker, count,
# neighbour and "next" name re-checked; the shape note uses str.replace, not %-formatting, after the KEYS
# fold stopped at step 5 on a "%" in its note). Run from the repository root.
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
T = 'TECH'
PREV = 'EGAN'
NEXT = 'PFGC'
N_DONE = 107
PF_PREV = 'MA'
Q = 'Screens/WATCHLIST RUN QUEUE.md'
RL = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
DONE = 'Screens/_daily/_wave7_done.txt'
ORDER = 'Screens/_daily/_wave7_order.txt'
RUN = 'Test Runs/2026-09-28 Run - TECH Bio-Techne.md'
R = 'Test Runs/_research 2026-09-28 TECH/'
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
assert L[h + 1].startswith('- **%s ' % PREV), L[h + 1][:40]
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
print('1 register: heading line', H2[0] + 1, 'before', before, 'after', after, 'first', ents[0][:24], 'second', ents[1][:24])
assert after == after_expected and ents[0].startswith('- **%s ' % T) and sum(e.startswith('- **%s ' % T) for e in ents) == 1
assert ents[1].startswith('- **%s ' % PREV)

# 2 done file
d = open(DONE, encoding='utf-8').read()
assert d.endswith('\n') and T not in d.split()
dnl = '\r\n' if '\r\n' in open(DONE, encoding='utf-8', newline='').read() else '\n'
open(DONE, 'a', encoding='utf-8', newline='').write(T + dnl)
dl = open(DONE, encoding='utf-8').read().split()
ol = open(ORDER, encoding='utf-8').read().split()
print('2 done', len(dl), dl[-1], 'prefix', dl == ol[:len(dl)], 'next', ol[len(dl)])
assert dl == ol[:len(dl)] and len(dl) == N_DONE and dl[-1] == T and ol[len(dl)] == NEXT

# 3 reading list
rl = open(RL, encoding='utf-8', newline='').read()
rnl = '\r\n' if '\r\n' in rl else '\n'
assert rl.rstrip().endswith('Next in the order file: %s.' % T)
note = open(R + 'fold_note.md', encoding='utf-8').read()
assert note.rstrip().endswith('Next in the order file: %s.' % NEXT)
if rnl == '\r\n':
    note = note.replace('\n', '\r\n')
if not rl.endswith(rnl):
    rl += rnl
open(RL, 'w', encoding='utf-8', newline='').write(rl + note)
print('3 RL ends', open(RL, encoding='utf-8').read().rstrip()[-40:])

# 4 alerts (a gate-clearer)
a = json.load(open(AL, encoding='utf-8'))
n0 = len(a['alerts'])
ids = {x['id'] for x in a['alerts']}
assert 'TECH-rerun-band' not in ids and 'TECH-floor-band' not in ids
bands = json.load(open(R + 'bands.json', encoding='utf-8'))
assert [b['id'] for b in bands] == ['TECH-floor-band', 'TECH-rerun-band'] and all(b['active'] is False for b in bands)
a['alerts'].extend(bands)
open(AL, 'w', encoding='utf-8').write(json.dumps(a, indent=1, ensure_ascii=False) + '\n')
json.load(open(AL, encoding='utf-8'))
print('4 alerts', n0, '->', len(a['alerts']))

# 4b PORTFOLIO row after MA
p = open(PF, encoding='utf-8', newline='').read()
pnl = '\r\n' if '\r\n' in p else '\n'
P = p.split(pnl)
ci = [i for i, l in enumerate(P) if l.startswith('| - | %s |' % PF_PREV)]
assert len(ci) == 1
assert not any(l.startswith('| - | %s |' % T) for l in P)
row = open(R + 'portfolio_row.md', encoding='utf-8').read().strip('\n')
P = P[:ci[0] + 1] + [row] + P[ci[0] + 1:]
open(PF, 'w', encoding='utf-8', newline='').write(pnl.join(P))
print('4b portfolio row at line', ci[0] + 2)

# 5 survival shapes index: count first, then enter TECH in #10's instances and add the dated note
t = open(SH, encoding='utf-8', newline='').read()
snl = '\r\n' if '\r\n' in t else '\n'
S = t.split(snl)
assert 'TECH (2026-09-28' not in t
rows = [l for l in S if re.match(r'^\| \d+ \|', l)]
mx = max(int(re.match(r'^\| (\d+) \|', l).group(1)) for l in rows)
print('5 shape rows', len(rows), 'max', mx)
assert len(rows) == 30 and mx == 30
k = [i for i, l in enumerate(S) if l.startswith('| 10 | **The camouflage**')]
assert len(k) == 1
line = S[k[0]].rstrip()
assert line.endswith('|')
add = open(R + 'shape_add.md', encoding='utf-8').read().strip('\n')
S[k[0]] = line[:-1].rstrip() + add + ' |'
snote = open(R + 'shape_note.md', encoding='utf-8').read().strip('\n').replace('ROWS', str(len(rows))).replace('MAXN', str(mx))
while S and S[-1] == '':
    S.pop()
S += ['', snote, '']
open(SH, 'w', encoding='utf-8', newline='').write(snl.join(S))
print('5 shapes updated')

# 6 run file self-audit: replace the pre-written fold line with the counted one
s = open(RUN, encoding='utf-8').read()
FL = [l for l in s.split(chr(10)) if l.startswith('- [x] Fold:')]
assert len(FL) == 1
fold_line = ("- [x] Fold: register entry {a} ({b} before, heading unique at line {hl}, TECH first and once, EGAN second), done file {n} lines ending TECH and equal to the order file's first {n}, next {nx}; bands `TECH-rerun-band` $29.78 and `TECH-floor-band` $25.40 written SUSPENDED (active false, a merger agreement naming the company is filed) and a `PORTFOLIO.md` row added after MA (a gate-clearer); survival-shapes index: TECH entered in #10's instances with a dated note ({r} rows, maximum {m}, counted before writing); TECH in no tier roster (the whole queue file searched; the only match is the EGAN entry's next-name line)"
             .format(a=after, b=before, hl=H2[0] + 1, n=len(dl), nx=NEXT, r=len(rows), m=mx))
s = s.replace(FL[0], fold_line)
open(RUN, 'w', encoding='utf-8').write(s)
print('6 run file updated')
