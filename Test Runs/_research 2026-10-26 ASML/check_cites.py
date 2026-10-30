"""Citation check for the ASML run file (2026-10-26).
1. No E-ids.  2. Every M/L/R id cited exists in principle_ledger_v5.csv.
3. Every quoted fragment in the text span that ends at an id (from the previous id, or the paragraph start) is found
   verbatim in that id's row; '[...]' inside a fragment splits it into parts that must each be found, in order.
   Spans flagged are printed for a human to read: a filing quote that happens to sit in a span is reported as
   'NOT IN ROW' and must be moved or re-read; the run file is corrected until this prints nothing flagged.
4. No em dash in lines that are not template headings."""
import csv, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RUN = os.path.join(ROOT, "Test Runs", "2026-10-26 Run - ASML ASML Holding.md")
rows = {}
for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8")):
    rows[r.get("﻿id") or r.get("id")] = r["quote_verbatim"]
text = open(RUN, encoding="utf-8").read()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
print("E-ids:", eids or "none"); bad += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
missing = sorted({i for i in ids if i not in rows})
print("ids cited:", len(set(ids)), "distinct;", "missing:", missing or "none"); bad += len(missing)
def norm(s):
    return re.sub(r"\s+", " ", s)


def sentence_start(para, end):
    """Index where the sentence holding position `end` starts: after the last sentence end (. ! ? followed by space
    and a capital, '*' or '(') that lies outside a double-quoted string."""
    start = 0
    for m in re.finditer(r"[.!?;:]\"?\s+(?=[A-Z*(\-])", para[:end]):
        if para[:m.start()].count('"') % 2 == 0:
            start = m.end()
    return start


for para in re.split(r"\n\s*\n", text):
    pos = 0
    for m in re.finditer(r"\[([MLR]\d{4}-\d{3})\]", para):
        s0 = max(pos, sentence_start(para, m.start()))
        span = para[s0:m.start()]
        pos = m.end()
        rid = m.group(1)
        row = norm(rows.get(rid, ""))
        for q in re.findall(r"\"([^\"]{3,})\"", span):
            q = norm(q)
            parts = [p.strip(" .,;") for p in q.split("[...]")]
            at = 0; ok = True
            for p in parts:
                if not p: continue
                k = row.find(p, at)
                if k < 0: ok = False; break
                at = k + len(p)
            if not ok:
                bad += 1
                print(f"NOT IN ROW {rid}: \"{q[:120]}\"")
for n, line in enumerate(text.splitlines(), 1):
    if "—" in line and not line.startswith("#"):
        print(f"em dash at line {n}: {line[:100]}"); bad += 1
print("FLAGS:", bad)
