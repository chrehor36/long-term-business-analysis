# Checks the BEP run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before a bold id is in that row's quote
# (whitespace, quote marks and dashes normalised; [...] splits a fragment into parts checked separately).
import csv, re, unicodedata

RUN = "Test Runs/2026-10-18 Run - BEP Brookfield Renewable Partners.md"
rows = {}
with open("principle_ledger_v5.csv", encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        rows[row["id"]] = row["quote_verbatim"]


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("—", "-"), ("–", "-")):
        s = s.replace(a, b)
    s = s.replace('"', "").replace("'", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip().lower()


txt = open(RUN, encoding="utf-8").read()
probs = 0
for m in re.finditer(r"\[E\d+-\d+\]", txt):
    print("E-ID:", m.group())
    probs += 1
ids = re.findall(r"\[((?:M|L|R)\d{4}-\d{3})\]", txt)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING ID:", i)
        probs += 1
LQ, RQ = "“", "”"
pat = ("(?:" + LQ + "([^" + RQ + "]{4,600})" + RQ + '|"([^"]{4,600})")'
       + '[^"' + LQ + "\\[\\n]{0,14}\\*\\*\\[((?:M|L|R)\\d{4}-\\d{3})\\]\\*\\*")
checked = 0
for m in re.finditer(pat, txt):
    frag, rid = (m.group(1) or m.group(2)), m.group(3)
    if rid not in rows:
        continue
    for p in re.split(r"\[\.\.\.\]", frag):
        if not norm(p):
            continue
        checked += 1
        if norm(p) not in norm(rows[rid]):
            print(f"NOT IN ROW {rid}: {p[:100]!r}")
            probs += 1
print("ids cited:", len(set(ids)), "fragments checked:", checked, "problems:", probs)
