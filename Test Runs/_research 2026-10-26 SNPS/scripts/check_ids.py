"""Citation check for the SNPS run file.
1. No E-id is cited.  2. Every cited M/L/R id exists in principle_ledger_v5.csv.
3. Every quoted fragment written beside an id (a "..." quote immediately before or after the bold id, in the same
   sentence) appears in that row's quote_verbatim; elisions written as [...] or ... are checked piece by piece.
Usage: python -I check_ids.py <run file> <ledger csv>"""
import csv, re, sys
run, ledger = sys.argv[1], sys.argv[2]
text = open(run, encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ledger, encoding="utf-8-sig"))}
norm = lambda s: re.sub(r"\s+", " ", s.replace("“", '"').replace("”", '"')).strip()
fails = 0
eids = sorted(set(re.findall(r"\[(E\d+-\d+)\]", text)))
if eids:
    print("E-ids cited:", eids); fails += 1
ids = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)))
missing = [i for i in ids if i not in rows]
if missing:
    print("ids not in ledger:", missing); fails += len(missing)
ID = r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*"
pairs = []
# quote then id:  "fragment" **[ID]**   (optionally with a short connector like ", " or ")" between)
for m in re.finditer(r'"([^"\n]{3,400})"[\s,.;:)]{0,3}' + ID, text):
    pairs.append((m.group(2), m.group(1)))
# id then quote:  **[ID]**, "fragment"  or  **[ID]** asks "fragment"
for m in re.finditer(ID + r'(?:,| asks| \(\d{4}\))?:? "([^"\n]{3,400})"', text):
    pairs.append((m.group(1), m.group(2)))
checked = 0
for i, frag in pairs:
    row = norm(rows.get(i, ""))
    pieces = [p.strip(" .,;") for p in re.split(r"\[\.\.\.\]|\.\.\.", norm(frag)) if p.strip(" .,;")]
    for p in pieces:
        checked += 1
        if p not in row:
            print(f"NOT IN ROW {i}: {p!r}"); fails += 1
print(f"ids cited {len(ids)}; quote fragments checked {checked}; failures {fails}")
sys.exit(1 if fails else 0)
