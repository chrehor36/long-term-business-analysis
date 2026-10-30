"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
that sits beside an id (same paragraph, the quote ending within 12 characters of the bracket) is in that
row's verbatim text, after normalising quotes, apostrophes and dashes.
usage: python -I check_run.py <run_file> <ledger_csv>"""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run, ledger = sys.argv[1], sys.argv[2]
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ledger, encoding="utf-8-sig"))}
text = open(run, encoding="utf-8").read()


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


bad = 0
eids = re.findall(r"\[E\d-\d+\]", text)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted({i for i in ids if i not in rows})
print(f"{len(ids)} id citations, {len(set(ids))} distinct; missing: {missing}")
bad += len(missing)
# quoted fragments immediately followed by an id
pat = re.compile(r'"([^"]{8,600}?)"[^"\[\n]{0,12}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', re.S)
n = 0
for m in pat.finditer(text):
    frag, i = m.group(1), m.group(2)
    n += 1
    if i not in rows:
        continue
    parts = [p.strip(" .,;:") for p in re.split(r"\[\.\.\.\]", frag) if p.strip(" .,;:")]
    row = norm(rows[i])
    for p in parts:
        if norm(p) not in row:
            print(f"NOT IN ROW {i}: {p!r}")
            bad += 1
print(f"{n} quoted fragments checked beside ids")
print("RESULT:", "PASS" if bad == 0 else f"FAIL ({bad})")
