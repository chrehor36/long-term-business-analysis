import sys, os, re, time, html, urllib.request
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = __import__("os").environ.get("CIK","1788348")
def fetch(acc, doc, out):
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
    rawp = out + ".htm"
    if not os.path.exists(rawp):
        req = urllib.request.Request(url, headers=UA)
        data = urllib.request.urlopen(req, timeout=120).read()
        open(rawp, "wb").write(data)
        time.sleep(0.3)
    t = open(rawp, "rb").read().decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(out + ".txt", "w", encoding="utf-8").write(t)
    print(out, len(t))
if __name__ == "__main__":
    for line in sys.argv[1:]:
        acc, doc, out = line.split(",")
        fetch(acc, doc, out)
