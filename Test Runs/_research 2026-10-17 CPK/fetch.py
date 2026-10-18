import sys, re, html, urllib.request, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = urllib.request.urlopen(req, timeout=120).read()
    open(out + ".htm", "wb").write(data)
    t = data.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(out + ".txt", "w", encoding="utf-8").write(t)
    print(out, len(t))
    time.sleep(0.3)
cik = "19745"
for line in sys.argv[1:]:
    acc, doc, name = line.split(",")
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    get(url, os.path.join("cache", name))
