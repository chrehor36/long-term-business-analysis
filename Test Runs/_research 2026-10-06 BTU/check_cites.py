import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
rows={r["id"]:r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv",encoding="utf-8-sig"))}
s=open("Test Runs/2026-10-06 Run - BTU Peabody Energy.md",encoding="utf-8").read()
bad=0
# 1. no E-ids (v4)
for m in re.finditer(r"\[(E\d+-\d+)\]", s): print("V4 ID", m.group(1)); bad+=1
ids=re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", s)
allids=set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", s))
for i in sorted(allids):
    if i not in rows: print("MISSING", i); bad+=1
print("ids cited:", len(allids))
# 2. every quoted fragment immediately before an id (within the same sentence/clause) is in that row
norm=lambda t: re.sub(r"\s+"," ",t).strip()
for m in re.finditer(r'"([^"]{3,})"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', s):
    frag, i = m.group(1), m.group(2)
    q = norm(rows.get(i,""))
    parts=[norm(p) for p in frag.split("[...]") if norm(p)]
    pos=0; ok=True
    for p in parts:
        k=q.find(p, pos)
        if k<0: ok=False; break
        pos=k+len(p)
    if not ok: print("FRAGMENT NOT IN ROW", i, "::", frag); bad+=1
# also fragments followed by ' is "' patterns: check all quoted strings on same line as an id (looser)
for line in s.split("\n"):
    ids_l=re.findall(r"\[([MLR]\d{4}-\d{3})\]", line)
    if not ids_l: continue
for ch in ["—"]:
    n=s.count(ch); print("em dashes in file:", n)
print("BAD" if bad else "ALL CHECKS PASS", bad)
