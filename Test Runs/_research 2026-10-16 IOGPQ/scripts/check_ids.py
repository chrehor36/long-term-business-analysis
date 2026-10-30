import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open("principle_ledger_v5.csv", encoding="utf-8"))}
norm = lambda s: re.sub(r"\s+", " ", s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')).strip()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
print("ids cited:", len(ids), "distinct:", len(set(ids)))
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); bad += 1
# quoted fragment directly before an id (allow punctuation/space between)
for m in re.finditer(r'"([^"]{4,400})"[\s.,;:)]*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run.replace("\n", " ")):
    frag, i = m.group(1), m.group(2)
    ok = i in rows and norm(frag) in norm(rows[i])
    print(("OK  " if ok else "FAIL"), i, frag[:70]); bad += (not ok)
print("RESULT:", "PASS" if not bad else f"FAIL ({bad})")
