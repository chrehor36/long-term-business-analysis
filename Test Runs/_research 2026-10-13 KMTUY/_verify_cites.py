# Dispatcher's check at the fold: every id in the CSV, no E-id, every quoted fragment beside an id is in that row.
import csv, re, sys
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
rows = {}
for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8")):
    rows[r[list(r.keys())[0]]] = r
t = open(ROOT + r"\Test Runs\2026-10-13 Run - KMTUY Komatsu.md", encoding="utf-8").read()
q = lambda s: s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
norm = lambda s: re.sub(r"\s+", " ", q(s)).lower()
ids = re.findall(r"\*\*\[?([MLR]\d{4}-\d{3})\]?\*\*", t)
print("ids", len(ids), "distinct", len(set(ids)), "missing", [i for i in set(ids) if i not in rows])
pairs = slips = 0
for m in re.finditer(r'"([^"\n]{6,400})"\s*\*\*\[?([MLR]\d{4}-\d{3})', q(t)):
    frag, i = m.groups()
    if i not in rows: continue
    pairs += 1
    txt = norm(" ".join(rows[i].values()))
    parts = [p.strip(" .,;:") for p in re.split(r"\[\.\.\.\]|\.\.\.|\u2026", norm(frag)) if p.strip(" .,;:")]
    if not all(p in txt for p in parts):
        slips += 1; print("SLIP", i, frag[:120])
print("pairs", pairs, "slips", slips, "E-ids", len(re.findall(r"\[E\d-\d+\]", t)))
