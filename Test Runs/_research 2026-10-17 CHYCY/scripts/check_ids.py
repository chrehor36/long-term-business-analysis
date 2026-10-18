# Check the run file: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv; (3) every quoted fragment
# that sits immediately beside an id (the quote just before **[ID]**, or ("...") just after it) is in that row.
# Fragments that fail are printed for a manual decision (a nearby quote may be a filing quote, not the row's).
import csv, re, sys
RUN = sys.argv[1]
LEDGER = sys.argv[2]
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(LEDGER, encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s.replace("“", '"').replace("”", '"')).strip()
fail = 0
eids = re.findall(r"\[E\d-\d+\]", text)
print("E-ids:", eids or "none"); fail += len(eids)
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
missing = sorted({i for i in ids if i not in rows})
print(f"ids cited: {len(ids)} ({len(set(ids))} distinct); missing from ledger: {missing or 'none'}"); fail += len(missing)
flat = norm(text)
checked = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", flat):
    i = m.group(1); row = norm(rows.get(i, ""))
    cands = []
    before = flat[max(0, m.start() - 260):m.start()]
    q = re.findall(r'"([^"]{4,400})"\s*(?:\(the [^)]*\))?\s*,?\s*$', before)
    if q: cands.append(q[-1])
    after = flat[m.end():m.end() + 300]
    q2 = re.match(r'\s*\(\s*"([^"]{4,400})"', after)
    if q2: cands.append(q2.group(1))
    for c in cands:
        checked += 1
        parts = [p.strip(" .,;") for p in c.split("[...]")]
        ok = all(norm(p) in row for p in parts if p)
        if not ok:
            fail += 1
            print(f"NOT IN ROW {i}: \"{c[:120]}\"")
print(f"fragments checked: {checked}; failures (incl. ids/E-ids): {fail}")
