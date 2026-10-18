import sys, os, re, time, urllib.request, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = "886835"
def get(url, path):
    if os.path.exists(path): return open(path, "rb").read()
    req = urllib.request.Request(url, headers=UA)
    b = urllib.request.urlopen(req, timeout=60).read()
    open(path, "wb").write(b); time.sleep(0.3); return b
def strip(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    return t
for arg in sys.argv[1:]:
    accn, doc, name = arg.split("|")
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{accn.replace('-','')}/{doc}"
    b = get(url, os.path.join("cache", name + ".htm"))
    open(os.path.join("cache", name + ".txt"), "w", encoding="utf-8").write(strip(b))
    print(name, len(b))
