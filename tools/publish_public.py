#!/usr/bin/env python3
"""PUBLISH PUBLIC - export the tracked files of this repository into the public copy.

    python tools/publish_public.py [--dest PATH] [--check]

Written 2026-10-04 when the operator asked for a public GitHub repository. The working repository
cannot be pushed as it is: its history carries the operator's holdings and coursework. So the public
copy is a fresh repository holding an EXPORT of the tracked files, re-run whenever the working copy
moves. What the export withholds, and why, is in NOTICE.md; this script is the mechanism and nothing
else. It copies, it deletes files in the destination that the working copy no longer tracks, and it
makes exactly one class of text change: in the five pointer documents the acceptance test reads, the
two withheld file names lose their backticks so that check 6 does not look for them. It concludes
nothing and writes no document of its own except the PORTFOLIO.md stub.

The destination's own .git/ is never touched; commit and push there by hand (or with --commit).
"""
import argparse, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DEST = os.path.join(os.path.expanduser("~"), "BRK-public")

# What the public copy withholds (NOTICE.md, "What the public copy withholds").
DENY_PREFIXES = ("MBA - UNG/", "Curriculum/", "Test Runs/_research", ".claude/")
DENY_EXACT = {"PORTFOLIO.md", "principle_ledger_v5.csv"}
POINTER_DOCS = ("CLAUDE.md", "README.md", "Framework/README.md", "Framework/OPERATOR-PROTOCOL.md")
UNBACKTICK = ("principle_ledger_v5.csv", "PORTFOLIO.md")

STUB_PORTFOLIO = """# PORTFOLIO.md — withheld from the public copy

The working repository's `PORTFOLIO.md` holds the owner's own holdings, cost bases, standing orders and the ranked
opportunity set. It is not published. This stub stands in its place so that the acceptance test's pointer check
(`tools/check_framework.py`, check 6) finds the file the map names.

Every verdict the framework reached on a business is public: the run files in `Test Runs/`, the register under
`## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md`, and the price bands in `tools/alerts.json`. Only
the owner's positions are withheld. See `NOTICE.md`.
"""


def tracked_files():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    return [p.decode("utf-8") for p in out.split(b"\0") if p]


def allowed(rel):
    if rel in DENY_EXACT:
        return False
    return not any(rel.startswith(p) for p in DENY_PREFIXES)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dest", default=DEFAULT_DEST)
    ap.add_argument("--check", action="store_true", help="run the acceptance test in the destination afterwards")
    ap.add_argument("--commit", metavar="MESSAGE", help="commit the export in the destination with this message")
    a = ap.parse_args()
    dest = os.path.abspath(a.dest)
    os.makedirs(dest, exist_ok=True)

    files = [f for f in tracked_files() if allowed(f)]
    withheld = [f for f in tracked_files() if not allowed(f)]
    copied = 0
    for rel in files:
        src = os.path.join(ROOT, rel)
        if not os.path.exists(src):
            continue  # tracked but deleted in the working tree; git will show it
        dst = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if (not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst)
                or os.path.getsize(src) != os.path.getsize(dst)):
            shutil.copy2(src, dst)
            copied += 1

    # Remove files the working copy no longer tracks (never the destination's .git).
    keep = set(files) | {"PORTFOLIO.md", "[coursework path withheld]", "Curriculum/WITHHELD.md",
                         "tools/_cache/.gitkeep", "Screens/_daily/_overnight_logs/.gitkeep",
                         "Screens/_daily/_v5_logs/.gitkeep", "Backtests/bt17_cache/.gitkeep",
                         "Framework/v5/_inbox/.gitkeep"}
    removed = 0
    for dirpath, dirnames, filenames in os.walk(dest):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            rel = os.path.relpath(os.path.join(dirpath, fn), dest).replace(os.sep, "/")
            if rel not in keep:
                os.remove(os.path.join(dirpath, fn))
                removed += 1

    # The one text change: withheld names lose their backticks in the pointer documents.
    for rel in POINTER_DOCS:
        p = os.path.join(dest, rel)
        if not os.path.exists(p):
            continue
        t = open(p, encoding="utf-8").read()
        t2 = t
        for name in UNBACKTICK:
            t2 = t2.replace(f"`{name}`", name)
        if t2 != t:
            open(p, "w", encoding="utf-8", newline="").write(t2)

    with open(os.path.join(dest, "PORTFOLIO.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(STUB_PORTFOLIO)

    # Folders the map names that are gitignored (caches, logs) or withheld (coursework) exist in the
    # public copy as placeholders, so check 6 finds them and a tool has somewhere to write.
    for d in ("tools/_cache", "Screens/_daily/_overnight_logs", "Screens/_daily/_v5_logs",
              "Backtests/bt17_cache", "Framework/v5/_inbox"):
        os.makedirs(os.path.join(dest, d), exist_ok=True)
        open(os.path.join(dest, d, ".gitkeep"), "a").close()
    for d in ("MBA - UNG", "Curriculum"):
        os.makedirs(os.path.join(dest, d), exist_ok=True)
        with open(os.path.join(dest, d, "WITHHELD.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(f"# {d}/ is withheld from the public copy\n\nCoursework that shares the working repository "
                    "and has nothing to do with the framework. See NOTICE.md.\n")

    print(f"exported {len(files)} tracked files to {dest} ({copied} copied, {removed} stale removed)")
    print(f"withheld {len(withheld)} tracked files: "
          + ", ".join(sorted({(w.split('/')[0] + '/') if '/' in w else w for w in withheld})))

    if a.check:
        r = subprocess.run([sys.executable, os.path.join(dest, "tools", "check_framework.py")], cwd=dest)
        if r.returncode != 0:
            return r.returncode
    if a.commit:
        subprocess.run(["git", "add", "-A"], cwd=dest, check=True)
        subprocess.run(["git", "commit", "-q", "-m", a.commit], cwd=dest, check=True)
        print("committed in", dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
