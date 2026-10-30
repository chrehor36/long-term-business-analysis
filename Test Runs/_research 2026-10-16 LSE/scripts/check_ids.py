"""Citation check for the LSE run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted
fragment standing immediately before an id (within 12 characters: closing quote, optional punctuation, then the bold id)
is found in that row's quote_verbatim, piece by piece where the fragment carries [...]. Prints PASS or the failures."""
import csv, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.normpath(os.path.join(here, "..", "..", ".."))
run = os.path.join(root, "Test Runs", "2026-10-16 Run - LSE Leishen Energy.md")
rows = {r["﻿id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(root, "principle_ledger_v5.csv"), encoding="utf-8"))}
text = open(run, encoding="utf-8").read()
flat = re.sub(r"\s+", " ", text)
fails = []
if re.search(r"\[E\d", flat):
    fails.append("E-id present")
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", flat)
for i in sorted(set(ids)):
    if i not in rows:
        fails.append(f"missing id {i}")
norm = lambda s: re.sub(r"\s+", " ", s).strip()
checked = 0
for m in re.finditer(r"“([^”]{3,}?)”|\"([^\"]{3,}?)\"", flat):
    q = m.group(1) or m.group(2)
    tail = flat[m.end(): m.end() + 30]
    t = re.match(r"[\s,.;:)]*\*\*\[([MLR]\d{4}-\d{3})\]\*\*", tail)
    if not t:
        continue
    rid = t.group(1)
    row = norm(rows.get(rid, ""))
    for piece in [norm(p) for p in q.split("[...]") if norm(p)]:
        checked += 1
        if piece not in row:
            fails.append(f"{rid}: fragment not in row: {piece[:90]}")
print(f"ids cited: {len(set(ids))}; fragments checked: {checked}")
print("PASS" if not fails else "FAIL\n" + "\n".join(fails))
sys.exit(1 if fails else 0)
