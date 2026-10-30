"""Fetch an EDGAR URL into cache/ and optionally strip HTML to text. Usage: fetch.py URL NAME"""
import sys, os, re, time, html, urllib.request, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(here, "cache")
url, name = sys.argv[1], sys.argv[2]
out = os.path.join(cache, name)
if not os.path.exists(out):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            break
        except Exception as e:
            print("retry", e); time.sleep(2)
    else:
        sys.exit("failed")
    open(out, "wb").write(data)
    time.sleep(0.3)
if name.endswith((".htm", ".html")):
    t = open(out, "rb").read().decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(out + ".txt", "w", encoding="utf-8").write(t)
print(out)
