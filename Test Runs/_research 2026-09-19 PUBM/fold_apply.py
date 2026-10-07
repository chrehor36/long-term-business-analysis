# Apply the PUBM fold: register entry, wave 5 strike and dated note, narrative fold, survival-shape instances.
import io, os
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: io.open(p, encoding="utf-8").read()
def wr(p, t): io.open(p, "w", encoding="utf-8", newline="").write(t)

q = os.path.join(ROOT, "Screens", "WATCHLIST RUN QUEUE.md")
t = rd(q)
nl = "\r\n" if "\r\n" in t else "\n"
reg = rd(os.path.join(H, "_register.md")).rstrip("\n").replace("\n", nl)
note = rd(os.path.join(H, "_wave5note.md")).strip("\n").replace("\n", nl)
# 1. register entry at the top of COMPLETED
head = nl + "## COMPLETED FROM THE QUEUE" + nl
assert t.count(head) == 1, t.count(head)
t = t.replace(head, head + reg + nl, 1)
# 2. strike PUBM in the wave 5 row
row = "| no share count from dei: read the cover | ~~META~~, ~~DASH~~, ~~PATH~~, PUBM, BZFD |"
assert t.count(row) == 1
t = t.replace(row, "| no share count from dei: read the cover | ~~META~~, ~~DASH~~, ~~PATH~~, ~~PUBM~~, BZFD |")
# 3. dated note after the PATH note
k = t.index("*Dated note, 2026-09-19 (the PATH run)")
e = t.index(nl, k)
t = t[:e] + nl + nl + note + t[e:]
wr(q, t)
print("queue ok")

rl = os.path.join(ROOT, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
t = rd(rl); nl2 = "\r\n" if "\r\n" in t else "\n"
fold = rd(os.path.join(H, "_fold.md")).replace("\n", nl2)
t = t.rstrip("\r\n") + nl2 + fold
wr(rl, t)
print("reading list ok")

sp = os.path.join(ROOT, "Screens", "SURVIVAL SHAPES - index.md")
t = rd(sp)
a = "operating income 0.71% of GOV) |"
assert t.count(a) == 1
t = t.replace(a, "operating income 0.71% of GOV), PUBM (2026-09-19, the mechanism: revenue per impression -66% FY2021-25 against cost per impression -52%, the savings *\"shared with our customers\"*; #2 as a feature) |")
b = "$1.09bn of buybacks retired the issuance) |"
assert t.count(b) == 1
t = t.replace(b, "$1.09bn of buybacks retired the issuance), PUBM (2026-09-19, a feature: stock pay 47-51% of operating cash FY2024-25, grant value above the charge FY2021-24; #11 the mechanism) |")
wr(sp, t)
print("shapes ok")
