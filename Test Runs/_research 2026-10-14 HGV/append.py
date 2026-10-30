import sys
run="../2026-10-14 Run - HGV Hilton Grand Vacations.md"
part=open(sys.argv[1],encoding="utf-8").read()
t=open(run,encoding="utf-8").read()
if not t.endswith("\n"): t+="\n"
open(run,"w",encoding="utf-8").write(t+"\n"+part.strip("\n")+"\n")
print("appended",len(part))
