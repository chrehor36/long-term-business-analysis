"""Fetch an EDGAR document and save HTML + plain text under cache/. Usage: fetch.py CIK ACCESSION DOC [name]"""
import sys, re, os, html, urllib.request, time
UA = "Chris Hrehor chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(here, "cache"); os.makedirs(cache, exist_ok=True)
def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            print("retry", e); time.sleep(2)
    raise SystemExit("failed " + url)
def totext(b):
    s = b.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    cik, acc, doc = sys.argv[1], sys.argv[2], sys.argv[3]
    name = sys.argv[4] if len(sys.argv) > 4 else doc
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    b = get(url)
    open(os.path.join(cache, name), "wb").write(b)
    t = totext(b) if doc.lower().endswith((".htm", ".html")) else b.decode("utf-8", "replace")
    open(os.path.join(cache, name + ".txt"), "w", encoding="utf-8").write(t)
    print(name, len(b), "bytes;", len(t.splitlines()), "lines")
