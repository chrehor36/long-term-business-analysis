"""Download each peer bank's FY2025 and FY2023 10-K primary document as text.

The competitor row is built from each filer's OWN reported ROTCE, efficiency ratio, net
interest margin and cost of deposits (operator rule 4: no name reaches a verdict on XBRL
alone; [E3-28] requires the same metric, same window, FILING-sourced). Two 10-Ks per peer
covers 2021-2025 because each carries three income-statement years and, for most, a
five-year or multi-year ratio discussion.
"""
import sys, os, re, json, urllib.request, html, time

sys.path.insert(0, os.path.join("C:/Users/chreh/OneDrive/Documents/BRK", "tools"))
import sources
from fetch2 import totext

D = os.path.dirname(os.path.abspath(__file__))
PEERS = ["PNC", "USB", "FITB", "KEY", "RF", "CFG", "MTB", "HBAN"]


def get(url):
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    return urllib.request.urlopen(req).read()


def tenks(cik):
    j = json.loads(get("https://data.sec.gov/submissions/CIK%s.json" % cik).decode())
    r = j["filings"]["recent"]
    out = []
    for f, fd, rd, acc, doc in zip(r["form"], r["filingDate"], r["reportDate"],
                                   r["accessionNumber"], r["primaryDocument"]):
        if f == "10-K":
            out.append((rd, fd, acc, doc))
    return j.get("name"), out


if __name__ == "__main__":
    meta = {}
    for t in PEERS:
        cik, nm = sources.cik_for(t)
        name, ks = tenks(cik)
        meta[t] = {"cik": cik, "name": name, "tenks": ks[:6]}
        print(t, cik, name)
        for rd, fd, acc, doc in ks:
            if not (rd.startswith("2025") or rd.startswith("2023")):
                continue
            out = os.path.join(D, "peer_%s_%s.txt" % (t, rd[:4]))
            if os.path.exists(out) and os.path.getsize(out) > 50000:
                print("  have", os.path.basename(out))
                continue
            url = "https://www.sec.gov/Archives/edgar/data/%s/%s/%s" % (
                cik.lstrip("0"), acc.replace("-", ""), doc)
            try:
                raw = get(url)
            except Exception as e:
                print("  FAIL", t, rd, e, url)
                continue
            open(out, "w", encoding="utf-8").write(totext(raw))
            print("  wrote", os.path.basename(out), len(raw), acc)
            time.sleep(0.3)
    json.dump(meta, open(os.path.join(D, "peer_meta.json"), "w"), indent=1)
