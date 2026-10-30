"""Check the GFF run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
that ends within 25 characters before an id is in that row (apostrophes and double quotes normalised; [...] splits)."""
import csv, re, sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-07 Run - GFF Griffon.md"
LED = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(LED, encoding="utf-8-sig"))}
txt = open(RUN, encoding="utf-8").read()
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip()
problems = []
if re.search(r"\[E\d-\d+\]", txt): problems.append("E-id present")
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", txt)
for i in sorted(set(ids)):
    if i not in rows: problems.append(f"missing id {i}")
checked = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", txt):
    i = m.group(1)
    before = txt[max(0, m.start() - 25):m.start()]
    if '"' not in before: continue
    end = m.start() - (len(before) - before.rfind('"'))
    start = txt.rfind('"', 0, end)
    if start < 0: continue
    frag = txt[start + 1:end]
    if "**[" in txt[end:m.start()]: continue  # another id sits between the quote and this one
    if len(frag) > 1500 or "\n\n" in frag: continue
    checked += 1
    row = norm(rows.get(i, ""))
    for piece in re.split(r"\[\.\.\.\]", frag):
        p = norm(piece).strip(" .,;:")
        if p and p not in row:
            problems.append(f"{i}: fragment not in row: {p[:90]!r}")
print(f"{len(set(ids))} distinct ids, {checked} quoted fragments checked, {len(problems)} problems")
for p in problems: print(" -", p)
sys.exit(1 if problems else 0)
