# check_quotes.py FILE : no E-ids; every M/L/R id exists in principle_ledger_v5.csv; each quoted fragment
# immediately preceding an id (on the same line, nearest "...") is a substring of that row (exact, then apostrophe-normalised).
import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
txt=open(sys.argv[1],encoding='utf-8').read()
bad=0
if re.search(r'\[E\d-\d+\]',txt): print('E-id found'); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',txt)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
norm=lambda s: s.replace('’',"'").replace('‘',"'").replace('�',"'").replace('“','"').replace('”','"')
n=0;flag=0
joined=re.sub(r'\n[ \t]*(?=\S)',' ',txt)
for line in joined.split('\n'):
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',line):
        pre=line[:m.start()]
        q=re.findall(r'"([^"]{6,})"\s*$',pre.rstrip()) or re.findall(r'"([^"]{6,})"[^"]{0,3}$',pre.rstrip())
        if not q: continue
        n+=1; print("  chk",m.group(1),q[-1][:50]) if "-v" in sys.argv else None; frag=q[-1].replace('[...]','\x00')
        parts=[p.strip() for p in frag.split('\x00') if p.strip()]
        row=rows.get(m.group(1),'')
        ok=all(p in row for p in parts) or all(norm(p) in norm(row) for p in parts)
        exact=all(p in row for p in parts)
        if not ok: print('NOT IN ROW',m.group(1),'|',frag[:120]); bad+=1
        elif not exact: print('apostrophe-normalised only',m.group(1),'|',frag[:80]); flag+=1
print(f'ids {len(set(ids))}, adjacent fragments {n}, failures {bad}, normalised-only {flag}')
