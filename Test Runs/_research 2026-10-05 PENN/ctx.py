import sys,re
f,pat=sys.argv[1],sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 300; lim=int(sys.argv[4]) if len(sys.argv)>4 else 5
s=open(f,encoding="utf-8",errors="ignore").read()
for i,m in enumerate(re.finditer(pat,s,re.I)):
    if i>=lim: break
    a=max(0,m.start()-n); b=min(len(s),m.end()+n)
    print("--",f,m.start()); print(re.sub(r"\s+"," ",s[a:b]))
