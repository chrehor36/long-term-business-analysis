"""Check for the HAS run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment
that stands immediately before a bold id (same sentence) is found in that row's quote. Prints problems; exit 1 on any."""
import csv, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUN = os.path.join(ROOT, "Test Runs", "2026-10-07 Run - HAS Hasbro.md")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()

problems = []
if re.search(r"\[E\d-\d+\]", text):
    problems.append("E-id present")
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows:
        problems.append("missing id " + i)
# quoted fragments: for each bold id, look back to the previous id or sentence-ish boundary and take quotes there
checked = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text):
    rid = m.group(1)
    start = max(text.rfind("**[", 0, m.start() - 1), text.rfind("\n", 0, m.start()))
    seg = text[start + 1:m.start()]
    # same sentence only: cut at the last sentence end that is outside quotation marks
    cut = max(seg.rfind(". "), seg.rfind("; "))
    while cut != -1 and (seg[:cut].count("“") + seg[:cut].count('"')) % 2 == 1:
        cut = max(seg.rfind(". ", 0, cut), seg.rfind("; ", 0, cut))
    if cut != -1:
        seg = seg[cut + 2:]
    # the quotes nearest before this id, after any earlier id
    frags = re.findall(r"[“\"]([^\"“”]{6,}?)[”\"]", seg)
    if not frags or rid not in rows:
        continue
    frag = frags[-1]
    pieces = [p for p in re.split(r"\s*\[\.\.\.\]\s*", frag) if p.strip()]
    q = norm(rows[rid])
    for p in pieces:
        pn = norm(p).strip(" .,;:")
        # nested quotation marks inside a row are printed as quotes in the row too; compare without them
        if pn.replace('"', "") not in q.replace('"', ""):
            problems.append(f"{rid}: fragment not in row: {p[:90]}")
    checked += 1
print(f"ids cited: {len(set(ids))} distinct, {len(ids)} uses; quoted fragments checked: {checked}")
for p in problems:
    print("PROBLEM", p)
print("PASS" if not problems else "FAIL")
sys.exit(1 if problems else 0)
