# usage: splice.py <section-file> <start-marker> <end-marker>
import sys
p="Test Runs/2026-10-16 Run - VSEC VSE Corporation.md"
s=open(p,encoding='utf-8').read()
new=open(sys.argv[1],encoding='utf-8').read()
a=s.index(sys.argv[2]); b=s.index(sys.argv[3])
open(p,'w',encoding='utf-8').write(s[:a]+new.rstrip('\n')+'\n\n'+s[b:])
print('ok',a,b)
