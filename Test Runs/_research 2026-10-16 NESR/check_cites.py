import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open(sys.argv[2], encoding="utf-8-sig"))}
bad = 0
if re.search(r"\[E\d+-\d+\]", run): print("E-id found"); bad += 1
ids = set(re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run))
for i in sorted(ids):
    if i not in rows: print("MISSING id", i); bad += 1
# quoted fragment followed (within 6 chars) by one or more bold ids
pat = re.compile(r'"([^"\n]{3,400})"\s{0,3}(?:\(?[a-z ]{0,0}\)?)?((?:\s*,?\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)')
norm = lambda t: re.sub(r"\s+", " ", t).strip()
n = 0
for m in pat.finditer(run.replace("\n", " ")):
    frag, idblock = m.group(1), m.group(2)
    cids = re.findall(r"[MLR]\d{4}-\d{3}", idblock)
    parts = [norm(p) for p in frag.split("[...]") if norm(p)]
    ok = any(all(p in norm(rows.get(c, "")) for p in parts) for c in cids)
    n += 1
    if not ok: print("NOT IN ROW:", cids, "::", frag[:120]); bad += 1
print(f"ids {len(ids)}, fragments checked {n}, problems {bad}")
print("PASS" if bad == 0 else "FAIL")
