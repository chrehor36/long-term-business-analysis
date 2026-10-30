# fetch an EDGAR document and strip it to text into cache/ (raw stays gitignored)
import sys, re, html, urllib.request, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def get(cik, acc, doc, name):
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    out = os.path.join("cache", name + ".txt")
    if os.path.exists(out): return out
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read().decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    open(out, "w", encoding="utf-8").write(t)
    return out
if __name__ == "__main__":
    print(get(*sys.argv[1:5]))
