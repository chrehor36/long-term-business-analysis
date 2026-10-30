# Check: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment adjacent to an id is in that row.
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
L = {r[0]: r[2] for r in csv.reader(open(r"C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv", encoding="utf-8"))}
t = open(r"C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-17 Run - BLGO BioLargo.md", encoding="utf-8").read()
bad = 0
for e in re.findall(r"\[E\d+-\d+\]", t): print("E-id found:", e); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", t)
for i in sorted(set(ids)):
    if i not in L: print("MISSING", i); bad += 1
norm = lambda s: re.sub(r"\s+", " ", s)
# a quoted fragment immediately followed (within the same line run) by an id
for m in re.finditer(r"\"([^\"]{6,400})\"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*", norm(t)):
    q, i = m.group(1), m.group(2)
    parts = [p.strip(" .,") for p in q.split("[...]")]
    for p in parts:
        if p and norm(p) not in norm(L.get(i, "")):
            print("NOT IN ROW", i, "::", p[:120]); bad += 1
print("ids cited:", len(set(ids)), "problems:", bad)
