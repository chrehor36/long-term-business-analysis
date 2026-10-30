"""Fetch the STANDARD-LINES peers' own 10-Ks for the TRV competitor row.

These are the peers TRV actually competes with, as against the specialty and E&S
writers carried in the MKL/CB row: personal auto and homeowners (PGR, ALL) and
standard commercial (CB, WRB, HIG, CNA, CINF).

Every cell in the row is read from the filer's own Form 10-K text on EDGAR.
XBRL is used for nothing here.
"""
import json, os, re, html, sys, time, urllib.request

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
OUT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(OUT, "std")
os.makedirs(RAW, exist_ok=True)

CIK = {"PGR": "0000080661", "ALL": "0000899051", "HIG": "0000874766",
       "CINF": "0000020286", "CNA": "0000021175", "WRB": "0000011544"}


def get(u):
    time.sleep(0.25)
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=180).read()


def totext(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?is)</(tr|p|div|table|h[1-6]|li)>", "\n", t)
    t = re.sub(r"(?is)</t[dh]>", " | ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r" *\n *", "\n", t)
    return re.sub(r"\n{3,}", "\n\n", t)


def main():
    for tic, cik in CIK.items():
        subs = json.loads(get("https://data.sec.gov/submissions/CIK%s.json" % cik))
        r = subs["filings"]["recent"]
        rows = [(f, d, a, p, rd) for f, d, a, p, rd
                in zip(r["form"], r["filingDate"], r["accessionNumber"],
                       r["primaryDocument"], r["reportDate"]) if f == "10-K"]
        for want in ("2025-12-31", "2023-12-31"):
            hit = [x for x in rows if x[4] == want]
            if not hit:
                print(tic, want, "NOT IN RECENT")
                continue
            f, d, a, p, rd = hit[0]
            dest = os.path.join(RAW, "%s_10K_%s.txt" % (tic, rd[:4]))
            url = ("https://www.sec.gov/Archives/edgar/data/%d/%s/%s"
                   % (int(cik), a.replace("-", ""), p))
            if not os.path.exists(dest):
                open(dest, "w", encoding="utf-8").write(totext(get(url)))
            print("%-5s %s acc %s filed %s  doc %s  -> %s"
                  % (tic, rd, a, d, p, os.path.basename(dest)))


if __name__ == "__main__":
    main()
