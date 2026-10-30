"""Fetch an EDGAR URL to cache/ and optionally strip to text. Usage: python -I fetch.py URL OUTNAME [--text]"""
import sys, urllib.request, re, html, os, gzip, time
UA = "Chris Hrehor chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
url, name = sys.argv[1], sys.argv[2]
out = os.path.join(here, "cache", name)
if not os.path.exists(out):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            break
        except Exception as e:
            print("retry", e); time.sleep(2)
    open(out, "wb").write(data)
if "--text" in sys.argv:
    raw = open(out, "rb").read().decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", raw)
    raw = re.sub(r"(?i)</td>|</th>", " | ", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw).replace("\xa0", " ")
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r"\n\s*\n+", "\n", raw)
    open(out + ".txt", "w", encoding="utf-8").write(raw)
    print("text chars", len(raw), out + ".txt")
else:
    print("bytes", os.path.getsize(out), out)
