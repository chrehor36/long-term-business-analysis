# Citation check for the JUTOY run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment that sits immediately before an id (closing quote, then at most a few characters, then the id)
# is found verbatim in that row (elisions "[...]" split the fragment into pieces, each of which must be found in order).
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
run, ledger = sys.argv[1], sys.argv[2]
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ledger, encoding="utf-8-sig"))}
text = open(run, encoding="utf-8").read()
flat = re.sub(r"\s*\n\s*", " ", text)   # join wrapped lines

bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted({i for i in ids if i not in rows})
if missing:
    print("missing ids:", missing); bad += 1
print(f"{len(ids)} id citations, {len(set(ids))} distinct, missing {len(missing)}")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

checked = 0
for m in re.finditer(r'"([^"]{6,}?)"[^"\[]{0,12}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, rid = m.group(1), m.group(2)
    row = norm(rows.get(rid, ""))
    pieces = [norm(p) for p in frag.split("[...]") if norm(p)]
    pos, ok = 0, True
    for p in pieces:
        k = row.find(p, pos)
        if k < 0:
            ok = False; break
        pos = k + len(p)
    checked += 1
    if not ok:
        bad += 1
        print(f"NOT IN ROW {rid}: \"{frag}\"")
print(f"{checked} quoted fragments checked beside ids")
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
