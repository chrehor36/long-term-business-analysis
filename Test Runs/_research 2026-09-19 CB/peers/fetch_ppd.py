# Extend the MKL competitor row (Test Runs/_research 2026-09-02 MKL/competitor-row.md) with the
# CURRENT-ACCIDENT-YEAR / PRIOR-YEAR-DEVELOPMENT separation the CB run needs.
# Primary filings only. Accessions taken from each registrant submissions JSON at fetch time.
import sys, os, re, html, json
sys.path.insert(0, os.path.abspath("tools"))
import sources

D = os.path.abspath("Test Runs/_research 2026-09-19 CB/peers")
if not os.path.isdir(D):
    os.makedirs(D)

PEERS = [("WRB", "11544"), ("ACGL", "947484"), ("RLI", "84246"),
         ("KNSL", "1669162"), ("AXS", "1214816"), ("MKL", "1096343")]


def strip(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?is)<br\s*/?>", "\n", h)
    h = re.sub(r"(?is)</(p|div|tr|h[1-6]|li)>", "\n", h)
    h = re.sub(r"(?is)</t[dh]>", " | ", h)
    h = re.sub(r"(?s)<[^>]+>", "", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t\xa0]+", " ", h)
    h = re.sub(r"\n\s*\n\s*\n+", "\n\n", h)
    return h


def latest_10k(cik):
    url = "https://data.sec.gov/submissions/CIK%010d.json" % int(cik)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name="subs_%s" % cik, max_age_h=24)
    if not isinstance(raw, str):
        raw = raw.decode("utf-8", "replace")
    j = json.loads(raw)
    r = j["filings"]["recent"]
    for form, date, acc, doc, rep in zip(r["form"], r["filingDate"], r["accessionNumber"],
                                         r["primaryDocument"], r["reportDate"]):
        if form == "10-K":
            return acc, doc, date, rep, j["name"]
    return None


for tk, cik in PEERS:
    acc, doc, date, rep, name = latest_10k(cik)
    out = os.path.join(D, "%s_tenk.txt" % tk)
    if not os.path.exists(out):
        url = "https://www.sec.gov/Archives/edgar/data/%s/%s/%s" % (cik, acc.replace("-", ""), doc)
        raw = sources._get(url, headers=sources.SEC_UA, cache_name="peer_%s" % tk, max_age_h=999)
        if not isinstance(raw, str):
            raw = raw.decode("utf-8", "replace")
        open(out, "w", encoding="utf-8").write(strip(raw))
    print("%-5s CIK %-8s %-34s acc %s  doc %s  filed %s  period %s  bytes %d"
          % (tk, cik, name, acc, doc, date, rep, os.path.getsize(out)))
