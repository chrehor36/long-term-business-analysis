import urllib.request, re, html, os, time, sys
UA = "Chris Hrehor chrehor36@gmail.com"
docs = [l.split() for l in sys.argv[1:]]
def strip(t):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t)
for name, cik, acc, doc in docs:
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read().decode("utf-8","replace")
    open(f"cache/{name}.txt","w",encoding="utf-8").write(strip(raw)); print("ok",name,len(raw)); time.sleep(0.5)
