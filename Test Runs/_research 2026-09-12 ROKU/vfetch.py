import sys, os, re, html, urllib.request
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
D = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-12 ROKU"
jobs = [
 ("vizio_10Q_2024Q3", "https://www.sec.gov/Archives/edgar/data/1835591/000183559124000089/vzio-20240930.htm"),
 ("vizio_10K_FY2023", "https://www.sec.gov/Archives/edgar/data/1835591/000183559124000011/vzio-20231231.htm"),
]
def totext(h):
    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?is)<br\s*/?>", "\n", h)
    h = re.sub(r"(?is)</(tr|p|div|h\d|li|table)>", "\n", h)
    h = re.sub(r"(?is)</t[dh]>", " | ", h)
    h = re.sub(r"(?s)<[^>]+>", "", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t\xa0]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h
for name, url in jobs:
    p = os.path.join(D, name + ".htm")
    if not os.path.exists(p):
        try:
            raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e:
            print(name, "FETCH FAIL", e); continue
        open(p, "wb").write(raw)
    h = open(p, "rb").read().decode("utf-8", "replace")
    t = totext(h)
    open(os.path.join(D, name + ".txt"), "w", encoding="utf-8").write(t)
    print(name, "bytes", len(h), "-> text", len(t))
