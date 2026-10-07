import sys, os, re, html, urllib.request
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
D = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-12 ROKU"
jobs = [
 ("p_AMZN_10K_FY2025","https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm"),
 ("p_NFLX_10K_FY2025","https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm"),
 ("p_TTD_10K_FY2025","https://www.sec.gov/Archives/edgar/data/1671933/000167193326000014/ttd-20251231.htm"),
 ("p_CMCSA_10K_FY2025","https://www.sec.gov/Archives/edgar/data/1166691/000162828026004994/cmcsa-20251231.htm"),
 ("p_CHTR_10K_FY2025","https://www.sec.gov/Archives/edgar/data/1091667/000109166726000017/chtr-20251231.htm"),
 ("p_WMT_10K_FY2026","https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm"),
 ("p_AAPL_10K_FY2025","https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm"),
 ("p_GOOGL_10K_FY2025","https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm"),
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
            raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
            open(p, "wb").write(raw)
        except Exception as e:
            print(name, "FETCH FAIL", repr(e)); continue
    h = open(p, "rb").read().decode("utf-8", "replace")
    t = totext(h)
    open(os.path.join(D, name + ".txt"), "w", encoding="utf-8").write(t)
    print(name, "html", len(h), "text", len(t))
