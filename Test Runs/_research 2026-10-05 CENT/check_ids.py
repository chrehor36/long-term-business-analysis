"""Checks for the CENT run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment written immediately before an id appears inside that row (pieces split on [...])."""
import csv, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
run = open(os.path.join(ROOT, "Test Runs", "2026-10-05 Run - CENT Central Garden and Pet.md"), encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
missing = sorted(set(i for i in ids if i not in rows))
print(f"ids cited: {len(ids)} ({len(set(ids))} distinct); missing: {missing or 'none'}"); bad += len(missing)
norm = lambda t: re.sub(r"\s+", " ", t)
pairs = re.findall(r"\"([^\"\n]{3,400})\"\s*(?:\(the transcript[^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for frag, i in pairs:
    if i not in rows: continue
    for piece in [p.strip(" .,;:") for p in frag.split("[...]")]:
        if piece and norm(piece) not in norm(rows[i]):
            print("NOT IN ROW", i, "|", piece); bad += 1
print(f"quoted fragments checked: {len(pairs)}")
# ids written with no quote before them are listed for a manual look
print("FAIL" if bad else "PASS")
sys.exit(1 if bad else 0)
