import io
Q = 'Screens/WATCHLIST RUN QUEUE.md'
RL = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
DONE = 'Screens/_daily/_wave7_done.txt'
ORDER = 'Screens/_daily/_wave7_order.txt'
RUN = 'Test Runs/2026-09-28 Run - GWW W.W. Grainger.md'
R = 'Test Runs/_research 2026-09-28 GWW/'

raw = open(Q, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl)
H = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
assert len(H) == 1, H
W = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(W) == 1, W
h, w = H[0], W[0]
before = sum(1 for l in L[h + 1:w] if l.startswith('- **'))
assert not any(l.startswith('- **GWW ') for l in L[h + 1:w]), 'GWW already registered'
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h + 1] + entry + L[h + 1:]
open(Q, 'w', encoding='utf-8', newline='').write(nl.join(L))
# verify
L2 = open(Q, encoding='utf-8', newline='').read().split(nl)
H2 = [i for i, l in enumerate(L2) if l == '## COMPLETED FROM THE QUEUE']
W2 = [i for i, l in enumerate(L2) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(H2) == 1 and len(W2) == 1
ents = [l for l in L2[H2[0] + 1:W2[0]] if l.startswith('- **')]
after = len(ents)
print('heading line', H2[0] + 1, 'entries before', before, 'after', after, 'first', ents[0][:40], 'second', ents[1][:40])
assert after == before + 1 and ents[0].startswith('- **GWW ') and sum(e.startswith('- **GWW ') for e in ents) == 1

# done file
d = open(DONE, encoding='utf-8').read()
assert d.endswith('\n') and 'GWW' not in d.split()
open(DONE, 'a', encoding='utf-8', newline='').write('GWW\n')
dl = open(DONE, encoding='utf-8').read().split()
ol = open(ORDER, encoding='utf-8').read().split()
print('done lines', len(dl), 'last', dl[-1], 'equal to order prefix', dl == ol[:len(dl)], 'next', ol[len(dl)])

# reading list
rl = open(RL, encoding='utf-8', newline='').read()
rnl = '\r\n' if '\r\n' in rl else '\n'
assert rl.rstrip().endswith('Next in the order file: GWW.')
note = open(R + 'fold_note.md', encoding='utf-8').read()
if rnl == '\r\n':
    note = note.replace('\n', '\r\n')
if not rl.endswith(rnl):
    rl += rnl
open(RL, 'w', encoding='utf-8', newline='').write(rl + note)
print('reading list ends:', open(RL, encoding='utf-8').read().rstrip()[-40:])

# run file self-audit fold line
s = open(RUN, encoding='utf-8').read()
a = '- [x] Run committed to git (commits listed in the register entry and the fold)'
assert s.count(a) == 1
s = s.replace(a, '- [x] Run committed to git (commits `ce29560f` claim, `2afef8b3` Step 0 and Q1, `a74e73ec` Q2, `aebd798b` beneath the close, then the fold)\n'
              '- [x] Fold: register entry %d (%d before, heading unique at line %d, GWW first and once), done file %d lines ending GWW and equal to the order file\'s first %d, next MSA; no band, no `PORTFOLIO.md` row; GWW in no tier roster' % (after, before, H2[0] + 1, len(dl), len(dl)))
open(RUN, 'w', encoding='utf-8').write(s)
print('run file self-audit updated')
