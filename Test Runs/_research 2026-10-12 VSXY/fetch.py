"""Fetch an EDGAR document and save as text (cache/). Usage: python fetch.py ACCESSION PRIMARYDOC NAME"""
import sys, re, urllib.request, html, os
acc, doc, name = sys.argv[1], sys.argv[2], sys.argv[3]
cik = "1856437" if len(sys.argv) < 5 else sys.argv[4]
url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
req = urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"})
raw = urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
t = re.sub(r"(?i)</td>", " | ", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
out = os.path.join(os.path.dirname(__file__), "cache", name + ".txt")
open(out, "w", encoding="utf-8").write(f"SOURCE {url}\nACCESSION {acc}\n" + t)
print(out, len(t))
