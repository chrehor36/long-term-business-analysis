#!/usr/bin/env python3
"""LEDGER VERBATIM - does every row of principle_ledger.csv match the document it cites?

Run standalone for the row-by-row report:   python tools/ledger_verbatim.py
On the v5 blind-read ledger:                python tools/ledger_verbatim.py principle_ledger_v5.csv
Imported by tools/check_framework.py as check 4 of the acceptance test, and by tools/v5_ledger.py,
which runs match_quote() on every row before it is appended (added 2026-10-03).

PRIME RULE 1 is the rule this enforces: "VERBATIM ONLY. The ledger takes exact quotes with
year and source file. Paraphrase is never recorded as quotation. Flag OCR and transcript
artifacts; never smooth them."

Promoted 2026-09-20 from the one-cycle scratch script `tools/_tmp_ledger_audit.py`, which
found six defective rows on 2026-09-20 06:32 - the first time in this repository's life that
any check opened a letter, a transcript or a talk. Every earlier check resolved a citation to
A ROW AND STOPPED THERE.

WHAT IT DOES AND DOES NOT DO. It opens each row's own cited file and looks for the row's own
words. It concludes nothing: it computes no new number, it does not hunt the shelf for a
better home for a failed fragment (that is diagnosis, and diagnosis belongs to the reader),
and it never edits. A failure is a prompt to read two documents, because A VERBATIM CHECK IS
A CHECK ON TWO DOCUMENTS, AND EITHER CAN BE THE DAMAGED ONE (the 06:32 durable rule).

MATCHING. On a letters-and-digits normalisation, which kills smart quotes, dash class, hard
wrapping, double spaces and the U+FFFD that two shelf extractions leave where an em dash
belongs. A quote carrying an elision marker ("..." or "[...]") is split into fragments, and
every fragment must be found IN DOCUMENT ORDER, each after the end of the last - so a splice
in reverse transcript order fails, which is how E4-19's was caught.

TWO DECLARED, VISIBLE EXCEPTIONS. Neither is silent and neither can rot:

  1. A row whose `quote_verbatim` opens "NOT A QUOTATION" is not a quotation and is not
     matched. The ledger holds one: E5-07, a recorded negative finding over the Wesco
     letters. The declaration has to be WRITTEN INTO THE CELL, so it is the author's claim
     and a reader sees it in the same glance the tool does.

  2. A row listed in `tools/shelf_damage.csv` cites a source file with a hole in it. The
     file is empty as of 2026-09-25: it held one row, E3-20, while `Munger Talks (PCA)/Talk 02`
     was missing "pari-mutuel system" and the ROW was the sound document; the hole was
     restored from two July captures on 2026-09-20 and the row verifies. The mechanism stays.
     A declared row is reported under its own heading on
     every run and does NOT fail the build, because failing it would punish the ledger for a
     defect in the shelf and would block every unrelated commit until the operator's own copy
     of the Almanack arrives (decision 13). But a declared row that DOES verify FAILS, so the
     exception dies the day its cause is repaired and cannot quietly outlive it.
"""
import csv, os, re, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "principle_ledger.csv")
DAMAGE = os.path.join(ROOT, "tools", "shelf_damage.csv")

# The source_file column has two spellings - a bare path in most rows, a path plus a
# parenthetical locator in 25 of them. Paths legitimately contain parentheses, e.g.
# "Munger Talks (PCA)/", so only a locator-looking parenthetical is stripped.
LOCATOR = re.compile(r"\s*\((?:line|lines|principle|p\.|pp\.|para|chapter|ch\.)[^)]*\)\s*$", re.I)
ELLIPSIS = re.compile(r"\s*(?:…|\.\s*\.\s*\.)\s*")
NOT_A_QUOTE = "NOT A QUOTATION"

_cache = {}


def _norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("‘", "'"), ("’", "'"), ("‛", "'"), ("ʼ", "'"),
                 ("“", '"'), ("”", '"'), ("„", '"')]:
        s = s.replace(a, b)
    s = re.sub(r"[‐-―−]+", "-", s)
    return re.sub(r"\s+", " ", s.replace(" ", " ")).strip()


def _loose(s):
    return re.sub(r"[^a-z0-9]+", "", _norm(s).lower())


def _loose_file(path):
    if path not in _cache:
        with open(path, encoding="utf-8", errors="replace") as f:
            _cache[path] = _loose(f.read())
    return _cache[path]


def declared_damage():
    """id -> the row of tools/shelf_damage.csv that declares it. Absent file means none."""
    if not os.path.exists(DAMAGE):
        return {}
    with open(DAMAGE, encoding="utf-8-sig", newline="") as f:
        return {r["id"].strip(): r for r in csv.DictReader(f) if r.get("id", "").strip()}


def match_quote(quote, full_path):
    """Does `quote` occur in the file at `full_path`, on the letters-and-digits normalisation,
    with every elision fragment found in document order? Returns (ok, n_fragments, missing),
    where `missing` lists the zero-based indices of fragments not found in order.

    Lifted out of verify() on 2026-10-03 so that tools/v5_ledger.py can run the same test on
    a row BEFORE appending it (the second ledger, principle_ledger_v5.csv). Pure extraction:
    the loop is the one verify() has run since 2026-09-20, unchanged."""
    text = _loose_file(full_path)
    frags = [f for f in (_loose(p) for p in ELLIPSIS.split(quote)) if f]
    ok, pos, missing = bool(frags), 0, []
    for n, frag in enumerate(frags):
        i = text.find(frag, pos)
        if i < 0:
            ok = False
            missing.append(n)
            pos = len(text)  # keep scanning so out-of-order fragments are named too
        else:
            pos = i + len(frag)
    return ok, len(frags), missing


def verify(ledger_path=LEDGER):
    """One record per ledger row of `ledger_path` (default: principle_ledger.csv; the v5 blind-read
    ledger is verified by the same function since 2026-10-03). Statuses:
    EXACT, ELISION_OK        - verified against the cited file
    DECLARED_NOT_A_QUOTE     - the cell says so in its first words
    SHELF_DAMAGE_DECLARED    - declared in tools/shelf_damage.csv, reported not failed
    STALE_DAMAGE_ENTRY       - declared damaged but the row now verifies: FAIL
    DEFECT                   - does not match its source and nothing declares why: FAIL
    NO_SOURCE_FILE           - the cited path is not on disk: FAIL
    SOURCE_IS_DIR            - the cited path is a folder, on a row that claims to quote: FAIL
    """
    damage = declared_damage()
    out = []
    with open(ledger_path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        rid = (r.get("id") or "").strip()
        quote = r.get("quote_verbatim") or ""
        raw_src = (r.get("source_file") or "").strip()
        src = LOCATOR.sub("", raw_src).strip()
        rec = {"id": rid, "source": raw_src, "status": None, "detail": ""}
        out.append(rec)

        if quote.lstrip().upper().startswith(NOT_A_QUOTE):
            rec["status"] = "DECLARED_NOT_A_QUOTE"
            continue

        full = os.path.join(ROOT, src)
        if os.path.isdir(full.rstrip("/")):
            rec["status"] = "SOURCE_IS_DIR"
            rec["detail"] = "a row that quotes must cite a document, not a folder"
            continue
        if not os.path.exists(full):
            rec["status"] = "NO_SOURCE_FILE"
            continue

        ok, nfrags, missing = match_quote(quote, full)

        if ok:
            rec["status"] = "ELISION_OK" if nfrags > 1 else "EXACT"
            if rid in damage:
                rec["status"] = "STALE_DAMAGE_ENTRY"
                rec["detail"] = ("row now verifies; delete its line from tools/shelf_damage.csv")
        elif rid in damage:
            rec["status"] = "SHELF_DAMAGE_DECLARED"
            rec["detail"] = "hole in the source at: %s" % damage[rid].get("missing_span", "")
        else:
            rec["status"] = "DEFECT"
            rec["detail"] = "fragment %s of %d not found in document order" % (
                [n + 1 for n in missing], nfrags)
    return out


FAIL_STATUSES = ("DEFECT", "NO_SOURCE_FILE", "SOURCE_IS_DIR", "STALE_DAMAGE_ENTRY")


def main():
    import sys, collections
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    # An optional path argument verifies another ledger of the same shape (the v5 ledger).
    path = sys.argv[1] if len(sys.argv) > 1 else LEDGER
    res = verify(path)
    c = collections.Counter(x["status"] for x in res)
    print("LEDGER VERBATIM   %d rows   %s" % (len(res), os.path.basename(path)))
    for k in sorted(c):
        print("  %-24s %d" % (k, c[k]))
    for x in res:
        if x["status"] not in ("EXACT", "ELISION_OK"):
            print("\n  %-8s %-22s %s" % (x["id"], x["status"], x["source"]))
            if x["detail"]:
                print("           %s" % x["detail"])
    return 1 if any(x["status"] in FAIL_STATUSES for x in res) else 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
