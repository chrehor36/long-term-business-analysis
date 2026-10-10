"""Fetch an EDGAR document and save HTML-stripped text under cache/. Usage: fetch.py CIK ACCESSION DOC OUTNAME"""
import sys, os, re, html, urllib.request, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e:
            time.sleep(2); err = e
    raise err
def text(b):
    s = b.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<ix:header>.*?</ix:header>", " ", s, flags=re.S)
    s = re.sub(r"(?i)</(p|div|tr|br|h\d|li)>|<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    cik, acc, doc, out = sys.argv[1:5]
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache"); os.makedirs(d, exist_ok=True)
    t = text(get(url)); open(os.path.join(d, out), "w", encoding="utf-8").write(t)
    print(out, len(t), url)
