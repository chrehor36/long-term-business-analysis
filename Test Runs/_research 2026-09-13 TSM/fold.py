"""TSM fold: one read-modify-write of the queue file and the reading list, then verification.
Run immediately before the fold commit (a concurrent run shares these files)."""
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
names_before = [l[:40] for l in before]
if any(l.startswith("- **TSM (") for l in lines[idx:]):
    sys.exit("TSM entry already present; nothing written")
# 1. register entry at the top of the list, directly under the LAST heading
lines = lines[:idx + 1] + ENTRY.rstrip("\n").split("\n") + lines[idx + 1:]
# 2. strike TM in the WAVE 5 table row
row = [i for i, l in enumerate(lines) if l.startswith("| foreign 20-F filers, short XBRL history |")]
assert len(row) == 1, row
assert " TSM, " in lines[row[0]], lines[row[0]]
lines[row[0]] = lines[row[0]].replace(" TSM, ", " ~~TSM~~, ", 1)
q2 = "\n".join(lines)
after, _ = count(q2.split("\n"))
assert len(after) == len(before) + 1, (len(before), len(after))
missing = [n for n in names_before if n not in [l[:40] for l in after]]
assert not missing, missing
# 3. reading list narrative, appended at the end
r = open(R, encoding="utf-8").read()
assert "## UPDATE 2026-09-13 - TSM:" not in r
r2 = r.rstrip("\n") + "\n\n" + NARR.strip("\n") + "\n"
open(Q, "w", encoding="utf-8").write(q2)
open(R, "w", encoding="utf-8").write(r2)
print("register", len(before), "->", len(after), "| strike:", lines[row[0]][:80])
