"""Fetch an EDGAR document and save raw + text into cache/. Usage: fetch.py ACCESSION DOC NAME"""
import sys, re, html, time, urllib.request, os
CIK = os.environ.get("CIK", "1141197")
acc, doc, name = sys.argv[1], sys.argv[2], sys.argv[3]
url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
req = urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com"})
raw = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
os.makedirs("cache", exist_ok=True)
open(f"cache/{name}.htm", "w", encoding="utf-8").write(raw)
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
t = re.sub(r"(?i)</td>", " | ", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t)
t = re.sub(r"[ \t\xa0]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(f"cache/{name}.txt", "w", encoding="utf-8").write(t)
print(name, url, len(t))
time.sleep(0.3)
