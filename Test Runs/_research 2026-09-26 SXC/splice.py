import sys
p='../2026-09-26 Run - SXC SunCoke Energy.md'
s=open(p,encoding='utf-8').read()
start=s.index(sys.argv[1]); end=s.index(sys.argv[2])
new=open(sys.argv[3],encoding='utf-8').read().rstrip('\n')+'\n\n'
s=s[:start]+new+s[end:]
open(p,'w',encoding='utf-8').write(s)
print('ok')
