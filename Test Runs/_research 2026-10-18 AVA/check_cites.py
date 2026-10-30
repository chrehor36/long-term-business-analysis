"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment immediately before an id is in that row's quote (curly/straight quotes normalised)."""
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-18 Run - AVA Avista.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
txt = open(RUN, encoding="utf-8").read()
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", txt)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", txt)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
# fragments: a "quoted" string followed (within 12 chars, through ** and spaces) by one or more ids
for m in re.finditer(r'"([^"]{3,})"((?:\s|\*|,|\(|\)|;|:|\.)*?)((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)', txt):
    frag = m.group(1); idlist = re.findall(r"[MLR]\d{4}-\d{3}", m.group(3))
    parts = [p for p in re.split(r"\s*\[\.\.\.\]\s*", frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(i, "")) for p in parts) for i in idlist)
    if not ok:
        print("FRAGMENT NOT IN ROW", idlist, "|", frag[:120]); bad += 1
print("ids:", len(set(ids)), "problems:", bad)
sys.exit(1 if bad else 0)
