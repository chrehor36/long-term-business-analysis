# usage: idcheck.py RUNFILE  -- checks: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every double-quoted fragment immediately preceding an id (same clause, since the previous id) is in that row (elisions [...] split)
import csv, re, sys, unicodedata
root=r"C:\Users\chreh\OneDrive\Documents\BRK"
rows={}
with open(root+r"\principle_ledger_v5.csv",encoding="utf-8-sig") as f:
    for r in csv.DictReader(f): rows[r["id"]]=r["quote_verbatim"]
def norm(s):
    for ch in "\u2019\u2018\u201c\u201d\u2014\u2013\ufffd'\"-": s=s.replace(ch,"~")
    s=re.sub(r"\*\*","",s)
    return re.sub(r"\s+"," ",s).strip().lower()
t=open(sys.argv[1],encoding="utf-8").read()
bad=0
for m in re.finditer(r"\[E\d+-\d+\]",t): print("E-ID:",m.group()); bad+=1
ids=re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",t)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING ID",i); bad+=1
# fragments: split text into segments ending at each id
pos=0; nfr=0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",t):
    seg=t[pos:m.start()]; pos=m.end()
    # only quotes in the last sentence-ish chunk before the id: after the previous id
    # take quoted strings in seg (straight or curly double quotes)
    qm=list(re.finditer(r'[\u201c"]([^"\u201c\u201d]{3,}?)[\u201d"]',seg))
    if not qm: continue
    if len(seg)-qm[-1].end()>40: continue   # only a quote sitting directly beside the id is that id's fragment
    q=qm[-1].group(1)
    rid=m.group(1)
    if rid not in rows: continue
    rowt=norm(rows[rid])
    for part in re.split(r"\[\.\.\.\]|\.\.\.",q):
        p=norm(part).strip(" ,.;:")
        if len(p)<3: continue
        nfr+=1
        if p not in rowt:
            print(f"NOT IN ROW {rid}: {part[:120]!r}"); bad+=1
print(f"ids cited: {len(set(ids))} distinct, {len(ids)} total; fragments checked: {nfr}; problems: {bad}")
