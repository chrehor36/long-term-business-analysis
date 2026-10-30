"""Check the PAM run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
that stands immediately before an id (in the same sentence) is in that row, elisions [...] split.
Usage: python -I check_run.py <run file> <ledger csv>"""
import csv, re, sys

run, ledger = sys.argv[1], sys.argv[2]
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ledger, encoding="utf-8-sig"))}
text = open(run, encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); bad += 1
print(f"{len(ids)} citations, {len(set(ids))} distinct ids")
# quote immediately preceding an id: "...." optional punctuation/space then **[ID]**
for m in re.finditer(r"[\"“]([^\"“”]{3,600}?)[\"”][^\"“”*\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text):
    q, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ""))
    for frag in re.split(r"\s*\[\.\.\.\]\s*", q):
        f = norm(frag).rstrip(".,;:")
        if f and f not in row:
            print(f"NOT IN ROW {i}: {f[:120]}"); bad += 1
print("PASS" if not bad else f"FAIL ({bad})")
