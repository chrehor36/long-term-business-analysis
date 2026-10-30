# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that
# immediately precedes an id (in the same sentence chunk) is found in that row (quotes and apostrophes normalised).
import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
run=open(sys.argv[1],encoding='utf-8').read()
rows={r[0]:r[2] for r in csv.reader(open(sys.argv[2],encoding='utf-8'))}
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�',"'")
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
for m in re.finditer(r'\[E\d+-\d+\]',run): print('E-ID FOUND',m.group()); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING ID',i); bad+=1
# fragments: for each id occurrence, take the text since the previous id or line break, find quoted strings in it
pat=re.compile(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
pos=0; prev_end=0; checked=0
for m in pat.finditer(run):
    seg=run[prev_end:m.start()]
    # cut at last sentence boundary-ish: last ';' or '. ' outside quotes is hard; use the whole segment since previous id
    quotes=[(mm.group(1),mm.end()) for mm in re.finditer(r'"([^"]{3,})"',seg)]
    # a quote counts as beside the id when it ends within 60 characters of it
    quotes=[q for q,e in quotes if len(seg)-e<=60]
    if quotes:
        q=quotes[-1]
        parts=[p.strip(' .,;') for p in q.split('[...]')]
        rt=norm(rows.get(m.group(1),''))
        for p in parts:
            if p and norm(p) not in rt:
                print(f'FRAGMENT NOT IN ROW {m.group(1)}: "{p[:120]}"'); bad+=1
        checked+=1
    prev_end=m.end()
print(f'ids: {len(set(ids))} distinct, {len(ids)} uses; fragments checked: {checked}; problems: {bad}')
sys.exit(1 if bad else 0)
