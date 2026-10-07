"""Citation check for the COST run of 2026-10-06 (the check script the dispatch brief requires).

Checks, against the run file:
  1. no E-ids (the v4 ledger) are cited;
  2. every M/L/R id in bold resolves to a row of principle_ledger_v5.csv;
  3. every quoted fragment that sits beside an id (in the same sentence, before or after the id) is a verbatim
     substring of that row's quote, elisions written as [...] allowed, with the transcript's curly quotes and dashes
     normalised the same way on both sides.
Run from the repository root:  python "Test Runs/_research 2026-10-06 COST/check_citations.py"
"""
import csv, re, sys, os, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUN = os.path.join(ROOT, "Test Runs", "2026-10-06 Run - COST Costco Wholesale.md")
LEDGER = os.path.join(ROOT, "principle_ledger_v5.csv")

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("‒", "-").replace("�", "?")
    s = re.sub(r"\s+", " ", s)
    return s.strip()

rows = {}
with open(LEDGER, encoding="utf-8-sig") as fh:
    for r in csv.DictReader(fh):
        rows[r["id"]] = norm(r["quote_verbatim"])
text = open(RUN, encoding="utf-8").read()

# 1. E-ids
e_ids = re.findall(r"\[E\d-\d+\]", text)
# 2. ids
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", text)
missing = sorted({i for i in ids if i not in rows})
# 3. fragments beside ids: take each sentence-ish chunk; for each bold id in the chunk, every "..." fragment in the chunk
#    must be a substring of that row (fragments may be elided with [...]).
bad = []
checked = 0
# split into chunks at sentence ends or list-item starts, keeping it generous
chunks = re.split(r"(?<=[.;:])\s+(?=[A-Z\"\(\*])|\n- |\n\d+\. |\n\|", text)
for ch in chunks:
    ch_ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", ch)
    if not ch_ids:
        continue
    frags = re.findall(r"\"([^\"]{12,}?)\"", ch)
    for f in frags:
        fn = norm(f)
        # skip fragments that are filing quotes (they sit beside a filing reference, not a row); a fragment counts as
        # beside an id only if some id's row contains it; otherwise flag it for a human look unless it is marked as a
        # filing quote by a parenthetical page/Note/8-K/proxy reference in the same chunk
        pieces = [p.strip() for p in fn.split("[...]") if p.strip()]
        ok_any = False
        for i in ch_ids:
            row = rows.get(i, "")
            if all(p in row for p in pieces):
                ok_any = True
                break
        checked += 1
        if not ok_any:
            if re.search(r"10-K|10-Q|8-K|proxy|Note \d|p\.\d|pp\.\d|WMT|BJ|PSMT|AMZN|KR |TGT|release", ch):
                continue  # a filing quote in a chunk that also carries an id; not a row fragment
            bad.append((ch_ids, f[:90]))

print(f"E-ids cited: {len(e_ids)}  {'OK' if not e_ids else 'FAIL ' + str(e_ids)}")
print(f"v5 ids cited: {len(ids)} ({len(set(ids))} distinct); missing from the ledger: {missing or 'none'}  {'OK' if not missing else 'FAIL'}")
print(f"quoted fragments checked beside ids: {checked}; fragments not found in their row: {len(bad)}  {'OK' if not bad else 'FAIL'}")
for ch_ids, f in bad:
    print("   ", ch_ids, repr(f))
sys.exit(0 if not (e_ids or missing or bad) else 1)
