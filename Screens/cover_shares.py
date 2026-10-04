#!/usr/bin/env python3
"""COVER SHARES - read the share count off the filed cover page, by class.

WHY THIS EXISTS. The single most-repeated defect in this project is a market cap built on
a share count that companyfacts could not supply. It has now been found FIVE separate times,
each by a full run rather than by a screen:

  LEVI  2026-08-31  37,602,843 pre-IPO pre-split shares from 2019-01-30. True count
                    384,850,562. The screen entry was wrong by 10.23x and the "26.3%
                    statute yield" was noise.
  NKE   2026-09-02  a 2015 count, 11.1 years stale.
  DKS   2026-09-02  93,768,978 from 2011-01-29, 15.6 years stale.
  PINS  2026-09-02  127,371,000 from 2019-03-31 - the PRE-IPO balance sheet, three weeks
                    before listing. The cap was 4.06x too small and the name sat in tier 1
                    on a 4.98% yield that is really 1.23%.
  BRK   standing    an A/B artifact returning a $473M cap and a 4,683% yield.

THE MECHANISM IS ALWAYS THE SAME, and it is not a bug in the filer's reporting. SEC
`companyfacts` DROPS DIMENSIONED FACTS. The moment a filer tags its cover page BY SHARE
CLASS - which every multi-class filer must - the undimensioned `dei:EntityCommonStockShares
Outstanding` row stops advancing, and the fallback chain lands on whatever that filer last
reported without dimensions, which can be a decade old or predate the IPO.

WHAT THIS TOOL DOES, AND WHAT IT REFUSES TO DO. It fetches the most recent periodic filing
and reads the rendered Cover page (R1.htm), which carries every dimensioned value with its
class label. It returns the classes and the counts. IT DOES NOT SUM THEM AUTOMATICALLY into
a single number for a caller to divide by, and that refusal is deliberate: whether two
classes are economically equivalent is a JUDGMENT that requires reading the charter -
Berkshire's A converts to 1,500 B, Ford's Class B is not traded at all, and a non-voting
tracking stock may not share in earnings at all. The tool gets the operator to the numbers
sooner. It does not conclude (operator rule 8), and the run still reads the filing
(operator rule 4).

Usage:  python cover_shares.py BRK-B MKL WTM L
        python cover_shares.py --queue        # every name in the corrected master queue
"""
import io, json, os, re, sys, time, urllib.request, html

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
PERIODIC = ("10-Q", "10-K", "20-F", "40-F", "10-K/A", "10-Q/A")


def get(url, tries=3):
    last = None
    for i in range(tries):
        try:
            return urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=90).read()
        except Exception as e:      # SEC rate-limits; back off rather than give up
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


def ticker_map():
    d = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
    return {str(v["ticker"]).upper(): (int(v["cik_str"]), v["title"]) for v in d.values()}


def latest_periodic(cik):
    """(form, filed, period, accession) for the newest periodic filing."""
    d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    r = d["filings"]["recent"]
    for i in range(len(r["form"])):
        if r["form"][i] in PERIODIC:
            return (r["form"][i], r["filingDate"][i], r["reportDate"][i],
                    r["accessionNumber"][i], d.get("name", ""))
    return None


def cover_counts(cik, accession):
    """[(class_label, count)] read off the rendered cover page, in document order.

    R1.htm is the Financial Report renderer's first statement, which for every modern
    filing is the Cover page. It carries the DIMENSIONED values - the ones companyfacts
    discards - with the class label immediately preceding each.
    """
    a = accession.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/R1.htm"
    txt = get(url).decode("utf-8", "replace")
    txt = html.unescape(re.sub(r"<[^>]+>", "\n", txt))
    lines = [re.sub(r"\s+", " ", x).strip() for x in txt.split("\n")]
    lines = [x for x in lines if x]

    # THE UNITS GUARD. Found on ALPHABET 2026-09-02: the renderer scales, and its header
    # says so - "shares in Millions" - so the cover page reports Class A as 5,868 for a
    # company with 5.868 BILLION Class A shares. Nike and Dick's carry no such header and
    # report in units. Reading the scale off the page is the only safe way; assuming units
    # understates by 1,000,000x and assuming millions overstates by the same. This project's
    # own screener README already records a units bug of exactly this shape - a double 1e6
    # division that once produced "509 passes".
    scale, scale_note = 1, ""
    head = " ".join(lines[:40])
    m = re.search(r"shares in (Million|Thousand|Billion)", head, re.I)
    if m:
        scale = {"thousand": 1_000, "million": 1_000_000,
                 "billion": 1_000_000_000}[m.group(1).lower()]
        scale_note = f"renderer header says 'shares in {m.group(1)}s'; scaled by {scale:,}"

    out, label = [], None
    LABEL_STOP = {"Document Information [Line Items]", "Cover Page - shares",
                  "Cover [Abstract]", "Document Information [Table]"}
    # THE LABEL IS NOT SPELLED THE SAME BY EVERY RENDERER. Found on NIKE 2026-09-02: DKS
    # and PINS emit "Entity Common Stock, Shares Outstanding" and Nike emits it WITHOUT the
    # comma, so a startswith() on the comma form returned nothing at all for a filer with
    # two classes and 1.48bn shares. Silent zero, on exactly the class of name this tool
    # exists to catch.
    VALUE_LABEL = re.compile(r"^Entity Common Stock,? Shares Outstanding")
    for i, x in enumerate(lines):
        if VALUE_LABEL.match(x):
            # the value is the next line that parses as a number
            for y in lines[i + 1:i + 4]:
                n = y.replace(",", "")
                if n.isdigit():
                    out.append((label or "(single class / undimensioned)",
                                int(n) * scale))
                    break
        elif x not in LABEL_STOP and not x.startswith("Entity ") and len(x) < 60:
            # candidate class label: remember the most recent short line that is not
            # boilerplate, since the renderer emits "Class B Common Stock" then the block
            if re.search(r"class|common|ordinary|series", x, re.I):
                label = x
    return out, scale_note


def report(tickers):
    tm = ticker_map()
    for t in tickers:
        key = next((k for k in (t.upper(), t.upper().replace(".", "-"),
                                t.upper().replace("-", ".")) if k in tm), None)
        if key is None:
            print(f"{t:8s} NOT AN SEC REGISTRANT in the live ticker file")
            continue
        cik, name = tm[key]
        try:
            f = latest_periodic(cik)
            if not f:
                print(f"{t:8s} no periodic filing found (CIK {cik})")
                continue
            form, filed, period, acc, coname = f
            counts, scale_note = cover_counts(cik, acc)
        except Exception as e:
            print(f"{t:8s} FETCH FAILED: {e}")
            continue
        print(f"\n{t}  {coname or name}")
        print(f"   {form} filed {filed}, period {period}, accession {acc}")
        if scale_note:
            print(f"   UNITS: {scale_note}")
        if not counts:
            print("   NO COVER SHARE COUNT PARSED - read the filing by hand.")
            continue
        for lab, n in counts:
            print(f"   {lab[:44]:46s} {n:>16,}")
        if len(counts) > 1:
            tot = sum(n for _, n in counts)
            print(f"   {'--- arithmetic sum, NOT a share count ---':46s} {tot:>16,}")
            print("   MULTIPLE CLASSES. Whether these are economically equivalent is a")
            print("   JUDGMENT from the charter, not arithmetic. Berkshire's A converts to")
            print("   1,500 B; Ford's Class B does not trade. READ THE FILING.")
        # the staleness the run needs to see
        print(f"   cover date is the filing's own as-of; do not substitute a cached count.")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--queue" in sys.argv:
        import csv
        p = os.path.join(HERE, "2026-09-02 MASTER RUN QUEUE (corrected).csv")
        args = [r["ticker"] for r in csv.DictReader(open(p, encoding="utf-8"))]
    if not args:
        print(__doc__)
        return
    report(args)


if __name__ == "__main__":
    main()
