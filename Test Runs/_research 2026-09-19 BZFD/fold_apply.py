# Apply the BZFD fold: register entry, wave 5 strike and dated note, narrative fold, survival-shape instances.
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
# 2. strike BZFD in the wave 5 row
row = "| no share count from dei: read the cover | ~~META~~, ~~DASH~~, ~~PATH~~, ~~PUBM~~, BZFD |"
assert t.count(row) == 1
t = t.replace(row, "| no share count from dei: read the cover | ~~META~~, ~~DASH~~, ~~PATH~~, ~~PUBM~~, ~~BZFD~~ |")
# 3. dated note after the PUBM note
k = t.index("*Dated note, 2026-09-19 (the PUBM run)")
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
a = "| customers pay a small part of the costs and new shareholders pay the rest | |"
assert t.count(a) == 1
t = t.replace(a, "| customers pay a small part of the costs and new shareholders pay the rest | BZFD (2026-09-19, a feature: the 2026 losses funded by selling 45.7M shares to a new controller, 40M of them paid mostly with a note secured by themselves; #19 the mechanism) |")
b = "holds the buyer's data, and reprices the terms every year | |"
assert t.count(b) == 1
t = t.replace(b, "holds the buyer's data, and reprices the terms every year | BZFD (2026-09-19, the mechanism: owned brands, route to the reader rented from search engines that answer on their own page, platforms that keep the traffic, and Amazon setting the commission on 28% of revenue; advertising revenue per measured hour -37% FY2022-25; #8 as a feature) |")
wr(sp, t)
print("shapes ok")
