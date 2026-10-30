# CLB fold. Run from the repository root. Every ticker, count and path below read before running
# (adapted from the OII fold; TICK, PREV, NEXT, the position 101 and the counts changed by hand).
import re
R = 'Test Runs/_research 2026-09-28 CLB/'
TICK = 'CLB'; PREV = 'ECL'; NEXT = 'KEYS'; POS = 101
q = 'Screens/WATCHLIST RUN QUEUE.md'
L = open(q, encoding='utf-8').read().split('\n')
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']; assert len(h) == 1, h
w = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]; assert len(w) == 1, w
before = sum(1 for l in L[h[0] + 1:w[0]] if l.startswith('- **'))
assert before == 242, before
assert L[h[0] + 1].startswith('- **' + PREV + ' ('), L[h[0] + 1][:40]
assert not any(l.startswith('- **' + TICK + ' (') for l in L), 'CLB already registered'
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
assert entry[0].startswith('- **' + TICK + ' (')
L = L[:h[0] + 1] + entry + L[h[0] + 1:]
open(q, 'w', encoding='utf-8').write('\n'.join(L))
# verify by counting back from the file
L2 = open(q, encoding='utf-8').read().split('\n')
h2 = [i for i, l in enumerate(L2) if l == '## COMPLETED FROM THE QUEUE']; w2 = [i for i, l in enumerate(L2) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(h2) == 1 and len(w2) == 1
after = sum(1 for l in L2[h2[0] + 1:w2[0]] if l.startswith('- **'))
assert after == 243 and L2[h2[0] + 1].startswith('- **CLB (') and L2[h2[0] + 1 + len(entry)].startswith('- **ECL ('), (after,)
assert sum(1 for l in L2 if l.startswith('- **CLB (')) == 1
print('register', before, '->', after, 'heading at line', h2[0] + 1)
# done file: append CLB only if the order file's line 101 is CLB and the done file has 100 lines ending ECL
order = [x.strip() for x in open('Screens/_daily/_wave7_order.txt', encoding='utf-8').read().split('\n') if x.strip()]
assert order[POS - 1] == TICK and order[POS] == NEXT, (order[POS - 1], order[POS])
d = 'Screens/_daily/_wave7_done.txt'
done = [x.strip() for x in open(d, encoding='utf-8').read().split('\n') if x.strip()]
assert len(done) == POS - 1 and done[-1] == PREV, (len(done), done[-1])
s = open(d, encoding='utf-8').read()
if not s.endswith('\n'): s += '\n'
open(d, 'w', encoding='utf-8').write(s + TICK + '\n')
done2 = [x.strip() for x in open(d, encoding='utf-8').read().split('\n') if x.strip()]
assert len(done2) == POS and done2 == order[:POS], 'done file does not equal the order file prefix'
print('done file', len(done2), 'lines ending', done2[-1])
# reading list
rl = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
s = open(rl, encoding='utf-8').read()
assert s.rstrip().endswith('Next in the order file: ' + TICK + '.')
note = open(R + 'fold_note.md', encoding='utf-8').read()
assert note.rstrip().endswith('Next in the order file: ' + NEXT + '.')
open(rl, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n' + note)
# shapes: count rows first
sh = 'Screens/SURVIVAL SHAPES - index.md'
s = open(sh, encoding='utf-8').read()
rows = [int(m.group(1)) for l in s.split('\n') for m in [re.match(r'^\| (\d+) \|', l)] if m]
assert len(rows) == 30 and max(rows) == 30, (len(rows), max(rows))
open(sh, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n' + open(R + 'shape_note.md', encoding='utf-8').read())
print('done')
