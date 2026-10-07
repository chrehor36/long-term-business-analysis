import sys
run='Test Runs/2026-09-28 Run - MSA MSA Safety.md'
frag=sys.argv[1]; start=sys.argv[2]; end=sys.argv[3]
s=open(run,encoding='utf-8').read()
f=open(frag,encoding='utf-8').read()
i=s.index(start); j=s.index(end,i)
assert s.count(start)==1
s=s[:i]+f+s[j:]
open(run,'w',encoding='utf-8').write(s)
print('ok',len(s))
