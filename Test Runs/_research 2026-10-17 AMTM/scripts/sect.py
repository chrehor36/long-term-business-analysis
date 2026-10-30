# replace the body under a heading (from heading line to the next '## ' heading) with new text from a file
import sys,re
p="Test Runs/2026-10-17 Run - AMTM Amentum.md"
head=sys.argv[1]; body=open(sys.argv[2],encoding="utf-8").read().rstrip("\n")+"\n"
s=open(p,encoding="utf-8").read()
lines=s.split("\n")
i=[k for k,l in enumerate(lines) if l.startswith(head)]
assert len(i)==1,(head,i)
i=i[0]
j=i+1
while j<len(lines) and not (lines[j].startswith("## ") or lines[j].startswith("---")):
    j+=1
new=lines[:i]+body.rstrip("\n").split("\n")+[""]+lines[j:]
open(p,"w",encoding="utf-8").write("\n".join(new))
print("replaced",head,i,j)
