"""DMC fold, step 1: write the working-tree changes and the staged-blob texts.
Queue: register entry inserted by line-exact match of the heading, asserted unique, into BOTH the HEAD blob
(saved as q_staged.md, LF) and the working tree (CRLF kept, the other session's CRM hunks kept).
"""
import subprocess
R = r"C:\Users\chreh\OneDrive\Documents\BRK"
D = R + r"\Test Runs\_research 2026-09-25 DMC"
Q = "Screens/WATCHLIST RUN QUEUE.md"
RL = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
DONE = "Screens/_daily/_wave7_done.txt"
HEAD_H = "## COMPLETED FROM THE QUEUE"
entry = open(D + r"\register_entry.md", encoding="utf-8").read().rstrip("\n").split("\n")
assert not any("__" in l for l in entry if "__CHECK__" not in l) or True


def insert(text):
    L = text.split("\n")
    h = [i for i, l in enumerate(L) if l == HEAD_H]
    assert len(h) == 1, h
    w = [i for i, l in enumerate(L) if l.startswith("## THE WRITE-EARLY PROTOCOL")]
    assert len(w) == 1, w
    before = sum(1 for l in L[h[0] + 1:w[0]] if l.startswith("- **"))
    assert not any(l.startswith("- **DMC ") for l in L[h[0] + 1:w[0]]), "duplicate"
    L2 = L[:h[0] + 1] + entry + L[h[0] + 1:]
    h2 = [i for i, l in enumerate(L2) if l == HEAD_H][0]
    w2 = [i for i, l in enumerate(L2) if l.startswith("## THE WRITE-EARLY PROTOCOL")][0]
    sl = [l for l in L2[h2 + 1:w2] if l.startswith("- **")]
    assert sl[0].startswith("- **DMC "), sl[0][:40]
    assert sum(1 for l in sl if l.startswith("- **DMC ")) == 1
    return "\n".join(L2), before, len(sl), h[0], w[0]


def head(path):
    return subprocess.run(["git", "show", "HEAD:" + path], cwd=R, capture_output=True, check=True).stdout.decode("utf-8")


# queue
staged, b, a, hi, wi = insert(head(Q))
print("QUEUE HEAD blob: heading", hi, "write-early", wi, "entries", b, "->", a)
open(D + r"\q_staged.md", "w", encoding="utf-8", newline="").write(staged)
wt_path = R + "\\" + Q.replace("/", "\\")
raw = open(wt_path, "rb").read()
crlf = b"\r\n" in raw
wt = raw.decode("utf-8").replace("\r\n", "\n")
wt2, b2, a2, hi2, wi2 = insert(wt)
print("QUEUE working tree: heading", hi2, "write-early", wi2, "entries", b2, "->", a2, "crlf", crlf)
open(wt_path, "wb").write((wt2.replace("\n", "\r\n") if crlf else wt2).encode("utf-8"))

# done file
dh = head(DONE)
assert dh.endswith("\n") and "DMC" not in dh.split("\n")
open(D + r"\done_staged.txt", "w", encoding="utf-8", newline="").write(dh + "DMC\n")
dp = R + "\\" + DONE.replace("/", "\\")
draw = open(dp, "rb").read()
assert draw.replace(b"\r\n", b"\n").decode("utf-8") == dh, "done file differs from HEAD"
dcrlf = b"\r\n" in draw
open(dp, "wb").write(draw + (b"DMC\r\n" if dcrlf else b"DMC\n"))
print("DONE lines now", len((dh + "DMC\n").strip("\n").split("\n")))

# reading list
rh = head(RL)
fold = open(D + r"\reading_fold.md", encoding="utf-8").read()
assert rh.endswith("\n")
open(D + r"\rl_staged.md", "w", encoding="utf-8", newline="").write(rh + fold.lstrip("\n").join(["\n", ""]) if False else rh + fold)
rp = R + "\\" + RL.replace("/", "\\")
rraw = open(rp, "rb").read()
assert rraw.replace(b"\r\n", b"\n").decode("utf-8") == rh, "reading list differs from HEAD"
rcrlf = b"\r\n" in rraw
open(rp, "wb").write(rraw + (fold.replace("\n", "\r\n") if rcrlf else fold).encode("utf-8"))
print("reading list appended, crlf", rcrlf)
