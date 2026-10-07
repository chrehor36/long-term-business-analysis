# OII fold. Run from the repository root. Every ticker and path below read before running.
import re
R = 'Test Runs/_research 2026-09-28 OII/'
TICK = 'OII'; PREV = 'SANM'; NEXT = 'ECL'
q = 'Screens/WATCHLIST RUN QUEUE.md'
L = open(q, encoding='utf-8').read().split('\n')
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']; assert len(h) == 1, h
assert L[h[0] + 1].startswith('- **' + PREV + ' ('), L[h[0] + 1][:40]
assert not any(l.startswith('- **' + TICK + ' (') for l in L), 'OII already registered'
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
assert entry[0].startswith('- **' + TICK + ' (')
L = L[:h[0] + 1] + entry + L[h[0] + 1:]
open(q, 'w', encoding='utf-8').write('\n'.join(L))
# done file: append OII only if the order file's line 99 is OII and the done file has 98 lines ending SANM
order = [x.strip() for x in open('Screens/_daily/_wave7_order.txt', encoding='utf-8').read().split('\n') if x.strip()]
assert order[98] == TICK and order[99] == NEXT, (order[98], order[99])
d = 'Screens/_daily/_wave7_done.txt'
done = [x.strip() for x in open(d, encoding='utf-8').read().split('\n') if x.strip()]
assert len(done) == 98 and done[-1] == PREV, (len(done), done[-1])
s = open(d, encoding='utf-8').read()
if not s.endswith('\n'): s += '\n'
open(d, 'w', encoding='utf-8').write(s + TICK + '\n')
# reading list
rl = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
s = open(rl, encoding='utf-8').read()
assert s.rstrip().endswith('Next in the order file: ' + TICK + '.')
open(rl, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n' + open(R + 'fold_note.md', encoding='utf-8').read())
# shapes: count rows first
sh = 'Screens/SURVIVAL SHAPES - index.md'
s = open(sh, encoding='utf-8').read()
rows = [int(m.group(1)) for l in s.split('\n') for m in [re.match(r'^\| (\d+) \|', l)] if m]
assert len(rows) == 30 and max(rows) == 30, (len(rows), max(rows))
open(sh, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n' + open(R + 'shape_note.md', encoding='utf-8').read())
print('done')
