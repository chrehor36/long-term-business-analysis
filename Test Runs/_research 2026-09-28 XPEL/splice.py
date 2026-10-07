import sys
run='Test Runs/2026-09-28 Run - XPEL XPEL.md'
start_h, end_marker, frag = sys.argv[1], sys.argv[2], sys.argv[3]
L=open(run,encoding='utf-8').read().split('\n')
si=[i for i,l in enumerate(L) if l.startswith(start_h)]
assert len(si)==1, si
s=si[0]
e=[i for i,l in enumerate(L) if i>s and l.startswith(end_marker)]
assert e, 'no end'
e=e[0]
new=open(frag,encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:s]+new+['']+L[e:]
open(run,'w',encoding='utf-8').write('\n'.join(L))
print('replaced lines',s+1,'to',e,'with',len(new))
