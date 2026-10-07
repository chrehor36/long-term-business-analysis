import re,sys
f=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]); w=int(sys.argv[4]) if len(sys.argv)>4 else 4000
L=open(f,encoding='utf-8').read().split('\n')
for i in range(a-1,min(b,len(L))):
    s=L[i]
    s=re.sub(r'(\s*\|\s*)+',' | ',s); s=re.sub(r'\$ \|','$',s); s=re.sub(r'\| \$ \|','|',s); s=re.sub(r'\$\s*\|?\s*','',s)
    s=re.sub(r'\(\s*\|\s*',' (',s); s=re.sub(r'\s*\|\s*\)',')',s)
    print(i+1,':',s[:w])
