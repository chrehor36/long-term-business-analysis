# Check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; quoted fragments immediately before an id are in that row.
import re, csv, sys
ROOT=r"C:\Users\chreh\OneDrive\Documents\BRK"
rows={x["id"]:x["quote_verbatim"] for x in csv.DictReader(open(ROOT+r"\principle_ledger_v5.csv",encoding="utf-8-sig"))}
t=open(ROOT+r"\Test Runs\2026-10-06 Run - PTEN Patterson-UTI Energy.md",encoding="utf-8").read()
def norm(s): return re.sub(r"\s+"," ",s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"')).strip()
print("E-ids:", re.findall(r"\[E\d-\d+\]",t))
ids=re.findall(r"\[([MLR]\d{4}-\d{3})\]",t)
print("ids cited:",len(ids),"distinct:",len(set(ids)))
print("missing:",[i for i in set(ids) if i not in rows])
bad=0
paras=re.split(r"\n\s*\n|\n(?=\s*(?:\d+\.|-|\|))",t)
for p in paras:
    pn=norm(p)
    for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",pn):
        start=max(pn.rfind("**[",0,m.start()-1),0)
        seg=pn[start:m.start()]
        # quotes in the segment
        for q in re.findall(r'"([^"]{6,})"',seg):
            ok=all(norm(f).strip(" .,") in norm(rows[m.group(1)]) for f in q.split("[...]") if norm(f).strip(" .,"))
            if not ok:
                bad+=1; print("CHECK",m.group(1),"<-",q[:120])
print("fragments flagged:",bad)
