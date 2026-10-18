# Dispatcher's citation check: every id exists; every quoted fragment adjacent to an id is in that row's quote.
import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["id"]: r for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
qcol = [k for k in next(iter(rows.values())).keys() if "quote" in k.lower()][0]
norm = lambda s: re.sub(r"\s+", " ", s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')).strip().lower()
ids = re.findall(r"\[((?:M|L|R)\d{4}-\d{3})\]", run)
print("ids", len(ids), "unique", len(set(ids)), "E-ids", len(re.findall(r"\[E\d", run)))
bad = [i for i in set(ids) if i not in rows]; print("missing", bad)
slips = 0; n = 0
for m in re.finditer(r'[\"\u201c]([^\"\u201c\u201d]{6,400})[\"\u201d]\s*(?:\*\*)?\s*((?:\*\*\[(?:M|L|R)\d{4}-\d{3}\]\*\*[,\s]*)+)', run):
    frag = m.group(1); cited = re.findall(r"(?:M|L|R)\d{4}-\d{3}", m.group(2)); n += 1
    parts = [p for p in re.split(r"\[\.\.\.\]|\.\.\.|\u2026", norm(frag)) if p.strip()]
    if not any(all(p.strip() in norm(rows.get(c, {}).get(qcol, "")) for p in parts) for c in cited):
        slips += 1; print("SLIP", cited, frag[:120])
print("fragments", n, "slips", slips)
