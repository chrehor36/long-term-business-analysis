import sys,re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
f=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
L=open(f,encoding="utf-8").read().split("\n")
out=[]
for i in range(a,min(b,len(L))):
    s=L[i].strip()
    if s in ("|",""): continue
    out.append(f"[{i}]{s[:300]}")
print(" ".join(out))
