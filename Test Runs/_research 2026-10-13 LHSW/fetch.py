import sys, os, re, time, html, urllib.request
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = "2004024"
def get(acc, doc, out):
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
    req = urllib.request.Request(url, headers=UA)
    raw = urllib.request.urlopen(req, timeout=120).read()
    with open(out + ".htm", "wb") as f: f.write(raw)
    t = raw.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    with open(out + ".txt", "w", encoding="utf-8") as f: f.write(t)
    print(out, len(raw), len(t))
for a in sys.argv[1:]:
    acc, doc, out = a.split(",")
    get(acc, doc, os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", out))
    time.sleep(0.3)
