# Citation check for the MPTI run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment in the same sentence-chunk before an id is in that id's row (quotes and dashes normalized).
import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(sys.argv[2], encoding="utf-8-sig"))}
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
# fragment check: for each id occurrence, take the text since the previous id occurrence (or 300 chars), find "..." spans
flat = re.sub(r"\s+", " ", run)
pos = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", flat):
    i = m.group(1)
    start = pos
    chunk = flat[start:m.start()]
    # last sentence-ish chunk: after the last ';' or '. ' boundary that precedes a quote? keep chunk as is, but only the quotes nearest
    spans = re.findall(r'"([^"]{3,}?)"', chunk.replace("“", '"').replace("”", '"'))
    # consider only the spans after the last id in the chunk
    row = norm(rows.get(i, ""))
    if spans:
        last = spans[-1]
        if norm(last) not in row:
            print(f"FRAGMENT NOT IN ROW {i}: \"{last[:120]}\"")
            bad += 1
    else:
        print(f"NO QUOTE BEFORE {i}: ...{chunk[-140:]}")
    pos = m.end()
print("ids cited:", len(set(ids)), "occurrences:", len(ids))
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
