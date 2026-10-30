"""Citation check for the ADRZY run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment placed immediately before an id is in that row (elisions [...] split the fragment).
Usage: python -I check_citations.py <run file> <ledger csv>   |  python -I check_citations.py --show ID ..."""
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2014", "-"), ("\u2013", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

def load(path):
    rows = {}
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows[r["id"]] = r["quote_verbatim"]
    return rows

if sys.argv[1] == "--show":
    rows = load(sys.argv[2])
    for i in sys.argv[3:]:
        print(i, "::", rows.get(i, "<<MISSING>>")); print()
    sys.exit()

run, ledger = sys.argv[1], sys.argv[2]
rows = load(ledger)
text = open(run, encoding="utf-8").read()
problems = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", eids); problems += len(eids)
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); problems += 1
# quoted fragment directly followed (within 12 chars) by a bold id
pat = re.compile(r'"([^"]{3,}?)"[^"\n]{0,12}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
n = 0
for m in pat.finditer(text):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    q = norm(rows[i])
    for piece in re.split(r"\[\.\.\.\]", frag):
        p = norm(piece).strip(" .,;:")
        if len(p) < 3:
            continue
        n += 1
        if p not in q:
            print(f"NOT IN ROW {i}: {piece!r}"); problems += 1
print(f"ids cited: {len(set(ids))}; fragments checked: {n}; problems: {problems}")
