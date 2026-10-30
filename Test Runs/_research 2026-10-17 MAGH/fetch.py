# fetch EDGAR documents for MAGH into cache/ and strip to text
import sys, urllib.request, re, html, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
CIK = "2046117"
docs = [
 ("20F_2026", "0001493152-26-043050", "form20-f.htm"),
 ("20F_2025", "0001493152-25-013424", "form20-f.htm"),
 ("20FA_2026", "0001493152-26-008628", "form20-fa.htm"),
 ("424B4", "0001641172-25-023166", "form424b4.htm"),
 ("6K_20260918", "0001493152-26-043266", "form6-k.htm"),
 ("6K_20260805", "0001493152-26-036115", "form6-k.htm"),
 ("6K_20260430", "0001493152-26-019717", "form6-k.htm"),
 ("6K_20251210", "0001493152-25-027002", "form6-k.htm"),
 ("6K_20250814", "0001641172-25-023712", "form6-k.htm"),
 ("NT20F_2026", "0001493152-26-040731", "formnt20-f.htm"),
 ("CORRESP_20260303", "0001493152-26-008682", "filename1.htm"),
 ("CORRESP_20260306", "0001493152-26-009050", "filename1.htm"),
 ("CORRESP_20250729a", "0001641172-25-021290", "filename1.htm"),
 ("CORRESP_20250729b", "0001641172-25-021288", "filename1.htm"),
 ("CORRESP_20250610", "0001641172-25-014488", "filename1.htm"),
]
os.makedirs("cache", exist_ok=True)
def strip(t):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
for name, acc, doc in docs:
    out = f"cache/{name}.txt"
    if os.path.exists(out): continue
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        raw = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
        open(f"cache/{name}.htm", "w", encoding="utf-8").write(raw)
        open(out, "w", encoding="utf-8").write(strip(raw))
        print("ok", name, len(raw))
    except Exception as e:
        print("FAIL", name, url, e)
    time.sleep(0.3)
