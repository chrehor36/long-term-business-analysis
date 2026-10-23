"""Fetch EDGAR documents for the EIX run into cache/ and strip them to text. Usage: fetch.py URL NAME"""
import sys, os, re, time, urllib.request, gzip, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url):
    for i in range(5):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
            b = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                b = gzip.decompress(b)
            return b
        except Exception as e:
            print("retry", i, e); time.sleep(2 + i * 3)
    raise SystemExit("failed " + url)
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
    url, name = sys.argv[1], sys.argv[2]
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
    b = get(url)
    raw = os.path.join(d, name + (".json" if url.endswith(".json") else ".htm"))
    open(raw, "wb").write(b)
    if not url.endswith(".json"):
        open(os.path.join(d, name + ".txt"), "w", encoding="utf-8").write(strip(b))
    print("ok", name, len(b))
