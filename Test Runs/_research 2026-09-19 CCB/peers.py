"""CCB competitor row - fetch each peer's latest 10-K primary document and grep it.

The row must be same metric, same window, filing-sourced [E3-28]. XBRL is transcription
only [E3-27], so the metric is read out of the filed document, not computed from tags.
"""
import sys, os, re, json, urllib.request, html, time

sys.path.insert(0, "C:/Users/chreh/OneDrive/Documents/BRK/tools")
import sources

D = os.path.dirname(os.path.abspath(__file__))
PEERS = {
    "TBBK": "0001295401",   # The Bancorp - the closest BaaS sponsor comparable
    "CASH": "0000907471",   # Pathward Financial - BaaS / partner solutions
    "CUBI": "0001488813",   # Customers Bancorp - digital/partner deposits
    "GDOT": "0001386278",   # Green Dot - BaaS + own programs
    "MCB":  "0001476034",   # Metropolitan Bank - exited BaaS/crypto by order
    "LOB":  "0001462120",   # Live Oak - digital SBA lender
    "HFWA": "0001046025",   # Heritage Financial - WA community bank
    "TSBK": "0001046050",   # Timberland Bancorp - WA community bank
    "COLB": "0000887343",   # Columbia Banking System - PNW
    "SOFI": "0001818874",   # SoFi - bank holding company, wave 6
}
PATS = [
    r"net interest margin[^|\n]{0,120}",
    r"cost of deposits[^|\n]{0,120}",
    r"total cost of deposits[^|\n]{0,120}",
    r"return on average (?:common )?equity[^|\n]{0,120}",
    r"consent order[^|\n]{0,200}",
    r"BaaS|banking[- ]as[- ]a[- ]service|fintech program|partner bank",
    r"Coastal Community Bank|Coastal Financial",
]


def get(url):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers=sources.SEC_UA)).read()


def totext(raw):
    s = raw.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style|ix:header)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)</(p|div|tr|table|h[1-6]|li)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s).replace("\u00a0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    return re.sub(r"\n[ \t]*\n+", "\n", s)


def latest_10k(cik):
    j = json.loads(get("https://data.sec.gov/submissions/CIK%s.json" % cik).decode())
    r = j["filings"]["recent"]
    for form, fd, rd, acc, doc in zip(r["form"], r["filingDate"], r["reportDate"],
                                      r["accessionNumber"], r["primaryDocument"]):
        if form == "10-K":
            return j["name"], fd, rd, acc, doc
    return j["name"], None, None, None, None


if __name__ == "__main__":
    out = open(os.path.join(D, "peers_row.txt"), "w", encoding="utf-8")
    for t, cik in PEERS.items():
        name, fd, rd, acc, doc = latest_10k(cik)
        print("=" * 70, file=out)
        print("%s  %s  CIK %s  10-K filed %s for %s  acc %s  doc %s"
              % (t, name, cik, fd, rd, acc, doc), file=out)
        path = os.path.join(D, "peer_%s.txt" % t)
        if not (os.path.exists(path) and os.path.getsize(path) > 1000):
            raw = get("https://www.sec.gov/Archives/edgar/data/%s/%s/%s"
                      % (cik.lstrip("0"), acc.replace("-", ""), doc))
            open(path, "w", encoding="utf-8").write(totext(raw))
            time.sleep(0.3)
        txt = open(path, encoding="utf-8").read()
        for p in PATS:
            hits = re.findall("(?i)" + p, txt)
            print("  [%s] n=%d" % (p[:40], len(hits)), file=out)
            for h in hits[:4]:
                print("      ", h.strip()[:200], file=out)
        print(t, "done")
    out.close()
