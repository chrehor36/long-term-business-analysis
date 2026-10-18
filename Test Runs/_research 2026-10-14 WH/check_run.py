"""Citation check for the WH run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment in the text segment just before an id (back to the previous id or the start of the line)
appears in that row (apostrophes and quote marks normalised, whitespace collapsed; [...] splits a fragment)."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
RUN = ROOT + r"\Test Runs\2026-10-14 Run - WH Wyndham Hotels & Resorts.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8-sig"))}
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '-').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(RUN, encoding="utf-8").read()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', text)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
missing = sorted(set(i for i in ids if i not in rows))
if missing: print("MISSING ids:", missing); bad += 1
print("distinct ids:", len(set(ids)), "citations:", len(ids))
skip = set(sys.argv[1:])
for line_no, line in enumerate(text.splitlines(), 1):
    pos = 0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', line):
        seg = line[pos:m.start()]
        pos = m.end()
        rid = m.group(1)
        if rid not in rows: continue
        row = norm(rows[rid])
        for q in re.findall(r'"([^"]+)"', seg):
            for frag in re.split(r'\[\.\.\.\]', q):
                f = norm(frag).strip(' .,;:')
                if len(f) < 4: continue
                if f not in row:
                    key = f"{line_no}:{rid}"
                    if key in skip: continue
                    print(f"line {line_no} {rid}: NOT IN ROW: {frag[:120]!r}"); bad += 1
print("RESULT:", "CLEAN" if bad == 0 else f"{bad} problem(s)")
