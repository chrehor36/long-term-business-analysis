import sys,re
f,pat=sys.argv[1],sys.argv[2]; a=int(sys.argv[3]) if len(sys.argv)>3 else 200; b=int(sys.argv[4]) if len(sys.argv)>4 else 1500; n=int(sys.argv[5]) if len(sys.argv)>5 else 3
t=open(f,encoding="utf-8").read()
for i,m in enumerate(re.finditer(pat,t)):
    if i>=n: break
    print("=== @",m.start(),":",re.sub(r"\s+"," ",t[max(0,m.start()-a):m.start()+b]),"\n")
