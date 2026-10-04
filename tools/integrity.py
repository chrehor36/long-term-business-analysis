#!/usr/bin/env python3
"""INTEGRITY — assemble the Q3 record.

    *** CANDIDATE — NOT ADMITTED TO v4. TESTED 2026-08-26 AND REJECTED. ***

    Three documented failures, full record in
    Framework/v4/TOOL TEST - integrity check, NOT ADMITTED.md :

      1. The XBRL layer is blind before ~2010 and inconsistent after. On the test
         set it reported WFC with ONE matter and KLAC with ZERO -- the two names
         the framework is proudest of catching. A silent failure pointing the
         wrong way.
      2. Keyword detection is drowned in boilerplate: "regulator penalty x2"
         appears identically in all seventeen Wells Fargo annual reports, so it
         cannot distinguish 2011 (Fed penalty) from 2009 (nothing).
      3. The Item 3 extraction does not isolate Item 3. A fixed window from the
         first "Legal Proceedings" match sweeps in Regulation and Supervision,
         and large filers make Item 3 a cross-reference to a note anyway.

    KEPT because annual_filings() is correct and reusable, and so the next
    attempt starts from this record instead of rediscovering it.

    DO NOT use its output as a Q3 input. Q3 is a manual read of the filed record.


    python tools/integrity.py WFC C KLAC --since 2000
    python tools/integrity.py TJX --text          # also pull Item 3 from the latest 10-K

WHAT IT DOES: lays out every litigation and loss-contingency matter a filer has
tagged, plus (with --text) the Item 3 Legal Proceedings narrative, each stamped
with the date it BECAME PUBLIC -- the filing date, not the fiscal period. That
stamp is what makes Q3 point-in-time honest: a run anchored at any date can cut
the list there and see only what was knowable.

WHAT IT REFUSES TO DO: decide whether a matter is disqualifying. Q3 is a binary
judgment made by a person reading the record [E2-26]. This tool fetches and
orders; it never scores. A high total is not a verdict and a low total is not a
clearance -- Wells Fargo's disqualifying matters were two penalties, not a big
number.

Ruling 14 test: does this get the same number sooner, or add a number? It gets
the same record sooner. It adds nothing.
"""
import sys
try:  # Windows consoles default to cp1252 and cannot encode the
    sys.stdout.reconfigure(encoding="utf-8")  # box-drawing / minus glyphs
except Exception:
    pass
import argparse, os, re, sys, html
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources as S

# Structured signals. Every one is an amount a filer chose to tag, so it is both
# material and dated. Filed date = the date it became public.
MONEY_TAGS = [
    "LitigationSettlementAmount",
    "LitigationSettlementExpense",
    "PaymentsForLegalSettlements",
    "LossContingencyDamagesAwardedValue",
    "LossContingencyDamagesSoughtValue",
    "LossContingencyAccrualAtCarryingValue",
    "LossContingencyEstimateOfPossibleLoss",
    "LossContingencyRangeOfPossibleLossMaximum",
    "GainLossRelatedToLitigationSettlement",
    "AccrualForEnvironmentalLossContingencies",
]
COUNT_TAGS = ["LossContingencyPendingClaimsNumber",
              "LossContingencyNewClaimsFiledNumber"]

# Words that mark a matter as REGULATORY or ADJUDICATED rather than ordinary
# commercial litigation. Presence is a prompt to read, never a score.
FLAGS = [
    ("consent order",     r"consent order|consent decree"),
    ("deferred pros.",    r"deferred prosecution|non-prosecution agreement"),
    ("regulator penalty", r"civil money penalt|civil penalt|fined by|assessed a penalt"),
    ("SEC action",        r"\bSEC\b[^.]{0,80}(?:action|charg|order|settle|investigat)"),
    ("DOJ",               r"Department of Justice|\bDOJ\b"),
    ("restatement",       r"restate(?:d|ment) (?:of|its|our|the) (?:prior|previously|financial)"),
    ("guilty/plea",       r"plead(?:ed|s)? guilty|pled guilty"),
    ("FCPA",              r"Foreign Corrupt Practices|\bFCPA\b"),
    ("fraud alleged",     r"\bfraud\b"),
    ("class action",      r"class action"),
]


def money_facts(facts, since):
    out = []
    for tax in ("us-gaap",):
        node = facts.get("facts", {}).get(tax, {})
        for t in MONEY_TAGS + COUNT_TAGS:
            if t not in node:
                continue
            for unit, pts in node[t]["units"].items():
                for x in pts:
                    filed = x.get("filed")
                    if not filed or filed < since:
                        continue
                    out.append(dict(tag=t, filed=filed, end=x.get("end"),
                                    form=x.get("form"), val=x.get("val"), unit=unit,
                                    fy=x.get("fy"), fp=x.get("fp")))
    # one row per (tag, value, end) -- keep the EARLIEST filing, i.e. when it became public
    best = {}
    for r in out:
        k = (r["tag"], r["val"], r["end"])
        if k not in best or r["filed"] < best[k]["filed"]:
            best[k] = r
    return sorted(best.values(), key=lambda r: r["filed"])


def annual_filings(cik, since):
    """EVERY 10-K/20-F, oldest first. Point-in-time honesty requires the whole
    history: the matter that disqualifies a company at a 2014 anchor lives in the
    2013 annual report, not in today's."""
    import json
    out = []
    txt = S._get(f"https://data.sec.gov/submissions/CIK{cik}.json", S.SEC_UA,
                 f"sub_{cik}.json", max_age_h=24 * 7)
    d = json.loads(txt)
    shards = [d["filings"]["recent"]]
    for f in d["filings"].get("files", []):
        try:
            shards.append(json.loads(S._get(
                f"https://data.sec.gov/submissions/{f['name']}", S.SEC_UA,
                f["name"], max_age_h=24 * 30)))
        except Exception:
            pass
    for r in shards:
        for fd, form, acc, doc in zip(r["filingDate"], r["form"],
                                      r["accessionNumber"], r["primaryDocument"]):
            if form in ("10-K", "20-F") and fd >= since and doc:
                out.append((fd, acc.replace("-", ""), doc))
    return sorted(set(out))


def latest_10k(cik):
    f = annual_filings(cik, "1990-01-01")
    return f[-1] if f else (None, None, None)


def item3_at(cik, ticker, fd, acc, doc):
    """Legal Proceedings narrative from ONE annual report, stamped with its filing
    date -- the date its contents became public."""
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/{doc}"
    try:
        raw = S._get(url, S.SEC_UA, f"ar_{ticker}_{fd}.htm", max_age_h=24 * 90)
    except Exception as e:
        return fd, None, f"fetch failed: {type(e).__name__}"
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    # take the LAST occurrence that has real body after it, not the table-of-contents hit
    best = ""
    for m in re.finditer(r"(?:ITEM\s*3[\.\s—-]*)?LEGAL\s+PROCEEDINGS", t, re.I):
        seg = t[m.start(): m.start() + 90000]
        if len(seg) > len(best) and sum(c.isalpha() for c in seg[:3000]) > 1200:
            best = seg
    return fd, (best or None), None


def scan_flags(text):
    hits = {}
    for label, pat in FLAGS:
        n = len(re.findall(pat, text, re.I))
        if n:
            hits[label] = n
    return hits


def run(ticker, since, want_text):
    cik, name = S.cik_for(ticker)
    if not cik:
        return dict(ticker=ticker, error="not an SEC filer")
    facts = S.sec_facts(cik)
    rows = money_facts(facts, since)
    money = [r for r in rows if r["tag"] not in COUNT_TAGS and isinstance(r["val"], (int, float))]
    big = sorted(money, key=lambda r: -abs(r["val"]))[:6]
    out = dict(ticker=ticker, name=name, cik=cik, n_matters=len(rows),
               first=rows[0]["filed"] if rows else None,
               last=rows[-1]["filed"] if rows else None, big=big, flags={}, ar=None)
    if want_text:
        hist = []
        for fd, acc, doc in annual_filings(cik, since):
            _, body, err = item3_at(cik, ticker, fd, acc, doc)
            if body:
                fl = scan_flags(body)
                if fl:
                    hist.append(dict(filed=fd, flags=fl, chars=len(body)))
        out["history"] = hist
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--since", default="2000-01-01")
    ap.add_argument("--text", action="store_true",
                    help="also pull Item 3 from the latest annual report (slow)")
    a = ap.parse_args()

    print("=" * 96)
    print("Q3 INTEGRITY RECORD — assembled, not judged.  CANDIDATE TOOL.")
    print("Every matter is stamped with the date it BECAME PUBLIC (the filing date),")
    print("so a point-in-time run can cut the list at its anchor. [E2-26]")
    print("=" * 96)
    print(f"{'ticker':<8}{'tagged matters':>15}{'first filed':>14}{'last filed':>13}"
          f"{'largest tagged amount':>26}")
    results = []
    for t in a.tickers:
        r = run(t.upper(), a.since, a.text)
        results.append(r)
        if r.get("error"):
            print(f"{t.upper():<8}  {r['error']}")
            continue
        big = f"{r['big'][0]['val']/1e6:,.0f}M {r['big'][0]['unit']}" if r["big"] else "—"
        print(f"{r['ticker']:<8}{r['n_matters']:>15}{str(r['first'] or '—'):>14}"
              f"{str(r['last'] or '—'):>13}{big:>26}")

    if a.text:
        print("\nITEM 3 LEGAL PROCEEDINGS — keyword prompts from the latest annual report")
        print("(a prompt to READ, never a score)\n")
        for r in results:
            if r.get("error"):
                continue
            if r.get("text_err") or not r.get("flags"):
                print(f"  {r['ticker']:<7} {r.get('text_err') or 'no flagged language found'}")
                continue
            fl = "  ".join(f"{k}×{v}" for k, v in
                           sorted(r["flags"].items(), key=lambda kv: -kv[1]))
            print(f"  {r['ticker']:<7} [AR {r['ar']}]  {fl}")

    print("\n" + "-" * 96)
    print("A high count is NOT a verdict and a low count is NOT a clearance.")
    print("Wells Fargo's disqualifying matters were two penalties, not a big number.")
    print("Q3 remains a person reading the record and making a binary call.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
