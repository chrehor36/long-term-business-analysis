"""Run check for the RWEOY run file: no E-ids; every M/L/R id in the v5 ledger;
every quoted fragment immediately before an id is inside that row's quote."""
import csv, re, sys, unicodedata
ROOT = r"C:\Projects\BRK"
RUN = ROOT + r"\Test Runs\2026-10-26 Run - RWEOY RWE.md"
rows = {r["\ufeffid"]: r["quote_verbatim"] for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8"))}
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2014", "-"), ("\u2013", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()
text = open(RUN, encoding="utf-8").read()
bad = 0
for m in re.finditer(r"\[E\d", text):
    print("E-id found at", m.start()); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING", i); bad += 1
pairs = 0
for m in re.finditer(r'"([^"\n]{4,400})"\s*\**\s*\[([MLR]\d{4}-\d{3})\]', text):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    pairs += 1
    for piece in frag.split("[...]"):
        p = norm(piece.strip(" .,;:"))
        if p and p not in norm(rows[i]):
            print("FRAGMENT NOT IN ROW", i, "|", piece[:80]); bad += 1
print(f"ids: {len(set(ids))} distinct; fragment pairs checked: {pairs}; problems: {bad}")
sys.exit(1 if bad else 0)
