import csv, re, sys
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
txt = open("Test Runs/2026-10-06 Run - ASO Academy Sports.md", encoding="utf-8").read()
ids = re.findall(r"\[([A-Z]+\d{0,4}-\d{2,3})\]", txt)
bad = [i for i in ids if i not in rows]
eids = [i for i in ids if i.startswith("E")]
print("ids cited:", len(ids), "distinct:", len(set(ids)), "missing:", bad, "E-ids:", eids)
norm = lambda s: re.sub(r"\s+", " ", s).strip()
fails = 0; checked = 0
# segments: text between consecutive ids; reset after filing-source parentheticals
pos = 0
for m in re.finditer(r"\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*", txt):
    seg = txt[pos:m.start()]; pos = m.end()
    cut = max(seg.rfind(k) for k in ("(10-K", "(10-Q", "(DEF 14A", "(8-K", "(prospectus", "(DKS", "Item 1A)", "(XBRL"))
    if cut >= 0: seg = seg[cut:]
    # paragraph start resets too
    if "\n\n" in seg: seg = seg[seg.rfind("\n\n"):]
    quotes = re.findall(r'"([^"]{6,}?)"(?=[^"]*$|[\s,.;:)\]*])', seg)
    quotes = re.findall(r'"(.+?)"', seg.replace("\n", " "))
    for q in quotes:
        for piece in q.split("[...]"):
            p = norm(piece).strip(" .,;:")
            if len(p) < 4: continue
            checked += 1
            if norm(p) not in norm(rows[m.group(1)]):
                fails += 1; print("NOT IN ROW", m.group(1), "|", p[:120])
print("fragments checked:", checked, "failures:", fails)
