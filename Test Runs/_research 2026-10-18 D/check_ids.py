"""Checks the D run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment directly before an id (or a run of ids) is in one of those rows."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
run = open(ROOT + r"\Test Runs\2026-10-18 Run - D Dominion Energy.md", encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open(ROOT + r"\principle_ledger_v5.csv", encoding="utf-8"))}
def norm(s):
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\ufffd", "")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()
problems = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
if eids: print("E-ids found:", eids); problems += len(eids)
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); problems += 1
# quoted fragment(s) immediately followed by one or more ids
pat = re.compile(r'(?:"([^"\n]{3,}?)"|\u201c([^\u201d\n]{3,}?)\u201d)\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:\s*,\s*|\s+)?)+)')
checked = 0
for m in pat.finditer(run):
    frag = m.group(1) or m.group(2)
    idl = re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group(3))
    pieces = [p for p in re.split(r"\[\.\.\.\]", frag) if len(norm(p)) > 2]
    for p in pieces:
        q = norm(p).strip(" .,;:")
        checked += 1
        if not any(q in norm(rows.get(i, "")) for i in idl):
            print("NOT IN ROW", idl, "::", p[:120]); problems += 1
print(f"ids cited: {len(set(ids))} distinct; fragments checked: {checked}; problems: {problems}")
