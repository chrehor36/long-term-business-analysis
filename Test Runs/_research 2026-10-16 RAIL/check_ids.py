"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
beside an id (the nearest quotation in the same sentence before the id, or in brackets right after it) is in that row.
Matching ignores [...] elisions (each piece must appear, in order) and normalizes whitespace."""
import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", run)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
def in_row(frag, row):
    pos = 0; r = norm(row)
    for piece in [norm(p) for p in frag.split("[...]") if norm(p)]:
        k = r.find(piece, pos)
        if k < 0: return False
        pos = k + len(piece)
    return True
checked = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run):
    i = m.group(1)
    if i not in rows: continue
    # the sentence up to the id: back to the previous id, line start of a list item, or sentence end
    start = max(run.rfind("**[", 0, m.start() - 1), run.rfind(". ", 0, m.start()), run.rfind("\n-", 0, m.start()),
                run.rfind("\n|", 0, m.start()))
    before = run[start:m.start()]
    after = run[m.end():m.end() + 400]
    frags = re.findall(r"[\"“]([^\"”]{6,}?)[\"”]", before)
    am = re.match(r"\s*\(\s*\"([^\"]{6,}?)\"", after)
    cands = ([frags[-1]] if frags else []) + ([am.group(1)] if am else [])
    for f in cands:
        checked += 1
        if not in_row(f, rows[i]):
            print(f"NOT IN ROW {i}: {f[:120]!r}"); bad += 1
print(f"ids {len(set(ids))} distinct, {len(ids)} uses; fragments checked {checked}; problems {bad}")
print("PASS" if bad == 0 else "FAIL")
