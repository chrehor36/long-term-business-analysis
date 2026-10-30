import sys,re
f,pat,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')
for i,l in enumerate(L):
    if re.search(pat,l,re.I):
        s=' '.join(x.strip() for x in L[i:i+n])
        s=re.sub(r'(\|\s*)+','| ',s); s=re.sub(r'\s+',' ',s)
        print(i,':',s[:700]); print()
