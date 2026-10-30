import re,sys
f,a,b,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
L=open(f,encoding='utf-8').read().split('\n')[a-1:b]
s='\n'.join(L)
s=s.replace('\u200b',' ')
s=re.sub(r'[ \t]*\|[ \t]*',' | ',s)
s=re.sub(r'(\s*\|\s*)+\n','\n',s)
s=re.sub(r'\n\s*\|?\s*\n','\n',s)
s=re.sub(r'[ \t]+',' ',s)
open(out,'w',encoding='utf-8').write(s)
print(len(s))
