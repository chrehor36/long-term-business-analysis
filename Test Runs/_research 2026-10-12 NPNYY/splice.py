import sys
p="Test Runs/2026-10-12 Run - NPNYY Nippon Yusen.md"
s=open(p,encoding="utf-8").read()
new=open(sys.argv[1],encoding="utf-8").read().rstrip()+"\n\n"
a=s.index(sys.argv[2]); b=s.index(sys.argv[3])
s=s[:a]+new+s[b:]
open(p,"w",encoding="utf-8").write(s)
