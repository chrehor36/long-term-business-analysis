"""MBGL fold: one read-modify-write of the queue and the reading list, verified by count."""
import re, sys
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
Q = ROOT + r"\Screens\WATCHLIST RUN QUEUE.md"
RL = ROOT + r"\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
HERE = ROOT + r"\Test Runs\_research 2026-09-13 MBGL\fold"
ENTRY_RE = re.compile(r"^- \*\*[A-Z][A-Z.\-]* \(", re.M)

def register_slice(text):
    # the LAST line that starts with the heading (the phrase also appears inside notes above it)
    starts = [m.start() for m in re.finditer(r"^## COMPLETED FROM THE QUEUE[ \t]*$", text, re.M)]
    if not starts:
        sys.exit("register heading not found")
    a = starts[-1]
    nxt = re.search(r"^## ", text[a + 5:], re.M)
    b = a + 5 + nxt.start() if nxt else len(text)
    return a, b

q = open(Q, encoding="utf-8").read()
a, b = register_slice(q)
before_entries = ENTRY_RE.findall(q[a:b])
n_before = len(before_entries)
tickers_before = re.findall(r"^- \*\*([A-Z][A-Z.\-]*) \(", q[a:b], re.M)
if "MBGL" in tickers_before:
    sys.exit("MBGL already registered - aborting")

# 1. register entry, newest first, directly under the heading line
entry = open(HERE + r"\register_entry.md", encoding="utf-8").read()
heading_end = q.index("\n", a) + 1
q = q[:heading_end] + entry + q[heading_end:]

# 2. strike MBGL in the WAVE 5 table, and add the dated grouping note under the table
old_row = "~~STLA~~, ~~GFS~~, MBGL, IHG |"
if old_row not in q:
    # tolerate a concurrent strike of IHG
    m = re.search(r"\| foreign 20-F filers, short XBRL history \|[^\n]*\n", q)
    row = m.group(0)
    if " MBGL," not in row:
        sys.exit("WAVE 5 row: MBGL not found unstruck: " + row)
    new_row = row.replace(" MBGL,", " ~~MBGL~~,")
    q = q.replace(row, new_row)
else:
    q = q.replace(old_row, "~~STLA~~, ~~GFS~~, ~~MBGL~~, IHG |")
table_anchor = "| cap rejected as a broken input: read the cover | HBB, LCID, SOUN, BIRD |"
m = re.search(r"^\| cap rejected as a broken input: read the cover \|[^\n]*\n", q, re.M)
if not m:
    sys.exit("WAVE 5 table end not found")
note = open(HERE + r"\wave5_note.md", encoding="utf-8").read()
q = q[:m.end()] + note + q[m.end():]

# verify
a2, b2 = register_slice(q)
after = re.findall(r"^- \*\*([A-Z][A-Z.\-]*) \(", q[a2:b2], re.M)
n_after = len(after)
missing = [t for t in tickers_before if t not in after]
if n_after != n_before + 1 or missing or after[0] != "MBGL":
    sys.exit(f"COUNT CHECK FAILED before={n_before} after={n_after} missing={missing} first={after[:2]}")
open(Q, "w", encoding="utf-8").write(q)
print(f"queue: register {n_before} -> {n_after}; first entry {after[0]}; nothing vanished")

# 3. narrative fold
rl = open(RL, encoding="utf-8").read()
if "## UPDATE 2026-09-13 - MBGL" in rl:
    sys.exit("narrative already present")
narr = open(HERE + r"\narrative.md", encoding="utf-8").read().replace("__COUNT__", str(n_after))
if not rl.endswith("\n"):
    rl += "\n"
rl += narr
open(RL, "w", encoding="utf-8").write(rl)
print("reading list: narrative appended; count stated", n_after)
