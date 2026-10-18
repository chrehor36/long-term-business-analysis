# fetch an EDGAR primary doc and strip to text into cache/
import sys, re, html, urllib.request, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e:
            print("retry", e); time.sleep(3)
    raise SystemExit("fail " + url)
def strip(b):
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
for arg in sys.argv[1:]:
    name, accn, doc = arg.split(",")
    url = f"https://www.sec.gov/Archives/edgar/data/1582244/{accn.replace('-','')}/{doc}"
    b = get(url)
    open(os.path.join("cache", name + ".txt"), "w", encoding="utf-8").write(strip(b))
    print(name, len(b)); time.sleep(0.5)
