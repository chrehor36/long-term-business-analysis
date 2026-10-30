import sys,re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
f=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
L=open(f,encoding="utf-8").read().split("\n")
mode=sys.argv[4] if len(sys.argv)>4 else "lines"
if mode=="join":
    print(re.sub(r"\s+"," "," ".join(L[a:b])).strip())
else:
    for i in range(a,min(b,len(L))): print(i, L[i])
