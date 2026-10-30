import re,sys
f=sys.argv[1]; 
t=open(f,encoding='utf-8',errors='replace').read()
t=re.sub(r'[ \t]+',' ',t)
pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 350
n=0
for m in re.finditer(pat,t,re.I):
    a=max(0,m.start()-w); b=min(len(t),m.end()+w)
    print('---',m.start()); print(t[a:b].replace('\n',' '))
    n+=1
    if n>=int(sys.argv[4]) if len(sys.argv)>4 else n>=12: break
