import sys,io
RUN='../2026-09-27 Run - KWR Quaker Houghton.md'
body=open(sys.argv[1],encoding='utf-8').read()
start,end=sys.argv[2],sys.argv[3]
t=open(RUN,encoding='utf-8').read()
i=t.index(start); j=t.index(end,i) if end!='EOF' else len(t)
assert t.count(start)==1, start
t=t[:i]+body+t[j:]
open(RUN,'w',encoding='utf-8',newline='\n').write(t)
print('ok',len(t))
