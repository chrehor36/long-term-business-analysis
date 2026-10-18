"""Fetch EDGAR documents to cache/ and write a plain-text copy. Usage: fetch.py ACCESSION PRIMARYDOC NAME"""
import sys, os, re, html, time, urllib.request
UA = "Chris Hrehor chrehor36@gmail.com"
CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    for i in range(4):
        try:
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            print("retry", e); time.sleep(3)
    raise SystemExit("failed " + url)
def totext(b):
    s = b.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
acc, doc, name = sys.argv[1:4]
url = f"https://www.sec.gov/Archives/edgar/data/1899658/{acc.replace('-','')}/{doc}"
b = get(url)
open(os.path.join(CACHE, name + ".htm"), "wb").write(b)
open(os.path.join(CACHE, name + ".txt"), "w", encoding="utf-8").write(totext(b))
print(name, len(b), url)
