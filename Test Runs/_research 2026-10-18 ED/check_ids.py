# Check for the ED run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment set
# directly beside an id (before it, or after "**[id]**, ") is found in that row, elisions [...] matched part by part in order.
import csv, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
RUN = "../2026-10-18 Run - ED Consolidated Edison.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("../../principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
problems = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", eids); problems += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); problems += 1
flat = re.sub(r"\s*\n\s*", " ", text)
def found(frag, rid):
    row = norm(rows.get(rid, ""))
    pos = 0
    for part in re.split(r"\[\.\.\.\]", frag):
        part = norm(part).strip(" .,;:")
        if not part:
            continue
        k = row.find(part, pos)
        if k < 0:
            return False
        pos = k + len(part)
    return True
checked = 0
# quote immediately before one or more ids:  "frag" **[ID]**  or  "frag" [ID]
for m in re.finditer(r"\"([^\"]{3,600})\"\s*(?:\([^)]{0,40}\)\s*)?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)", flat):
    frag, idblock = m.group(1), m.group(2)
    rids = re.findall(r"[MLR]\d{4}-\d{3}", idblock)
    checked += 1
    if not any(found(frag, r) for r in rids):
        print("NOT IN ROW", rids, "::", frag[:120]); problems += 1
# id followed by ', "frag"'
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*,\s*\"([^\"]{3,600})\"", flat):
    rid, frag = m.group(1), m.group(2)
    checked += 1
    if not found(frag, rid):
        print("NOT IN ROW (after)", rid, "::", frag[:120]); problems += 1
print(f"ids cited: {len(set(ids))} distinct; quoted fragments checked: {checked}; problems: {problems}")
