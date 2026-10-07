import sys,re
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')[a-1:b]
t='\n'.join(L)
t=re.sub(r'\s*\|\s*(\|\s*)*',' | ',t)
t=re.sub(r'\$ \| ','$',t)
t=re.sub(r'\( \| ','(',t)
t=re.sub(r' \| \)',')',t)
t=re.sub(r'\n(\s*\|\s*)+\n','\n',t)
t=re.sub(r'\n\s*\|\s*','\n',t)
print(t)
