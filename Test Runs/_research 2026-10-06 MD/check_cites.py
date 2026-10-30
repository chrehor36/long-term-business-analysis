import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
s=open('Test Runs/2026-10-06 Run - MD Pediatrix Medical Group.md',encoding='utf-8').read()
norm=lambda t:re.sub(r'\s+',' ',t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip().lower()
bad=0
if re.search(r'\bE\d-\d+\b|\[E\d',s): print('E-id found'); bad+=1
ids=set(re.findall(r'\[([LMR]\d{4}-\d{3})\]',s))
for i in sorted(ids):
    if i not in rows: print('MISSING',i); bad+=1
# each quoted fragment followed (within 6 chars) by one or more ids must be in one of those rows
for m in re.finditer(r'"([^"\n]{4,400})"((?:[\s,]*\*\*\[[LMR]\d{4}-\d{3}\]\*\*)+)',s):
    frag=m.group(1); ids_=re.findall(r'[LMR]\d{4}-\d{3}',m.group(2))
    parts=[p for p in re.split(r'\s*\[\.\.\.\]\s*',frag) if p.strip()]
    ok=any(all(norm(p) in norm(rows.get(i,'')) for p in parts) for i in ids_)
    if not ok: print('NOT IN ROW',ids_,'|',frag[:120]); bad+=1
print(len(ids),'ids;', 'FAIL' if bad else 'PASS', bad)
