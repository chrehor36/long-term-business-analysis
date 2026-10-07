import sys,re
f,start,n=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')
t=' '.join(L[start-1:start-1+n])
t=re.sub(r'\|\s*\|',' ',t); t=re.sub(r'\|',' ',t); t=re.sub(r'\$\s+','$',t); t=re.sub(r'\(\s*([\d,\.]+)\s*\)?\s*\)',r'(\1)',t)
t=re.sub(r'\s+',' ',t)
print(t)
