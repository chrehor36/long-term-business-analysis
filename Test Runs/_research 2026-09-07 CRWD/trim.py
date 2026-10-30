import os,re,glob
d=os.path.join(os.path.dirname(os.path.abspath(__file__)),'stmts')
for p in glob.glob(os.path.join(d,'*.txt')):
    t=open(p,encoding='utf-8').read()
    # cut everything from the first XBRL element-definition block
    m=re.search(r'\nX\s*\n\s*\n?[-+] (Definition|References)',t)
    if m: t=t[:m.start()]
    t=re.sub(r'\n{3,}','\n\n',t)
    open(p,'w',encoding='utf-8').write(t)
print("trimmed", len(glob.glob(os.path.join(d,'*.txt'))))
