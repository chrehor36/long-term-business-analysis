import csv,re,sys,unicodedata
run=open(sys.argv[1],encoding='utf8').read()
rows={}
with open('principle_ledger_v5.csv',encoding='utf8',newline='') as f:
    r=csv.reader(f);h=next(r)
    for row in r: rows[row[0]]=' '.join(row)
def n(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('\u2019',"'"),('\u2018',"'"),('\u201c','"'),('\u201d','"'),('\u2014','-'),('\u2013','-')]: s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).lower()
bad=0;ids=re.findall(r'\[([MLRE]\d{4}-\d{3})\]',run)
print('ids',len(ids),'distinct',len(set(ids)),'E-ids',[i for i in ids if i.startswith('E')])
for i in set(ids):
    if i not in rows: print('MISSING',i);bad+=1
for m in re.finditer(r'"([^"]{6,}?)"\s*\*\*\[([MLR]\d{4}-\d{3})\]',n(run).replace('**[','**[') if False else run):
    pass
txt=run
for m in re.finditer(r'["\u201c]([^"\u201c\u201d]{6,}?)["\u201d][^\[\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',txt):
    q,i=m.group(1),m.group(2)
    parts=[p.strip(' .,;') for p in re.split(r'\[\.\.\.\]|\.\.\.',q) if p.strip(' .,;')]
    for p in parts:
        if n(p) not in n(rows.get(i,'')): print('SLIP',i,repr(p[:90]));bad+=1
print('bad',bad)
