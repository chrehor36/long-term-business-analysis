# The FY2023 10-K of each peer, to push the current-accident-year row back to 2021.
import sys, os, re, html, json
sys.path.insert(0, os.path.abspath("tools"))
import sources
sys.path.insert(0, os.path.abspath("Test Runs/_research 2026-09-19 CB/peers"))
from fetch_ppd import strip, D

PEERS = [("WRB", "11544"), ("ACGL", "947484"), ("RLI", "84246"),
         ("KNSL", "1669162"), ("AXS", "1214816")]


def tenk_for_period(cik, period_prefix):
    url = "https://data.sec.gov/submissions/CIK%010d.json" % int(cik)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name="subs_%s" % cik, max_age_h=24)
    if not isinstance(raw, str):
        raw = raw.decode("utf-8", "replace")
    j = json.loads(raw)
    r = j["filings"]["recent"]
    for form, date, acc, doc, rep in zip(r["form"], r["filingDate"], r["accessionNumber"],
                                         r["primaryDocument"], r["reportDate"]):
        if form == "10-K" and str(rep).startswith(period_prefix):
            return acc, doc, date, rep
    return None


for tk, cik in PEERS:
    got = tenk_for_period(cik, "2023")
    if not got:
        print("%-5s NO FY2023 10-K FOUND in the recent submissions window" % tk)
        continue
    acc, doc, date, rep = got
    out = os.path.join(D, "%s_tenk_FY2023.txt" % tk)
    if not os.path.exists(out):
        url = "https://www.sec.gov/Archives/edgar/data/%s/%s/%s" % (cik, acc.replace("-", ""), doc)
        raw = sources._get(url, headers=sources.SEC_UA, cache_name="peer23_%s" % tk, max_age_h=999)
        if not isinstance(raw, str):
            raw = raw.decode("utf-8", "replace")
        open(out, "w", encoding="utf-8").write(strip(raw))
    print("%-5s acc %s  doc %-28s filed %s  period %s  bytes %d"
          % (tk, acc, doc, date, rep, os.path.getsize(out)))
