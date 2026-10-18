"""Fetch an EDGAR document and strip it to text in cache/. Usage: fetch.py ACCESSION DOC NAME"""
import sys, re, html, urllib.request, os
acc, doc, name = sys.argv[1], sys.argv[2], sys.argv[3]
cik = "1969863"
url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
req = urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"})
raw = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
here = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(here, "cache", name + ".htm"), "w", encoding="utf-8").write(raw)
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
t = re.sub(r"(?i)</td>|</th>", " | ", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(os.path.join(here, "cache", name + ".txt"), "w", encoding="utf-8").write(t)
print(name, len(t), url)
