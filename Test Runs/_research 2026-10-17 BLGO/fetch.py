# fetch an EDGAR document and save html + plain text into cache/
import sys, re, html, urllib.request, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
def get(acc, doc, name):
    url = f"https://www.sec.gov/Archives/edgar/data/880242/{acc.replace('-','')}/{doc}"
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", name)
    if not os.path.exists(out + ".txt"):
        raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read().decode("utf-8", "replace")
        t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
        t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
        t = re.sub(r"(?i)</td>", " | ", t)
        t = re.sub(r"<[^>]+>", " ", t)
        t = html.unescape(t).replace("\xa0", " ")
        t = re.sub(r"[ \t]+", " ", t)
        t = re.sub(r"\n\s*\n+", "\n", t)
        open(out + ".txt", "w", encoding="utf-8").write(t)
        time.sleep(0.3)
    print(name, os.path.getsize(out + ".txt"))
for line in sys.argv[1:]:
    acc, doc, name = line.split(",")
    get(acc, doc, name)
