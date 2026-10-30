"""Check the NRG run file: every id exists in the v5 ledger; no E-ids; every quoted fragment placed right before an id is in that row."""
import csv, re, sys, os
root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
run = open(os.path.join(root, "Test Runs", "2026-10-26 Run - NRG NRG Energy.md"), encoding="utf-8").read()
rows = {}
with open(os.path.join(root, "principle_ledger_v5.csv"), encoding="utf-8-sig") as f:
    for r in csv.DictReader(f): rows[r["id"]] = r["quote_verbatim"]
def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", t).strip()
bad = 0
ids = re.findall(r"\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*", run)
if re.search(r"\[E\d", run): print("E-id found"); bad += 1
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
# quoted fragment immediately followed (within a few chars) by an id
for m in re.finditer(r"\"([^\"]{6,600})\"\s*\**\s*(?:\*\*)?\[([A-Z]+\d{4}-\d{3})\]", run.replace("“", '"').replace("”", '"')):
    frag, i = m.group(1), m.group(2)
    parts = [p for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]
    row = norm(rows.get(i, ""))
    for p in parts:
        if norm(p).strip(" .,") not in row:
            print("NOT IN ROW", i, "::", p[:120]); bad += 1
print(f"ids cited: {len(set(ids))}; quote checks done; problems: {bad}")
sys.exit(1 if bad else 0)
