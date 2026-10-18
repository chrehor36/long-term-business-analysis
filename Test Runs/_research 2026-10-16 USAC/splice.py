import sys
p="Test Runs/2026-10-16 Run - USAC USA Compression Partners.md"
start,end,src=sys.argv[1],sys.argv[2],sys.argv[3]
s=open(p,encoding='utf-8').read()
new=open(src,encoding='utf-8').read()
a=s.index(start); b=s.index(end) if end!='EOFILE' else len(s)
s=s[:a]+new.rstrip('\n')+"\n\n"+s[b:]
open(p,'w',encoding='utf-8').write(s)
