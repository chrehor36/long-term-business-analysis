# usage: python web.py URL [outfile]  -> prints status and links (href) or saves binary to outfile
import sys, re, urllib.request, gzip, html, ssl
url = sys.argv[1]
H = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
     "Accept": "text/html,application/pdf,*/*", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip"}
req = urllib.request.Request(url, headers=H)
try:
    import certifi; r = urllib.request.urlopen(req, timeout=180, context=ssl.create_default_context(cafile=certifi.where()))
except urllib.error.HTTPError as e:
    print("HTTP", e.code, url); sys.exit(1)
except Exception as e:
    print("ERR", repr(e), url); sys.exit(1)
raw = r.read()
if r.headers.get("Content-Encoding") == "gzip":
    raw = gzip.decompress(raw)
print("HTTP", r.status, r.headers.get("Content-Type"), len(raw), r.geturl())
if len(sys.argv) > 2:
    open(sys.argv[2], "wb").write(raw); print("saved", sys.argv[2]); sys.exit(0)
t = raw.decode("utf-8", "replace")
pat = sys.argv[3] if len(sys.argv) > 3 else None
for m in re.finditer(r'(?is)<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', t):
    txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', m.group(2)))).strip()
    print(m.group(1), "|", txt[:120])
