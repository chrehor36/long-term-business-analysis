# fetch an EDGAR document into cache/f and write a wrapped text copy beside it
import sys, urllib.request, re, html, textwrap, os, time, gzip
UA = {'User-Agent': 'Chris Hrehor chrehor36@gmail.com', 'Accept-Encoding': 'gzip'}
out = sys.argv[1]; url = sys.argv[2]
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache', 'f')
req = urllib.request.Request(url, headers=UA)
b = urllib.request.urlopen(req, timeout=60).read()
if b[:2] == b'\x1f\x8b': b = gzip.decompress(b)
open(os.path.join(d, out + '.htm'), 'wb').write(b)
t = b.decode('utf-8', errors='ignore')
t = re.sub(r'(?is)<(script|style).*?</\1>', '', t); t = re.sub(r'<[^>]+>', ' ', t); t = html.unescape(t); t = re.sub(r'\s+', ' ', t)
open(os.path.join(d, out + '.txt'), 'w', encoding='utf-8').write(textwrap.fill(t, 220))
print(out, len(t)); time.sleep(0.3)
