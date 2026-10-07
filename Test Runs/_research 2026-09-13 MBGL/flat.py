import sys,re,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')[a-1:b]
t=' '.join(x.strip() for x in L)
t=t.replace(' ',' ')
t=re.sub(r'\s*\|\s*',' ',t)
t=re.sub(r'\$\s+','$',t); t=re.sub(r'\(\s+','(',t); t=re.sub(r'\s+\)',')',t); t=re.sub(r'\s+%','%',t)
t=re.sub(r'\s+',' ',t)
w=int(sys.argv[4]) if len(sys.argv)>4 else 250
for i in range(0,len(t),w): print(t[i:i+w])
