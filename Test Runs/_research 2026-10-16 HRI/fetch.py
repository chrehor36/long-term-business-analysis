"""Fetch an EDGAR document into cache/ and write a plain-text copy (cache/, gitignored if large)."""
import sys, re, html, urllib.request, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
def fetch(acc, doc, name, cik="1364479"):
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    out = os.path.join("cache", name)
    if not os.path.exists(out + ".htm"):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        data = urllib.request.urlopen(req).read()
        open(out + ".htm", "wb").write(data)
        time.sleep(0.3)
    raw = open(out + ".htm", "rb").read().decode("utf-8", "ignore")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<ix:header>.*?</ix:header>", " ", raw, flags=re.S)
    raw = re.sub(r"(?i)</(p|div|tr|br|h\d|li|table)>", "\n", raw)
    raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
    raw = re.sub(r"(?i)</t[dh]>", " | ", raw)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    txt = re.sub(r"[ \t\xa0]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt)
    open(out + ".txt", "w", encoding="utf-8").write(txt)
    print(name, len(txt))
if __name__ == "__main__":
    a = sys.argv[1:]
    fetch(a[0], a[1], a[2], *(a[3:4]))
