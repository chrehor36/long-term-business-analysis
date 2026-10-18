# Check the run file's citations against principle_ledger_v5.csv:
#  1. no E-ids; 2. every M/L/R id exists; 3. every quoted fragment placed directly before an id
#     (pattern: "fragment" **[ID]** or "fragment" [ID]) is a substring of that row's quote.
# usage: python -I check_ids.py <run file> <ledger csv>
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
run, ledger = sys.argv[1], sys.argv[2]
rows = {r["﻿id"] if "﻿id" in r else r["id"]: r for r in csv.DictReader(open(ledger, encoding="utf-8"))}

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

text = open(run, encoding="utf-8").read()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", text)
if eids:
    print("E-ids found:", sorted(set(eids))); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted({i for i in ids if i not in rows})
if missing:
    print("MISSING ids:", missing); bad += 1
print(f"{len(ids)} id citations, {len(set(ids))} distinct, {len(missing)} missing")
# quoted fragment directly before an id (allow ", " or " " or "), " between)
pat = re.compile(r"[\"“]([^\"“”]{6,}?)[\"”][\s,;:.)(]*(?:\*\*)?\[([MLR]\d{4}-\d{3})\]")
n = 0
for m in pat.finditer(text):
    frag, rid = m.group(1), m.group(2)
    if rid not in rows:
        continue
    n += 1
    q = norm(rows[rid]["quote_verbatim"])
    parts = [p for p in re.split(r"\[\.\.\.\]|\.\.\.", frag)]
    ok = all(norm(p).strip(" .,;:") in q for p in parts if norm(p).strip(" .,;:"))
    if not ok:
        bad += 1
        print(f"NOT IN ROW {rid}: \"{frag}\"")
print(f"{n} quoted fragments checked; {'PASS' if bad == 0 else 'FAIL'}")
sys.exit(1 if bad else 0)
