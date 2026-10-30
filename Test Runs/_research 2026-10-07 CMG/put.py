# replace the body of a run-file section (from its heading line to the next '## ' or '---' heading) with new text
import sys,re
p="Test Runs/2026-10-07 Run - CMG Chipotle.md"
head=sys.argv[1]; new=open(sys.argv[2],encoding='utf-8').read().rstrip('\n')+'\n'
s=open(p,encoding='utf-8').read()
i=s.index(head)
j=s.find('\n## ',i+len(head)); k=s.find('\n---\n',i+len(head))
ends=[x for x in (j,k) if x!=-1]; e=min(ends) if ends else len(s)
s=s[:i]+new+s[e:]
open(p,'w',encoding='utf-8').write(s)
print('ok',head)
