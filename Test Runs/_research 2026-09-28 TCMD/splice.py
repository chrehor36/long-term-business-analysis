import sys
run="../2026-09-28 Run - TCMD Tactile Systems Technology.md"
body=open(sys.argv[1],encoding='utf-8').read()
start,end=sys.argv[2],sys.argv[3]
t=open(run,encoding='utf-8').read()
i=t.index(start); j=t.index(end) if end!='EOF' else len(t)
assert t.count(start)==1, start
t=t[:i]+body+(t[j:] if end!='EOF' else '')
open(run,'w',encoding='utf-8').write(t); print('ok',len(t))
