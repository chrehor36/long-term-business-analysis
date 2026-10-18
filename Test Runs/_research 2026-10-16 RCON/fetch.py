"""Fetch an EDGAR document and save raw + plain text into cache/. Usage: python fetch.py ACCESSION PRIMARYDOC NAME"""
import sys, re, html, urllib.request, os
acc, doc, name = sys.argv[1], sys.argv[2], sys.argv[3]
url = f"https://www.sec.gov/Archives/edgar/data/1442620/{acc.replace('-','')}/{doc}"
req = urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com"})
raw = urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")
os.makedirs("cache", exist_ok=True)
open(f"cache/{name}.htm", "w", encoding="utf-8").write(raw)
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
t = re.sub(r"(?i)</td>", " | ", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(f"cache/{name}.txt", "w", encoding="utf-8").write(t)
print(name, len(t), url)
