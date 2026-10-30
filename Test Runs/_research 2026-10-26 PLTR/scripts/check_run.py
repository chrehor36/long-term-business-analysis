"""Check the run file's citations: no E-ids; every M/L/R id in the ledger; every quoted fragment placed
immediately before an id (a "..." then optional punctuation/space then **[ID]**) is in that row, with [...]
elisions matched piece by piece in order. Usage: python -I check_run.py <ledger.csv> <runfile>
"""
import csv, re, sys


def norm(s):
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"),
                 ("–", "-"), ("�", "")):
        s = s.replace(a, b)
    return " ".join(s.split()).lower()


rows = {r["id"]: norm(r["quote_verbatim"]) for r in csv.DictReader(open(sys.argv[1], encoding="utf-8-sig"))}
text = open(sys.argv[2], encoding="utf-8").read()
fail = 0
ids = re.findall(r"\*\*\[([A-Z][0-9A-Z]*-[0-9]+)\]\*\*", text)
for i in ids:
    if i.startswith("E"):
        print("E-ID:", i); fail += 1
    elif i not in rows:
        print("MISSING ID:", i); fail += 1
# quotes directly before an id: "...." [punct/space up to 3 chars] **[ID]**
qpat = re.compile(r'"([^"\n]{3,600})"[\s.,;:)]{0,3}\*\*\[([A-Z][0-9A-Z]*-[0-9]+)\]\*\*')
checked = 0
for m in qpat.finditer(text):
    q, i = m.group(1), m.group(2)
    row = rows.get(i, "")
    pos = 0
    ok = True
    for piece in [p for p in re.split(r"\[\.\.\.\]", q)]:
        p = norm(piece).strip(" .,;:")
        if not p:
            continue
        k = row.find(p, pos)
        if k < 0:
            ok = False
            break
        pos = k + len(p)
    checked += 1
    if not ok:
        print(f"QUOTE NOT IN ROW {i}: {q[:120]}"); fail += 1
print(f"ids cited {len(ids)} ({len(set(ids))} distinct); quotes checked {checked}; failures {fail}")
sys.exit(1 if fail else 0)
