"""Fetch helper for the TPC run. Transcription only: downloads SEC documents and strips HTML to text.
Usage:
  python fetch.py list CIK [forms...]        -> lists filings (form, date, accession, primary doc)
  python fetch.py doc URL OUTNAME            -> saves stripped text to OUTNAME
  python fetch.py facts CIK OUTNAME          -> saves companyfacts json
"""
import sys, json, re, time, html, urllib.request, os

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
HERE = os.path.dirname(os.path.abspath(__file__))


def get(url, tries=4):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(2 + 2 * i)


def strip(b):
    t = b.decode("utf-8", errors="replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>", "\n", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t)
    t = t.replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t


def main():
    cmd = sys.argv[1]
    if cmd == "list":
        cik = int(sys.argv[2])
        forms = set(sys.argv[3:])
        d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
        rows = []
        def add(r):
            for f, dt, acc, doc, rd in zip(r["form"], r["filingDate"], r["accessionNumber"], r["primaryDocument"], r["reportDate"]):
                if not forms or f in forms:
                    rows.append((dt, f, acc, doc, rd))
        add(d["filings"]["recent"])
        for extra in d["filings"].get("files", []):
            add(json.loads(get("https://data.sec.gov/submissions/" + extra["name"])))
        for r in sorted(rows):
            print(*r, sep=" | ")
    elif cmd == "doc":
        url, out = sys.argv[2], sys.argv[3]
        b = get(url)
        txt = strip(b) if url.lower().endswith((".htm", ".html")) else b.decode("utf-8", errors="replace")
        with open(os.path.join(HERE, out), "w", encoding="utf-8") as f:
            f.write(txt)
        print(out, len(txt))
    elif cmd == "facts":
        cik = int(sys.argv[2])
        b = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")
        with open(os.path.join(HERE, sys.argv[3]), "wb") as f:
            f.write(b)
        print(sys.argv[3], len(b))


if __name__ == "__main__":
    main()
