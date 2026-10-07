"""Fetch Nintendo English IR documents (rung 3, company IR site). Saves PDF + extracted text.
Logs every URL tried with status, so obstacles can be named."""
import os, sys, urllib.request, urllib.error
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "ntdo")
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) research Chris Hrehor chrehor36@gmail.com"

URLS = sys.argv[1:] or [
    "https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf",
    "https://www.nintendo.co.jp/ir/pdf/2025/annual2503e.pdf",
    "https://www.nintendo.co.jp/ir/pdf/2024/annual2403e.pdf",
]

log = open(os.path.join(OUT, "_fetch_log.txt"), "a", encoding="utf-8")
for u in URLS:
    name = u.rstrip("/").split("/")[-1] or "index.html"
    if u.split("/")[-2] not in name:
        name = u.split("/")[-2] + "_" + name
    dest = os.path.join(OUT, name)
    try:
        req = urllib.request.Request(u, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
            ctype = r.headers.get("Content-Type", "")
        with open(dest, "wb") as f:
            f.write(data)
        msg = "OK %s %d bytes %s -> %s" % (u, len(data), ctype, name)
        if data[:4] == b"%PDF":
            doc = pymupdf.open(dest)
            with open(dest + ".txt", "w", encoding="utf-8") as f:
                for i, p in enumerate(doc):
                    f.write("\n=== PAGE %d ===\n" % (i + 1))
                    f.write(p.get_text())
            msg += " pages=%d" % doc.page_count
    except urllib.error.HTTPError as e:
        msg = "HTTP %s %s" % (e.code, u)
    except Exception as e:
        msg = "ERR %s %s: %s" % (u, type(e).__name__, e)
    print(msg)
    log.write(msg + "\n")
log.close()
