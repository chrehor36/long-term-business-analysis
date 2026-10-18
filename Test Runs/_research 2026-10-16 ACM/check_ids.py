import csv, re, sys
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("../../principle_ledger_v5.csv", encoding="utf-8-sig"))}
run = open("../2026-10-16 Run - ACM AECOM.md", encoding="utf-8").read()
def norm(s): return re.sub(r"\s+", " ", s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"')).strip().lower()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
if eids: print("E-ids:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); bad += 1
print("distinct ids", len(set(ids)), "occurrences", len(ids))
# quoted fragment immediately before one or more ids (allow ', ' between ids and a short parenthesis)
for m in re.finditer(r'"([^"\n]{3,400})"[^"\n]{0,40}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)', run):
    frag = m.group(1); idl = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    between = run[m.end(1)+1:m.start(2)]
    if '"' in between: continue
    parts = [p for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]
    ok = any(all(norm(p.strip(" .,")) in norm(rows.get(i,"")) for p in parts) for i in idl)
    if not ok:
        print("NOT IN ROW:", idl, "|", frag[:120]); bad += 1
print("FAIL" if bad else "PASS", bad)
