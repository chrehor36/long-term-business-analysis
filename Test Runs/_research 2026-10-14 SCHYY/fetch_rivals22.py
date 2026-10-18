"""Fetch the three SEC-filing rivals' FY2022 annual reports (covering 2020-2022) into cache/ and strip to text."""
import urllib.request, re, html, sys, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
D = [("wynn22", "1174922", "000117492223000048", "wynn-20221231.htm"),
     ("mgm22", "789570", "000078957023000008", "mgm-20221231.htm"),
     ("mlco22", "1381640", "000119312523086859", "d396630d20f.htm"),
     ("scl18", "1755281", "000175528119000042", "a2018scl20-f.htm")]
out = sys.argv[1]
for name, cik, acc, doc in D:
    p = os.path.join(out, name + ".txt")
    if os.path.exists(p): continue
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{doc}"
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read().decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(t); t = re.sub(r"\s+", " ", t)
    open(p, "w", encoding="utf-8").write(t); print(name, len(t))
