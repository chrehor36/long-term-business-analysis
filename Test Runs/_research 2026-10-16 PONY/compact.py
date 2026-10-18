import sys
L=open(sys.argv[1],encoding='utf-8').read().split('\n')
a,b=int(sys.argv[2]),int(sys.argv[3])
out=[]
for s in L[a:b]:
    s=s.strip().strip('|').strip().replace('​','')
    if s: out.append(s)
print(' ~ '.join(out))
