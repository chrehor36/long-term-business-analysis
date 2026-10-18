import sys,re
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')[a-1:b]
out=' '.join(x.strip() for x in L if x.strip())
out=re.sub(r'\s+',' ',out)
import textwrap
print('\n'.join(textwrap.wrap(out,220)))
