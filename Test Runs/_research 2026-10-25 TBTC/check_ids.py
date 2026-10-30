# Check for the TBTC run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that
# stands immediately before an id (quote, optional punctuation/space, then **[ID]**) is in that row's quote_verbatim.
import csv, re, sys
ROOT = r"C:\Projects\BRK"
RUN = ROOT + r"\Test Runs\2026-10-25 Run - TBTC Table Trac.md"
rows = {}
with open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = r["quote_verbatim"]
text = open(RUN, encoding="utf-8").read()
bad = 0
ids = re.findall(r"\*\*\[([A-Z][0-9A-Z-]+)\]\*\*", text)
for i in set(ids):
    if i.startswith("E"):
        print("E-id found:", i); bad += 1
    elif i not in rows:
        print("MISSING id:", i); bad += 1
def norm(s):
    return re.sub(r"\s+", " ", s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')).strip()
# quoted fragment directly before an id (allow a closing punctuation and spaces between)
for m in re.finditer(r"\"([^\"]{3,600})\"[\s,.;:)]*\*\*\[([A-Z][0-9A-Z-]+)\]\*\*", text):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    row = norm(rows[i])
    for piece in re.split(r"\[\.\.\.\]", frag):
        p = norm(piece).strip(" .,;:")
        if p and p not in row:
            print(f"NOT IN ROW {i}: {piece[:120]!r}"); bad += 1
print(f"ids checked: {len(set(ids))}; problems: {bad}")
sys.exit(1 if bad else 0)
