# replace the body of a section (from its heading line to the next '## ' heading) with the given file's text
import sys,re
p="Test Runs/2026-10-23 Run - EVRG Evergy.md"
head,frag=sys.argv[1],sys.argv[2]
s=open(p,encoding="utf-8").read()
new=open(frag,encoding="utf-8").read().rstrip("\n")+"\n\n"
i=s.index(head)
j=s.find("\n## ",i+len(head))
j = len(s) if j<0 else j+1
s=s[:i]+new+s[j:]
open(p,"w",encoding="utf-8",newline="\n").write(s)
print("ok",head)
