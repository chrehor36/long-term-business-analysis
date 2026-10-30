"""Checks on the SBS run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that
stands immediately before an id (a "..." followed by the bold id, or by a parenthesis then the id) is in that row."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = "Test Runs/2026-10-28 Run - SBS Sabesp.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
txt = open(RUN, encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("“", '"').replace("”", '"')).strip()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", txt)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", txt)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
# quoted fragment immediately followed by an id
for m in re.finditer(r'"([^"]{6,600})"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', txt):
    frag, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ""))
    for part in [p for p in frag.split("[...]") if p.strip()]:
        if norm(part).strip(" .,;:") not in row:
            print(f"FRAGMENT NOT IN ROW {i}: {part[:120]!r}"); bad += 1
print(f"{len(set(ids))} distinct ids, {len(ids)} citations; E-ids {len(eids)}; problems {bad}")
sys.exit(1 if bad else 0)
