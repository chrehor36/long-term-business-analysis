import sys
run=r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-27 Run - MEDP Medpace Holdings.md'
start,end,body=sys.argv[1],sys.argv[2],sys.argv[3]
L=open(run,encoding='utf-8').read().split('\n')
si=[i for i,l in enumerate(L) if l.startswith(start)]; assert len(si)==1,(start,si)
if end=='EOF': ei=len(L)
else:
    ei=[i for i,l in enumerate(L) if l.startswith(end) and i>si[0]]; assert ei,(end); ei=ei[0]
B=open(body,encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:si[0]]+B+['']+L[ei:]
open(run,'w',encoding='utf-8').write('\n'.join(L))
print('spliced',si[0],ei,len(B))
