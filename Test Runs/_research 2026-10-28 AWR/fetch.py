"""Fetch SEC documents into cache/ and strip to text. Usage: fetch.py URL OUTNAME"""
import sys, os, re, time, html, urllib.request, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(here, "cache")
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    time.sleep(0.2)
    return data
def strip(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    url, name = sys.argv[1], sys.argv[2]
    raw = get(url)
    p = os.path.join(cache, name)
    if name.endswith(".json"):
        open(p, "wb").write(raw)
    else:
        open(p, "w", encoding="utf-8").write(strip(raw))
    print(p, len(raw))
