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
# 2026-10-06, the owner's decision on transparency: the research folders are published (their scripts, outputs and
# working notes), minus the filing dumps, so "Test Runs/_research" left this tuple; see research_allowed().
DENY_PREFIXES = ("MBA - UNG/", "Curriculum/", ".claude/")

# 2026-10-06: what a research folder keeps in the public copy. The raw filings and data pulls are 11 GB on disk and
# re-fetchable from EDGAR by the accession numbers every run records (operator rule 4); the tracked dumps committed
# before the ignore rules are 3.3 GB. Neither fits a GitHub repository. The scripts, outputs and notes (about 180 MB)
# are what a reader needs to reproduce a run's arithmetic, and they are published. Three tests, all three must pass:
# the folder belongs to a published run (a withheld kind's folder stays withheld with it); the file name is not a
# filing or XBRL dump by the same patterns .gitignore uses; the file is under RESEARCH_MAX_BYTES.
RESEARCH_DUMP = re.compile(r"(10-?K|10-?Q|DEF ?_?14A|8-?K|20-?F|\btenk|\btenq|ten-k|ten-q|_body\b|_fy20|_FY20|"
                           r"companyfacts|submissions|\bsubs\.json|_raw\.json|\.htm$|\.html$|\.pdf$|\.xlsx$)", re.I)
RESEARCH_MAX_BYTES = 200_000
RESEARCH_DIR = re.compile(r"^Test Runs/_research (\d{4}-\d{2}-\d{2}) ([A-Za-z0-9.\-]+)(?: |/)")
PUBLIC_RUNS = set()  # (date, ticker) of every published purchase run; filled in main()


def research_allowed(rel):
    if not rel.startswith("Test Runs/_research"):
        return True
    m = RESEARCH_DIR.match(rel)
    # A folder named by date and ticker belongs to that run and is published only if the run is; a folder named
    # otherwise (the batch folders of 2026-08-26 and earlier) belongs to no withheld kind and gets the file tests alone.
    if m and (m.group(1), m.group(2)) not in PUBLIC_RUNS:
        return False
    base = rel.rsplit("/", 1)[-1]
    if RESEARCH_DUMP.search(base) or "/cache/" in rel:
        return False
    try:
        return os.path.getsize(os.path.join(ROOT, rel)) < RESEARCH_MAX_BYTES
    except OSError:
        return False
# 2026-10-05: v5 adopted, so principle_ledger_v5.csv is published (the governing documents cite it).
DENY_EXACT = {"PORTFOLIO.md"}
POINTER_DOCS = ("CLAUDE.md", "README.md", "Framework/README.md", "Framework/OPERATOR-PROTOCOL.md")
UNBACKTICK = ("PORTFOLIO.md", "MBA - UNG/")  # MBA placeholder removed 2026-10-05 at the owner's request

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


# 2026-10-05, the owner's instruction: holding reviews, notes on holdings, hold reads and research passes carry the
# owner's positions (share counts, cost bases, accounts, keep or sell words), so they are withheld like PORTFOLIO.md.
# The templates stay public. Purchase runs stay public: they are written blind and carry no position.
DENY_RUN_KINDS = re.compile(r"^Test Runs/[^/_][^/]* (Holding Review|Note|HOLD READ|RESEARCH PASS) - ")


def allowed(rel):
    if rel in DENY_EXACT:
        return False
    if DENY_RUN_KINDS.match(rel):
        return False
    if not research_allowed(rel):
        return False
    return not any(rel.startswith(p) for p in DENY_PREFIXES)


RUN_FILE = re.compile(r"^Test Runs/(\d{4}-\d{2}-\d{2}) Run - ([A-Za-z0-9.\-]+) ")


def public_runs(tracked):
    """(date, ticker) of every tracked purchase run file; the research folders of these are published."""
    out = set()
    for f in tracked:
        m = RUN_FILE.match(f)
        if m and not DENY_RUN_KINDS.match(f):
            out.add((m.group(1), m.group(2)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dest", default=DEFAULT_DEST)
    ap.add_argument("--check", action="store_true", help="run the acceptance test in the destination afterwards")
    ap.add_argument("--commit", metavar="MESSAGE", help="commit the export in the destination with this message")
    a = ap.parse_args()
    dest = os.path.abspath(a.dest)
    os.makedirs(dest, exist_ok=True)

    # 2026-10-06, the operator's branches: the export writes master only. The public repository also carries
    # `experimental` and `ben-graham`, each worked in its own folder (git worktrees); an export pointed at one of
    # them, or at a destination switched off master, would overwrite that branch with master's files.
    if os.path.isdir(os.path.join(dest, ".git")) or os.path.isfile(os.path.join(dest, ".git")):
        br = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=dest,
                            capture_output=True, text=True).stdout.strip()
        if br != "master":
            sys.exit(f"refused: {dest} is on branch '{br}', not master. The export writes master only; "
                     f"branch work is done in its own folder, never through this script.")

    tracked = tracked_files()
    PUBLIC_RUNS.update(public_runs(tracked))
    files = [f for f in tracked if allowed(f)]
    withheld = [f for f in tracked if not allowed(f)]
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
    keep = set(files) | {"PORTFOLIO.md", "Curriculum/WITHHELD.md",
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

    # Coursework paths are redacted from every exported text file (owner's request, 2026-10-05): a
    # path inside the coursework folder names the course and its files, and the public copy names neither.
    mba_path = re.compile(r"MBA - UNG/[^`\n|]*?\.(?:md|txt|csv|pdf|docx|pptx|xlsx)")
    for dirpath, dirnames, filenames in os.walk(dest):
        if ".git" in dirpath.split(os.sep):
            continue
        for fn in filenames:
            if not fn.lower().endswith((".md", ".csv", ".txt", ".py", ".json", ".ps1")):
                continue
            fp = os.path.join(dirpath, fn)
            try:
                s = open(fp, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            s2 = mba_path.sub("[coursework path withheld]", s)
            if s2 != s:
                open(fp, "w", encoding="utf-8", newline="").write(s2)

    with open(os.path.join(dest, "PORTFOLIO.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(STUB_PORTFOLIO)

    # Folders the map names that are gitignored (caches, logs) or withheld (coursework) exist in the
    # public copy as placeholders, so check 6 finds them and a tool has somewhere to write.
    for d in ("tools/_cache", "Screens/_daily/_overnight_logs", "Screens/_daily/_v5_logs",
              "Backtests/bt17_cache", "Framework/v5/_inbox"):
        os.makedirs(os.path.join(dest, d), exist_ok=True)
        open(os.path.join(dest, d, ".gitkeep"), "a").close()
    # "MBA - UNG" got a WITHHELD.md placeholder here until 2026-10-05; the owner asked that nothing of it
    # appear in the public copy, so it is now absent, gitignored there, and its name is unbackticked above.
    shutil.rmtree(os.path.join(dest, "MBA - UNG"), ignore_errors=True)
    gi = os.path.join(dest, ".gitignore")
    if os.path.exists(gi):
        lines = [l for l in open(gi, encoding="utf-8").read().splitlines() if "MBA - UNG" not in l]
        with open(gi, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines).rstrip() + "\n\n# coursework, never published\nMBA - UNG/\n")
    for d in ("Curriculum",):
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
