"""Fetch an EDGAR document and save HTML plus a plain-text version into cache/."""
import sys, re, html, urllib.request, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
def fetch(url, name):
    os.makedirs("cache", exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    data = urllib.request.urlopen(req, timeout=60).read()
    open(os.path.join("cache", name + ".htm"), "wb").write(data)
    t = data.decode("utf-8", errors="replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(os.path.join("cache", name + ".txt"), "w", encoding="utf-8").write(t)
    print(name, len(t))
    time.sleep(0.3)
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        acc, doc, name = arg.split(",")
        cik = "1320854"
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
        fetch(url, name)
