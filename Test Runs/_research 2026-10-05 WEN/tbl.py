import sys,re
f,start,n=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')[start-1:start-1+n]
s=' '.join(x.strip() for x in L)
s=re.sub(r'(\|\s*)+','| ',s)
s=re.sub(r'\s+',' ',s)
# break at alpha labels
s=re.sub(r' \| (?=[A-Z][a-z])','\n',s)
print(s)
