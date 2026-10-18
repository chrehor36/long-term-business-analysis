"""Citation check for the BIPC run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
that sits immediately before an id (within the same sentence) is found verbatim in that row (elisions [...] split)."""
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
ROOT = "C:/Users/chreh/OneDrive/Documents/BRK/"
RUN = ROOT + "Test Runs/2026-10-17 Run - BIPC Brookfield Infrastructure Corp.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(ROOT + "principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\ufffd", "")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

problems = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", eids); problems += len(eids)
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); problems += 1
# quoted fragment(s) directly before an id: "...." **[ID]**  (allow up to 3 ids chained)
for m in re.finditer(r"\u201c([^\u201d]{3,400})\u201d\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)|\"([^\"]{3,400})\"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)", text):
    frag = m.group(1) or m.group(3)
    idblock = m.group(2) or m.group(4)
    cited = re.findall(r"\[([MLR]\d{4}-\d{3})\]", idblock)
    parts = [p for p in re.split(r"\[\.\.\.\]", frag) if p.strip()]
    ok = False
    for c in cited:
        row = norm(rows.get(c, ""))
        if all(norm(p) in row for p in parts):
            ok = True; break
    if not ok:
        print("FRAGMENT NOT IN ROW", cited, "|", frag[:160]); problems += 1
print("ids cited:", len(set(ids)), "| problems:", problems)
