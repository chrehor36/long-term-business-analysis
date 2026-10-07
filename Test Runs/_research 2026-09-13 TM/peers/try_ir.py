import sys, os, re, time
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) research fetch; Chris Hrehor chrehor36@gmail.com"}

url, name = sys.argv[1], sys.argv[2]
t0 = time.time()
try:
    r = requests.get(url, headers=UA, timeout=180)
except Exception as e:
    print("EXCEPTION", type(e).__name__, str(e)[:300])
    sys.exit(0)
print("status", r.status_code, "type", r.headers.get("Content-Type"), "bytes", len(r.content), "secs %.1f" % (time.time() - t0), "final", r.url)
if r.status_code != 200:
    print(r.text[:500])
    sys.exit(0)
if r.content[:4] == b"%PDF":
    p = os.path.join(HERE, name + ".pdf")
    open(p, "wb").write(r.content)
    import fitz
    doc = fitz.open(p)
    out = []
    for i, page in enumerate(doc):
        out.append("\n=== PAGE %d ===\n" % (i + 1) + page.get_text())
    txt = "SOURCE URL: " + url + "\n" + "".join(out)
    open(os.path.join(HERE, name + ".txt"), "w", encoding="utf-8").write(txt)
    print("pages", len(doc), "chars", len(txt))
else:
    open(os.path.join(HERE, name + ".html"), "wb").write(r.content)
    print(r.text[:300])
