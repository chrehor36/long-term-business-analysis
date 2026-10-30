"""Fetch an EDGAR document and write plain text into cache/. Usage: fetch.py ACCESSION PRIMARYDOC OUTNAME"""
import sys, re, html, time, urllib.request, os
UA = "Chris Hrehor chrehor36@gmail.com"
import os
CIK = os.environ.get("CIK","1650729")
def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            time.sleep(2 + i * 2)
    raise SystemExit("failed " + url)
def to_text(b):
    s = b.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)
    s = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    acc, doc, out = sys.argv[1], sys.argv[2], sys.argv[3]
    outdir = sys.argv[4] if len(sys.argv) > 4 else "cache"
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
    t = to_text(get(url))
    open(os.path.join(outdir, out), "w", encoding="utf-8").write(f"SOURCE {url}\nACCESSION {acc}\n" + t)
    print(out, len(t))
