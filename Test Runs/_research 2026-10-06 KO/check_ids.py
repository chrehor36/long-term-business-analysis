"""Check the run file against principle_ledger_v5.csv:
 (1) every v5 id [M/L/R yyyy-nnn] cited exists in the ledger;
 (2) every double-quoted fragment immediately followed by a bold id is a substring of that row's quote
     (whitespace collapsed; [...] elisions split the fragment into parts, each checked in order).
Usage: python check_ids.py"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RUN = os.path.join(ROOT, "Test Runs", "2026-10-06 Run - KO Coca-Cola.md")
LEDGER = os.path.join(ROOT, "principle_ledger_v5.csv")

rows = {}
with open(LEDGER, encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        rows[row["id"]] = row["quote_verbatim"]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


text = open(RUN, encoding="utf-8").read()
found = re.findall(r"\b([MLR]\d{4}-\d{3})\b", text)
missing = sorted({i for i in found if i not in rows})
print(f"ids cited: {len(set(found))} distinct, {len(found)} total; missing from ledger: {missing or 'none'}")

bad = 0
checked = 0
for m in re.finditer(r"\"([^\"]{8,}?)\"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text.replace("“", '"').replace("”", '"')):
    frag, rid = m.group(1), m.group(2)
    q = norm(rows.get(rid, ""))
    parts = [norm(p) for p in re.split(r"\[\.\.\.\]", frag) if norm(p)]
    pos = 0
    ok = True
    for p in parts:
        p = p.strip(" .,;")
        i = q.find(p, pos)
        if i < 0:
            ok = False
            break
        pos = i + len(p)
    checked += 1
    if not ok:
        bad += 1
        print(f"  NOT VERBATIM {rid}: \"{frag[:120]}\"")
print(f"quoted fragments checked: {checked}; not verbatim: {bad}")
