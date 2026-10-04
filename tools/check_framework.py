#!/usr/bin/env python3
"""VERIFICATION — the framework's own acceptance test.

Run:  python tools/check_framework.py

Six checks, three from the v4 plan, two adopted 2026-09-20 and one on 2026-09-25:
  1. NO PHANTOM CITATIONS  - every [Exx-nn] cited in the docs exists in the ledger
  2. ZERO UNLABELLED NUMBERS - every claim carrying a number resolves to a ledger id
     or sits in a block labelled CONVENTION
  3. LEDGER INTEGRITY - well-formed, no duplicate ids, every row has a source file
     that actually exists on disk
  4. LEDGER VERBATIM - every row matches its cited source verbatim, with elisions marked
     and in document order (tools/ledger_verbatim.py)
  5. NO PHANTOM CITATIONS IN ANY RUN FILE - the sweep over Test Runs/
  6. POINTERS RESOLVE - every path named in a pointer document (CLAUDE.md, the protocol,
     Framework/README.md) exists on disk

Since 2026-10-03 checks 3 and 4 also run on principle_ledger_v5.csv when it exists (the v5
blind-read ledger, ids M/L/R<year>-<nnn>), and `--also <path>` checks one more document for a
single run without making it governing. Run:  python tools/check_framework.py --also "Framework/v5/DRAFT - THE FRAMEWORK v5.md"

Check 2 works on BLOCKS (paragraph / list item / table row), not lines, because the
documents are hard-wrapped and a citation frequently lands on the wrapped line.

Check 4 was adopted on the operator's instruction of 2026-09-20 (decision 14). Checks 1 to 3
resolve a citation to A ROW AND STOP THERE; until check 4 existed nothing in this repository
had ever asked whether the row matches the document it cites, and the six rows that did not
were found by a scratch script wired to nothing. It enforces PRIME RULE 1 rather than assuming
it. It opens only each row's own cited file, concludes nothing and computes nothing new; its
two exceptions (a cell that declares itself NOT A QUOTATION, and a row whose source file is
declared damaged in tools/shelf_damage.csv) are printed on every run rather than passed over.
"""
import sys
try:  # Windows consoles default to cp1252 and cannot encode the
    sys.stdout.reconfigure(encoding="utf-8")  # box-drawing / minus glyphs
except Exception:
    pass
import csv, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ledger_verbatim

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "principle_ledger.csv")
# The v5 blind-read ledger (2026-10-03): rows written by the meetings read, ids M/L/R<year>-<nnn>.
# Checked by checks 3 and 4 exactly as the first ledger is, whenever the file exists. Its ids join
# the set that checks 1, 2 and 5 resolve against. Nothing in DOCS cites it until v5 is adopted.
LEDGER_V5 = os.path.join(ROOT, "principle_ledger_v5.csv")
DOCS = [
    os.path.join(ROOT, "Framework", "THE FRAMEWORK v4.md"),
    os.path.join(ROOT, "Test Runs", "_TEMPLATE - Company Run.md"),
    # Sector methods carry rules, so they are governing documents and must pass the same
    # test. Added 2026-09-02 with the insurer method: a rule that escapes the acceptance
    # test because it lives in a different file is exactly the drift v4 was built to end.
    os.path.join(ROOT, "Framework",
                 "SECTOR METHOD - owner earnings for insurers and "
                 "float-bearing holding companies.md"),
    # The holdings framework governs owned positions, so it and its review surface pass the
    # same test. Added 2026-09-13 when the operator adopted it.
    os.path.join(ROOT, "Framework", "THE HOLDINGS FRAMEWORK.md"),
    os.path.join(ROOT, "Test Runs", "_TEMPLATE - Holding Review.md"),
    # The operator protocol and the prime rules moved out of CLAUDE.md on 2026-09-25, when
    # CLAUDE.md became the map of the project. Until then the protocol's own citations were
    # never verified, because CLAUDE.md was not in this list. Both files pass the same test now.
    os.path.join(ROOT, "Framework", "OPERATOR-PROTOCOL.md"),
    os.path.join(ROOT, "CLAUDE.md"),
]

# Pointer documents: files whose job is to point at other files. Check 6 asks one thing of
# them, whether every path they name exists on disk. Added 2026-09-25: pointer files had gone
# stale repeatedly that month (a ledger count in CLAUDE.md two rebuilds behind the file, a
# Framework README routing to v3.0 PDFs until 2026-09-20) and nothing had ever asked. Same
# shape as check 3's source-file-exists test: it concludes nothing and adds no number.
POINTER_DOCS = [
    os.path.join(ROOT, "CLAUDE.md"),
    os.path.join(ROOT, "Framework", "OPERATOR-PROTOCOL.md"),
    os.path.join(ROOT, "Framework", "README.md"),
    os.path.join(ROOT, "README.md"),   # the human front door; joined once rewritten, 2026-09-25
    os.path.join(ROOT, "PORTFOLIO.md"),  # names a run file on nearly every row; joined 2026-09-26
]
PATH_EXT = (".md", ".py", ".csv", ".json", ".txt", ".ps1")


def pointer_paths(text):
    """Every backtick span that reads as a repository path: it contains a slash or ends in a
    file extension. Spans holding a <placeholder> or a leading command word are not paths."""
    for span in re.findall(r"`([^`\n]+)`", text):
        s = span.strip()
        if "<" in s or s.startswith(("python ", "git ", "claude ")):
            continue
        if "/" in s or s.lower().endswith(PATH_EXT):
            yield s

# Two id classes: E<era>-<nn> (principle_ledger.csv) and, since 2026-10-03, M/L/R<year>-<nnn>
# (principle_ledger_v5.csv: meeting, letter and signed-report-section rows of the v5 blind read).
# One regex, so every check that resolves ids sees both. The leading letter keeps ISO dates out,
# and a sweep of every document on 2026-10-03 found zero strings of the new shape, so no backlog.
ID = re.compile(r"\b(?:E[1-5]-\d{2}|[MLR](?:19|20)\d{2}-\d{3})\b")
# A class of ids can only be resolved against the ledger that holds it. Where the v5 ledger is not on
# disk (the public copy of this repository withholds it until v5 is adopted), the v5 class is not
# checked at all rather than failed as phantom (2026-10-04).
if not os.path.exists(LEDGER_V5):
    ID = re.compile(r"\bE[1-5]-\d{2}\b")

# Numbers that are never framework rules: dates, version strings, ordered-list
# markers, section pointers, and the project's own audit/backtest record.
BENIGN = re.compile(
    r"^[-*\s]*\**\d+[\.\)]"                # "1." / "- **1." ordered list marker
    r"|^[-*\s]*\**\(\d+\)"                 # "(1)" sub-item marker
    r"|^\|"                                # table rows get their own block
    r"|20\d\d-\d\d-\d\d"                   # ISO dates
    r"|\bv\d(\.\d)?\b"                     # version strings
    r"|\bQ[1-6]\b|\bSTEP \d"               # section pointers
    r"|\bH[1-5]\b"                         # holdings-framework section pointers (added 2026-09-13)
    r"|\b(?:operator )?rule \d\b|\bPRIME RULE \d|\bcheck \d|\bsection \d|\bdecision \d"
                                           # rule, check, section and decision pointers (added 2026-09-25,
                                           # when the protocol and the map joined DOCS)
    r"|year-\d\b"                          # "year-1 growth" is a term, not a threshold
    r"|\bBT-\d+"                           # backtest ids
)
# Blocks that are the honesty record or meta-commentary rather than rules.
META_MARKERS = (
    "market-beating claim", "look-ahead bug", "backtest", "anchors, mean",
    "one-year holdings", "numeric rules", "had no corpus", "This document replaces",
    "register of what went", "accession number", "Copy `Test Runs",
    # Added 2026-09-02 with the insurer sector method. A governing document sometimes has
    # to cite THE PROJECT'S OWN measurements - a screen artifact it produced, a count of
    # its own queue - and those are audit record, not rules, exactly like the backtest
    # numbers above. The marker is deliberately a literal phrase the author must WRITE,
    # so the exemption is claimed on purpose and is visible to the reader.
    "this project's own record",
)


def blocks(text):
    """Split into logical blocks: blank-line separated, but each list item and each
    table row is its own block so a citation cannot be borrowed from a neighbour."""
    out, buf = [], []
    for raw in text.split("\n"):
        s = raw.rstrip()
        starts_item = bool(re.match(r"^\s*([-*+]|\d+[\.\)])\s", s)) or s.startswith("|")
        if not s.strip():
            if buf: out.append("\n".join(buf)); buf = []
        elif starts_item and buf:
            out.append("\n".join(buf)); buf = [s]
        else:
            buf.append(s)
    if buf: out.append("\n".join(buf))
    return out


def load_ledger(path=LEDGER):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    return rows[0], rows[1:]


def main():
    fails = []
    ledger_ids = set()
    # Both ledgers pass checks 3 and 4; the second only when it exists (2026-10-03).
    ledgers = [LEDGER] + ([LEDGER_V5] if os.path.exists(LEDGER_V5) else [])
    for ledger_path in ledgers:
        lname = os.path.basename(ledger_path)
        header, body = load_ledger(ledger_path)

        # ---- check 3: ledger integrity -----------------------------------------
        ids = [r[0].strip() for r in body if r]
        dupes = {i for i in ids if ids.count(i) > 1}
        malformed = [r[0] for r in body if len(r) != len(header)]
        if dupes: fails.append(f"{lname}: duplicate ids {sorted(dupes)}")
        if malformed: fails.append(f"{lname}: malformed rows {malformed}")

        missing_src = []
        for r in body:
            if len(r) < 5: continue
            # strip only a trailing "(line N)"/"(lines N-M)" locator; paths
            # legitimately contain parentheses, e.g. "Munger Talks (PCA)/"
            src = re.sub(r"\s*\([^)]*\b(?:lines?|pp?\.|principle|para|ch)\b[^)]*\)\s*$",
                         "", r[4]).strip()
            if src and not os.path.exists(os.path.join(ROOT, src.rstrip("/"))):
                missing_src.append((r[0], src))
        if missing_src:
            fails.append(f"{lname}: {len(missing_src)} rows cite a source file not on disk")
            for i, s in missing_src[:8]: fails.append(f"          {i} -> {s}")

        ledger_ids |= set(ids)
        print(f"LEDGER            {len(body)} rows, {len(set(ids))} unique ids   {lname}"
              f"{'' if not (dupes or malformed) else '   <-- PROBLEM'}")
        print(f"                  source files on disk: {len(body)-len(missing_src)}/{len(body)}")

        # ---- check 4: ledger verbatim ------------------------------------------
        # Opens each row's own cited source and looks for the row's own words. The two declared
        # exceptions are printed here on every run, so neither can go quiet: a cell that declares
        # itself NOT A QUOTATION, and a row whose SOURCE file is damaged (tools/shelf_damage.csv).
        # A declared-damaged row that VERIFIES is a failure, so the exception cannot outlive its
        # cause. See tools/ledger_verbatim.py for the full reasoning.
        vres = ledger_verbatim.verify(ledger_path)
        vcount = {}
        for x in vres:
            vcount[x["status"]] = vcount.get(x["status"], 0) + 1
        verified = vcount.get("EXACT", 0) + vcount.get("ELISION_OK", 0)
        vfails = [x for x in vres if x["status"] in ledger_verbatim.FAIL_STATUSES]
        print(f"                  verbatim against cited source: {verified}/{len(vres)}"
              f"   {'OK' if not vfails else '<-- PROBLEM'}")
        for x in vres:
            if x["status"] not in ("EXACT", "ELISION_OK"):
                print(f"                    {x['id']}  {x['status']}"
                      f"{'  ' + x['detail'] if x['detail'] else ''}")
        if vfails:
            fails.append(f"{lname}: {len(vfails)} rows do not match their cited source verbatim")
            for x in vfails[:8]:
                fails.append(f"          {x['id']} {x['status']} {x['detail']}")

    # ---- check 5: no phantom citations anywhere in Test Runs/ ------------------------
    # Adopted 2026-09-20 at the operator's "Fix" (decision 7 of the 2026-09-20 03:32 audit).
    # Checks 1 and 2 cover the five governing documents; the 1,000-odd run files under
    # Test Runs/ cite the same ids and nothing had ever asked whether they resolve. The sweep
    # opens every .md under Test Runs/, collects [Ex-nn] ids, and reports any id that is not
    # a ledger row. Measured before adoption: 1,044 files, 23,475 citations, 0.7 s, zero
    # phantoms - so it locks in a property rather than opening a backlog. It concludes nothing.
    tr_files = tr_cites = 0
    tr_phantom = {}
    tr_root = os.path.join(ROOT, "Test Runs")
    for root_, _, fs in os.walk(tr_root):
        for fn in fs:
            if not fn.endswith(".md"):
                continue
            tr_files += 1
            try:
                txt = open(os.path.join(root_, fn), encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            c = set(ID.findall(txt))
            tr_cites += len(c)
            ph = sorted(c - ledger_ids)
            if ph:
                tr_phantom[fn] = ph
    print(f"TEST RUNS         {tr_files} files, {tr_cites} distinct id citations, "
          f"phantom in {len(tr_phantom)} files   {'OK' if not tr_phantom else '<-- PROBLEM'}")
    if tr_phantom:
        fails.append(f"Test Runs: {len(tr_phantom)} files cite ids not in the ledger")
        for fn, ph in list(tr_phantom.items())[:8]:
            fails.append(f"          {fn[:70]} -> {ph[:5]}")

    # ---- check 6: every path named in a pointer document exists --------------------
    # Resolves each span relative to the pointer file's own folder first (Framework/README.md
    # names its siblings bare), then to the repository root.
    pt_checked, pt_missing = 0, []
    for path in POINTER_DOCS:
        if not os.path.exists(path):
            pt_missing.append((os.path.basename(path), "(the pointer file itself)")); continue
        text = open(path, encoding="utf-8").read()
        here = os.path.dirname(path)
        for s in pointer_paths(text):
            pt_checked += 1
            rel = s.rstrip("/")
            if not (os.path.exists(os.path.join(here, rel)) or os.path.exists(os.path.join(ROOT, rel))):
                pt_missing.append((os.path.basename(path), s))
    print(f"POINTERS          {pt_checked} paths named in {len(POINTER_DOCS)} pointer files, "
          f"{len(pt_missing)} missing   {'OK' if not pt_missing else '<-- PROBLEM'}")
    if pt_missing:
        fails.append(f"pointers: {len(pt_missing)} paths named in a pointer file are not on disk")
        for fn, s in pt_missing[:12]:
            fails.append(f"          {fn} -> {s}")

    # ---- checks 1 and 2 -----------------------------------------------------
    for path in DOCS:
        if not os.path.exists(path):
            print(f"\n{os.path.basename(path)}: NOT FOUND — skipped"); continue
        text = open(path, encoding="utf-8").read()
        name = os.path.basename(path)

        cited = set(ID.findall(text))
        phantom = sorted(cited - ledger_ids)
        if phantom: fails.append(f"{name}: phantom citations {phantom}")

        unlabelled = []
        for b in blocks(text):
            stripped = "\n".join(l for l in b.split("\n") if not l.lstrip().startswith(">"))
            if not re.search(r"\d", stripped): continue
            if ID.search(b) or "CONVENTION" in b: continue
            if any(m in b for m in META_MARKERS): continue
            digits = [d for d in re.findall(r"[^\n]*\d[^\n]*", stripped)
                      if not BENIGN.search(d.strip())]
            if digits:
                unlabelled.append(b.strip().replace("\n", " ")[:110])

        print(f"\n{name}")
        print(f"  ledger ids cited      {len(cited)}")
        print(f"  phantom citations     {len(phantom)}   {'OK' if not phantom else phantom}")
        print(f"  unlabelled numbers    {len(unlabelled)}   {'OK' if not unlabelled else '<-- REVIEW'}")
        for u in unlabelled: print(f"      {u}")
        if unlabelled:
            fails.append(f"{name}: {len(unlabelled)} numeric blocks with no ledger id "
                         f"and no CONVENTION label")

    print("\n" + "=" * 70)
    if fails:
        print("FAIL")
        for f in fails: print("  -", f)
        return 1
    print("PASS — every number resolves to a verbatim source or a confessed convention,\n"
          "       and every ledger row matches the document it cites.")
    return 0


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="the framework's acceptance test")
    # --also <path>: run checks 1 and 2 on one more document for this run only, without adding
    # it to DOCS. Added 2026-10-03 so a v5 DRAFT in Framework/v5/ can be checked on demand while
    # it is not governing. Adoption adds the final path to DOCS with a dated comment, as before.
    ap.add_argument("--also", action="append", default=[], metavar="PATH",
                    help="also check this document (repeatable); not added to DOCS")
    args = ap.parse_args()
    for p in args.also:
        DOCS.append(p if os.path.isabs(p) else os.path.join(ROOT, p))
    sys.exit(main())
