import sys, io
# usage: splice.py fragment start_marker end_marker(inclusive line startswith)
run = '../2026-09-28 Run - KEYS Keysight Technologies.md'
frag, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
L = open(run, encoding='utf-8').read().split('\n')
si = [i for i, l in enumerate(L) if l.startswith(start)]
assert len(si) == 1, (start, si)
si = si[0]
ei = [i for i, l in enumerate(L) if i > si and l.startswith(end)]
assert ei, end
ei = ei[0]
F = open(frag, encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:si] + F + L[ei+1:]
open(run, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
print('replaced lines', si+1, 'to', ei+1, 'with', len(F))
