"""Fetch EDGAR documents into cache/edgar (gitignored). Usage: fetch.py URL [outname]"""
import sys, urllib.request, gzip, os, re, html
UA = "Chris Hrehor chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "cache", "edgar")
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    return data
def strip(b):
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    url = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else url.rsplit("/", 1)[-1]
    data = get(url)
    p = os.path.join(out, name)
    if name.endswith(".txt") and not url.endswith(".txt"):
        open(p, "w", encoding="utf-8").write(strip(data))
    else:
        open(p, "wb").write(data)
    print(p, len(data))
