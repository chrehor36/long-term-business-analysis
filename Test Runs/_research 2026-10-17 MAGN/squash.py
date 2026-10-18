import sys,re
t=open(sys.argv[1],encoding='utf-8').read().split('\n')
a,b=int(sys.argv[2]),int(sys.argv[3])
s=' '.join(t[a-1:b])
s=s.replace('​',' ').replace('|',' ')
s=re.sub(r'\$\s+','$',s); s=re.sub(r'\(\s+','(',s); s=re.sub(r'\s+\)',')',s)
s=re.sub(r'\s+',' ',s)
import textwrap
print('\n'.join(textwrap.wrap(s,250)))
