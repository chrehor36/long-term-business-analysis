import sys
F='../2026-09-27 Run - JNJ Johnson & Johnson.md'
t=open(F,encoding='utf-8').read()
start,end,body=sys.argv[1],sys.argv[2],open(sys.argv[3],encoding='utf-8').read()
i=t.index(start); j=t.index(end,i)
assert t.count(start)==1, 'start not unique'
t=t[:i]+body+t[j:]
open(F,'w',encoding='utf-8',newline='\n').write(t)
print('ok',len(t))
