# Fetch SEC primary documents and save as plain text (transcription only).
import sys, os, re, html, time, urllib.request
OUT = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def fetch(cik, accn, doc, name):
    p = os.path.join(OUT, name + ".txt")
    if os.path.exists(p): return p
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn.replace('-','')}/{doc}"
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode("utf-8","replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(p, "w", encoding="utf-8").write(f"SOURCE {url}\nACCESSION {accn}\n" + t)
    time.sleep(0.3)
    return p
if __name__ == "__main__":
    for line in open(sys.argv[1]):
        line=line.strip()
        if not line or line.startswith("#"): continue
        cik, accn, doc, name = line.split()
        try: print(fetch(cik, accn, doc, name))
        except Exception as e: print("FAIL", name, e)
