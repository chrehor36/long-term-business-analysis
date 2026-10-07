import csv, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
run = open("Test Runs/2026-10-06 Run - ADT ADT Inc.md", encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
bad = 0
print("em dashes:", run.count("—"), " en dashes:", run.count("–"))
eids = re.findall(r"\[E\d+-\d+\]", run); print("E-ids:", eids)
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
allids = re.findall(r"\[([A-Z]\d{4}-\d{3})\]", run)
missing = sorted(set(i for i in allids if i not in rows)); print("ids cited:", len(set(allids)), "missing:", missing)
bad += len(missing) + len(eids)
# every quoted fragment immediately before an id (allowing ' (...)' or text-free gap) must be in that row
norm = lambda s: s.replace("“", '"').replace("”", '"')
for m in re.finditer(r'"([^"\n]{3,400})"\)?\s*(?:\*\*\[([MLR]\d{4}-\d{3})\]\*\*)', run):
    frag, i = m.group(1), m.group(2)
    pieces = [p.strip() for p in frag.split("[...]") if p.strip()]
    for p in pieces:
        if norm(p) not in norm(rows[i]):
            print("NOT IN ROW", i, "::", p); bad += 1
# fragments in the form **[ID]** ("...") 
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*\s*\("([^"\n]{3,400})"\)', run):
    i, frag = m.group(1), m.group(2)
    if norm(frag) not in norm(rows[i]): print("NOT IN ROW (paren)", i, "::", frag); bad += 1
# ids with no quoted fragment adjacent: list for manual review
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run):
    before = run[max(0, m.start()-3):m.start()]
    after = run[m.end():m.end()+3]
    if '"' not in before and '("' not in after:
        ctx = run[max(0, m.start()-90):m.end()].replace("\n", " ")
        print("  no adjacent quote:", m.group(1), "|", ctx)
print("BAD:", bad)
