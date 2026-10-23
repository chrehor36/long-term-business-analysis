"""Check the ETR run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment written
immediately before an id (the quote, then the bold id) is found in that id's row, piece by piece across [...] elisions.
Usage (from the repository root): python -I -X utf8 "Test Runs/_research 2026-10-23 ETR/check_ids.py" """
import csv, re, sys
RUN = "Test Runs/2026-10-23 Run - ETR Entergy.md"
rows = {}
with open("principle_ledger_v5.csv", encoding="utf-8") as f:
    r = csv.reader(f); next(r)
    for row in r: rows[row[0]] = row[2]
text = open(RUN, encoding="utf-8").read()

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()

problems = []
eids = re.findall(r"\[E\d-\d+\]", text)
if eids: problems.append(f"E-ids present: {sorted(set(eids))}")
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows: problems.append(f"missing id {i}")
# quote immediately followed by an id: "...." **[ID]**  (straight or curly quotes)
pat = re.compile(r"[\"“]([^\"“”]{6,}?)[\"”][^\"“”*\n]{0,4}\*\*\[([MLR]\d{4}-\d{3})\]\*\*")
checked = 0
for m in pat.finditer(text.replace("\n  ", " ").replace("\n", " ")):
    q, i = m.group(1), m.group(2)
    if i not in rows: continue
    row = norm(rows[i]); checked += 1
    for piece in re.split(r"\[\.\.\.\]", q):
        p = norm(piece).strip(" .,;:")
        if len(p) < 4: continue
        if p not in row:
            problems.append(f"{i}: fragment not in row: {p[:90]!r}")
print(f"ids cited: {len(set(ids))} distinct; quote-id pairs checked: {checked}")
print("\n".join(problems) if problems else "0 problems")
sys.exit(1 if problems else 0)
