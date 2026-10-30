import sys
f='Test Runs/2026-09-27 Run - KRT Karat Packaging.md'
body=open(sys.argv[1],encoding='utf-8').read()
start,end=sys.argv[2],sys.argv[3]
s=open(f,encoding='utf-8').read()
assert s.count(start)==1, ('start',s.count(start))
i=s.index(start)
j=s.index(end,i) if end!='EOF' else len(s)
s=s[:i]+body+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('spliced',i,j)
