"""STLA fold: one read-modify-write of the queue file and the reading list, then verification.
Run immediately before the fold commit (concurrent runs share these files)."""
import re, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
Q = os.path.join(ROOT, "Screens", "WATCHLIST RUN QUEUE.md")
R = os.path.join(ROOT, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY = open(os.path.join(HERE, "fold_entry.md"), encoding="utf-8").read().rstrip("\n") + "\n"
NARR = open(os.path.join(HERE, "fold_narrative.md"), encoding="utf-8").read()
PAT = re.compile(r"^- \*\*[A-Z][A-Z.\-]* \(")
def count(lines):
    idx = max(i for i, l in enumerate(lines) if l.startswith("## COMPLETED FROM THE QUEUE"))
    return [l for l in lines[idx:] if PAT.match(l)], idx
q = open(Q, encoding="utf-8").read()
lines = q.split("\n")
before, idx = count(lines)
names_before = [l[:60] for l in before]
if any(l.startswith("- **STLA (") for l in lines[idx:]):
    sys.exit("STLA entry already present; nothing written")
lines = lines[:idx + 1] + ENTRY.rstrip("\n").split("\n") + lines[idx + 1:]
row = [i for i, l in enumerate(lines) if l.startswith("| foreign 20-F filers, short XBRL history |")]
assert len(row) == 1, row
assert " STLA, " in lines[row[0]], lines[row[0]]
lines[row[0]] = lines[row[0]].replace(" STLA, ", " ~~STLA~~, ", 1)
q2 = "\n".join(lines)
after, _ = count(q2.split("\n"))
assert len(after) == len(before) + 1, (len(before), len(after))
missing = [n for n in names_before if n not in [l[:60] for l in after]]
assert not missing, missing
r = open(R, encoding="utf-8").read()
assert "## UPDATE 2026-09-13 - STLA:" not in r
r2 = r.rstrip("\n") + "\n\n" + NARR.strip("\n") + "\n"
open(Q, "w", encoding="utf-8").write(q2)
open(R, "w", encoding="utf-8").write(r2)
print("register", len(before), "->", len(after), "| strike:", lines[row[0]])
print("top entries:", [l[:22] for l in after[:3]])
