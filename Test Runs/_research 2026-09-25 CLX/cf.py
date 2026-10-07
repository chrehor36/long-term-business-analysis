import re,sys
f,key,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
t=open(f,encoding='utf-8').read()
idx=[m.start() for m in re.finditer(key,t)]
k=int(sys.argv[4]) if len(sys.argv)>4 else -1
s=t[idx[k]:idx[k]+n]
s=s.replace('|',' ')
s=re.sub(r'\(\s*([\d,\.]+)\s*\)',r'(\1)',s)
s=re.sub(r'\s+',' ',s)
s=re.sub(r' (?=[A-Z][a-z])','\n',s)
print(s)
