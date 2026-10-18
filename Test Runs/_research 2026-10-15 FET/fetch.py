"""Fetch an EDGAR URL into cache/ and optionally strip to text. Usage: python -I fetch.py URL outname"""
import sys, time, urllib.request, gzip, re, html, os
UA = "Chris Hrehor chrehor36@gmail.com"
url, out = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
dest = os.path.join(here, "cache", out)
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
    sys.exit(1)
open(dest, "wb").write(data)
if out.endswith(".txt.src"):
    pass
if len(sys.argv) > 3 and sys.argv[3] == "strip":
    t = data.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(dest + ".txt", "w", encoding="utf-8").write(t)
    print(dest + ".txt", len(t))
else:
    print(dest, len(data))
