# Dispatcher's citation check (overnight 2026-10-16, KBR; copied from the ACM fold): every quoted fragment within 60 chars before a v5 id must be in that row.
import csv,re,sys
run=open(sys.argv[1],encoding='utf-8').read()
rows={x['id']:x['quote_verbatim'] for x in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
def n(s): return re.sub(r'\s+',' ',s.translate(str.maketrans({'\u2019':"'",'\u2018':"'",'\u201c':'"','\u201d':'"','\u2014':'-','\u2013':'-'}))).strip().lower()
bad=0; cnt=0
for m in re.finditer(r'\[([MLR]\d{4}-\d{3})\]',run):
    i=m.group(1); cnt+=1
    if i not in rows: print('MISSING',i); bad+=1; continue
    seg=run[max(0,m.start()-600):m.start()]
    q=list(re.finditer(r'["\u201c]([^"\u201c\u201d]{3,}?)["\u201d]',seg))
    if not q or len(seg)-q[-1].end()>60: continue
    for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026',n(q[-1].group(1))):
        p=p.strip(' .,;:')
        if p and p not in n(rows[i]): print('SLIP',i,'|',q[-1].group(1)[:100]); bad+=1
print('ids',cnt,'problems',bad, 'E-ids', len(re.findall(r'\[E\d-\d+\]',run)))
