"""Citation check for the LBYYQ run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment
directly followed by an id is in that row (elisions [...] split into parts; whitespace normalised)."""
import csv,re,sys
ROOT=r"C:\Users\chreh\OneDrive\Documents\BRK"
run=open(ROOT+r"\Test Runs\2026-10-17 Run - LBYYQ Libbey.md",encoding="utf-8").read()
rows={r[0]:r[2] for r in csv.reader(open(ROOT+r"\principle_ledger_v5.csv",encoding="utf-8"))}
norm=lambda s:re.sub(r"\s+"," ",s).strip()
bad=0
e=re.findall(r"\[E\d+-\d+\]",run)
if e: print("E-ids:",e); bad+=len(e)
ids=re.findall(r"\[([MLR]\d{4}-\d{3})\]",run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id",i); bad+=1
pat=re.compile(r'"([^"]{3,}?)"[^"\n]{0,6}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
n=0
for q,i in pat.findall(run.replace("\n"," ")):
    n+=1
    if i not in rows: continue
    for part in q.split("[...]"):
        p=norm(part)
        if p and p not in norm(rows[i]):
            print(f"NOT IN {i}: {p[:120]}"); bad+=1
print(f"{len(set(ids))} distinct ids, {n} quote-id pairs checked, {bad} problems")
sys.exit(1 if bad else 0)
