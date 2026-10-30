import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
bad = 0
eids = re.findall(r'\[E\d-\d+\]', run)
print("E-ids:", eids or "none")
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
missing = sorted(set(i for i in ids if i not in rows))
print("ids cited:", len(set(ids)), "missing:", missing or "none")
bad += len(missing) + len(eids)
# fragments: a quoted string followed (within 3 chars) by one or more bold ids
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('�', "'"))
n = 0
for m in re.finditer(r'"([^"\n]{6,})"\s{0,3}((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)', run):
    frag = m.group(1)
    cited = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [p.strip(' .,') for p in frag.split('[...]') if p.strip(' .,')]
    ok = any(all(norm(p) in norm(rows.get(c, '')) for p in parts) for c in cited)
    n += 1
    if not ok:
        bad += 1
        print("NOT FOUND:", cited, "|", frag[:120])
print("fragments checked:", n, "failures:", bad)
