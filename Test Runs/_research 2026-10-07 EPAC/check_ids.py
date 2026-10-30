"""Check the EPAC run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment that sits immediately before an id (or before a run of ids) is in one of those rows.
Usage: python check_ids.py "<run file>"
"""
import csv, re, sys, unicodedata

LEDGER = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = re.sub(r"\*\*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

rows = {}
with open(LEDGER, encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = norm(r["quote_verbatim"])

text = open(sys.argv[1], encoding="utf-8").read()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", sorted(set(eids))); bad += 1

ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted({i for i in ids if i not in rows})
if missing:
    print("MISSING ids:", missing); bad += 1

# quote immediately followed by one or more ids: "...." **[ID]**, **[ID2]**
pat = re.compile(r'"([^"\n]{3,600})"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,;\s]*(?:and\s*)?)+)')
checked = 0
for m in pat.finditer(text):
    q = m.group(1)
    idl = re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group(2))
    parts = [norm(p) for p in re.split(r"\[\.\.\.\]|\.\.\.", q) if norm(p).strip(" .,;:")]
    ok = any(all(p.strip(" .,;:") in rows.get(i, "") for p in parts) for i in idl)
    checked += 1
    if not ok:
        bad += 1
        print("QUOTE NOT IN ROW:", idl, "|", q[:160])
print(f"ids cited: {len(set(ids))}; quotes checked: {checked}; problems: {bad}")
sys.exit(1 if bad else 0)
