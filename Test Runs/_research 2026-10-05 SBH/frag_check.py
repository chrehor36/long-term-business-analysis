import csv, re, sys
L="c:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv"
rows={r["id"]:r["quote_verbatim"] for r in csv.DictReader(open(L,encoding="utf-8-sig"))}
def norm(s): return re.sub(r"\s+"," ",re.sub(r"[^\x00-\x7f]","?",s)).strip()
pairs=[l.split("|",1) for l in sys.stdin.read().strip().splitlines()]
bad=0
for i,f in pairs:
    i=i.strip(); f=f.strip()
    if i not in rows: print("MISSING", i); bad+=1; continue
    ok=all(norm(p) in norm(rows[i]) for p in f.split(" [...] "))
    if not ok: print("NOMATCH", i, "|", f); bad+=1
print("bad", bad)
