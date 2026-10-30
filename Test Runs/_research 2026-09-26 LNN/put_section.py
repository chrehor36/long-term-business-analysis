import sys
run='Test Runs/2026-09-26 Run - LNN Lindsay.md'
sec,start,end=sys.argv[1],sys.argv[2],sys.argv[3]
t=open(run,encoding='utf-8').read(); s=open(sec,encoding='utf-8').read()
a=t.index(start); assert t.count(start)==1
b=t.index(end,a)
t=t[:a]+s.rstrip('\n')+'\n\n'+t[b:]
open(run,'w',encoding='utf-8').write(t); print('ok',a,b)
