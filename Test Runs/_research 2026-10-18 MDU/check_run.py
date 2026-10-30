# Checks for the MDU run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment placed directly before an id is in that row (elisions [...] split the fragment).
import csv,re,sys
sys.stdout.reconfigure(encoding="utf-8")
BRK=r"C:\Users\chreh\OneDrive\Documents\BRK"
rows={r[0].lstrip("\ufeff"):r[2] for r in csv.reader(open(BRK+r"\principle_ledger_v5.csv",encoding="utf-8"))}
t=open(BRK+r"\Test Runs\2026-10-18 Run - MDU MDU Resources Group.md",encoding="utf-8").read()
flat=re.sub(r"\s*\n\s*"," ",t)
norm=lambda x:re.sub(r"\s+"," ",x).strip()
bad=0
e=re.findall(r"\[E\d+-\d+\]",t)
if e: print("E-ids found:",e); bad+=1
ids=set(re.findall(r"\[([MLR]\d{4}-\d{3})\]",t))
miss=[i for i in ids if i not in rows]
if miss: print("missing ids:",miss); bad+=1
n=0
for m in re.finditer(r'"([^"]{6,}?)"\s*[.,;:]?\)?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*',flat):
    frag,i=m.group(1),m.group(2); n+=1
    row=norm(rows.get(i,""))
    for part in frag.split("[...]"):
        part=norm(part).strip(" .,;:")
        if part and part not in row:
            print("NOT IN ROW",i,"::",part[:120]); bad+=1
print("ids:",len(ids),"quoted fragments checked:",n,"problems:",bad)
sys.exit(1 if bad else 0)
