# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# immediately before an id (in the same sentence or line) is contained in that row's quote.
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-18 Run - AXIAY AXIA Energia.md"
LED = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(LED, encoding="utf-8-sig"))}
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\ufffd", "'")
    return re.sub(r"\s+", " ", s)
txt = open(RUN, encoding="utf-8").read()
flat = re.sub(r"\s*\n\s*", " ", txt)
probs = 0
if re.search(r"\[E\d", txt): print("E-id found"); probs += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", flat)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING ID", i); probs += 1
# fragment check: a "..." directly followed (within 12 chars) by **[ID]**
n = 0
for m in re.finditer(r'"([^"]{3,400})"[^"\[]{0,14}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, i = m.group(1), m.group(2); n += 1
    if i not in rows: continue
    parts = [p.strip(" .,;:") for p in frag.split("[...]")]
    q = norm(rows[i])
    for p in parts:
        if p and norm(p) not in q:
            print(f"FRAGMENT NOT IN ROW {i}: {p[:120]}"); probs += 1
print(f"ids cited: {len(set(ids))}; fragments checked: {n}; problems: {probs}")
