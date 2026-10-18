"""Check the AEE run file: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment that sits in the
same sentence-span as an id (the text between the previous id or line start and the id) is found in at least one of
the ids cited in that span. Curly and straight quotes and apostrophes are normalized for the comparison only."""
import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
RUN='../2026-10-18 Run - AEE Ameren.md'
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(RUN,encoding='utf-8').read()
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�','')
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
for m in re.finditer(r'\[E\d',t): print('E-id at',m.start()); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
# fragments: for each paragraph/line, split into segments ending at an id group
blocks=re.split(r'\n(?=\s*(?:- |\||#|\n))',t)
for ln,line in enumerate((b.replace('\n',' ') for b in blocks),1):
    # segments: text up to each run of ids
    pos=0
    for m in re.finditer(r'((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)',line):
        seg=line[pos:m.start()]; cited=re.findall(r'[MLR]\d{4}-\d{3}',m.group(1)); pos=m.end()
        for q in re.findall(r'"([^"]+)"|“([^”]+)”',seg):
            q=q[0] or q[1]
            parts=[p for p in re.split(r'\s*\[\.\.\.\]\s*',q) if p.strip()]
            for p in parts:
                if not any(norm(p) in norm(rows.get(c,'')) for c in cited):
                    print(f'L{ln}: fragment not in {cited}: "{p[:90]}"'); bad+=1
print('ids cited:',len(set(ids)),'problems:',bad)
