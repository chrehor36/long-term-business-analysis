# Wider check: every quoted fragment followed within 220 chars by a bold id (with no other quote between) is tested against that id cluster.
import csv, re, sys
L = "C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv"
rows = {(x.get("id") or x.get("\ufeffid")): x["quote_verbatim"] for x in csv.DictReader(open(L, encoding="utf-8-sig"))}
def norm(s):
    for a,b in [("\u2019","'"),("\u2018","'"),("\u201c",'"'),("\u201d",'"'),("\u2014","-"),("\u2013","-"),("\ufffd","")]: s=s.replace(a,b)
    return re.sub(r"\s+"," ",s).strip().lower()
flat = re.sub(r"\s+", " ", open(sys.argv[1], encoding="utf-8").read())
for m in re.finditer(r'"([^"]{3,700})"', flat):
    tail = flat[m.end():m.end()+220]
    q = tail.find('"'); seg = tail if q < 0 else tail[:q]
    idl = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", seg)
    if not idl: continue
    parts = [p for p in re.split(r"\[\.\.\.\]", m.group(1)) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(i,"")) for p in parts) for i in idl)
    print("OK " if ok else "?? ", idl, m.group(1)[:110])
