import csv,re,sys
rows={r[0]:r[2] for r in csv.reader(open("principle_ledger_v5.csv",encoding="utf-8"))}
s=open("Test Runs/2026-10-05 Run - SLVM Sylvamo.md",encoding="utf-8").read()
ids=re.findall(r"\[([A-Z]+\d{4}-\d{3})\]",s)
bad=[i for i in ids if i not in rows]; e=[i for i in ids if not re.match(r"^[MLR]\d",i)]
print("ids",len(ids),"distinct",len(set(ids)),"missing",bad,"non-MLR",e)
print("em dashes", s.count("—"), "en dashes", s.count("–"))
# fragments: a quoted "..." immediately followed (within 3 chars) by **[id]**
norm=lambda t: re.sub(r"\s+"," ",t.replace("“",'"').replace("”",'"'))
fails=0;n=0
for m in re.finditer(r'"([^"]{6,400}?)"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s):
    frag,i=m.group(1),m.group(2); n+=1
    q=norm(rows[i]); f=norm(frag)
    if f not in q and f.rstrip(".?,") not in q:
        fails+=1; print("FRAG FAIL",i,"|",frag[:120])
print("fragments checked",n,"fails",fails)
