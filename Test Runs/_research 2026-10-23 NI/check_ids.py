import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
txt=open('Test Runs/2026-10-23 Run - NI NiSource.md',encoding='utf-8').read()
def norm(s):
    s=s.replace('�',' ').replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('—','-').replace('–','-')
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
eids=re.findall(r'\[E\d-\d+\]',txt)
if eids: print('E-ids found:',eids); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',txt)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
# fragments: a double-quoted string followed within 3 chars by **[ID]**
pat=re.compile(r'"((?:[^"]|""|"(?=[^"]*"\s*\*\*))*?)"\s{0,3}(\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)*)')
n=0
for m in re.finditer(r'"([^"\n]{3,600}?)"\s{0,3}((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)',txt.replace('\n',' ')):
    frag=m.group(1); idl=re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    parts=[p for p in re.split(r'\s*\[\.\.\.\]\s*',frag) if p.strip()]
    ok=any(all(norm(p) in norm(rows.get(i,'')) for p in parts) for i in idl)
    n+=1
    if not ok:
        print('FRAGMENT NOT IN ROW',idl,'::',frag[:160]); bad+=1
print(f'{len(set(ids))} distinct ids, {n} quoted fragments checked, problems: {bad}')
