import re, sys
sys.stdout.reconfigure(encoding="utf-8")
L=open(sys.argv[1],encoding="utf-8",errors="replace").read().split("\n")
a,b=int(sys.argv[2]),int(sys.argv[3])
out=[];cur=""
for l in L[a:b]:
    s=l.strip().strip("|").strip()
    if not s: continue
    if re.match(r"^[\$\(\)\d,\.\-%| ]+$", s) or s in ("$","-",")"):
        cur+=" "+s.replace("|","").replace(" ","")
    else:
        if cur: out.append(cur)
        cur=s
out.append(cur); print("\n".join(o for o in out if o))
