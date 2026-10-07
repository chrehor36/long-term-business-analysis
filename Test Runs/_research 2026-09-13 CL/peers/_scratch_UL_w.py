import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
# usage: file regex [before] [after] [maxhits]
f=sys.argv[1]; pat=re.compile(sys.argv[2],re.I)
b=int(sys.argv[3]) if len(sys.argv)>3 else 200
a=int(sys.argv[4]) if len(sys.argv)>4 else 400
mx=int(sys.argv[5]) if len(sys.argv)>5 else 30
L=open(f,encoding="utf-8").read().split("\n")
n=0
for i,l in enumerate(L):
    for m in pat.finditer(l):
        n+=1
        if n>mx: break
        print(f"[{i}@{m.start()}] ...{l[max(0,m.start()-b):m.end()+a]}...\n")
print("hits",n)
