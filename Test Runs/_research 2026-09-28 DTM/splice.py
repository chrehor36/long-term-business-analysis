import sys
run='../2026-09-28 Run - DTM DT Midstream.md'
body=open(sys.argv[1],encoding='utf-8').read()
start,end=sys.argv[2],sys.argv[3]
s=open(run,encoding='utf-8').read()
i=s.index(start); j=s.index(end)
assert s.count(start)==1 and s.count(end)==1, (s.count(start),s.count(end))
s=s[:i]+body+s[j:]
open(run,'w',encoding='utf-8').write(s)
print('ok',len(s))
