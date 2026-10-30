"""Check the LSTR run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment immediately before an id (in the same sentence) is in that row's quote (curly/straight quotes normalized)."""
import csv, re, os, sys
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(os.path.dirname(here))
rows={r["id"]:r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(root,"principle_ledger_v5.csv"),encoding="utf-8-sig"))}
run=open(os.path.join(root,"Test Runs","2026-10-10 Run - LSTR Landstar.md"),encoding="utf-8").read()
norm=lambda s: re.sub(r"\s+"," ",s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"')).strip()
bad=0
if re.search(r"\[E\d", run): print("E-id found"); bad+=1
ids=re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); bad+=1
# fragments: a quoted string followed (within 3 chars incl. punctuation) by an id
for m in re.finditer(r"\"([^\"]{6,})\"[.,;:]?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    parts=[p for p in norm(frag).split("[...]")]
    for p in parts:
        p=p.strip(" .")
        if p and p not in norm(rows[i]): print("NOT IN ROW", i, "::", p[:90]); bad+=1
print(len(set(ids)),"ids checked;", "PASS" if not bad else f"FAIL {bad}")
