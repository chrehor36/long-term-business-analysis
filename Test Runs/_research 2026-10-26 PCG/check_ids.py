"""Check the PCG run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
placed immediately before an id is found verbatim (whitespace-normalised, [...] splits) in that row."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:/Projects/BRK/"
run = open(ROOT + "Test Runs/2026-10-26 Run - PCG PG&E.md", encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ROOT + "principle_ledger_v5.csv", encoding="utf-8-sig"))}
norm = lambda s: re.sub(r"\s+", " ", s).strip()
text = norm(run)
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
missing = sorted(set(i for i in ids if i not in rows))
if missing:
    print("missing ids:", missing); bad += 1
print(f"{len(ids)} id citations, {len(set(ids))} distinct, all present: {not missing}")
checked = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text):
    pre = text[:m.start()]
    tail = pre[-4:]
    # a quote ends right before the id (allowing ". " or ", " or " ")
    mm = re.search(r'"([^"]{3,})"[.,;:]?\s?$', pre[-2000:])
    if not mm:
        continue
    frag = mm.group(1)
    row = norm(rows.get(m.group(1), ""))
    pieces = [p.strip(" .,") for p in frag.split("[...]") if p.strip(" .,")]
    ok = all(p in row for p in pieces)
    checked += 1
    if not ok:
        bad += 1
        print("NOT IN ROW", m.group(1), "|", frag[:160])
print(f"{checked} quoted fragments beside ids checked")
print("PASS" if not bad else f"FAIL ({bad})")
