import sys
run='../2026-09-27 Run - JKHY Jack Henry.md'
start,end,body=sys.argv[1],sys.argv[2],sys.argv[3]
s=open(run,encoding='utf-8').read()
lines=s.split('\n')
si=[i for i,l in enumerate(lines) if l.startswith(start)]
assert len(si)==1,(start,si)
si=si[0]
ei=[i for i,l in enumerate(lines) if i>si and l.startswith(end)]
assert ei,(end)
ei=ei[0]
b=open(body,encoding='utf-8').read().rstrip('\n').split('\n')
lines=lines[:si]+b+lines[ei:]
open(run,'w',encoding='utf-8',newline='\n').write('\n'.join(lines))
print('replaced',si,ei,'with',len(b),'lines')
