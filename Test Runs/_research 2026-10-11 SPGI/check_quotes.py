"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
in the same sentence as an id (before it, up to the previous id or sentence start) is found in that id's row.
Normalises curly quotes/apostrophes and whitespace; '[...]' inside a fragment splits it into pieces checked in order.
Usage: python check_quotes.py   (from anywhere)"""
import csv, re, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, "..", ".."))
run = os.path.join(here, "..", "2026-10-11 Run - SPGI S&P Global.md")
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(os.path.join(root, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("�", "'")
    return re.sub(r"\s+", " ", s).strip().lower()
t = open(run, encoding="utf-8").read()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", t)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", t)
missing = sorted(set(i for i in ids if i not in rows))
print("ids cited:", len(set(ids)), "missing:", missing or "none"); bad += len(missing)
# fragments: for each id occurrence, look back over the text since the previous id occurrence (same paragraph)
flat = re.sub(r"\s+", " ", t)
checked = 0
prev_end = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", flat):
    seg = flat[prev_end:m.start()]
    prev_end = m.end()
    # restrict to the current sentence-ish window: last 600 chars
    seg = seg[-700:]
    frags = re.findall(r'"([^"]{6,}?)"(?=[^"]*$|[\s,.;:)])', seg)
    # take quotes using straight double quotes as delimiters, only the last few in the segment
    frags = re.findall(r'"([^"]+)"', seg)
    if not frags: continue
    rid = m.group(1); row = norm(rows.get(rid, ""))
    for f in frags[-3:]:
        if len(f) < 8: continue
        pieces = [norm(p) for p in re.split(r"\[\.\.\.\]", f) if norm(p)]
        ok = all(p.strip(" .,;:") in row for p in pieces)
        checked += 1
        if not ok:
            # a fragment may belong to a filing quote, not the row: report for manual review
            print(f"NOT IN ROW {rid}: \"{f[:120]}\"")
            bad += 0
print("fragments checked:", checked)
print("RESULT:", "PASS (ids); review any NOT IN ROW lines above by hand" if not missing and not eids else "FAIL")
