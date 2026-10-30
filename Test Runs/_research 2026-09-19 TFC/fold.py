"""TFC fold - ONE read-modify-write per shared file, immediately before the commit.

CONCURRENT RUNS SHARE THIS TREE. Every edit below is: read the whole file, count what is there
with a LINE-START anchored regex, splice, count again, assert exactly one thing was added, write
once. No count is trusted from the brief.
"""
import io, os, re, sys

ROOT = "C:/Users/chreh/OneDrive/Documents/BRK"
QUEUE = os.path.join(ROOT, "Screens/WATCHLIST RUN QUEUE.md")
READING = os.path.join(ROOT, "Screens/2026-08-31 PREPPED READING LIST (operator lists).md")
SHAPES = os.path.join(ROOT, "Screens/SURVIVAL SHAPES - index.md")
LOG = os.path.join(ROOT, "Screens/_daily/OVERNIGHT LOG.md")
SEC = os.path.dirname(os.path.abspath(__file__))


def rd(p):
    return io.open(p, encoding="utf-8", newline="").read()


def wr(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def piece(name):
    return rd(os.path.join(SEC, name))


def register_slice(t):
    """The COMPLETED FROM THE QUEUE slice, anchored on a LINE-START regex.

    The heading text also occurs inline many times in this file (the ACNB and SOFI folds both
    recorded it), so the anchor must be ^## at a line start and the slice must end at the next
    ^## that is not the same heading.
    """
    m = re.search(r"(?m)^## COMPLETED FROM THE QUEUE[ \t]*$", t)
    assert m, "register heading not found with a line-start anchor"
    nxt = re.search(r"(?m)^## (?!COMPLETED FROM THE QUEUE)", t[m.end():])
    end = m.end() + (nxt.start() if nxt else len(t) - m.end())
    return m, end, t[m.end():end]


def count_entries(sl):
    return len(re.findall(r"(?m)^- \*\*", sl))


# ---------------------------------------------------------------- 1 + 2. THE QUEUE
t = rd(QUEUE)
m, end, sl = register_slice(t)
before = count_entries(sl)
print("register entries BEFORE:", before)
assert "TFC (Truist Financial Corporation)" not in t, "TFC entry already present - refusing"

entry = piece("fold_queue_entry.md").rstrip("\n") + "\n"
# insert as the newest entry, immediately after the heading line
t2 = t[:m.end()] + "\n" + entry + t[m.end():]

m2, end2, sl2 = register_slice(t2)
after = count_entries(sl2)
print("register entries AFTER :", after)
assert after == before + 1, "expected exactly one entry added, got %d -> %d" % (before, after)

# strike TFC in the WAVE 6 table row
row_old = "| TFC | Truist Financial Corporation | bank | **RUN** - see the operator ruling below |"
assert t2.count(row_old) == 1, "WAVE 6 TFC row not found exactly once"
row_new = ("| ~~TFC~~ | Truist Financial Corporation | bank | **RUN 2026-09-19 - struck. "
           "FAIL at Q2, OUT on the business:** on the FDIC Call Report's own uniform definitions "
           "Truist Bank has the **WORST five-year mean pre-tax return on assets (0.991% against "
           "Regions' 1.875%) and the WORST five-year mean return on equity (7.03% against 13.86%) "
           "of the nine largest US regional banks**, out of mid-pack funding costs (4th of 9), a "
           "mid-pack margin (5th of 9) and mid-pack leverage; number-one deposit share in ONE of "
           "fourteen states; free deposits -28% and branches -31% in five years. Q3 recorded OUT "
           "at gate weight on **[E3-29]**; Q4 recorded IN on survival. **TWELVE perimeter events, "
           "ONE clean year. The CEO changed on 2026-09-01, eighteen days before the run.** Price "
           "US$48.56, cap US$59,322.2M. Register entry 132. See COMPLETED. |")
t3 = t2.replace(row_old, row_new)

# strike TFC in the operator-ruling sentence
rul_old = "**So ~~CCB~~, ~~ACNB~~, ~~SOFI~~, ~~JPM~~ and TFC are run**"
assert t3.count(rul_old) == 1, "operator-ruling sentence not found exactly once"
t4 = t3.replace(rul_old, "**So ~~CCB~~, ~~ACNB~~, ~~SOFI~~, ~~JPM~~ and ~~TFC~~ are run**")

# dated note beside the ruling (operator rule 6), placed after the OTTR/SOFI notes block, i.e.
# immediately before the HOW A BANK IS RUN heading
anchor = "**HOW A BANK IS RUN, FROM THE CORPUS - read before briefing one:**"
assert t4.count(anchor) == 1, "HOW A BANK IS RUN anchor not found exactly once"
note = piece("fold_queue_note.md").rstrip("\n") + "\n\n"
t5 = t4.replace(anchor, note + anchor)

wr(QUEUE, t5)
print("queue written; TFC struck in 2 places, 1 dated note added")

# ---------------------------------------------------------------- 3. NARRATIVE FOLD
r = rd(READING)
head = "## UPDATE 2026-09-19 - TFC:"
assert head not in r, "TFC narrative fold already present - refusing"
nar = piece("fold_narrative.md")
if not r.endswith("\n"):
    r += "\n"
wr(READING, r + "\n" + nar)
print("narrative fold appended,", len(nar), "chars")

# ---------------------------------------------------------------- 4. SURVIVAL SHAPES
s = rd(SHAPES)
rows_before = len(re.findall(r"(?m)^\| \d+ \|", s))
assert "The bought ratio" not in s, "shape already present - refusing"
nums = sorted(set(int(x) for x in re.findall(r"(?m)^\| (\d+) \|", s)))
print("shape rows BEFORE:", rows_before, "| numbers used:", nums[-4:])
newnum = max(nums) + 1
shape_row = piece("fold_shape_row.md").rstrip("\n").replace("{{N}}", str(newnum))
# insert after the last numbered row
last = None
for mm in re.finditer(r"(?m)^\| \d+ \|[^\n]*\n", s):
    last = mm
assert last, "no numbered rows found"
s2 = s[:last.end()] + shape_row + "\n" + s[last.end():]
rows_after = len(re.findall(r"(?m)^\| \d+ \|", s2))
print("shape rows AFTER :", rows_after, "| new number:", newnum)
assert rows_after == rows_before + 1, "expected exactly one shape row added"

open_old = "**Open:** SPOT asked"
assert s2.count(open_old) == 1
s3 = s2.replace(open_old, piece("fold_shape_open.md").rstrip("\n").replace("{{N}}", str(newnum)) + " " + open_old)
wr(SHAPES, s3)
print("shapes index written")

# ---------------------------------------------------------------- 5. OVERNIGHT LOG
lg = rd(LOG)
assert "| TFC |" not in lg, "TFC log line already present - refusing"
line = piece("fold_log_line.md").rstrip("\n")
if not lg.endswith("\n"):
    lg += "\n"
wr(LOG, lg + line + "\n")
print("log line appended")
print("\nFOLD STEPS 1,2,3,4 and the log DONE. Step 4 of THE FOLD (alerts + PORTFOLIO row) is "
      "DELIBERATELY NOT DONE: TFC failed at Q2 on the BUSINESS, so the QLYS ruling of 2026-09-07 "
      "bars a price band and a PORTFOLIO row. Step 5 (check_framework) and step 6 (pathspec "
      "commit) are run from the shell.")
