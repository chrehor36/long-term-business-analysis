import sys
run='../2026-09-28 Run - ECL Ecolab.md'
frag, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
L=open(run,encoding='utf-8').read().split('\n')
si=[i for i,l in enumerate(L) if l==start]; ei=[i for i,l in enumerate(L) if l==end]
assert len(si)==1 and len(ei)==1 and si[0]<ei[0], (si,ei)
F=open(frag,encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:si[0]]+F+['']+L[ei[0]:]
open(run,'w',encoding='utf-8').write('\n'.join(L))
print('ok', si, ei, len(F))
