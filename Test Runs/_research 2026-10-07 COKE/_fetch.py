# Fetch an EDGAR document and strip it to text in cache/. Usage: python _fetch.py CIK ACCESSION DOC OUTNAME
import sys, re, html, os, time, urllib.request
cik, acc, doc, out = sys.argv[1:5]
url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
req = urllib.request.Request(url, headers={'User-Agent': 'Chris Hrehor chrehor36@gmail.com'})
raw = urllib.request.urlopen(req, timeout=120).read().decode('utf-8', errors='replace')
t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', raw)
t = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', t)
t = re.sub(r'(?i)</td>|</th>', ' | ', t)
t = re.sub(r'<[^>]+>', ' ', t)
t = html.unescape(t).replace('\xa0', ' ')
t = re.sub(r'[ \t]+', ' ', t)
t = re.sub(r'\n\s*\n+', '\n', t)
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
open(os.path.join(d, out), 'w', encoding='utf-8').write(t)
print(out, len(t), url)
time.sleep(0.3)
