import sys, os, re, time, urllib.request, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def get(url, out):
    if os.path.exists(out): return out
    req = urllib.request.Request(url, headers=UA)
    data = urllib.request.urlopen(req, timeout=60).read()
    open(out, "wb").write(data); time.sleep(0.3); return out
def to_text(path):
    raw = open(path, "rb").read().decode("utf-8", "ignore")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", raw)
    raw = re.sub(r"(?i)</td>|</th>", " | ", raw)
    raw = re.sub(r"(?s)<[^>]+>", "", raw)
    raw = html.unescape(raw).replace("\xa0", " ")
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r"\n\s*\n+", "\n", raw)
    return raw
if __name__ == "__main__":
    cik, acc, doc, name = sys.argv[1:5]
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    p = get(url, os.path.join("cache", name + ".htm"))
    open(os.path.join("cache", name + ".txt"), "w", encoding="utf-8").write(to_text(p))
    print(name, os.path.getsize(p))
