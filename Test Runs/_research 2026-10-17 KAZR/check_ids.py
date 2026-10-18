# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment on the same line directly before an id appears in that row's quote.
import csv, re, os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
run = os.path.join(root, "Test Runs", "2026-10-17 Run - KAZR Skyline Builders Group Holding.md")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(root, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
text = open(run, encoding="utf-8").read()
probs = 0
if re.search(r"\[E\d", text):
    print("E-id found"); probs += 1
def norm(s):
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()
n = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text):
    n += 1
    i = m.group(1)
    if i not in rows:
        print("missing id", i); probs += 1; continue
    line = text[:m.start()].split("\n")[-1]
    seg = re.split(r"\*\*\[[MLR]\d{4}-\d{3}\]\*\*", line)[-1]
    for frag in re.findall(r'"([^"]{6,})"', seg):
        for part in frag.split("[...]"):
            if part.strip() and norm(part) not in norm(rows[i]):
                print("fragment not in", i, ":", part[:90]); probs += 1
print("ids checked:", n, "problems:", probs)
