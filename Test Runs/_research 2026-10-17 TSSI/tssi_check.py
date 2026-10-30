# Id check for the TSSI run: no E-ids; every M/L/R id in the v5 ledger; every quote immediately before an id is in that row.
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run = open(sys.argv[1], encoding="utf-8").read()
rows = {x["\ufeffid"]: x["quote_verbatim"] for x in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8"))}
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
bad = 0
eids = re.findall(r"\bE\d+-\d+\b", run)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
missing = sorted({i for i in ids if i not in rows})
print(f"ids cited: {len(ids)} ({len(set(ids))} distinct); missing: {missing or 'none'}"); bad += len(missing)
checked = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run):
    before = run[max(0, m.start()-1500):m.start()]
    q = re.search(r'"([^"]+)"\s*(\([^)]*\))?\s*$', before)
    if not q: continue
    frag = q.group(1)
    row = norm(rows.get(m.group(1), ""))
    parts = [p.strip(" .,;:") for p in re.split(r"\[\.\.\.\]", frag)]
    ok = all(norm(p) in row for p in parts if p)
    checked += 1
    if not ok:
        bad += 1; print("NOT IN ROW:", m.group(1), "|", frag[:160])
print("quotes checked beside ids:", checked)
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
