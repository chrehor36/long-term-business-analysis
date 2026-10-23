import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run = open("Test Runs/2026-10-23 Run - EDN Edenor.md", encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
norm = lambda s: re.sub(r"\s+", " ", s).strip()
problems = 0
if re.search(r"\[E\d", run): print("E-id found"); problems += 1
ids = list(re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run))
for m in ids:
    if m.group(1) not in rows: print("MISSING", m.group(1)); problems += 1
# fragments: quoted text that ends within 40 characters before an id (the fragment set beside it)
prev_end = 0
for m in ids:
    start = max(prev_end, run.rfind("\n\n", 0, m.start()))
    seg = run[start:m.start()]
    prev_end = m.end()
    for qm in re.finditer(r"\"([^\"]+)\"", seg):
        q = qm.group(1)
        if len(seg) - qm.end() > 40:   # only the fragment set directly beside the id
            continue
        if m.group(1) in rows and norm(q) not in norm(rows[m.group(1)]):
            print(f"NOT IN ROW {m.group(1)}: {norm(q)[:120]}")
            problems += 1
print("ids:", len(ids), "distinct:", len({m.group(1) for m in ids}), "problems:", problems)
