import sys,re
f,pat,before,after=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
t=open(f,encoding='utf-8').read()
t=re.sub(r'\s+',' ',t)
for m in re.finditer(pat,t,re.I):
    print("<<<",t[max(0,m.start()-before):m.end()+after],">>>")
    print()
