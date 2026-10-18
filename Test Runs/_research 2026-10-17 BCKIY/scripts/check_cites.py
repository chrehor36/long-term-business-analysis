# Citation check for the run file.
# 1. No E-ids. 2. Every M/L/R id in bold brackets exists in principle_ledger_v5.csv.
# 3. Every quoted fragment ("...") that sits immediately before an id (same sentence span, the nearest quote to the left
#    of the id, with only spaces, commas, parentheses or an em-free connector between) is a substring of that row's quote,
#    after normalising quotes, dashes, whitespace and the [...] elision (each piece between elisions must appear, in order).
import csv, re, sys, unicodedata
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
RUN = ROOT + r"\Test Runs\2026-10-17 Run - BCKIY Babcock International Group.md"
rows = {}
with open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = r["quote_verbatim"]

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2014", "-"), ("\u2013", "-"), ("\ufffd", "?")]:
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

t = open(RUN, encoding="utf-8").read()
bad = 0
if re.search(r"\[E\d", t):
    print("E-id present"); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", t)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); bad += 1
# quoted fragment immediately followed by one or more ids
pat = re.compile(r'"([^"]{3,}?)"\s*((?:\(?[^"\n]{0,40}?\)?\s*)?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
checked = 0
for m in pat.finditer(t):
    frag, gap, i = m.group(1), m.group(2), m.group(3)
    if len(gap) > 40 or i not in rows:
        continue
    q = norm(rows[i]); ok = True; pos = 0
    for piece in [p for p in re.split(r"\[\.\.\.\]|\.\.\.", frag)]:
        pn = norm(piece).strip(" .,;:")
        if not pn:
            continue
        k = q.find(pn, pos)
        if k < 0:
            ok = False; break
        pos = k + len(pn)
    checked += 1
    if not ok:
        print("NOT IN ROW", i, "::", frag[:120]); bad += 1
print("ids", len(set(ids)), "quote-id pairs checked", checked, "problems", bad)
sys.exit(1 if bad else 0)
