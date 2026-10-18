import csv, re, sys
LEDGER='../../principle_ledger_v5.csv'
RUN='../2026-10-17 Run - HLEO Helio.md'
rows={r[0]:r[2] for r in csv.reader(open(LEDGER,encoding='utf-8-sig'))}
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('—','-').replace('–','-')
    return re.sub(r'\s+',' ',s).strip().lower()
txt=open(RUN,encoding='utf-8').read()
bad=0; nfr=0
ids=re.findall(r'\[([MLRE]\d{4}-\d{3}|E\d+-\d+)\]',txt)
for i in ids:
    if i.startswith('E') or re.match(r'E\d',i): print('E-ID',i); bad+=1
    elif i not in rows: print('MISSING',i); bad+=1
# quoted fragment immediately before one or more ids
for m in re.finditer(r'"([^"]{3,600}?)"\s*(?:\([^)]*\)\s*)?((?:,?\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)',txt):
    frag=m.group(1); idl=re.findall(r'\[([MLR]\d{4}-\d{3})\]',m.group(2))
    parts=[p for p in re.split(r'\[\.\.\.\]',frag) if p.strip()]
    nfr+=1
    for p in parts:
        if not any(norm(p) in norm(rows.get(i,'')) for i in idl):
            print('NOT IN ROW',idl,'::',p[:90]); bad+=1
print("fragments checked:",nfr); print("ids:",len(ids),'distinct:',len(set(ids)),'problems:',bad)
sys.exit(1 if bad else 0)
