import sys,re
run='Test Runs/2026-09-26 Run - KEX Kirby.md'
start,end,src=sys.argv[1],sys.argv[2],sys.argv[3]
t=open(run,encoding='utf-8').read()
L=t.split('\n')
si=[i for i,l in enumerate(L) if l.strip()==start]; ei=[i for i,l in enumerate(L) if l.strip()==end]
assert len(si)==1 and len(ei)==1 and si[0]<ei[0], (si,ei)
new=open(src,encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:si[0]]+new+['']+L[ei[0]:]
open(run,'w',encoding='utf-8',newline='\n').write('\n'.join(L))
print('ok',len(L))
