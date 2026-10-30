import sys, urllib.request, re, html, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
def fetch(url, out):
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        return
    req = urllib.request.Request(url, headers=UA)
    data = urllib.request.urlopen(req, timeout=60).read()
    open(out, "wb").write(data)
    time.sleep(0.3)
def totext(src, dst):
    s = open(src, encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<ix:header>.*?</ix:header>", " ", s, flags=re.S)
    s = re.sub(r"(?i)</(p|div|tr|br|h\d|li|table)>", "\n", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    open(dst, "w", encoding="utf-8").write(s)
if __name__ == "__main__":
    cik, acc, doc, name = sys.argv[1:5]
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    out = os.path.join("cache", name + ".htm")
    fetch(url, out)
    totext(out, os.path.join("cache", name + ".txt"))
    print(name, os.path.getsize(os.path.join("cache", name + ".txt")))
