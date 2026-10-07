import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')
out=[]
for l in L[a-1:b]:
    s=l.replace('\u200b','').strip()
    if s: out.append(s)
print(' | '.join(out))
