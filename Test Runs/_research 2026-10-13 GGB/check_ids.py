# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that
# sits immediately before an id (in the same sentence) is a substring of that row's quote.
import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(sys.argv[2], encoding="utf-8-sig"))}
norm = lambda s: re.sub(r"\s+", " ", s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')).strip()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", run)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
# quoted fragments followed (within the same line run) by one or more ids
flat = run.replace("\n", " ")
for m in re.finditer(r"\u201c([^\u201d]{6,}?)\u201d\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)", flat):
    frag = m.group(1); idlist = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    parts = [p.strip() for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(i, "")) for p in parts) for i in idlist)
    if not ok: print("FRAGMENT NOT IN ROW", idlist, "::", frag[:120]); bad += 1
for m in re.finditer(r'"([^"]{6,}?)"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)', flat):
    frag = m.group(1); idlist = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    parts = [p.strip() for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(i, "")) for p in parts) for i in idlist)
    if not ok: print("FRAGMENT NOT IN ROW", idlist, "::", frag[:120]); bad += 1
print("ids cited:", len(set(ids)), "checks failed:", bad)
print("PASS" if bad == 0 else "FAIL")
