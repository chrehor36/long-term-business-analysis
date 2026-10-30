import sys
run = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-27 Run - AIT Applied Industrial Technologies.md'
start_mark, end_mark, body = sys.argv[1], sys.argv[2], sys.argv[3]
L = open(run, encoding='utf-8').read().split('\n')
si = [i for i, l in enumerate(L) if l.startswith(start_mark)]
assert len(si) == 1, si
ei = [i for i, l in enumerate(L) if i > si[0] and l.startswith(end_mark)]
assert ei, 'no end'
e = ei[0]
new = open(body, encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:si[0]] + new + L[e + 1:]
open(run, 'w', encoding='utf-8').write('\n'.join(L))
print('replaced lines', si[0] + 1, 'to', e + 1, 'with', len(new))
