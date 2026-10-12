# fetch an EDGAR URL to cache/, strip HTML to text as well. usage: fetch.py URL NAME
import sys, os, re, time, html, urllib.request
UA = "Chris Hrehor chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(here, "cache")
url, name = sys.argv[1], sys.argv[2]
out = os.path.join(cache, name)
if not os.path.exists(out):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    for i in range(5):
        try:
            data = urllib.request.urlopen(req, timeout=60).read(); break
        except Exception as e:
            print("retry", e); time.sleep(2)
    open(out, "wb").write(data)
    time.sleep(0.3)
raw = open(out, "rb").read().decode("utf-8", "replace")
if name.endswith((".htm", ".html")):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    open(out + ".txt", "w", encoding="utf-8").write(t)
    print(out + ".txt", len(t))
else:
    print(out, len(raw))
