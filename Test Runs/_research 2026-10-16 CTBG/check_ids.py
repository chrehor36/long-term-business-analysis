"""Check the CTBG run file: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment beside an id is in that row."""
import csv, re, sys

ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
run = open(ROOT + r"\Test Runs\2026-10-16 Run - CTBG Coil Tubing Technology.md", encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig"))}


def norm(s):
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\ufffd", "'")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


bad = 0
for e in re.findall(r"\[E\d+-\d+\]", run):
    print("E-id found:", e)
    bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i)
        bad += 1
# a quoted fragment followed within 40 characters by a bold id
for m in re.finditer(r'"([^"]{6,400})"[^"\[]{0,40}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    for part in frag.split("[...]"):
        p = norm(part).strip(" .,;:")
        if p and p not in norm(rows.get(i, "")):
            print("NOT IN ROW", i, "|", part[:90])
            bad += 1
print("distinct ids:", len(set(ids)), "problems:", bad)
sys.exit(1 if bad else 0)
