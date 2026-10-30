"""Citation check for the AWK run file.
1. no E-ids; 2. every M/L/R id exists in principle_ledger_v5.csv;
3. every quoted fragment immediately before an id (same paragraph, the last "..." before the id) is in that row
   (pieces split on [...]); ids with no quote right before them are listed as BARE for review.
Usage: python -I check_cites.py"""
import csv, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RUN = os.path.join(ROOT, "Test Runs", "2026-10-28 Run - AWK American Water Works.md")
rows = {r[0]: r[2] for r in csv.reader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8-sig").read()

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("�", "")
    return re.sub(r"\s+", " ", s).strip().lower()

bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
missing = sorted({i for i in ids if i not in rows})
if missing:
    print("MISSING ids:", missing); bad += 1
print(f"{len(ids)} id citations, {len(set(ids))} distinct")

bare = []
for para in re.split(r"\n\s*\n", text):
    for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", para):
        rid = m.group(1)
        before = para[:m.start()]
        # the text between the previous id (if any) and this one
        prev = list(re.finditer(r"\*\*\[[MLR]\d{4}-\d{3}\]\*\*", before))
        seg = before[prev[-1].end():] if prev else before
        quotes = re.findall(r"[\"“]([^\"“”]{3,}?)[\"”]", seg)
        if not quotes:
            # allow an id that directly follows another id's quote chain: "...", **[A]**, **[B]**
            bare.append((rid, seg[-120:].replace("\n", " ")))
            continue
        q = quotes[-1]
        row = norm(rows.get(rid, ""))
        for piece in re.split(r"\[\.\.\.\]", q):
            p = norm(piece).strip(" .,;:")
            if p and p not in row:
                print(f"NOT IN ROW {rid}: \"{piece.strip()}\""); bad += 1
print(f"BARE (no quote between this id and the previous one): {len(bare)}")
for rid, ctx in bare:
    print(f"  {rid}: ...{ctx}")
print("RESULT:", "FAIL" if bad else "PASS (quotes and ids)")
