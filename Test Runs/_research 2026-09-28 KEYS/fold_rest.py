# Steps 5 and 6 of fold.py, re-run after fold.py stopped at step 5 on a format error in shape_note.md
# ("44%" read as a format directive); steps 1-4 had completed and printed their verified counts, and the
# shapes file had not been written. The counts step 6 reports are recomputed from the files as written.
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
NEXT = 'ESI'
Q = 'Screens/WATCHLIST RUN QUEUE.md'
DONE = 'Screens/_daily/_wave7_done.txt'
RUN = 'Test Runs/2026-09-28 Run - KEYS Keysight Technologies.md'
R = 'Test Runs/_research 2026-09-28 KEYS/'
SH = 'Screens/SURVIVAL SHAPES - index.md'

raw = open(Q, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
L2 = raw.split(nl)
H2 = [i for i, l in enumerate(L2) if l == '## COMPLETED FROM THE QUEUE']
W2 = [i for i, l in enumerate(L2) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(H2) == 1 and len(W2) == 1
ents = [l for l in L2[H2[0] + 1:W2[0]] if l.startswith('- **')]
after = len(ents)
before = after - 1
assert ents[0].startswith('- **KEYS ') and ents[1].startswith('- **CLB ')
assert sum(e.startswith('- **KEYS ') for e in ents) == 1
dl = open(DONE, encoding='utf-8').read().split()
assert dl[-1] == 'KEYS' and len(dl) == 102
print('register', before, '->', after, 'heading line', H2[0] + 1, 'done', len(dl))

# 5 survival shapes index: count first, then enter KEYS in #10's instances and add the dated note
t = open(SH, encoding='utf-8', newline='').read()
snl = '\r\n' if '\r\n' in t else '\n'
S = t.split(snl)
assert 'KEYS (2026-09-28' not in t
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
assert s.count(a0) == 1 and '- [x] Fold:' not in s
fold_line = ('- [x] Fold: register entry %d (%d before, heading unique at line %d, KEYS first and once, CLB second), done file %d lines ending KEYS and equal to the order file\'s first %d, next %s; bands `KEYS-rerun-band` $154.81 and `KEYS-floor-band` $110.11 armed and a `PORTFOLIO.md` row added after ECL (a gate-clearer); survival-shapes index: KEYS entered in #10\'s instances with a dated note (%d rows, maximum %d, counted before writing); KEYS in no tier roster (the whole queue file searched)\n'
             % (after, before, H2[0] + 1, len(dl), len(dl), NEXT, len(rows), mx))
s = s.replace(a0, fold_line + a0)
open(RUN, 'w', encoding='utf-8', newline='\n').write(s)
print('run file updated')
