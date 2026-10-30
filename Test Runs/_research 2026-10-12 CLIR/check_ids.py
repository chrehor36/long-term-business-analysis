import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(sys.argv[1], encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')).strip().lower()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", text)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted(set(i for i in ids if i not in rows))
print("ids cited:", len(ids), "distinct:", len(set(ids)), "missing:", missing or "none"); bad += len(missing)
# every quoted fragment followed (within the same paragraph, before the next quote) by an id: check against that id's row
paras = re.split(r"\n\s*\n|\n- |\n\| ", text)
checked = 0
for p in paras:
    for m in re.finditer(r"[\"\u201c]([^\"\u201c\u201d]{4,}?)[\"\u201d]\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)", p):
        frag, idblock = m.group(1), m.group(2)
        cid = re.findall(r"[MLR]\d{4}-\d{3}", idblock)
        parts = [x.strip(" .,;:") for x in frag.split("[...]") if x.strip(" .,;:")]
        ok = any(all(norm(pt) in norm(rows.get(c, "")) for pt in parts) for c in cid)
        checked += 1
        if not ok:
            bad += 1; print("FRAGMENT NOT IN ROW:", cid, "|", frag[:120])
print("fragments checked:", checked, "problems:", bad)
