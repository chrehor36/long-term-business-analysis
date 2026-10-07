"""TTSH fold, step 1: write the working-tree changes and the staged-blob texts.
Queue: register entry inserted by line-exact match of the heading, asserted unique, into BOTH the HEAD blob
(saved as q_staged.md, LF) and the working tree (line endings kept, the other session's CRM hunks kept).
The entry's placeholders are filled from the HEAD blob's own count, never inherited.
"""
import subprocess
R = r"C:\Users\chreh\OneDrive\Documents\BRK"
D = R + r"\Test Runs\_research 2026-09-25 TTSH"
Q = "Screens/WATCHLIST RUN QUEUE.md"
RL = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
DONE = "Screens/_daily/_wave7_done.txt"
HEAD_H = "## COMPLETED FROM THE QUEUE"
T = "TTSH"


def head(path):
    return subprocess.run(["git", "show", "HEAD:" + path], cwd=R, capture_output=True, check=True).stdout.decode("utf-8")


def locate(L):
    h = [i for i, l in enumerate(L) if l == HEAD_H]
    assert len(h) == 1, h
    w = [i for i, l in enumerate(L) if l.startswith("## THE WRITE-EARLY PROTOCOL")]
    assert len(w) == 1, w
    return h[0], w[0]


HB = head(Q).split("\n")
hi, wi = locate(HB)
before = sum(1 for l in HB[hi + 1:wi] if l.startswith("- **"))
assert not any(l.startswith("- **" + T + " ") for l in HB[hi + 1:wi]), "duplicate"
raw_entry = open(D + r"\register_entry.md", encoding="utf-8").read().rstrip("\n")
entry = (raw_entry.replace("__HI__", str(hi)).replace("__WI__", str(wi))
         .replace("__B__", str(before)).replace("__A__", str(before + 1))).split("\n")
assert not any("__" in l for l in entry), "unfilled placeholder"
assert before + 1 == 171, before


def insert(text):
    L = text.split("\n")
    h, w = locate(L)
    b = sum(1 for l in L[h + 1:w] if l.startswith("- **"))
    assert not any(l.startswith("- **" + T + " ") for l in L[h + 1:w]), "duplicate"
    L2 = L[:h + 1] + entry + L[h + 1:]
    h2, w2 = locate(L2)
    sl = [l for l in L2[h2 + 1:w2] if l.startswith("- **")]
    assert sl[0].startswith("- **" + T + " "), sl[0][:40]
    assert sl[1].startswith("- **DMC "), sl[1][:40]
    assert sum(1 for l in sl if l.startswith("- **" + T + " ")) == 1
    return "\n".join(L2), b, len(sl), h, w


staged, b, a, h0, w0 = insert("\n".join(HB))
print("QUEUE HEAD blob: heading", h0, "write-early", w0, "entries", b, "->", a)
open(D + r"\q_staged.md", "w", encoding="utf-8", newline="").write(staged)
wt_path = R + "\\" + Q.replace("/", "\\")
raw = open(wt_path, "rb").read()
crlf = b"\r\n" in raw
wt = raw.decode("utf-8").replace("\r\n", "\n")
wt2, b2, a2, h2, w2 = insert(wt)
print("QUEUE working tree: heading", h2, "write-early", w2, "entries", b2, "->", a2, "crlf", crlf)
open(wt_path, "wb").write((wt2.replace("\n", "\r\n") if crlf else wt2).encode("utf-8"))

# done file
dh = head(DONE)
assert dh.endswith("\n") and T not in dh.split("\n") and dh.strip("\n").split("\n")[-1] == "DMC"
open(D + r"\done_staged.txt", "w", encoding="utf-8", newline="").write(dh + T + "\n")
dp = R + "\\" + DONE.replace("/", "\\")
draw = open(dp, "rb").read()
assert draw.replace(b"\r\n", b"\n").decode("utf-8") == dh, "done file differs from HEAD"
dcrlf = b"\r\n" in draw
open(dp, "wb").write(draw + ((T + "\r\n") if dcrlf else (T + "\n")).encode())
print("DONE lines now", len((dh + T + "\n").strip("\n").split("\n")))

# reading list
rh = head(RL)
fold = open(D + r"\reading_fold.md", encoding="utf-8").read()
assert rh.endswith("\n")
open(D + r"\rl_staged.md", "w", encoding="utf-8", newline="").write(rh + fold)
rp = R + "\\" + RL.replace("/", "\\")
rraw = open(rp, "rb").read()
assert rraw.replace(b"\r\n", b"\n").decode("utf-8") == rh, "reading list differs from HEAD"
rcrlf = b"\r\n" in rraw
open(rp, "wb").write(rraw + (fold.replace("\n", "\r\n") if rcrlf else fold).encode("utf-8"))
print("reading list appended, crlf", rcrlf)
