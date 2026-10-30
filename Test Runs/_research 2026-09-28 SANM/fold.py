import re
R = 'Test Runs/_research 2026-09-28 SANM/'
q = 'Screens/WATCHLIST RUN QUEUE.md'
L = open(q, encoding='utf-8').read().split('\n')
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']; assert len(h) == 1, h
assert L[h[0] + 1].startswith('- **WING ('), L[h[0] + 1][:40]
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h[0] + 1] + entry + L[h[0] + 1:]
open(q, 'w', encoding='utf-8').write('\n'.join(L))
# done file
d = 'Screens/_daily/_wave7_done.txt'
s = open(d, encoding='utf-8').read()
if not s.endswith('\n'): s += '\n'
open(d, 'w', encoding='utf-8').write(s + 'WING\n')
# reading list
rl = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
s = open(rl, encoding='utf-8').read()
assert s.rstrip().endswith('Next in the order file: SANM.')
open(rl, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n' + open(R + 'fold_note.md', encoding='utf-8').read())
# shapes
sh = 'Screens/SURVIVAL SHAPES - index.md'
s = open(sh, encoding='utf-8').read()
open(sh, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n' + open(R + 'shape_note.md', encoding='utf-8').read())
print('done')
