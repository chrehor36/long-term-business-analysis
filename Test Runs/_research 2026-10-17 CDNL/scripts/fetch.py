# fetch an EDGAR document and write a plain-text copy beside it (cache/)
import sys, re, html, urllib.request, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e:
            print("retry", e); time.sleep(3)
    raise SystemExit("failed " + url)
def totext(b):
    s = b.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
cik, acc, doc, name, outdir = sys.argv[1:6]
url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
b = get(url)
open(os.path.join(outdir, name + ".htm"), "wb").write(b)
open(os.path.join(outdir, name + ".txt"), "w", encoding="utf-8").write(totext(b))
print(name, len(b))
