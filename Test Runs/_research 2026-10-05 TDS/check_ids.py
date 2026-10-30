import csv,re,sys,unicodedata
rows={r["id"]:r["quote_verbatim"] for r in csv.DictReader(open("../../principle_ledger_v5.csv",encoding="utf-8-sig"))}
s=open("../2026-10-05 Run - TDS Telephone and Data Systems.md",encoding="utf-8").read()
def norm(x): return re.sub(r"\s+"," ",x.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"')).strip()
ids=re.findall(r"\[([A-Z]+\d{4}-\d{3}|E\d+-\d+)\]",s)
print("ids cited:",len(ids),"distinct:",len(set(ids)))
bad=[i for i in set(ids) if i not in rows]; print("missing/E ids:",bad)
eids=re.findall(r"\[E\d",s); print("E-ids:",eids)
# fragments: text between previous id marker and this id, same paragraph
prob=0
for m in re.finditer(r"\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*",s):
    start=max(s.rfind("**[",0,m.start()-1), s.rfind("\n\n",0,m.start()), 0)
    if s.rfind("**[",0,m.start()-1)>=0:
        pe=s.find("]**",s.rfind("**[",0,m.start()-1))
        start=max(start, pe+3 if pe< m.start() else 0)
    seg=s[start:m.start()]
    frags=re.findall(r"\"([^\"]{4,})\"",seg)
    row=norm(rows[m.group(1)])
    for f in frags:
        for piece in f.split("[...]"):
            p=norm(piece).strip(" .,;:")
            if len(p)<4: continue
            if p not in row:
                prob+=1; print(f"CHECK {m.group(1)}: «{p[:110]}»")
print("fragments not in row:",prob)
