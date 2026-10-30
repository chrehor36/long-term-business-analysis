import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(sys.argv[1], encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
bad = 0
if re.search(r"\[E\d", text): print("E-id found"); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); bad += 1
# quoted fragments immediately before an id (same paragraph, within 3 chars of **[)
for m in re.finditer(r'"([^"]{6,}?)"[^"\n]{0,4}\*\*\[([MLR]\d{4}-\d{3})\]', text):
    q, i = m.group(1), m.group(2)
    parts = [norm(p).strip(" .,") for p in q.split("[...]")]
    row = norm(rows.get(i, ""))
    for p in parts:
        if p and p not in row: print("NOT IN ROW", i, "|", p[:120]); bad += 1
print("ids:", len(set(ids)), "problems:", bad)
