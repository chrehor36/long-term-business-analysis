import re,sys
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
t=open(f,encoding='utf-8').read().split('\n')
s='\n'.join(t[a:b]).replace('​','')
s=re.sub(r'\n\s*\|\s*(?=\n)','',s)
s=re.sub(r'\n\s*\|\s*',' | ',s)
s=re.sub(r'(\|\s*)+\|',' |',s)
print(s)
