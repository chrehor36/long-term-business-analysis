# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment in the same sentence-chunk as an id appears verbatim in one of the ids cited beside it.
import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
run=open('Test Runs/2026-10-17 Run - SNIRF Senior plc.md',encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
norm=lambda s: re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('\ufffd','')).strip().lower()
bad=0
for e in re.findall(r'\[E\d-\d+\]',run): print('E-id found',e); bad+=1
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',run))
for i in sorted(ids):
    if i not in rows: print('MISSING id',i); bad+=1
# fragment check: split into chunks ending at an id group; quotes in a chunk must be in one of the ids that follow it
for chunk in re.split(r'(?<=\]\*\*)', run):
    cid=re.findall(r'\[([MLR]\d{4}-\d{3})\]',chunk)
    if not cid: continue
    last=chunk.rfind('**[')
    text=chunk[:last][-260:]
    # take the text after the previous id group only (the chunk already starts there)
    for q in re.findall(r'"([^"]{6,})"',text):
        nq=norm(q).replace('[...]','|')
        parts=[p.strip(' .,;') for p in nq.split('|') if p.strip(' .,;')]
        ok=any(all(p in norm(rows.get(c,'')) for p in parts) for c in cid)
        if not ok:
            print('QUOTE NOT IN ROW', cid, '::', q[:120]); bad+=1
print('ids:',len(ids),'problems:',bad)
