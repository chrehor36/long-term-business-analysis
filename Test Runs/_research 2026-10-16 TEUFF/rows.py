import sys,re
lines=open(sys.argv[1],encoding='utf-8').read().split('\n')[int(sys.argv[2]):int(sys.argv[3])]
buf=[]
for l in lines:
    s=l.strip().strip('|').strip()
    if not s: continue
    if re.search(r'[A-Za-z]{3}',s) and buf and re.search(r'\d',' '.join(buf)) :
        print(' '.join(buf)); buf=[]
    elif re.search(r'[A-Za-z]{3}',s) and buf:
        print(' '.join(buf)); buf=[]
    buf.append(s)
print(' '.join(buf))
