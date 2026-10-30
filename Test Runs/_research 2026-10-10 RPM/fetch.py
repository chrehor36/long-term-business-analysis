"""Fetch an EDGAR document and save it as text under cache/. Usage: python fetch.py CIK ACCESSION DOC OUTNAME"""
import sys, re, html, time, urllib.request, gzip, os
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
            r = urllib.request.urlopen(req, timeout=60)
            b = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                b = gzip.decompress(b)
            return b.decode("utf-8", "replace")
        except Exception as e:
            print("retry", e); time.sleep(2 + i * 2)
    raise SystemExit("failed " + url)
def totext(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", h)
    h = re.sub(r"(?i)</td>|</th>", " | ", h)
    h = re.sub(r"(?s)<[^>]+>", "", h)
    h = html.unescape(h).replace("\xa0", " ")
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h
if __name__ == "__main__":
    cik, acc, doc, out = sys.argv[1:5]
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    t = totext(get(url))
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
    open(os.path.join(d, out), "w", encoding="utf-8").write(f"SOURCE {url}\n" + t)
    print(out, len(t))
