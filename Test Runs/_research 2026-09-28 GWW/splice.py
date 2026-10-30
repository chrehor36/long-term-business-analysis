p = 'Test Runs/2026-09-28 Run - GWW W.W. Grainger.md'
L = open(p, encoding='utf-8').read().split('\n')
i = [k for k, l in enumerate(L) if l.startswith('## Q3 — ARE THEY HONEST') or l.startswith('## MATERIAL BENEATH THE CLOSE')]
assert len(i) == 1, i
tail = open('Test Runs/_research 2026-09-28 GWW/tail.md', encoding='utf-8').read()
open(p, 'w', encoding='utf-8').write('\n'.join(L[:i[0]]) + '\n' + tail)
print('written at line', i[0] + 1)
