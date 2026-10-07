import sys,re
sys.stdout.reconfigure(encoding="utf-8")
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding="utf-8").read().split("\n")[a-1:b]
s=" ".join(x.strip() for x in L)
s=re.sub(r"(\s*\|\s*)+"," | ",s); s=re.sub(r"\$ \| ","$",s); s=re.sub(r"\( \| ","(",s)
print(s)
