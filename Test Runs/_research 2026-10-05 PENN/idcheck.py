import csv,re,sys
L=r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows={}
with open(L,encoding="utf-8-sig") as f:
    for r in csv.DictReader(f): rows[r["id"]]=r["quote_verbatim"]
txt=open(sys.argv[1],encoding="utf-8").read()
def norm(s):
    s=s.replace("\u2019","'").replace("\u2018","'").replace("\u201c",'"').replace("\u201d",'"')
    s=re.sub(r"\s+"," ",s)
    return s.strip().lower()
bad=0
e=re.findall(r"\[E\d-\d+\]",txt); print("E-ids:",e)
ids=re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",txt)
missing=[i for i in set(ids) if i not in rows]; print("ids:",len(set(ids)),"missing:",missing)
# quoted fragments followed (within 12 chars, possibly after ** or punctuation) by an id
for m in re.finditer(r'"([^"\n]{6,}?)"[^"\n]{0,14}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',txt):
    q,i=m.group(1),m.group(2)
    if i not in rows: continue
    row=norm(rows[i])
    parts=[p.strip(" .,;") for p in re.split(r"\[\.\.\.\]|\.\.\.",q)]
    ok=all(norm(p) in row for p in parts if len(p)>2)
    if not ok:
        bad+=1; print("NOT IN ROW",i,"::",q)
# multi-line quotes: rejoin wrapped text
flat=re.sub(r"\s*\n\s*"," ",txt)
for m in re.finditer(r'"([^"]{6,}?)"[^"]{0,14}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',flat):
    q,i=m.group(1),m.group(2)
    if i not in rows or len(q)>400: continue
    row=norm(rows[i])
    parts=[p.strip(" .,;") for p in re.split(r"\[\.\.\.\]|\.\.\.",q)]
    if not all(norm(p) in row for p in parts if len(p)>2):
        bad+=1; print("NOT IN ROW (flat)",i,"::",q)
print("bad:",bad)
