# Dispatcher's check (overnight cycle 2026-10-11): each quoted fragment before a v5 id, back to the previous id, against that row.
import csv, re, sys
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
rows = {}
with open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8") as f:
    r = csv.reader(f); h = next(r)
    for x in r: rows[x[0]] = x
n = lambda s: re.sub(r"\s+", " ", s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", "-")).strip().lower()
txt = open(ROOT + r"\Test Runs\2026-10-11 Run - AMBQ Ambiq Micro.md", encoding="utf-8").read()
# join paragraphs so quotes split across lines are seen whole
paras = re.split(r"\n\s*\n", txt)
ok = bad = 0
for p in paras:
    p1 = " ".join(p.split("\n"))
    last = 0
    for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", p1):
        seg = p1[last:m.start()]; last = m.end()
        row = rows.get(m.group(1))
        if not row: print("MISSING ID", m.group(1)); bad += 1; continue
        body = n(" ".join(row))
        for q in re.findall(r'"([^"]{8,})"', seg):
            parts = [x for x in re.split(r"\s*\[\.\.\.\]\s*|\.\.\.", q) if len(x.strip()) > 3]
            if all(n(x) in body for x in parts): ok += 1
            else: bad += 1; print("CHECK", m.group(1), "|", q[:120])
print("matched", ok, "flagged", bad)
