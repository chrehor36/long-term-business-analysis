# check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment beside an id is in that row.
import csv,re,sys
sys.stdout.reconfigure(encoding="utf-8")
rows={r["id"]:r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv",encoding="utf-8-sig"))}
t=open("Test Runs/2026-10-23 Run - EVRG Evergy.md",encoding="utf-8").read()
probs=0
if re.search(r"\[E\d-\d+\]",t): print("E-id found"); probs+=1
ids=re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",t)
for i in set(ids):
    if i not in rows: print("MISSING id",i); probs+=1
norm=lambda x: re.sub(r"\s+"," ",x).strip()
# for each id occurrence, take quoted fragments in the text between the previous id (or line start) and this id
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",t):
    i=m.group(1); start=max(t.rfind("**[",0,m.start()-1), t.rfind("\n- ",0,m.start()), t.rfind("\n\n",0,m.start()))
    seg=t[start:m.start()]
    # skip quotes that are filings (heuristic: only check quotes immediately preceding the id within 400 chars)
    seg=seg[-600:]
    qs=re.findall(r"\"([^\"]{8,})\"",seg)
    if not qs: continue
    q=qs[-1]
    if i in rows:
        row=norm(rows[i]); frag=norm(q)
        parts=[p.strip() for p in frag.split("[...]")]
        ok=all(p in row for p in parts if p)
        if not ok:
            print(f"CHECK {i}: \"{frag[:120]}\""); probs+=1
print("ids:",len(set(ids)),"problems:",probs)
