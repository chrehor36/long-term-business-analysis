# The fold for PFGC, a Q2 close: steps 1 (register), 2 (done file), 3 (reading list), 5 (shapes dated note), 6 (run-file fold line).
# Adapted from Test Runs/_research 2026-09-28 TECH/fold.py; step 4 (alerts, PORTFOLIO) is not done because the file failed on the business.
# Run from the repository root.
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
T = 'PFGC'
PREV = 'TECH'
NEXT = 'POWL'
N_DONE = 108
Q = 'Screens/WATCHLIST RUN QUEUE.md'
RL = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
DONE = 'Screens/_daily/_wave7_done.txt'
ORDER = 'Screens/_daily/_wave7_order.txt'
RUN = 'Test Runs/2026-09-28 Run - PFGC Performance Food Group.md'
R = 'Test Runs/_research 2026-09-28 PFGC/'
SH = 'Screens/SURVIVAL SHAPES - index.md'

# roster check first: the whole queue file, before anything is written
raw = open(Q, encoding='utf-8', newline='').read()
hits = [l for l in raw.splitlines() if re.search(r'\bPFGC\b', l)]
print('0 PFGC lines in the queue file before the fold:', len(hits), [h[:60] for h in hits])
assert len(hits) == 1 and hits[0].startswith('- **TECH ') is False and 'Next in the order file: PFGC.' in hits[0]

# 1 register entry, by line (line-exact heading, asserted unique, inserted first, counted back)
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

# 5 survival shapes index: count first, then the dated note only (Q4 not reached)
t = open(SH, encoding='utf-8', newline='').read()
snl = '\r\n' if '\r\n' in t else '\n'
S = t.split(snl)
assert 'the PFGC fold' not in t
rows = [l for l in S if re.match(r'^\| \d+ \|', l)]
mx = max(int(re.match(r'^\| (\d+) \|', l).group(1)) for l in rows)
print('5 shape rows', len(rows), 'max', mx)
assert len(rows) == 30 and mx == 30
snote = open(R + 'shape_note.md', encoding='utf-8').read().strip('\n').replace('ROWS', str(len(rows))).replace('MAXN', str(mx))
while S and S[-1] == '':
    S.pop()
S += ['', snote, '']
open(SH, 'w', encoding='utf-8', newline='').write(snl.join(S))
print('5 shapes note added')

# 6 run file self-audit: replace the pre-written fold line with the counted one
s = open(RUN, encoding='utf-8').read()
FL = [l for l in s.split(chr(10)) if l.startswith('- [x] Fold:')]
assert len(FL) == 1
fold_line = ("- [x] Fold: register entry {a} ({b} before, heading unique at line {hl}, PFGC first and once, TECH second), done file {n} lines ending PFGC and equal to the order file's first {n}, next {nx}; no bands and no `PORTFOLIO.md` row (a Q2 close, the QLYS ruling; reversal conditions in words beneath the close); survival-shapes index: a dated note only ({r} rows, maximum {m}, counted before writing; #11 as a signature, #6 as a feature, neither entered as an instance); PFGC in no tier roster (the whole queue file searched before the fold; the only match was the TECH entry's next-name line)"
             .format(a=after, b=before, hl=H2[0] + 1, n=len(dl), nx=NEXT, r=len(rows), m=mx))
s = s.replace(FL[0], fold_line)
open(RUN, 'w', encoding='utf-8').write(s)
print('6 run file updated')
