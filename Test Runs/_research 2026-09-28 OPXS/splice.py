import sys
run='Test Runs/2026-09-28 Run - OPXS Optex Systems Holdings.md'
body=open(sys.argv[1],encoding='utf-8').read()
start,end=sys.argv[2],sys.argv[3]
s=open(run,encoding='utf-8').read()
i=s.index(start); j=s.index(end,i+len(start)) if end!='EOF' else len(s)
assert s.count(start)==1, start
s=s[:i]+body+s[j:]
open(run,'w',encoding='utf-8',newline='\n').write(s)
print('ok',len(s))
