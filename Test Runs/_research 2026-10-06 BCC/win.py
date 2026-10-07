import sys,re
f,pat,n=sys.argv[1],sys.argv[2],int(sys.argv[3]); k=int(sys.argv[4]) if len(sys.argv)>4 else 1
L=open(f,encoding='utf-8').read().split('\n')
hits=[i for i,l in enumerate(L) if re.search(pat,l)]
for h in hits[:k]:
    s=' '.join(x.strip() for x in L[h:h+n])
    s=re.sub(r'(\|\s*)+','| ',s); s=re.sub(r'\$\s*\|?\s*','$',s)
    print(f'--- line {h}:',s[:3000]); print()
