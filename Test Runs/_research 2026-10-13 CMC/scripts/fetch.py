"""Fetch an EDGAR document and save HTML-to-text into cache/. Usage: fetch.py CIK ACCESSION DOC OUTNAME"""
import sys, re, html, urllib.request, os
cik, acc, doc, out = sys.argv[1:5]
url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
req = urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"})
raw = urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")
base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
os.makedirs(base, exist_ok=True)
if doc.endswith(('.htm', '.html')):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
else:
    t = raw
open(os.path.join(base, out), "w", encoding="utf-8").write(f"SOURCE {url}\n" + t)
print(out, len(t))
