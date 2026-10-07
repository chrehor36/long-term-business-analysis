"""Download a primary document and text-extract it (PDF via PyMuPDF). Records status.
usage: python dl.py URL OUTNAME"""
import sys, os, time, urllib.request, ssl

url, out = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
       "Accept": "*/*", "Accept-Encoding": "identity"}
t0 = time.time()
try:
    import certifi
    ctx = ssl.create_default_context(cafile=certifi.where())
except Exception:
    ctx = ssl.create_default_context()
try:
    req = urllib.request.Request(url, headers=hdr)
    with urllib.request.urlopen(req, timeout=90, context=ctx) as r:
        data = r.read()
        status = r.status
        ctype = r.headers.get("Content-Type")
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code} after {time.time()-t0:.1f}s: {url}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR {type(e).__name__}: {e} after {time.time()-t0:.1f}s: {url}")
    sys.exit(1)
path = os.path.join(here, out)
open(path, "wb").write(data)
print(f"HTTP {status} {ctype} {len(data):,} bytes in {time.time()-t0:.1f}s -> {out}")
if data[:4] == b"%PDF":
    import fitz
    doc = fitz.open(path)
    txtpath = os.path.splitext(path)[0] + ".txt"
    with open(txtpath, "w", encoding="utf-8") as f:
        f.write(f"SOURCE URL: {url}\nFETCHED: {time.strftime('%Y-%m-%d %H:%M:%S')} HTTP {status} {len(data)} bytes, {doc.page_count} pages\n")
        for i, p in enumerate(doc):
            f.write(f"\n=== PDF PAGE {i+1} ===\n")
            f.write(p.get_text())
    print(f"{doc.page_count} pages -> {os.path.basename(txtpath)}")
