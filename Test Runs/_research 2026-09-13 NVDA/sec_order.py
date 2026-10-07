"""Q3 honesty: the SEC administrative order behind press release 2022-79 (the release on disk names only 'SEC Order').
Tries the conventional litigation/admin path; writes SEC_order_33-11060.txt if found. SEC User-Agent from tools/sources."""
import sys, os, io, urllib.request
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources, pypdf
OUT = os.path.dirname(os.path.abspath(__file__))
for url in ["https://www.sec.gov/files/litigation/admin/2022/33-11060.pdf",
            "https://www.sec.gov/litigation/admin/2022/33-11060.pdf"]:
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers=sources.SEC_UA), timeout=60).read()
        r = pypdf.PdfReader(io.BytesIO(raw))
        txt = "\n".join(p.extract_text() or "" for p in r.pages)
        open(os.path.join(OUT, "SEC_order_33-11060.txt"), "w", encoding="utf-8").write(url + "\n" + txt)
        print("OK", url, len(r.pages), "pages"); break
    except Exception as e:
        print("FAIL", url, e)
