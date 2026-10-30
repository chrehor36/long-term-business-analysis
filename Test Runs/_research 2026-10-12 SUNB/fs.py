import re,sys
L=open(sys.argv[1],encoding='utf-8').read().split('\n')
a,b=int(sys.argv[2]),int(sys.argv[3])
s=' '.join(x.strip().strip('|').strip() for x in L[a-1:b])
s=re.sub(r'\s+',' ',s)
print(s)
