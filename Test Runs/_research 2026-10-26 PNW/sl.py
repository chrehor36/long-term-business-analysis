import sys,re
sys.stdout.reconfigure(encoding='utf-8')
t=open('cache/'+sys.argv[1]+'.txt',encoding='utf-8').read();a,b=int(sys.argv[2]),int(sys.argv[3])
s=t[a:b]; s=re.sub(r'\n[\s|]*\n','\n',s); s=re.sub(r'\s*\|\s*(\n\s*\|\s*)+',' | ',s); s=re.sub(r'[ \t]+',' ',s)
print(s)
