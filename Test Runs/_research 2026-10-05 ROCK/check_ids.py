import csv,re,sys
rows={}
for r in csv.DictReader(open("principle_ledger_v5.csv",encoding="utf-8-sig")):
    rows[r.get("id") or r.get("﻿id")]=r["quote_verbatim"]
s=open("Test Runs/2026-10-05 Run - ROCK Gibraltar Industries.md",encoding="utf-8").read()
ok=True
e=re.findall(r"\[E\d+-\d+\]",s)
print("E-ids:",e); ok&= not e
ids=re.findall(r"\[([MLR]\d{4}-\d{3})\]",s)
missing=sorted(set(i for i in ids if i not in rows)); print("ids used:",len(set(ids)),"missing:",missing); ok&=not missing
def norm(t): return re.sub(r"[‘’“”'\"�]","",t).replace("  "," ")
# quoted fragment immediately followed by one or more bold ids
pat=re.compile(r'"([^"\n]{3,400})"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)')
n=0
for m in pat.finditer(s):
    frag=m.group(1); cited=re.findall(r"[MLR]\d{4}-\d{3}",m.group(2)); n+=1
    exact=any(frag in rows.get(c,"") for c in cited)
    loose=any(norm(frag) in norm(rows.get(c,"")) for c in cited)
    if not exact:
        print(("LOOSE-OK " if loose else "FAIL ")+str(cited)+" :: "+frag)
        ok&=loose
print("quoted fragments checked:",n)
print("RESULT", "PASS" if ok else "FAIL")
