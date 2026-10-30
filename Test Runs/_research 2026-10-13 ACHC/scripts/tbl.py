import sys,re
# collapse "| " cell separators into one line per row for a range of lines
lines=open(sys.argv[1],encoding='utf-8').read().split('\n')
a,b=int(sys.argv[2]),int(sys.argv[3])
buf=[]
for l in lines[a-1:b]:
    s=l.strip()
    if s in ('|',''): continue
    s=s.strip('| ').strip()
    if not s: continue
    if re.fullmatch(r'[\(\)\$%,\d\.\-—–]+',s) or s in ('$',')','%','(','—'):
        buf.append(s)
    else:
        if buf: print('   ', ' '.join(buf)); buf=[]
        print(s[:200])
if buf: print('   ',' '.join(buf))
