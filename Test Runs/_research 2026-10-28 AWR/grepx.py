import sys; sys.stdout.reconfigure(encoding="utf-8")
import sys,re
f,a,b,pat,w=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5]) if len(sys.argv)>5 else 700
L=open(f,encoding='utf-8').read().split('\n')
for i in range(a-1,min(b,len(L))):
    s=L[i]
    for m in re.finditer(pat,s,re.I):
        st=max(0,m.start()-w//3); print(i+1,'|',s[st:st+w].strip()); break
