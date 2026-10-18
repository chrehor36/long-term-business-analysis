# Dispatcher's citation check (overnight fold 2026-10-12): every quoted fragment (straight or curly quotes)
# followed within 120 characters by a cluster of v5 ids must be in one of those rows; every id resolves; no E-ids.
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = "Test Runs/2026-10-12 Run - NPNYY Nippon Yusen.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
t = open(RUN, encoding="utf-8").read()
def norm(s):
    s = s.replace("\u2019","'").replace("\u2018","'").replace("\u201c",'"').replace("\u201d",'"')
    return re.sub(r"\s+"," ",s).strip().lower()
ids = set(re.findall(r"[MLR]\d{4}-\d{3}", t))
print("ids", len(ids), "missing", [i for i in ids if i not in rows], "E-ids", re.findall(r"\[E\d-\d+\]", t))
n = bad = 0
for m in re.finditer(r'[\"\u201c]([^\"\u201c\u201d\n]{8,}(?:\n[^\"\u201c\u201d\n]+)*?)[\"\u201d]', t):
    after = t[m.end():m.end()+120]
    if re.search(r'[\"\u201c]', after.split("[",1)[0]): continue
    cl = re.match(r"[^\"\u201c]*?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,;\s]*(?:and\s*)?)+)", after)
    if not cl: continue
    idl = re.findall(r"[MLR]\d{4}-\d{3}", cl.group(1)); n += 1
    parts = [p.strip(" .,;") for p in m.group(1).split("[...]")]
    if not any(all(norm(p) in norm(rows.get(i,"")) for p in parts if p) for i in idl):
        bad += 1; print("SLIP?", idl, "::", m.group(1)[:140].replace("\n"," "))
print("checked", n, "flagged", bad)
