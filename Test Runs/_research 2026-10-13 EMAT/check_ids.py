import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
def norm(s):
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()
eids = re.findall(r"\[E\d+-\d+\]", run)
print("E-ids:", eids or "none")
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
missing = sorted(set(i for i in ids if i not in rows))
print("ids cited:", len(set(ids)), "missing:", missing or "none")
bad = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run):
    i = m.group(1)
    start = max(run.rfind("**[", 0, m.start() - 1), run.rfind("\n\n", 0, m.start()), run.rfind("\n- ", 0, m.start()))
    window = run[start:m.start()]
    # the quoted fragment(s) closest before the id: take the last quote in the window
    quotes = re.findall(r"\"([^\"]{8,}?)\"|“([^”]{8,}?)”", window.replace("\n", " "))
    if not quotes: continue
    q = [a or b for a, b in quotes][-1]
    row = norm(rows.get(i, ""))
    parts = [p.strip(" .,;") for p in re.split(r"\[\.\.\.\]", norm(q))]
    ok = all(p in row for p in parts if p)
    if not ok:
        bad += 1
        print("CHECK", i, "|", q[:160])
print("fragments not found:", bad)
