import sys
run = r'../2026-09-28 Run - WING Wingstop.md'
frag, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(run, encoding='utf-8').read()
f = open(frag, encoding='utf-8').read()
lines = s.split('\n')
si = [i for i, l in enumerate(lines) if l.startswith(start)]
ei = [i for i, l in enumerate(lines) if l.startswith(end)]
assert len(si) == 1 and len(ei) == 1 and si[0] < ei[0], (si, ei)
new = lines[:si[0]] + f.rstrip('\n').split('\n') + [''] + lines[ei[0]:]
open(run, 'w', encoding='utf-8').write('\n'.join(new))
print('spliced', si[0], ei[0])
