import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-17 Run - MTRX Matrix Service.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
flat = re.sub(r"\s*\n\s*", " ", text)
norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
print("E-ids:", eids or "none"); bad += len(eids)
ids = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)))
missing = [i for i in ids if i not in rows]
print("ids cited:", len(ids), "missing:", missing or "none"); bad += len(missing)
checked = 0
# quote directly before an id:  "..." **[ID]**   or  "..." [...] **[ID]**
for m in re.finditer(r'"([^"]{3,}?)"\s*(?:\.|,|;)?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    q, i = m.group(1), m.group(2)
    for piece in [p for p in q.split("[...]") if p.strip()]:
        checked += 1
        if norm(piece) not in norm(rows.get(i, "")):
            bad += 1; print("NOT IN ROW", i, "::", piece[:90])
# quote directly after an id:  **[ID]**: "..."
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*\s*:\s*"([^"]{3,}?)"', flat):
    i, q = m.group(1), m.group(2)
    for piece in [p for p in q.split("[...]") if p.strip()]:
        checked += 1
        if norm(piece) not in norm(rows.get(i, "")):
            bad += 1; print("NOT IN ROW", i, "::", piece[:90])
emd = text.count("\u2014")
print("fragments checked:", checked, " problems:", bad, " em dashes in file (all should be inside quotes):", emd)
