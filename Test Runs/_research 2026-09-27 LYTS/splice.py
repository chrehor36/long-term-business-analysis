import sys
run='Test Runs/2026-09-27 Run - LYTS LSI Industries.md'
body,start,end=sys.argv[1],sys.argv[2],sys.argv[3]
t=open(run,encoding='utf-8').read()
i=t.index(start); j=t.index(end,i+1) if end!='EOF' else len(t)
assert t.count(start)==1, 'start not unique'
b=open(body,encoding='utf-8').read()
if not b.endswith('\n'): b+='\n'
t=t[:i]+b+('\n' if end!='EOF' else '')+t[j:]
open(run,'w',encoding='utf-8').write(t)
print('ok',len(t))
