import sys, os, re, time, urllib.request, html
UA = "Chris Hrehor chrehor36@gmail.com"
CIK = "1084991"
def get(acc, doc, out):
    p = os.path.join("cache", out)
    if os.path.exists(p): return p
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = urllib.request.urlopen(req, timeout=60).read()
    open(p, "wb").write(data); time.sleep(0.3)
    return p
def totext(p):
    raw = open(p, "rb").read().decode("utf-8", "ignore")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", raw)
    raw = re.sub(r"(?i)</td>|</th>", " | ", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    t = html.unescape(raw)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    tp = p.rsplit(".",1)[0] + ".txt"
    open(tp, "w", encoding="utf-8").write(t)
    return tp
if __name__ == "__main__":
    for line in open(sys.argv[1]):
        line=line.strip()
        if not line or line.startswith("#"): continue
        acc, doc, out = line.split()
        p = get(acc, doc, out); print(totext(p), os.path.getsize(p))
