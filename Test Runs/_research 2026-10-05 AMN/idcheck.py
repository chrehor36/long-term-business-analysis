import csv,re,sys
rows={}
for r in csv.DictReader(open("principle_ledger_v5.csv",encoding="utf-8")):
    rows[r[list(r.keys())[0]]]=" ".join(r.values())
def norm(s): return re.sub(r"\s+"," ",s.replace("’","'").replace("“",'"').replace("”",'"')).lower()
txt=open(sys.argv[1],encoding="utf-8").read()
bad=0
if re.search(r"\[E\d",txt): print("E-ID FOUND"); bad=1
ids=re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",txt)
for i in set(ids):
    if i not in rows: print("MISSING",i); bad=1
# quoted fragment immediately before an id: "...." **[ID]**
for m in re.finditer(r'"([^"]{4,400})"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',txt):
    frag,i=m.group(1),m.group(2)
    if i in rows:
        for part in frag.split("[...]"):
            if norm(part.strip()) and norm(part.strip()) not in norm(rows[i]):
                print("NOT IN ROW",i,"|",part.strip()[:90]); bad=1
print("ids",len(set(ids)),"checked; bad" if bad else "PASS")
