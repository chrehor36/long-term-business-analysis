# fetch an EDGAR document and strip to text; usage: python -I fetch.py URL OUTNAME
import sys, urllib.request, re, html, time, os
url, out = sys.argv[1], sys.argv[2]
req = urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"})
for i in range(5):
    try:
        raw = urllib.request.urlopen(req, timeout=120).read(); break
    except Exception as e:
        print("retry", e); time.sleep(3)
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
open(os.path.join(d, out + ".htm"), "wb").write(raw)
t = raw.decode("utf-8", "ignore")
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
t = re.sub(r"(?i)</td>", " | ", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(os.path.join(d, out + ".txt"), "w", encoding="utf-8").write(t)
print(out, len(t))
