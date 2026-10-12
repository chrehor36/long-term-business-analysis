# Citation check for the EQPT run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment that closes within 70 characters before an id (with no other id between) is in that row
# (apostrophes, replacement characters and dash forms normalised; [...] splits a fragment into parts that must
# each appear, in order).
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
BRK = r"C:\Users\chreh\OneDrive\Documents\BRK"
rows = {r["\ufeffid"]: r["quote_verbatim"] for r in csv.DictReader(open(BRK + r"\principle_ledger_v5.csv", encoding="utf-8"))}
run = open(BRK + r"\Test Runs\2026-10-12 Run - EQPT EquipmentShare.md", encoding="utf-8").read()


def norm(s):
    for a in "\u2019\u2018'\ufffd`\u00b4":
        s = s.replace(a, "'")
    for a in "\u201c\u201d":
        s = s.replace(a, '"')
    for a in "\u2014\u2013":
        s = s.replace(a, "-")
    return re.sub(r"\s+", " ", s).strip().lower()


probs = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
if eids:
    print("E-ids found:", eids)
    probs += len(eids)
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", run))
for i in sorted(ids):
    if i not in rows:
        print("MISSING id", i)
        probs += 1
n = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run):
    i = m.group(1)
    if i not in rows:
        continue
    before = run[max(0, m.start() - 900):m.start()]
    close = before.rfind('"')
    if close < 0 or len(before) - close > 70:
        continue
    seg = before[close + 1:]
    if "**[" in seg:
        continue
    opn = before.rfind('"', 0, close)
    if opn < 0:
        continue
    frag = before[opn + 1:close]
    if "\n\n" in frag or len(frag) < 4:
        continue
    n += 1
    row = norm(rows[i])
    pos = 0
    ok = True
    for p in re.split(r"\[\.\.\.\]", frag):
        q = norm(p).strip(" .,;:")
        if not q:
            continue
        k = row.find(q, pos)
        if k < 0:
            ok = False
            break
        pos = k + len(q)
    if not ok:
        print(f'FRAGMENT NOT IN ROW {i}: "{frag}"')
        probs += 1
print(f"ids: {len(ids)}, fragments checked: {n}, problems: {probs}")
