#!/usr/bin/env python3
"""v5 LEDGER HELPER - the only way rows enter principle_ledger_v5.csv.

The v5 blind read (Framework/v5/PREREGISTRATION - v5 blind read and comparison.md, 2026-10-03)
writes its rows to a second ledger with the same first eight columns as principle_ledger.csv and
four more: speaker, kind, heading, unit. This helper does four mechanical things and nothing else:

  add <rows.json>      validate each row, MATCH ITS QUOTE AGAINST ITS SOURCE with the acceptance
                       test's own matcher (tools/ledger_verbatim.match_quote), refuse the whole
                       batch if any row fails, assign ids, append with csv.writer
  verify               run check 4 on the v5 ledger; exit 1 on any failing status
  unit "<key>"         print the line span and headings of an order-file unit, and its letter and
                       signed report sections, so the reader reads by line span and does not skim
  status "<key>"       rows already written for a unit, and its note's PROGRESS line
  erratum <id> "<text>" append a dated ERRATUM to one row's evolution_notes; nothing else changes (2026-10-04)
  count [--by X]       counts by year, speaker, kind, unit or prefix
  init                 create the empty ledger with its header (idempotent)

The tooling test (Framework/OPERATOR-PROTOCOL.md): a tool may get the same number sooner, never
add a number. This helper sequences ids, runs a match check_framework would run later anyway,
and counts rows. It chooses no quote, writes no concept and produces no figure for any document.

Ids: M<year>-<nnn> for Annual Meetings/ rows, L<year>-<nnn> for Shareholder Letters/ rows,
R<year>-<nnn> for the signed sections of Annual Reports/ rows; three digits; assigned here only.
A row's prefix follows its source folder, so a reader cannot mislabel a source.

Rows arrive as a JSON list of objects with these keys (id is NOT supplied):
  quote_verbatim, year, source_file, concept, speaker, kind, heading, unit
and optionally evolution_notes. era and supports_gate_or_sheet are written as "(blind read)".
"""
import argparse, collections, csv, io, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ledger_verbatim as lv

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = lv.ROOT
LEDGER_V5 = os.path.join(ROOT, "principle_ledger_v5.csv")
ORDER = os.path.join(ROOT, "Screens", "_daily", "_v5_order.txt")
NOTES = os.path.join(ROOT, "Framework", "v5", "notes")
HEADER = ["id", "era", "quote_verbatim", "year", "source_file", "concept",
          "supports_gate_or_sheet", "evolution_notes", "speaker", "kind", "heading", "unit"]
KINDS = ("rule", "test", "definition", "mistake-and-lesson", "tension")
SPEAKER = re.compile(r"^(BUFFETT|MUNGER|ABEL|JAIN|OTHER:[A-Za-z][A-Za-z .'\-]*)$")
PREFIX_BY_FOLDER = {"Annual Meetings": "M", "Shareholder Letters": "L", "Annual Reports": "R"}
BLIND = "(blind read)"
# The signed, chairman-authored sections of a printed annual report (CASE 2 of the v5 case).
# Widened 2026-10-04 from the first units' reports: the 1997 report marks sections `===== Title =====`,
# and the reprinted Owner's Manual carries PURCHASE-ACCOUNTING ADJUSTMENTS between its listed sections.
SIGNED = re.compile(r"^[\s=*_-]*(ACQUISITION CRITERIA|OWNER-RELATED BUSINESS PRINCIPLES|"
                    r"AN OWNER'S MANUAL|OWNER'S MANUAL|INTRINSIC VALUE[^a-z]*|"
                    r"PURCHASE-ACCOUNTING ADJUSTMENTS|THE MANAGING OF BERKSHIRE)[\s=*_-]*$")
LOCATOR = lv.LOCATOR
SHORT_LOCATOR = re.compile(r"\(lines?\s+(\d+)\)\s*$")


def _read_rows():
    if not os.path.exists(LEDGER_V5):
        return []
    with open(LEDGER_V5, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def cmd_init(_):
    if os.path.exists(LEDGER_V5):
        print("exists:", LEDGER_V5)
        return 0
    with open(LEDGER_V5, "w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f, lineterminator="\n").writerow(HEADER)
    print("created:", LEDGER_V5)
    return 0


def _next_ids(prefix, year, existing):
    taken = {int(i.split("-")[1]) for i in existing if i.startswith(f"{prefix}{year}-")}
    n = max(taken) if taken else 0
    while True:
        n += 1
        yield f"{prefix}{year}-{n:03d}"


def cmd_add(a):
    with open(a.json, encoding="utf-8") as f:
        new = json.load(f)
    if not isinstance(new, list) or not new:
        print("REFUSED: the JSON must be a non-empty list of row objects"); return 1
    existing = _read_rows()
    existing_ids = [r["id"] for r in existing]
    existing_quotes = {lv._loose(r["quote_verbatim"]) for r in existing}
    problems, prepared = [], []
    gens = {}
    for k, r in enumerate(new, 1):
        tag = f"row {k}"
        for key in ("quote_verbatim", "year", "source_file", "concept", "speaker", "kind", "heading", "unit"):
            if not str(r.get(key, "")).strip():
                problems.append(f"{tag}: missing {key}")
        if problems and problems[-1].startswith(tag):
            continue
        year = str(r["year"]).strip()
        if not re.fullmatch(r"(19|20)\d{2}", year):
            problems.append(f"{tag}: year must be four digits, got {year!r}")
        if r["kind"] not in KINDS:
            problems.append(f"{tag}: kind {r['kind']!r} not in {KINDS}")
        if not SPEAKER.match(r["speaker"].strip()):
            problems.append(f"{tag}: speaker {r['speaker']!r} not BUFFETT/MUNGER/ABEL/JAIN/OTHER:<name>")
        raw_src = r["source_file"].strip()
        # one locator form: "(lines N)" becomes "(lines N-N)" (2026-10-04, after 1996 AM wrote both)
        raw_src = SHORT_LOCATOR.sub(lambda m: f"(lines {m.group(1)}-{m.group(1)})", raw_src)
        src = LOCATOR.sub("", raw_src).strip()
        folder = src.split("/")[0]
        prefix = PREFIX_BY_FOLDER.get(folder)
        if not prefix:
            problems.append(f"{tag}: source folder {folder!r} is not one the v5 read admits")
            continue
        if prefix == "M" and not r["heading"].strip().startswith("### "):
            problems.append(f"{tag}: a meeting row's heading must be the '### N. ...' line it sits under")
        full = os.path.join(ROOT, src)
        if not os.path.exists(full):
            problems.append(f"{tag}: source file not on disk: {src}")
            continue
        quote = r["quote_verbatim"]
        if lv._loose(quote) in existing_quotes:
            problems.append(f"{tag}: duplicate of a quote already in the v5 ledger")
            continue
        ok, nfrags, missing = lv.match_quote(quote, full)
        if not ok:
            problems.append(f"{tag}: DEFECT fragment {[m + 1 for m in missing]} of {nfrags} "
                            f"not found in document order in {src}")
            continue
        existing_quotes.add(lv._loose(quote))
        gens.setdefault((prefix, year), _next_ids(prefix, year, existing_ids))
        rid = next(gens[(prefix, year)])
        existing_ids.append(rid)
        prepared.append([rid, BLIND, quote, year, raw_src, r["concept"].strip(), BLIND,
                         str(r.get("evolution_notes", "")).strip(), r["speaker"].strip(),
                         r["kind"], r["heading"].strip(), r["unit"].strip()])
    if problems:
        print(f"REFUSED: {len(problems)} problem(s); nothing appended")
        for p in problems:
            print("  -", p)
        return 1
    if not os.path.exists(LEDGER_V5):
        cmd_init(None)
    buf = io.StringIO()
    csv.writer(buf, lineterminator="\n").writerows(prepared)
    with open(LEDGER_V5, "a", encoding="utf-8", newline="") as f:
        f.write(buf.getvalue())
    for row in prepared:
        print("appended", row[0], "|", row[8], "|", row[9], "|", row[2][:70].replace("\n", " "))
    return 0


def cmd_verify(_):
    if not os.path.exists(LEDGER_V5):
        print("no v5 ledger yet"); return 0
    res = lv.verify(LEDGER_V5)
    c = collections.Counter(x["status"] for x in res)
    print(f"V5 LEDGER VERBATIM   {len(res)} rows")
    for k in sorted(c):
        print(f"  {k:<24} {c[k]}")
    bad = [x for x in res if x["status"] in lv.FAIL_STATUSES]
    for x in bad:
        print(f"\n  {x['id']:<12} {x['status']:<22} {x['source']}\n           {x['detail']}")
    return 1 if bad else 0


def _order_line(key):
    with open(ORDER, encoding="utf-8") as f:
        for line in f:
            parts = [p.strip() for p in line.rstrip("\n").split("|")]
            if parts and parts[0] == key:
                return parts
    return None


def _lines(path):
    with open(os.path.join(ROOT, path), encoding="utf-8", errors="replace") as f:
        return f.read().split("\n")


def cmd_unit(a):
    parts = _order_line(a.key)
    if not parts:
        print("no such unit key in", ORDER); return 1
    key, transcript, heading, letter, report = (parts + ["-"] * 5)[:5]
    lines = _lines(transcript)
    h2 = [i for i, l in enumerate(lines, 1) if l.startswith("## ")]
    start = next((i for i in h2 if lines[i - 1].strip() == heading), None)
    if start is None:
        print(f"heading {heading!r} not found in {transcript}"); return 1
    end = next((i - 1 for i in h2 if i > start), len(lines))
    words = sum(len(l.split()) for l in lines[start - 1:end])
    print(f"UNIT {key}")
    print(f"  transcript  {transcript}  lines {start}-{end}  (~{words} words)")
    for i in range(start, end + 1):
        if lines[i - 1].startswith("### "):
            print(f"    {i:>5}  {lines[i - 1].strip()}")
    if letter != "-":
        ll = _lines(letter)
        print(f"  letter      {letter}  lines 1-{len(ll)}  (~{sum(len(l.split()) for l in ll)} words)")
    if report != "-":
        rl = _lines(report)
        print(f"  report      {report}  lines 1-{len(rl)}; signed sections found at:")
        found = [(i, l.strip()) for i, l in enumerate(rl, 1) if SIGNED.match(l)]
        for i, l in found:
            print(f"    {i:>5}  {l}")
        if not found:
            print("    (no signed-section heading found by the pattern; read the contents page by hand)")
        # Which earlier R-rows still match this year's reprint (added 2026-10-04 after the 2007 and 2008 AM
        # units did this by hand): MATCH means the sentence is reprinted unchanged, DRIFT means the wording
        # moved and the reader should look at that sentence. The reader may not open earlier reports; the
        # helper runs the same matcher the acceptance test runs. Same number sooner, no number added.
        rrows = [r for r in _read_rows() if r["id"].startswith("R")]
        if not found:
            # No signed section is printed at all (FY2018 onward), so MATCH/DRIFT would report every R-row as
            # dropped. That is an absence of the whole reprint, recorded once in the note, not 49 drops.
            print("  earlier R-rows against this report: not run, no signed section is printed in this report")
            rrows = []
        if rrows:
            full = os.path.join(ROOT, report)
            drift = [r for r in rrows if not lv.match_quote(r["quote_verbatim"], full)[0]]
            print(f"  earlier R-rows against this report: {len(rrows) - len(drift)} MATCH, {len(drift)} DRIFT")
            # For each DRIFT: do the sentence's opening words still occur in this file? "reworded" means the
            # passage is still here with changed wording; "opening not found" means it may have been dropped,
            # which is itself a change of lesson. Added 2026-10-04 after the 2010 AM unit had to open an
            # earlier report to tell the two apart. The reader still reads the sentence; this only points.
            text = lv._loose_file(full)
            for r in drift:
                head = lv._loose(" ".join(r["quote_verbatim"].split()[:8]))
                where = "reworded (opening words still present)" if head and head in text else "opening not found (dropped?)"
                print(f"    {r['id']:<10} {where}")
    return 0


def cmd_status(a):
    rows = [r for r in _read_rows() if r.get("unit", "").strip() == a.key]
    c = collections.Counter((r["id"][0], r["kind"]) for r in rows)
    print(f"UNIT {a.key}: {len(rows)} rows")
    for (p, k), n in sorted(c.items()):
        print(f"  {p} {k:<20} {n}")
    note = os.path.join(NOTES, f"{a.key}.md")
    if os.path.exists(note):
        prog = [l for l in open(note, encoding="utf-8").read().split("\n") if l.startswith("PROGRESS:")]
        print("  note:", os.path.relpath(note, ROOT), "|", prog[-1] if prog else "(no PROGRESS line)")
    else:
        print("  note: none")
    return 0


def cmd_erratum(a):
    """Append a dated ERRATUM to one row's evolution_notes. Nothing else in the row may change: the quote,
    the source and the heading are what the acceptance test holds the row to, and a wrong quote is a new
    row plus a note, never an edit. Added 2026-10-04 after three units reported wrong cross-references
    they had no way to correct. Rewrites the file through csv.writer, as ledger_v4_additions.py did."""
    import datetime
    with open(LEDGER_V5, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    header, body = rows[0], rows[1:]
    col = header.index("evolution_notes")
    hit = [r for r in body if r and r[0] == a.id]
    if not hit:
        print("no such id:", a.id); return 1
    stamp = datetime.date.today().isoformat()
    note = f"ERRATUM {stamp}: {a.text.strip()}"
    hit[0][col] = (hit[0][col] + " | " + note) if hit[0][col].strip() else note
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header); w.writerows(body)
    with open(LEDGER_V5, "w", encoding="utf-8-sig", newline="") as f:
        f.write(buf.getvalue())
    print("erratum appended to", a.id, "|", note)
    return 0


def cmd_count(a):
    rows = _read_rows()
    key = {"year": lambda r: r["year"], "speaker": lambda r: r["speaker"], "kind": lambda r: r["kind"],
           "unit": lambda r: r["unit"], "prefix": lambda r: r["id"][0]}[a.by]
    c = collections.Counter(key(r) for r in rows)
    print(f"{len(rows)} rows by {a.by}")
    for k in sorted(c):
        print(f"  {k:<28} {c[k]}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init").set_defaults(fn=cmd_init)
    p = sub.add_parser("add"); p.add_argument("json"); p.set_defaults(fn=cmd_add)
    sub.add_parser("verify").set_defaults(fn=cmd_verify)
    p = sub.add_parser("unit"); p.add_argument("key"); p.set_defaults(fn=cmd_unit)
    p = sub.add_parser("status"); p.add_argument("key"); p.set_defaults(fn=cmd_status)
    p = sub.add_parser("erratum"); p.add_argument("id"); p.add_argument("text"); p.set_defaults(fn=cmd_erratum)
    p = sub.add_parser("count"); p.add_argument("--by", default="year",
                                                choices=("year", "speaker", "kind", "unit", "prefix"))
    p.set_defaults(fn=cmd_count)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
