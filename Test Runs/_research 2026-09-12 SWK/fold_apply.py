"""Apply the SWK fold to the queue and the reading list WITHOUT sweeping a concurrent run's
uncommitted edits into this commit.

For each file: take the HEAD blob, apply only the SWK edits to it, and stage that exact content
with `git update-index` from a blob written by `git hash-object -w`. Then apply the same edits to
the working-tree copy (which also carries the other run's uncommitted edits), so that when that run
stages its file, the diff it commits contains only its own hunks.
"""
import subprocess, sys

ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
RES = ROOT + r"\Test Runs\_research 2026-09-12 SWK"
Q = "Screens/WATCHLIST RUN QUEUE.md"
R = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"

entry = open(RES + r"\fold_entry.md", encoding="utf-8").read()
narr = open(RES + r"\fold_narrative.md", encoding="utf-8").read()

ROSTER_OLD = "SWK, ~~ARM~~, ~~CALX~~,"
ROSTER_NEW = "~~SWK~~, ~~ARM~~, ~~CALX~~,"
LIVE_OLD = "SWK is the one still live."
LIVE_NEW = ("SWK is the one still live. *(SWK RUN 2026-09-12: struck - closed at Q2 on the business; all "
            "four unlabelled names have now failed Q2, and none of them on the arithmetic the tier "
            "describes.)*")
HEAD_MARK = "## COMPLETED FROM THE QUEUE\n"


def git(*a, inp=None):
    return subprocess.run(["git", *a], cwd=ROOT, input=inp, capture_output=True, check=True)


def edit_queue(s):
    assert s.count(ROSTER_OLD) == 1, "roster anchor"
    s = s.replace(ROSTER_OLD, ROSTER_NEW)
    assert s.count(LIVE_OLD) == 1, "live anchor"
    s = s.replace(LIVE_OLD, LIVE_NEW)
    assert s.count(HEAD_MARK) == 1, "completed anchor"
    s = s.replace(HEAD_MARK, HEAD_MARK + entry)
    return s


def edit_reading(s):
    if not s.endswith("\n"):
        s += "\n"
    return s + narr


for path, fn in ((Q, edit_queue), (R, edit_reading)):
    head = git("show", f"HEAD:{path}").stdout.decode("utf-8")
    staged = fn(head)
    blob = git("hash-object", "-w", "--stdin", inp=staged.encode("utf-8")).stdout.decode().strip()
    mode = git("ls-files", "-s", "--", path).stdout.decode().split()[0]
    git("update-index", "--cacheinfo", f"{mode},{blob},{path}")
    wt_path = ROOT + "\\" + path.replace("/", "\\")
    wt = open(wt_path, encoding="utf-8", newline="").read()
    crlf = "\r\n" in wt
    wt_n = wt.replace("\r\n", "\n")
    wt_new = fn(wt_n)
    if crlf:
        wt_new = wt_new.replace("\n", "\r\n")
    open(wt_path, "w", encoding="utf-8", newline="").write(wt_new)
    print("staged and applied:", path)
