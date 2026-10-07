import sys
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')[a-1:b]
out=[]
for l in L:
    s=l.strip()
    if s in ('','|','$','| |','|  |'): continue
    out.append(s.replace(' | ','|'))
print(' ~ '.join(out))
