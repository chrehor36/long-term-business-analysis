"""Citation check for the WHR run file.
1. no E-ids; 2. every M/L/R id exists in principle_ledger_v5.csv;
3. every quoted fragment that sits beside an id (quote then id within 40 characters, or id then ':' and quote)
   appears in that id's row ([...] elisions split the fragment; curly and straight quotes normalised)."""
import csv, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUN = os.path.join(ROOT, "Test Runs", "2026-10-17 Run - WHR Whirlpool.md")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
flat = re.sub(r"\s+", " ", text)
problems = 0
if re.search(r"\[E\d", text):
    print("E-id found"); problems += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text))
for i in sorted(ids):
    if i not in rows:
        print("MISSING id", i); problems += 1
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()
pairs = []
for m in re.finditer(r'"([^"]{6,}?)"[^"\[]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    pairs.append((m.group(1), m.group(2)))
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*:\s*"([^"]{6,}?)"', flat):
    pairs.append((m.group(2), m.group(1)))
for q, i in pairs:
    row = norm(rows.get(i, ""))
    parts = [p.strip(" .,;:") for p in norm(q).split("[...]")]
    if not all(p in row for p in parts if p):
        print(f"FRAGMENT not in {i}: {q[:120]}"); problems += 1
print(f"ids: {len(ids)}; quote-id pairs checked: {len(pairs)}; problems: {problems}")
sys.exit(1 if problems else 0)
