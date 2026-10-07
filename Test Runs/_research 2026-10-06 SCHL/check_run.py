import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
L="C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv"
R="C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-06 Run - SCHL Scholastic.md"
rows={r[0]:r[2] for r in csv.reader(open(L,encoding="utf-8-sig"))}
s=open(R,encoding="utf-8").read()
def norm(t):
    t=re.sub(r"[\u2018\u2019\u201c\u201d'\"`]","Q",t)
    t=t.replace("\ufffd","Q")
    return re.sub(r"\s+"," ",t).strip()
bad=0
eids=re.findall(r"\[E\d+-\d+\]",s); print("E-ids:",eids); bad+=len(eids)
ids=re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",s)
allids=re.findall(r"\[([A-Z]+\d*-\d+)\]",s)
for i in set(allids):
    if i not in rows: print("MISSING id",i); bad+=1
print("ids cited:",len(ids),"distinct",len(set(ids)))
# each quoted fragment immediately before an id (within ~ 12 chars) must be in that row
flat=re.sub(r"\s+"," ",s)
checked=0
for m in re.finditer(r"\"([^\"]{3,600}?)\"[^\"\[]{0,40}\*\*\[([MLR]\d{4}-\d{3})\]\*\*",flat):
    frag,i=m.group(1),m.group(2)
    checked+=1
    if norm(frag).rstrip(".") not in norm(rows[i]):
        print("NOT IN ROW",i,"::",frag); bad+=1
# also fragments followed by id after a semicolon list like  "...", **[id]**; check pattern "...“ **[id]**" handled above

print("fragments checked:",checked); print("problems:",bad)
