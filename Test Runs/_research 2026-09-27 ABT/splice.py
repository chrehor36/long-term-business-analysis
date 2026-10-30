import sys
R='../2026-09-27 Run - ABT Abbott Laboratories.md'
s=open(R,encoding='utf-8').read()
body=open(sys.argv[1],encoding='utf-8').read()
start=s.index(sys.argv[2]); end=s.index(sys.argv[3])
s=s[:start]+body.rstrip('\n')+'\n\n'+s[end:]
open(R,'w',encoding='utf-8').write(s)
print('ok', len(s))
