"""Citation check for the PED run: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment adjacent to an id is in that row."""
import csv, re, sys
run = open("Test Runs/2026-10-16 Run - PED PEDEVCO.md", encoding="utf-8").read()
rows = {}
for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8")):
    rows[r.get("\ufeffid") or r.get("id")] = r["quote_verbatim"]
fail = 0
if re.search(r"\[E\d+-\d+\]", run): print("E-id found"); fail += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); fail += 1
norm = lambda t: re.sub(r"\s+", " ", t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"'))
# a quoted fragment followed (within 12 chars) by one or more ids: the fragment must be in at least... each id's row
for m in re.finditer(r"\"([^\"]{8,}?)\"((?:[\s,.;:]*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)", run.replace("\n", " ")):
    frag = norm(m.group(1)).strip()
    for i in re.findall(r"[MLR]\d{4}-\d{3}", m.group(2)):
        parts = [p.strip() for p in frag.split("[...]")]
        if not all(norm(p) in norm(rows.get(i, "")) for p in parts if p):
            print("NOT IN ROW", i, "|", frag[:90]); fail += 1
print(f"ids cited: {len(set(ids))}; failures: {fail}")
print("PASS" if fail == 0 else "FAIL"); sys.exit(1 if fail else 0)
