import sys
p="Test Runs/2026-10-23 Run - EVRG Evergy.md"
a,b,frag=sys.argv[1],sys.argv[2],sys.argv[3]
s=open(p,encoding="utf-8").read()
new=open(frag,encoding="utf-8").read().rstrip("\n")+"\n"
i=s.index(a); j=s.index(b,i)
s=s[:i]+new+s[j:]
open(p,"w",encoding="utf-8",newline="\n").write(s)
print("ok")
