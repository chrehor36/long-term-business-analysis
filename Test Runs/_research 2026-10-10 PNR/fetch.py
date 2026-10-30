"""Fetch an EDGAR document and save raw + stripped text under cache/. Usage: python fetch.py ACCESSION DOC NAME [CIK]"""
import sys, re, html, urllib.request, gzip, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
            r = urllib.request.urlopen(req, timeout=60).read()
            try: r = gzip.decompress(r)
            except Exception: pass
            return r
        except Exception as e:
            print("retry", e); time.sleep(2)
    raise SystemExit("failed " + url)
def strip(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    acc, doc, name = sys.argv[1:4]
    cik = sys.argv[4] if len(sys.argv) > 4 else "77360"
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    b = get(url)
    os.makedirs("cache", exist_ok=True)
    open(f"cache/{name}.txt", "w", encoding="utf-8").write(strip(b))
    print(name, len(b), url)
