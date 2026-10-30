"""Run-file check: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment set immediately before an id
(within the same paragraph, "..." then optional text-free gap then **[ID]**) is found in that row, elisions [...] or ...
split into pieces, apostrophes and quote marks normalized (the ledger carries both ’ and U+FFFD)."""
import csv, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, "..", ".."))
run = os.path.join(root, "Test Runs", "2026-10-23 Run - FE FirstEnergy.md")
rows = {}
with open(os.path.join(root, "principle_ledger_v5.csv"), encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = r["quote_verbatim"]
text = open(run, encoding="utf-8").read()

def norm(s):
    s = s.replace("�", "'").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("\n", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

problems = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids present:", sorted(set(eids))); problems += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); problems += 1
# quoted fragment then (optional short connective without quotes) then **[ID]**
flat = re.sub(r"\n\s*", " ", text)
pat = re.compile(r'"([^"]{3,600}?)"\s*[.,;:]?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
checked = 0
for m in pat.finditer(flat):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    row = norm(rows[i])
    pieces = [p for p in re.split(r"\[\.\.\.\]|\.\.\.", frag) if p.strip()]
    for p in pieces:
        q = norm(p).strip(" .,;:")
        if q and q not in row:
            print("NOT IN ROW", i, "|", p[:120]); problems += 1
    checked += 1
print("ids:", len(set(ids)), "fragments checked:", checked, "problems:", problems)
sys.exit(1 if problems else 0)
