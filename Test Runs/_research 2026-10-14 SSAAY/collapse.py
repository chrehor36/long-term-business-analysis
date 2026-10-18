import sys,re
s=open(sys.argv[1],encoding='utf-8').read()
s=' '.join(x.strip(' |') for x in s.split('\n') if x.strip(' |'))
s=re.sub(r'\$ ','$',s); s=re.sub(r'\( ','(',s); s=re.sub(r' \)',')',s)
open(sys.argv[1]+'.flat','w',encoding='utf-8').write(s)
