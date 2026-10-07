import csv, re, sys
L="c:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv"
F="c:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-05 Run - SBH Sally Beauty.md"
rows={r["id"]:r["quote_verbatim"] for r in csv.DictReader(open(L,encoding="utf-8-sig"))}
s=open(F,encoding="utf-8").read()
def norm(x): return re.sub(r"\s+"," ",re.sub(r"[^\x00-\x7f]","?",x)).strip()
ids=re.findall(r"\[([A-Z]+\d{4}-\d{3})\]",s)
print("ids cited:",len(ids),"distinct:",len(set(ids)))
eids=re.findall(r"\[E\d+-\d+\]",s); print("E-ids:",eids)
missing=[i for i in set(ids) if i not in rows]; print("missing:",missing)
bad=0
# a quoted fragment directly before an id (allow one or two ids in a row after it)
for m in re.finditer(r'"([^"\n]{3,400})"\s*((?:\*\*\[[A-Z]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)',s):
    frag=m.group(1); for_ids=re.findall(r"\[([A-Z]\d{4}-\d{3})\]",m.group(2))
    parts=[p for p in frag.split("[...]")]
    if not any(all(norm(p.strip(" ."))[:200] in norm(rows.get(i,"")) for p in parts if p.strip()) for i in for_ids):
        print("NOMATCH",for_ids,"|",frag[:120]); bad+=1
print("fragment mismatches:",bad)
