# Check the run file's citations: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id is in that row's quote (elisions [...] split into pieces).
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
run, ledger = sys.argv[1], sys.argv[2]
rows = {}
with open(ledger, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = r["quote_verbatim"]

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

text = open(run, encoding="utf-8").read()
flat = re.sub(r"\s+", " ", text)
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
missing = sorted({i for i in ids if i not in rows})
if missing:
    print("missing ids:", missing); bad += 1
# fragment "..." followed (within a short gap of punctuation/spaces) by **[ID]**
for m in re.finditer(r'[\"“]([^\"“”]{6,}?)[\"”][\s,.;:]{0,3}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, rid = m.group(1), m.group(2)
    q = norm(rows.get(rid, ""))
    for piece in [p for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]:
        p = norm(piece).strip(" .,;")
        if p and p not in q:
            print("NOT IN ROW", rid, "::", piece[:120]); bad += 1
print("ids cited:", len(set(ids)), "| problems:", bad)
sys.exit(1 if bad else 0)
