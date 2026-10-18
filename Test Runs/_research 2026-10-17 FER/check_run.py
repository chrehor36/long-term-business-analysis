import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
run,ledger=sys.argv[1],sys.argv[2]
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(ledger,encoding='utf-8-sig'))}
t=open(run,encoding='utf-8').read()
def norm(s):
    s=s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2014','-').replace('\u2013','-')
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
eids=re.findall(r'\[E\d-\d+\]',t)
if eids: print('E-ids found',eids); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
# quoted fragment followed by one or more ids
flat=re.sub(r'\s+',' ',t)
for m in re.finditer(r'"([^"]{3,400})"((?:[^"\[]{0,40}?\*\*\[[MLR]\d{4}-\d{3}\]\*\*,?\s*)+)',flat):
    frag=m.group(1); idl=re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    parts=[norm(x) for x in frag.split('[...]') if x.strip()]
    ok=any(all(pp.strip(' .,') in norm(rows.get(i,'')) for pp in parts) for i in idl)
    if not ok: print('FRAGMENT NOT IN ROW',idl,'::',frag[:120]); bad+=1
print('ids:',len(set(ids)),'problems:',bad)
