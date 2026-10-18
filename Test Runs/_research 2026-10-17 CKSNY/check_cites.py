# Citation check for the CKSNY run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment directly followed by one or more ids is found (after [...] splitting) in one of those rows.
import csv,re,sys,unicodedata
ROOT=sys.argv[1]
run=open(ROOT+"/Test Runs/2026-10-17 Run - CKSNY Vesuvius.md",encoding="utf-8").read()
rows={r[0]:r[2] for r in csv.reader(open(ROOT+"/principle_ledger_v5.csv",encoding="utf-8"))}
def norm(x):
    x=x.replace("“",'"').replace("”",'"').replace("’","'").replace("‘","'").replace("—","-").replace("–","-")
    return re.sub(r"\s+"," ",x).strip().lower()
bad=0
eids=re.findall(r"\[E\d+-\d+\]",run)
if eids: print("E-ids:",eids); bad+=1
ids=set(re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",run))
for i in sorted(ids):
    if i not in rows: print("MISSING",i); bad+=1
pat=re.compile(r'"([^"\n]{3,400})"[\s,]*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[\s,]*)+)')
n=0
for m in pat.finditer(run.replace("\n  "," ")):
    q=m.group(1); cids=re.findall(r"[MLR]\d{4}-\d{3}",m.group(2)); n+=1
    frags=[f for f in re.split(r"\[\.\.\.\]",q) if f.strip()]
    ok=all(any(norm(f.strip(" .,")) in norm(rows.get(c,"")) for c in cids) for f in frags)
    if not ok: print("NOT IN ROW:",cids,"|",q[:120]); bad+=1
print(f"ids {len(ids)}, quoted fragments checked {n}, problems {bad}")
