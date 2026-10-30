import sys,re
f=sys.argv[1]; pats=sys.argv[2:]
s=re.sub(r'\s+',' ',open(f,encoding='utf-8').read())
for p in pats:
    for m in re.finditer(p,s,re.I):
        a=max(0,m.start()-int(350)); b=min(len(s),m.end()+450)
        print('>>',p,'@',m.start(),':',s[a:b]); print()
