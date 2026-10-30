"""Run-file citation check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
immediately before an id (within the same sentence) appears in that row's quote (elisions [...] split)."""
import csv, re, sys, unicodedata
RUN = "../2026-10-16 Run - HRI Herc Holdings.md"
LED = "../../principle_ledger_v5.csv"
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-")]:
        s = s.replace(a, b)
    s = re.sub("['�\-]", "", s)  # apostrophes, dashes and replacement characters dropped on both sides
    s = re.sub("['�\\-]", "", s)  # apostrophes, dashes and replacement characters dropped on both sides
    return re.sub(r"\s+", " ", s).strip().lower()
rows = {}
with open(LED, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        rows[r["id"]] = norm(r["quote_verbatim"])
text = open(RUN, encoding="utf-8").read()
bad = 0
for m in re.finditer(r"\bE\d-\d{2}\b", text):
    print("E-id found:", m.group(0)); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id:", i); bad += 1
# quote then ids: "...." then optional punctuation/space then **[ID]** (possibly several ids)
pat = re.compile(r'"([^"]{6,600})"[\s,.;:)]*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[\s,]*)+)')
n = 0
for m in pat.finditer(text):
    q = m.group(1); cited = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    frags = [norm(x) for x in re.split(r"\[\.\.\.\]|\.\.\.", q) if norm(x).strip(" .,;:")]
    ok = any(all(fr.strip(" .,;:") in rows.get(c, "") for fr in frags) for c in cited)
    n += 1
    if not ok:
        print("QUOTE NOT IN ROW:", cited, "|", q[:120]); bad += 1
print(f"ids cited: {len(set(ids))}; quotes checked: {n}; problems: {bad}")
sys.exit(1 if bad else 0)
