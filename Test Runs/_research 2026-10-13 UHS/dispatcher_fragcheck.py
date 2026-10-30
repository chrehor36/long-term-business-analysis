import csv,re,sys
L={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf8'))}
hdr=next(csv.reader(open('principle_ledger_v5.csv',encoding='utf8')))
qi=[i for i,h in enumerate(hdr) if 'quote' in h.lower()][0]
t=open(sys.argv[1],encoding='utf8').read()
norm=lambda s:re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
bad=0;n=0
print('E-ids:',re.findall(r'\[E\d-\d+\]',t))
for m in re.finditer(r'\*\*\[?((?:[MLR]\d{4}-\d{3}[a-z]?)(?:[,;] ?[MLR]\d{4}-\d{3}[a-z]?)*)\]?\*\*',t):
    ids=re.findall(r'[MLR]\d{4}-\d{3}[a-z]?',m.group(1))
    for i in ids:
        if i not in L: print('PHANTOM',i);bad+=1
    pre=t[max(0,m.start()-400):m.start()]
    q=re.findall(r'[\"\u201c]([^\"\u201c\u201d]{6,})[\"\u201d]\s*[\(\[]?\s*$',pre.rstrip(' ,;'))
    if not q: continue
    n+=1
    frags=[f for f in re.split(r'\[\.\.\.\]|\.\.\.',q[-1]) if len(f.strip())>3]
    src=' '.join(norm(L[i][qi]) for i in ids if i in L)
    for f in frags:
        if norm(f).strip(' .,;:') not in src: print('SLIP',ids,repr(f[:90]));bad+=1
print('quoted cites checked',n,'problems',bad)
