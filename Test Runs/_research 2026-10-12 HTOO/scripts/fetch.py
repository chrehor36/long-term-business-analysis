"""Fetch an EDGAR document and strip it to text. Usage: fetch.py URL OUTNAME (written into ../cache)."""
import sys, re, html, urllib.request, os, time
url, out = sys.argv[1], sys.argv[2]
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'cache')
req = urllib.request.Request(url, headers={'User-Agent': 'Chris Hrehor chrehor36@gmail.com', 'Accept-Encoding': 'identity'})
raw = urllib.request.urlopen(req, timeout=120).read().decode('utf-8', 'replace')
t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', raw)
t = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>', '\n', t)
t = re.sub(r'(?i)</td>|</th>', ' | ', t)
t = re.sub(r'<[^>]+>', ' ', t)
t = html.unescape(t).replace('\xa0', ' ')
t = re.sub(r'[ \t]+', ' ', t)
t = re.sub(r'\n\s*\n+', '\n', t)
open(os.path.join(d, out), 'w', encoding='utf-8').write(t)
print(out, len(t))
time.sleep(0.3)
