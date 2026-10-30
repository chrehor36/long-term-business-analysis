# fetch an EDGAR document and save html + text into cache/
import sys, re, html, urllib.request, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
def fetch(url, out):
    p = os.path.join("cache", out)
    if not os.path.exists(p + ".htm"):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
        data = urllib.request.urlopen(req).read()
        open(p + ".htm", "wb").write(data); time.sleep(0.3)
    raw = open(p + ".htm", "rb").read().decode("utf-8", "ignore")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", raw)
    raw = re.sub(r"(?i)</td>", " | ", raw)
    t = html.unescape(re.sub(r"<[^>]+>", "", raw))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(p + ".txt", "w", encoding="utf-8").write(t)
    print(out, len(t))
for arg in sys.argv[1:]:
    url, out = arg.split("=>")
    fetch(url, out)
