import re
D = 'Test Runs/_research 2026-09-27 KWR/'
P = 'Screens/SURVIVAL SHAPES - index.md'
t = open(P, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in t else '\n'
rows = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \|', t)]
print('shapes rows', len(rows), 'max', max(rows))
assert 'the KWR fold' not in t
n = open(D + 'shapes_note.md', encoding='utf-8').read().replace('@@ROWS@@', str(len(rows))).replace('@@MAX@@', str(max(rows)))
if not t.endswith('\n'):
    t += nl
t += n.lstrip('\n').replace('\n', nl)
open(P, 'w', encoding='utf-8', newline='').write(t)
R = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
r = open(R, encoding='utf-8', newline='').read()
nl2 = '\r\n' if '\r\n' in r else '\n'
assert 'UPDATE 2026-09-27 - KWR' not in r
if not r.endswith('\n'):
    r += nl2
r += open(D + 'fold_note.md', encoding='utf-8').read().replace('\n', nl2)
open(R, 'w', encoding='utf-8', newline='').write(r)
print('appended')
