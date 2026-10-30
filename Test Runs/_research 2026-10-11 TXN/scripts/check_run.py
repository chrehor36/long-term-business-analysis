import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-11 Run - TXN Texas Instruments.md"
LED = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(LED, encoding="utf-8-sig"))}
t = open(RUN, encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')).strip()
# 1. E-ids
eids = re.findall(r"\[E\d+-\d+\]", t)
print("E-ids:", eids or "none")
# 2. every M/L/R id resolves
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", t)
missing = sorted(set(i for i in ids if i not in rows))
print(f"ids cited: {len(ids)} occurrences, {len(set(ids))} distinct; missing: {missing or 'none'}")
# 3. quoted fragments beside an id: quotes between the previous id group (or paragraph start) and an id group
problems = []; checked = 0
paras = re.split(r"\n\s*\n", t)
for p in paras:
    p1 = p.replace("\n", " ")
    pos = 0
    for m in re.finditer(r"((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)", p1):
        seg = p1[pos:m.start()]; pos = m.end()
        grp = re.findall(r"[MLR]\d{4}-\d{3}", m.group(1))
        # only the quote(s) in the clause immediately before the id group: after the last sentence/semicolon break
        clause = re.split(r"(?<=[.;:])\s+(?=[A-Z(*])", seg)[-1] if seg else ""
        qs = re.findall(r"\"([^\"]{3,})\"", clause)
        for k, q in enumerate(qs):
            nearest = (k == len(qs) - 1)
            checked += 1
            parts = [norm(x) for x in q.split("[...]") if norm(x)]
            ok = any(all(pp.lower() in norm(rows.get(g, "")).lower() for pp in parts) for g in grp)
            if not ok:
                problems.append(("NEAREST" if nearest else "earlier-in-clause", grp, q[:140]))
print(f"quoted fragments checked beside ids: {checked}; not found in the row: {len(problems)}")
for kind, g, q in problems:
    print("  ", kind, g, "|", q)
