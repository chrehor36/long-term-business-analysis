"""Fetch an SEC URL to the cache folder, then write a plain-text copy. Usage: fetch.py URL NAME"""
import sys, urllib.request, re, html, os, time, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
url, name = sys.argv[1], sys.argv[2]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cache")
req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
for i in range(5):
    try:
        r = urllib.request.urlopen(req, timeout=60); data = r.read()
        if r.headers.get("Content-Encoding") == "gzip": data = gzip.decompress(data)
        break
    except Exception as e:
        print("retry", e); time.sleep(3)
open(os.path.join(out, name), "wb").write(data)
if name.endswith((".htm", ".html")):
    t = data.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(os.path.join(out, name.rsplit(".",1)[0] + ".txt.cache"), "w", encoding="utf-8").write(t)
print("ok", name, len(data))
