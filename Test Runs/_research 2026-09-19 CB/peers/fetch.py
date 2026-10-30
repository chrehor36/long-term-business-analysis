#!/usr/bin/env python3
"""Fetch SEC primary documents for the insurance peer row, strip to text.

Usage:
  python fetch.py list CIK            -- list 10-K / 40-F filings (form, date, accession, primary doc)
  python fetch.py doc CIK ACCESSION DOCNAME OUTNAME   -- fetch and strip one document
  python fetch.py index CIK ACCESSION  -- list every file in a filing

Everything lands in this directory. Fetch only, no judgment (operator rule 8).
"""
import sys, os, json, re, html
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources

HERE = os.path.dirname(os.path.abspath(__file__))


def subs(cik):
    c = f"{int(cik):010d}"
    txt = sources._get(f"https://data.sec.gov/submissions/CIK{c}.json",
                       headers=sources.SEC_UA, cache_name=f"sub_{c}.json", max_age_h=24 * 7)
    return json.loads(txt)


def cmd_list(cik):
    d = subs(cik)
    print(d.get("name"), "CIK", cik)
    r = d["filings"]["recent"]
    for i, f in enumerate(r["form"]):
        if f in ("10-K", "40-F", "10-K/A", "40-F/A"):
            print(f"{f:8s} {r['filingDate'][i]}  {r['accessionNumber'][i]}  {r['primaryDocument'][i]}  rptdate={r.get('reportDate',[''])[i]}")


def strip(h):
    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?is)<br[^>]*>", "\n", h)
    h = re.sub(r"(?is)</(tr|p|div|h\d|table)>", "\n", h)
    h = re.sub(r"(?is)</t[dh]>", " | ", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = html.unescape(h)
    h = h.replace("\u00a0", " ").replace("\u2019", "'").replace("\u2014", "--")
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r"\n[ \t]*\|?[ \t]*(\|[ \t]*)*\n", "\n", h)
    h = re.sub(r"\n{3,}", "\n\n", h)
    return h


def cmd_index(cik, acc):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{acc}-index.htm"
    txt = sources._get(url, headers=sources.SEC_UA, cache_name=f"idx_{acc}.html", max_age_h=24 * 30)
    t = strip(txt)
    print(t[:6000])


def cmd_doc(cik, acc, doc, out):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}"
    raw = sources._get(url, headers=sources.SEC_UA, cache_name=f"raw_{acc}_{doc}", max_age_h=24 * 90)
    t = strip(raw)
    p = os.path.join(HERE, out)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(t)
    print(f"wrote {p}  {len(t)} chars  from {url}")


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "list":
        cmd_list(sys.argv[2])
    elif c == "index":
        cmd_index(sys.argv[2], sys.argv[3])
    elif c == "doc":
        cmd_doc(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
