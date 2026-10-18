# Check for the NPNYY run of 2026-10-12: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment
# that sits beside an id (same paragraph or bullet, before the id) is in that row's quote.
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = "Test Runs/2026-10-12 Run - NPNYY Nippon Yusen.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", text)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); bad += 1
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()
# split into blocks (bullets / paragraphs); within a block, each quote is checked against the ids that follow it
blocks = re.split(r"\n(?=- |\n|\*\*|\|)", text)
checked = 0
for b in blocks:
    for m in re.finditer(r'"([^"]{6,}?)"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)', b):
        q = m.group(1); idl = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
        parts = [p.strip(" .,;") for p in q.split("[...]")]
        ok = any(all(norm(p) in norm(rows.get(i, "")) for p in parts if p) for i in idl)
        checked += 1
        if not ok:
            print("QUOTE NOT IN ROW", idl, "::", q[:120]); bad += 1
print(f"ids used: {len(set(ids))}; quotes checked beside ids: {checked}; problems: {bad}")
sys.exit(1 if bad else 0)
